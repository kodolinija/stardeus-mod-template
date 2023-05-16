using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Game.AI;
using Game.Components;
using Game.Data;
using KL.Utils;
using UnityEngine;


namespace IngredientBuffer
{
    public class IngredientBuffer
    {
        public bool fillCompletelyBeforeCrafting = false;
        //TODO hauling batch size

        public Mat[] ingredients = null;

        //TODO delete test value
        public int testvalue;

        public CrafterComp comp;

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
                    MaxStackSize = array[i].StackSize//TODO make it slider compatible
                };
                D.Err(""+ingredients[i].Type.NameT+" " + ingredients[i].StackSize + " " + ingredients[i].MaxStackSize);
            }
        }

        public void TryEjectBuffer()
        {

        }

        public void OnSave(ComponentData data)
        {
            if (!isActive)
                return;
            data.SetBool("fillBufferBeforeCrafting", false);
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
            fillCompletelyBeforeCrafting = data.GetBool("fillBufferBeforeCrafting", false);
            IsActive = true;
        }

        public void RebuildIngredientsReq(bool forced=false)
        {
            if (!isActive)
                return;
            if (ingredients == null)
                return;
            if (!forced)
            {
                //TODO request if buffer cannot afford another production
            }
            for (int i = 0; i < ingredients.Length; i++)
            {
                Mat mat = ingredients[i];
                if (mat.Diff >= 1)
                {
                    comp.MissingMats.Add(new MatRequest
                    {
                        Type = mat.Type,
                        Amount = mat.Diff,//TODO make it slider compatible
                        IsAmountOptional = true,
                        Requester = comp
                    });
                }
            }
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
                        if (mat.StackSize == mat.MaxStackSize)
                        {
                            //((MatDeficitEventHolder)deficitEv.GetValue(This)).ClearIf(mat.Type);
                        }
                    }
                }
            }
        }

        public void FillFromBuffer()
        {
            if (!isActive)
                return;
            Mat[] requiredIngredients = comp.GetIngredients();
            for(int i = 0; i < requiredIngredients.Length; i++)
            {
                Mat required=requiredIngredients[i];
                for(int j = 0; j < ingredients.Length; j++)
                {
                    if(required.Type == ingredients[j].Type)
                    {
                        int amount=Mathf.Min(required.Diff, ingredients[j].StackSize);
                        required.StackSize += amount;
                        ingredients[j].StackSize -= amount;
                        requiredIngredients[i] = required;
                        break;
                    }
                }
            }
        }
    }
}
