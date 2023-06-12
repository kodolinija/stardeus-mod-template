using System.Collections.Generic;
using System.Diagnostics;
using Game;
using Game.Components;
using Game.Data;
using KL.Utils;
using UnityEngine;

namespace IngredientBuffer
{
    public class IngredientBufferTracker
    {
        private static Dictionary<CrafterComp,IngredientBuffer> crafterBuffer=new Dictionary<CrafterComp, IngredientBuffer>();

        [RuntimeInitializeOnLoadMethod]
        private static void Init()
        {
            The.SysSig.GameIdChanged.AddListener(OnGameIdChanged);
        }

        public static void OnGameIdChanged(int id)
        {
            Info("OnGameIdChanged");

            crafterBuffer.Clear();
        }

        public static void OnLateReady(CrafterComp comp)
        {
            Info("OnLateReady");
            
            if (!crafterBuffer.ContainsKey(comp))
            {
                //newly built assembler compatibility
                IngredientBuffer buf = new IngredientBuffer(comp);
                buf.IsActive = true;
                crafterBuffer.Add(comp, buf);
            }
            IngredientBufferComp bufferComp = comp.Entity.GetComponent<IngredientBufferComp>();
            if (bufferComp == null)
            {
                //dynamic CrafterComp support
                bufferComp = new IngredientBufferComp();
                comp.Entity.AddComponent(bufferComp);
            }
            IngredientBuffer buffer = crafterBuffer[comp];
            buffer.wrapper = bufferComp;
            bufferComp.buffer = buffer;

            //activate threshold check and publish hauling ad if possible
            //moved from OnLoad() because Entity.PosProvider may not have been assigned
            buffer.RefillThreshold = buffer.RefillThreshold;
        }

        public static void OnSave(CrafterComp comp, ComponentData data)
        {
            Info("OnSave");

            crafterBuffer[comp].OnSave(data);
        }

        public static void OnLoad(CrafterComp comp, ComponentData data)
        {
            Info("OnLoad");

            IngredientBuffer buffer = new IngredientBuffer(comp);
            crafterBuffer.Add(comp, buffer);
            buffer.OnLoad(data);
        }

        public static void RebuildIngredientsReq(CrafterComp comp)
        {
            if (!crafterBuffer.ContainsKey(comp))
            {
                Info("RebuildIngredientsReq: CrafterComp not in tracker! " + comp + "@" + comp.Entity.Position);
                return;
            }
            crafterBuffer[comp].RebuildIngredientsReq();
        }

        public static void ProvideRequestedMat(CrafterComp comp, UnstoredMatComp unstoredMat)
        {
            if (!crafterBuffer.ContainsKey(comp))
            {
                Info("ProvideRequestedMat: CrafterComp not in tracker! " + comp + "@" + comp.Entity.Position);
                return;
            }
            crafterBuffer[comp].ProvideRequestedMat(unstoredMat);
        }

        public static void FillFromBuffer(CrafterComp comp)
        {
            if (!crafterBuffer.ContainsKey(comp))
            {
                Info("FillFromBuffer: CrafterComp not in tracker! " + comp + "@" + comp.Entity.Position);
                return;
            }
            crafterBuffer[comp].FillFromBuffer();
        }

        public static void SwitchToCrafting(CrafterComp comp)
        {
            if (!crafterBuffer.ContainsKey(comp))
            {
                Info("SwitchToCrafting: CrafterComp not in tracker! " + comp + "@" + comp.Entity.Position);
                return;
            }
            IngredientBuffer buffer=crafterBuffer[comp];
            //it's not redundant!
            buffer.IsActive = buffer.IsActive;
            buffer.wrapper.OnRecipeChange();
        }

        public static void StopProducing(CrafterComp comp)
        {
            if (!crafterBuffer.ContainsKey(comp))
            {
                Info("StopProducing: CrafterComp not in tracker! " + comp + "@" + comp.Entity.Position);
                return;
            }
            IngredientBuffer buffer = crafterBuffer[comp];
            buffer.wrapper.GetUIBlock().NeedsListRebuild = true;
            buffer.TryEjectBuffer();
            buffer.RefillThreshold = 1;
        }

        //cannot detour OnRemove without modifying BaseComponent<T>.OnRemove or other methods
        //this is the bypass by using IngredientBufferComp.OnRemove()
        //can indeed handle vanilla situations like destruction or deconstruction
        //but cannot capture remove event if the CrafterComp is destroyed dynamically
        public static void Remove(IngredientBuffer buffer)
        {
            Info("OnRemove");

            if (buffer.comp == null)
            {
                D.Err("[IngredientBuffer] Trying to remove a buffer without CrafterComp reference!");
                return;
            }
            crafterBuffer.Remove(buffer.comp);
            buffer.TryEjectBuffer();
        }

        public static void RelocateTo(CrafterComp comp, Entity target)
        {
            Info("RelocateTo");

            if (!crafterBuffer.ContainsKey(comp))
            {
                D.Err("[IngredientBuffer] Cannot find buffer on the target of relocation! Is this sandbox mode (InstantBuild)?");
                return;
            }
            IngredientBufferComp from = crafterBuffer[comp].wrapper;
            IngredientBufferComp to = target.GetComponent<IngredientBufferComp>();
            if (to == null)
            {
                D.Err("[IngredientBuffer] Cannot find an IngredientBufferComp on the target of relocation!");
                return;
            }
            from.CopyConfigTo(to);
        }

        [Conditional("DEBUG")]
        public static void Info(string s)
        {
            D.Err(s);
        }
    }
}
