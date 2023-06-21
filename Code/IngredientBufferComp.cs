using System.Collections.Generic;
using System.Diagnostics;
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
    public class IngredientBufferComp : BaseComponent<IngredientBufferComp>, IUIDataProvider, IUIContextMenuProvider, IUISubmenuProvider, IComponent, IUIMultiSelectable, ICopyableComp, IUINoAutoPair
    {
        private UDB uiBlock = null;
        private UDB isActiveBlock = null;
        private UDB fillCrafterBlock = null;
        private UDB potentialBlock = null;
        private UDB refillSliderBlock = null;
        private UDB haulingSliderBlock = null;
        private Dictionary<MatType,UDB> ingredientsBlock = new Dictionary<MatType,UDB>();
        private UDB ejectBlock = null;

        public IngredientBuffer buffer;

        private static string _priorityTooltip = null;
        private static string PriorityTooltip
        {
            get
            {
                if (_priorityTooltip == null)
                {
                    string text;
                    string o = The.Bindings.GetBinding(ActionType.ShiftModifier).AllControlGlyphs(out text, "<br>", false);
                    string o2 = The.Bindings.GetBinding(ActionType.CtrlModifier).AllControlGlyphs(out text, "<br>", false);
                    _priorityTooltip = "priority.block.shift.tip".T(o, o2);
                }
                return _priorityTooltip;
            }
        }

        public bool HasSubmenuNow => true;

        public string SubmenuTitle => "ingredientbuffer.ui.title".T();

        public string CommonActionId => CommonActionIngredientBuffer.CommonActionId;

        public bool IsReachableForCommonAction => base.Entity != null && base.Entity.IsActive && this.buffer != null;

        public bool IsCopyable => this.buffer != null && this.buffer.comp != null;

        public string CopyConfigText => "ingredientbuffer.ui.copy.config.text".T(base.Tile.Definition.NameT);

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

        public bool CopyConfigTo(ICopyableComp target)
        {
            IngredientBufferComp to = target as IngredientBufferComp;
            if (to == null || to.buffer == null || to.buffer.comp == null)
                return false;
            //let through if to.buffer.comp.Demand==null, for the RelocateTo()
            if (to.buffer.comp.Demand != null && to.buffer.comp.Demand.craftableId != this.buffer.comp.Demand?.craftableId)
                return false;
            this.buffer.CopyTo(to.buffer);
            to.UpdateUIDetails();
            return true;
        }

        public bool CanCopyTo(ICopyableComp comp)
        {
            IngredientBufferComp to = comp as IngredientBufferComp;
            return to != null && to.buffer != null && to.buffer.comp.Demand?.craftableId == this.buffer.comp.Demand?.craftableId;
        }

        public override void OnRemove()
        {
            IngredientBufferTracker.Remove(buffer);
        }

        public void ContextActions(List<UDB> res)
        {
            GetUIDetails(res);
        }

        public UDB GetUIBlock()
        {
            if(base.Tile.IsConstructed && base.Tile.ENode.IsReachable)
            {
                if (buffer.IsActive && buffer.ingredients != null && buffer.comp.Demand != null)
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

            res.Add(fillCrafterBlock);
            res.Add(haulingSliderBlock);
            res.Add(isActiveBlock);
            if (buffer.IsActive && buffer.ingredients != null)
            {
                res.Add(potentialBlock);
                res.Add(refillSliderBlock);
                foreach (UDB udb in ingredientsBlock.Values)
                    res.Add(udb);
                res.Add(ejectBlock);
            }
            else if(buffer.IsActive && buffer.ingredients == null)
            {
                res.Add(uiBlock);
            }

            addTestUI(res);
            
        }

        public void UpdateUIBlock()
        {
            if(uiBlock == null)
            {
                uiBlock = UDB.Create(this, UDBT.IText, "Icons/Color/Warning", null).WithGroupId(UDBGH.Management);
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
            if (isActiveBlock == null)
            {
                isActiveBlock = UDB.Create(this, UDBT.DBtn, "Icons/Color/Warning", buffer.IsActive ? "ingredientbuffer.ui.disable.buffer".T() : "ingredientbuffer.ui.enable.buffer".T())
                    .WithClickFunction(delegate
                    {
                        GetUIBlock().NeedsListRebuild = true;
                        buffer.IsActive = !buffer.IsActive;
                        isActiveBlock.NeedsListRebuild = true;
                    });
            }
            isActiveBlock.UpdateTitle(buffer.IsActive ? "ingredientbuffer.ui.disable.buffer".T() : "ingredientbuffer.ui.enable.buffer".T());

            if (fillCrafterBlock == null)
            {
                fillCrafterBlock = UDB.Create(this, UDBT.DTextBtn, buffer.fillCrafterInventoryFirst ? "Icons/Color/Check" : "Icons/Color/Cross", "ingredientbuffer.ui.fillcrafterinventoryfirst".T());
                fillCrafterBlock.WithText2(T.Toggle)
                    .WithTooltip("ingredientbuffer.tooltip.fillcrafterinventoryfirst".T())
                    .WithClickFunction(delegate
                    {
                        buffer.fillCrafterInventoryFirst = !buffer.fillCrafterInventoryFirst;
                        fillCrafterBlock.UpdateIcon(buffer.fillCrafterInventoryFirst ? "Icons/Color/Check" : "Icons/Color/Cross");
                    });
            }
            fillCrafterBlock.UpdateIcon(buffer.fillCrafterInventoryFirst ? "Icons/Color/Check" : "Icons/Color/Cross");

            if (haulingSliderBlock == null)
            {
                haulingSliderBlock = UDB.Create(this, UDBT.DSlider, "Icons/Color/FillLimit", "ingredientbuffer.ui.haulingbatchsize".T())
                    .WithRange(1f, 100f)
                    .WithTooltip("ingredientbuffer.tooltip.haulingbatchsize".T())
                    .WithValueChangeFunction(delegate (UDB b, object v)
                    {
                        buffer.haulingBatchSize = Mathf.RoundToInt((float)v);
                    });
            }
            haulingSliderBlock.UpdateValue(buffer.haulingBatchSize);

            if (buffer.IsActive && buffer.ingredients != null && buffer.comp.Demand != null)
            {
                if (potentialBlock == null)
                {
                    potentialBlock = UDB.Create(this, UDBT.IProgress, null, null).WithGroupId(UDBGH.Management)
                        .WithTooltipFunction(delegate (UDB b)
                        {
                            Def def = buffer?.comp?.Demand?.Product;
                            if (def == null)
                                return "";
                            Caches.StringBuilder.Clear();
                            Caches.StringBuilder.Append("available.count".T(base.S.Sys.Inventory.CountOf(def)));
                            Caches.StringBuilder.Append("<br>");
                            Caches.StringBuilder.Append("ingredientbuffer.tooltip.buffered.count".T((int)b.Value, (int)b.MaxValue));
                            return Caches.StringBuilder.ToString();
                        });
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
                    UDB udb;
                    if(!ingredientsBlock.TryGetValue(mat.Type, out udb))
                    {
                        int index = i;

                        udb = UDB.Create(this, UDBT.IPriority, mat.Type.IconId, mat.Type.NameT)
                        .WithTooltipFunction(delegate(UDB b)
                        {
                            Caches.StringBuilder.Clear();
                            Caches.StringBuilder.Append("available.count".T(base.S.Sys.Inventory.CountOf(mat.Type.Def)));
                            Caches.StringBuilder.Append("<br>");
                            Caches.StringBuilder.Append(PriorityTooltip);
                            return Caches.StringBuilder.ToString();
                        })
                        .WithIconTint(mat.Type.IconTint)
                        .WithIconClickFunction(()=>ShowAmountInputContext(index))
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
                    refillSliderBlock = UDB.Create(this, UDBT.DSlider, "Icons/Color/FillLimit", "ingredientbuffer.ui.refillthreshold".T())
                        .WithTooltip("ingredientbuffer.tooltip.refillthreshold".T())
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

                if(ejectBlock == null)
                {
                    ejectBlock = UDB.Create(this, UDBT.DBtn, "Icons/Color/Warning", "ingredientbuffer.ui.eject.all".T())
                        .WithClickFunction(delegate
                        {
                            buffer.TryEjectBuffer(true);
                            UpdateUIDetails();
                        });
                }
            }
            else
            {
                ingredientsBlock.Clear();
            }
        }

        private void ShowAmountInputContext(int index)
        {
            if (buffer?.comp?.Demand == null || buffer?.ingredients == null)
            {
                UISounds.PlayActionDenied();
            }
            else
            {
                UIAmountInputContext amountContext = new UIAmountInputContext(base.S)
                    .WithConfirmAction(delegate
                    {
                        base.S.Sig.HideContextMenu.Send();
                    }).WithCurrentAmountChangeFun(delegate (int amt)
                    {
                        if (buffer?.comp?.Demand != null && buffer?.ingredients != null)
                        {
                            if (amt > 100000)
                            {
                                amt = 100000;
                            }
                            if (index >= buffer.ingredients.Length || index >= buffer.comp.Demand.Craftable.Ingredients.Length)
                                return;
                            if (buffer.ingredients[index].Type != buffer.comp.Demand.Craftable.Ingredients[index].Type)
                                return;
                            int delta = amt - buffer.ingredients[index].MaxStackSize / buffer.comp.Demand.Craftable.Ingredients[index].StackSize;
                            if (buffer.TryAdjustMaxStackSize(index, delta))
                                UpdateUIDetails();
                        }
                    }).WithCurrentAmountTextFunc(delegate
                    {
                        if (buffer?.comp?.Demand != null && buffer?.ingredients != null)
                        {
                            if (index >= buffer.ingredients.Length || index >= buffer.comp.Demand.Craftable.Ingredients.Length)
                                return Units.XNum(1);
                            if (buffer.ingredients[index].Type != buffer.comp.Demand.Craftable.Ingredients[index].Type)
                                return Units.XNum(1);
                            return Units.XNum(buffer.ingredients[index].MaxStackSize / buffer.comp.Demand.Craftable.Ingredients[index].StackSize);
                        }
                        return Units.XNum(1);
                    }).WithCurrentAmountValueFunc(delegate
                    {
                        if (buffer?.comp?.Demand != null && buffer?.ingredients != null)
                        {
                            if (index >= buffer.ingredients.Length || index >= buffer.comp.Demand.Craftable.Ingredients.Length)
                                return 1;
                            if (buffer.ingredients[index].Type != buffer.comp.Demand.Craftable.Ingredients[index].Type)
                                return 1;
                            return buffer.ingredients[index].MaxStackSize / buffer.comp.Demand.Craftable.Ingredients[index].StackSize;
                        }
                        return 1;
                    })
                    .WithSliderText(T.WantedAmount)
                    .WithSliderRange(1, 100)
                    .WithHeaderText(buffer.ingredients[index].Type.NameT)
                    .WithSliderIcon(buffer.ingredients[index].Type.Def.Preview);
                base.S.Sig.ShowContextMenu.Send(amountContext);
            }
        }

        public void OnRecipeChange()
        {
            ingredientsBlock.Clear();
            if(potentialBlock != null)
                potentialBlock.NeedsListRebuild = true;
            if (uiBlock != null)
                uiBlock.NeedsListRebuild = true;
        }

        [Conditional("DEBUG")]
        private void addTestUI(List<UDB> res)
        {
            res.Add(UDB.Create(this, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "buffer")
                .WithText2("Peek")
                .WithClickFunction(delegate {
                    StringBuilder sb = new StringBuilder();
                    sb.Append("isActive: ").Append(buffer.IsActive).AppendLine();
                    sb.Append("fillCrafterInventoryFirst: ").Append(buffer.fillCrafterInventoryFirst).AppendLine();
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
