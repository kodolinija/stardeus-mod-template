using System;
using System.Collections.Generic;
using System.Text;
using Game;
using Game.Components;
using Game.Constants;
using Game.Data;
using Game.Input;
using Game.UI;
using Game.Utils;
using KL.Utils;
using UnityEngine;

namespace IngredientBuffer
{
    public class IngredientBufferComp : BaseComponent<IngredientBufferComp>, IUIDataProvider, IUIContextMenuProvider, IUISubmenuProvider, IComponent
    {
        private UDB uiBlock = null;
        private UDB isActiveBlock = null;
        private UDB fillCrafterBlock = null;
        private UDB potentialBlock = null;
        private UDB refillSliderBlock = null;
        private UDB haulingSliderBlock = null;
        private Dictionary<MatType,UDB> ingredientsBlock = new Dictionary<MatType,UDB>();

        public IngredientBuffer buffer;

        public bool HasSubmenuNow => true;

        public string SubmenuTitle => "ingredientbuffer.ui.title".T();

        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
        private static void Register()
        {
            BaseComponent<IngredientBufferComp>.AddComponentPrototype(new IngredientBufferComp());
            Ready.WhenCore(InjectDefs);
        }

        public static void InjectDefs()
        {
            ComponentConfig comp = new ComponentConfig();
            comp.Component = BaseComponent<IngredientBufferComp>.componentName;
            comp.Properties = new SerializableProperty[0];
            comp.EnsureHash();

            string crafterCompName=BaseComponent<CrafterComp>.componentName;
            int inject_count = 0;
            StringBuilder sb = new StringBuilder();

            foreach (Def def in The.Defs.Defs.Values)
            {
                if (def.Components != null && def.HasComponent(crafterCompName))
                {
                    ComponentConfig[] array = new ComponentConfig[def.Components.Length + 1];
                    int j = 0;
                    for (int i = 0; i < def.Components.Length; i++)
                    {
                        array[j++] = def.Components[i];
                        if (def.Components[i].Component == crafterCompName)
                            array[j++] = comp;
                    }
                    def.Components = array;
                    sb.Append(def.NameKey).AppendLine();
                    inject_count++;
                }
            }
            D.Warn("[IngredientBuffer] Injected " + inject_count + " defs: \n"+sb.ToString());
        }

        public void ContextActions(List<UDB> res)
        {
            GetUIDetails(res);
        }

        public UDB GetUIBlock()
        {
            if(base.Tile.IsConstructed && base.Tile.EnergyNode.IsReachable)
            {
                if (buffer.IsActive && buffer.ingredients != null)
                {
                    if (potentialBlock == null)
                    {
                        UpdateUIDetails();
                    }
                    return potentialBlock;
                }
                UpdateUIBlock();
                return uiBlock;
            }
            return null;
        }

        public void GetUIDetails(List<UDB> res)
        {
            UpdateUIDetails();

            res.Add(isActiveBlock);
            res.Add(fillCrafterBlock);
            if (buffer.IsActive && buffer.ingredients != null)
            {
                res.Add(potentialBlock);
                foreach(UDB udb in ingredientsBlock.Values)
                    res.Add(udb);
                res.Add(refillSliderBlock);
                res.Add(haulingSliderBlock);
            }
            else
            {
                res.Add(uiBlock);
            }

            addTestUI(res);
            
        }

        public void UpdateUIBlock()
        {
            if(uiBlock == null)
            {
                uiBlock = UDB.Create(this, UDBT.IText, "Icons/Color/Warning", null);
            }
            if (!buffer.IsActive)
            {
                uiBlock.UpdateTitle("ingredientbuffer.ui.buffer.disabled".T());
                return;
            }
            if (buffer.comp.Demand == null)
            {
                uiBlock.UpdateTitle("ingredientbuffer.ui.crafter.no.demand".T());
                return;
            }
        }

        public void UpdateUIDetails()
        {
            //TODO tooltips, icon click function

            if (isActiveBlock == null)
            {
                isActiveBlock = UDB.Create(this, UDBT.DTextBtn, buffer.IsActive ? "Icons/Color/Check" : "Icons/Color/Cross", "isActive");
                isActiveBlock.WithText2(T.Toggle)
                    .WithClickFunction(delegate
                    {
                        GetUIBlock().NeedsListRebuild = true;
                        buffer.IsActive = !buffer.IsActive;
                        isActiveBlock.UpdateIcon(buffer.IsActive ? "Icons/Color/Check" : "Icons/Color/Cross");
                        isActiveBlock.NeedsListRebuild = true;
                    });
            }
            if (fillCrafterBlock == null)
            {
                fillCrafterBlock = UDB.Create(this, UDBT.DTextBtn, buffer.fillCrafterInventoryFirst ? "Icons/Color/Check" : "Icons/Color/Cross", "fillCrafterInventoryFirst");
                fillCrafterBlock.WithText2(T.Toggle)
                    .WithClickFunction(delegate
                    {
                        buffer.fillCrafterInventoryFirst = !buffer.fillCrafterInventoryFirst;
                        fillCrafterBlock.UpdateIcon(buffer.fillCrafterInventoryFirst ? "Icons/Color/Check" : "Icons/Color/Cross");
                    });
            }
            if (buffer.IsActive && buffer.ingredients != null)
            {
                if (potentialBlock == null)
                {
                    potentialBlock = UDB.Create(this, UDBT.IProgress, null, null);
                }
                //do not use MatType because output might be beings
                potentialBlock.UpdateIcon(buffer.comp.Demand.Product.Preview);
                potentialBlock.UpdateTitle(buffer.comp.Demand.Product.NameT);
                potentialBlock.UpdateIconTint(buffer.comp.Demand.Product.UITint);
                Mat product = buffer.GetPotentialBufferProduction();
                potentialBlock.UpdateValue(product.StackSize);
                potentialBlock.UpdateRange(0f, product.MaxStackSize);

                for (int i = 0; i < buffer.ingredients.Length; i++)
                {
                    Mat mat = buffer.ingredients[i];
                    
                    string tooltip = null;

                    UDB udb;
                    if(!ingredientsBlock.TryGetValue(mat.Type, out udb))
                    {
                        if(tooltip == null)
                        {
                            string text;
                            string o = The.Bindings.GetBinding(ActionType.ShiftModifier).AllControlGlyphs(out text, "<br>", false);
                            string o2 = The.Bindings.GetBinding(ActionType.CtrlModifier).AllControlGlyphs(out text, "<br>", false);
                            tooltip = "priority.block.shift.tip".T(o, o2);
                        }
                        int index = i;

                        udb = UDB.Create(this, UDBT.IPriority, mat.Type.IconId, mat.Type.NameT)
                        .WithTooltip(tooltip)
                        .WithIconTint(mat.Type.IconTint)
                        .WithClickFunction(delegate
                        {
                            int delta = -1;
                            if (The.Bindings.IsPressed(ActionType.CtrlModifier))
                            {
                                delta = -50;
                            }
                            else if (The.Bindings.IsPressed(ActionType.ShiftModifier))
                            {
                                delta = -10;
                            }
                            if (buffer.TryAdjustMaxStackSize(index, delta))
                            {
                                udb.UpdateValue(buffer.ingredients[index].StackSize);
                                udb.UpdateRange(0f, buffer.ingredients[index].MaxStackSize);
                                this.UpdateUIDetails();
                            }
                        }).WithClick2Function(delegate
                        {
                            int delta = 1;
                            if (The.Bindings.IsPressed(ActionType.CtrlModifier))
                            {
                                delta = 50;
                            }
                            else if (The.Bindings.IsPressed(ActionType.ShiftModifier))
                            {
                                delta = 10;
                            }
                            if (buffer.TryAdjustMaxStackSize(index, delta))
                            {
                                udb.UpdateValue(buffer.ingredients[index].StackSize);
                                udb.UpdateRange(0f, buffer.ingredients[index].MaxStackSize);
                                this.UpdateUIDetails();
                            }
                        });
                        ingredientsBlock.Add(mat.Type,udb);
                    }
                    udb.UpdateValue(buffer.ingredients[i].StackSize);
                    udb.UpdateRange(0f, buffer.ingredients[i].MaxStackSize);
                }

                if (refillSliderBlock == null)
                {
                    refillSliderBlock = UDB.Create(this, UDBT.DSlider, "Icons/Color/FillLimit", "refillThreshold")
                        .WithValueChangeFunction(delegate (UDB b, object v)
                        {
                            buffer.RefillThreshold = Mathf.RoundToInt((float)v);
                        });
                }
                int cap = Mathf.Max(product.MaxStackSize, 1);
                if (buffer.RefillThreshold> cap)
                    buffer.RefillThreshold = cap;
                refillSliderBlock.UpdateRange(1f, Mathf.Max(product.MaxStackSize, 1));
                refillSliderBlock.UpdateValue(buffer.RefillThreshold);
                if (haulingSliderBlock == null)
                {
                    haulingSliderBlock= UDB.Create(this, UDBT.DSlider, "Icons/Color/FillLimit", "haulingBatchSize")
                        .WithRange(1f, 100f)
                        .WithValueChangeFunction(delegate (UDB b, object v)
                        {
                            buffer.haulingBatchSize = Mathf.RoundToInt((float)v);
                        });
                }
                haulingSliderBlock.UpdateValue(buffer.haulingBatchSize);
            }
            else
            {
                ingredientsBlock.Clear();
            }
        }

        public void OnRecipeChange()
        {
            ingredientsBlock.Clear();
        }

        [Obsolete]
        private void addTestUI(List<UDB> res)
        {
            res.Add(UDB.Create(this, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "buffer")
                .WithText2("Peek")
                .WithClickFunction(delegate {
                    StringBuilder sb = new StringBuilder();
                    sb.Append("isActive: ").Append(buffer.IsActive).AppendLine();
                    sb.Append("fillCompletelyBeforeCrafting: ").Append(buffer.fillCrafterInventoryFirst).AppendLine();
                    sb.Append("refillThreshold: ").Append(buffer.RefillThreshold).AppendLine();
                    sb.Append("haulingBatchSize: ").Append(buffer.haulingBatchSize).AppendLine();
                    sb.Append("ingredients: ").AppendLine();
                    if (buffer.ingredients == null)
                        sb.Append("null");
                    else
                    {
                        foreach (Mat mat in buffer.ingredients)
                            sb.Append(mat.StackSize).Append("/").Append(mat.MaxStackSize).Append(" ").Append(mat.Type.NameT).AppendLine();
                    }
                    UIPopupWidget.Spawn("Icons/Color/Warning", "Buffer", sb.ToString()); 
                }));
            res.Add(UDB.Create(this, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "progress to 99%")
                .WithText2("Set")
                .WithClickFunction(delegate { buffer.comp.Progress = 0.99f; }));
            res.Add(UDB.Create(this, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "missing mats")
                .WithText2("Peek")
                .WithClickFunction(delegate {
                    StringBuilder sb = new StringBuilder();
                    foreach (MatRequest mr in buffer.comp.MissingMats)
                        sb.Append(mr.Amount).Append(mr.Type.NameT).AppendLine();
                    UIPopupWidget.Spawn("Icons/Color/Warning", "MissingMats", sb.ToString());
                }));
            res.Add(UDB.Create(this, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "comps")
                .WithText2("Peek")
                .WithClickFunction(delegate {
                    StringBuilder sb = new StringBuilder();
                    foreach (IComponent comp in this.Entity.Components)
                        sb.Append(comp.GetName()).AppendLine();
                    UIPopupWidget.Spawn("Icons/Color/Warning", "Components", sb.ToString());
                }));
        }
    }
}
