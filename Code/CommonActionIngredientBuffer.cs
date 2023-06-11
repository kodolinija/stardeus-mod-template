using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Game.Components;
using Game.Components.CommonActions;
using Game.Constants;
using Game.Data;
using Game.UI.Parts;
using Game.Utils;
using UnityEngine;

namespace IngredientBuffer
{
    internal class CommonActionIngredientBuffer : CommonAction
    {
        public const string CommonActionId = "ingredientbuffer.common.action";

        private List<IngredientBufferComp> buffers = new List<IngredientBufferComp>(64);
        private List<IngredientBufferComp> activeBuffers = new List<IngredientBufferComp>(64);
        private List<IngredientBufferComp> inactiveBuffers = new List<IngredientBufferComp>(64);
        private int buffersCycleIdx = 0;
        private int activeBuffersCycleIdx = 0;
        private int inactiveBuffersCycleIdx = 0;

        private UDB buffersBlock = null;
        private UDB activeBuffersBlock = null;
        private UDB inactiveBuffersBlock = null;

        public override string Id => CommonActionId;

        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
        private static void Register()
        {
            CommonAction.Add(new CommonActionIngredientBuffer());
        }

        public override void OnAppendUIBlocks(GameState s, UIDataBlockListView view, List<IComponent> common)
        {
            this.ResetState();
            foreach(IComponent c in common)
            {
                if (!(c is IngredientBufferComp))
                    continue;
                IngredientBufferComp comp = (IngredientBufferComp)c;
                buffers.Add(comp);
                if(comp.buffer.IsActive)
                    activeBuffers.Add(comp);
                else
                    inactiveBuffers.Add(comp);
            }

            if (activeBuffersBlock == null)
            {
                activeBuffersBlock = UDB.Create("common_action", UDBT.ITextBtn, "Icons/Color/Store", "ingredientbuffer.common.action.buffer.enabled".T())
                    .WithText2("ingredientbuffer.ui.disable".T())
                    .WithClickFunction(delegate
                    {
                        foreach(IngredientBufferComp comp in activeBuffers)
                        {
                            if (comp.IsReachableForCommonAction)
                            {
                                comp.buffer.IsActive = false;
                                comp.GetUIBlock().NeedsListRebuild = true;
                            }
                        }
                        s.Sig.HideContextMenu.Send();
                        activeBuffersBlock.NeedsListRebuild = true;
                    });
                base.AddEntityCycle(activeBuffersBlock, activeBuffers, () => this.activeBuffersCycleIdx, () => this.activeBuffersCycleIdx++);
            }
            if(activeBuffers.Count > 0)
            {
                activeBuffersBlock.UpdateText(Units.XNum(activeBuffers.Count));
                view.AddBlock(activeBuffersBlock);
            }

            if (inactiveBuffersBlock == null)
            {
                inactiveBuffersBlock = UDB.Create("common_action", UDBT.ITextBtn, "Icons/Color/Store", "ingredientbuffer.common.action.buffer.disabled".T())
                    .WithText2("ingredientbuffer.ui.enable".T())
                    .WithClickFunction(delegate
                    {
                        foreach (IngredientBufferComp comp in inactiveBuffers)
                        {
                            if (comp.IsReachableForCommonAction)
                            {
                                comp.buffer.IsActive = true;
                                comp.GetUIBlock().NeedsListRebuild = true;
                            }
                        }
                        s.Sig.HideContextMenu.Send();
                        buffersBlock.NeedsListRebuild = true;
                    });
                base.AddEntityCycle(inactiveBuffersBlock, inactiveBuffers, () => this.inactiveBuffersCycleIdx, () => this.inactiveBuffersCycleIdx++);
            }
            if(inactiveBuffers.Count > 0)
            {
                inactiveBuffersBlock.UpdateText(Units.XNum(inactiveBuffers.Count));
                view.AddBlock(inactiveBuffersBlock);
            }

            if (buffersBlock == null)
            {
                buffersBlock = UDB.Create("common_action", UDBT.ITextBtn, "Icons/Color/Warning", "ingredientbuffer.common.action.eject.all")
                    .WithText2(T.Eject)
                    .WithClickFunction(delegate
                    {
                        foreach (IngredientBufferComp comp in buffers)
                        {
                            if (comp.IsReachableForCommonAction)
                            {
                                comp.buffer.TryEjectBuffer(true);
                                comp.UpdateUIDetails();
                            }
                        }
                    });
                base.AddEntityCycle(buffersBlock, buffers, () => buffersCycleIdx, () => this.buffersCycleIdx++);
            }
            if (buffers.Count > 0)
            {
                buffersBlock.UpdateText(Units.XNum(buffers.Count));
                view.AddBlock(buffersBlock);
            }
        }

        public override void ResetState()
        {
            buffers.Clear();
            activeBuffers.Clear();
            inactiveBuffers.Clear();
            buffersCycleIdx = 0;
            activeBuffersCycleIdx = 0;
            inactiveBuffersCycleIdx = 0;
        }
    }
}
