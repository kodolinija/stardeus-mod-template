using System.Collections.Generic;
using Game.Components;
using Game.Data;
using KL.Utils;
using UnityEngine;


namespace IngredientBuffer
{
    public class IngredientBuffer
    {
        public bool fillCrafterInventoryFirst = true;
        public int haulingBatchSize = 20;

        public Mat[] ingredients = null;
        public int ingredientHash = 0;

        public CrafterComp comp;

        private int refillThreshold = 1;
        public int RefillThreshold
        {
            get { return refillThreshold; }
            set
            {
                refillThreshold = value;
                if (isActive && ingredients != null && comp.Demand != null)
                {
                    if (GetPotentialBufferProduction().StackSize < refillThreshold)
                    {
                        comp.RebuildIngredientsReq();
                    }
                }
            }
        }

        private bool isActive = false;
        public bool IsActive
        {
            get { return isActive; }
            set
            {
                isActive = value;
                if (isActive && comp.Demand != null)
                {
                    if(!VerifyBuffer())
                        RebuildBuffer();
                }
                if (!isActive)
                {
                    TryEjectBuffer();
                }
            }
        }

        public IngredientBuffer(CrafterComp comp)
        {
            this.comp = comp;
        }

        public bool VerifyBuffer()
        {
            if (ingredients == null||ingredients.Length!=comp.GetIngredients().Length)
                return false;
            Mat[] required = comp.GetIngredients();
            for (int i = 0; i < ingredients.Length; i++)
                if (ingredients[i].Type != required[i].Type)
                    return false;
            return true;
        }

        public void RebuildBuffer()
        {
            TryEjectBuffer();
            Mat[] array = comp.Demand.Craftable.Ingredients;
            ingredients = new Mat[array.Length];
            for (int i = 0; i < array.Length; i++)
            {
                ingredients[i] = new Mat
                {
                    Type = array[i].Type,
                    MaxStackSize = array[i].StackSize
                };
            }
            ingredientHash += 1;
        }

        public void TryEjectBuffer()
        {
            if (ingredients != null)
            {
                foreach (Mat mat in ingredients)
                {
                    if (mat.StackSize >= 1)
                    {
                        EntityUtils.SpawnRawMaterial(mat, comp.Tile.Transform.WorkSpot, 0.5f, true, true);
                    }
                }
                ingredients = null;
            }
        }

        public bool TryAdjustMaxStackSize(int hash, int index, int delta)
        {
            if (ingredients == null || ingredientHash != hash || index >= ingredients.Length)
                return false;
            Mat[] mats=comp.GetIngredients();
            if (mats == null || index >= mats.Length)
                return false;
            int mult = mats[index].MaxStackSize;
            int newsize = ingredients[index].MaxStackSize + delta * mult;
            if (newsize < mult)
                newsize = mult;
            if (newsize < ingredients[index].StackSize)
            {
                Mat drop = ingredients[index].Copy;
                drop.StackSize = drop.StackSize - newsize;
                EntityUtils.SpawnRawMaterial(drop, comp.Tile.Transform.WorkSpot, 0.5f, true, true);
                ingredients[index].StackSize = newsize;
            }
            ingredients[index].MaxStackSize = newsize;
            return true;
        }

        public Mat GetPotentialBufferProduction()
        {
            if (comp.Demand == null)
                return default(Mat);
            Mat mat = default(Mat);
            mat.Type = comp.Demand.Craftable.ProductDef.MatType;
            mat.StackSize = 0;
            mat.MaxStackSize = 0;
            int mult = comp.Demand.Craftable.OutputMultiplier;
            if (mult < 1)
                mult = 1;
            if (!VerifyBuffer())
                return mat;
            int minBufferStock = 1 << 30, minBufferCapacity = 1 << 30;
            for(int i = 0; i < ingredients.Length; i++)
            {
                int required = comp.Demand.Craftable.Ingredients[i].StackSize;
                minBufferStock = Mathf.Min(minBufferStock, (int)(ingredients[i].StackSize / required));
                minBufferCapacity = Mathf.Min(minBufferCapacity, (int)(ingredients[i].MaxStackSize / required));
            }
            mat.StackSize = minBufferStock;
            mat.MaxStackSize = minBufferCapacity;
            return mat;
        }

        public void OnSave(ComponentData data)
        {
            if (!isActive)
                return;
            data.SetBool("fillCrafterInventoryFirst", fillCrafterInventoryFirst);
            data.SetInt("refillThreshold", refillThreshold);
            data.SetInt("haulingBatchSize", haulingBatchSize);
            data.SetMats("ingredientBuffer", ingredients);
        }

        public void OnLoad(ComponentData data)
        {
            ingredients = data.GetMats("ingredientBuffer", null);
            if (ingredients == null)
            {
                isActive = false;
                return;
            }
            fillCrafterInventoryFirst = data.GetBool("fillCrafterInventoryFirst", true);
            refillThreshold = data.GetInt("refillThreshold", 1);
            haulingBatchSize = data.GetInt("haulingBatchSize", 20);
            IsActive = true;
        }

        public void RebuildIngredientsReq(bool skipThresholdCheck=false)
        {
            if (!isActive)
                return;
            if (ingredients == null)
                return;
            if (!skipThresholdCheck)
            {
                if (GetPotentialBufferProduction().StackSize >= refillThreshold)
                    return;
            }
            if (fillCrafterInventoryFirst && comp.MissingMats.Count > 0)
            {
                //crafter already has mat requests, fulfill those first
                return;
            }
            List<MatRequest> list = new List<MatRequest>();
            for (int i = 0; i < ingredients.Length; i++)
            {
                Mat mat = ingredients[i];
                if (mat.Diff >= 1)
                {
                    MatRequest mr = comp.MissingMats.Find(m=>m.Type==mat.Type);
                    if (mr == null)
                    {
                        list.Add(new MatRequest
                        {
                            Type = mat.Type,
                            Amount = Mathf.Min(mat.Diff, haulingBatchSize),
                            IsAmountOptional = true,
                            Requester = comp
                        });
                    }
                    else
                    {
                        if (mr.Amount < haulingBatchSize)
                            mr.Amount = Mathf.Min(mr.Amount + mat.Diff, haulingBatchSize);
                    }
                }
            }
            comp.MissingMats.AddRange(list);
        }

        public void ProvideRequestedMat(UnstoredMatComp unstoredMat)
        {
            if (!IsActive)
                return;
            if (ingredients == null)
                return;
            for (int i = 0; i < ingredients.Length; i++)
            {
                Mat mat = ingredients[i];
                if (mat.Type == unstoredMat.Type)
                {
                    int diff = mat.Diff;
                    if (diff > 0)
                    {
                        int wantedAmount = Mathf.Min(diff, unstoredMat.StackSize);
                        if (wantedAmount == 0)
                            continue;
                        wantedAmount = unstoredMat.Take(mat.Type, null, wantedAmount, comp.GetCurrentAd());
                        mat.StackSize += wantedAmount;
                        ingredients[i] = mat;
                    }
                }
            }
        }

        public void FillFromBuffer()
        {
            if (!isActive)
                return;
            Mat[] requiredIngredients = comp.GetIngredients();
            bool shouldRequestMat = false;
            for(int i = 0; i < requiredIngredients.Length; i++)
            {
                Mat required=requiredIngredients[i];
                D.Ass(required.Type == ingredients[i].Type, "Incorrect ingredient ordering in FillFromBuffer()");
                int amount = Mathf.Min(required.Diff, ingredients[i].StackSize);
                required.StackSize += amount;
                ingredients[i].StackSize -= amount;
                requiredIngredients[i] = required;
                
                if(ingredients[i].StackSize/required.MaxStackSize<refillThreshold)
                    shouldRequestMat = true;
            }
            if (shouldRequestMat)
            {
                RebuildIngredientsReq(true);
                comp.TriggerHaulingAdNow();
            } 
        }
    }
}
