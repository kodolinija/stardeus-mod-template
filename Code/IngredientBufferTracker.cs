using System.Collections.Generic;
using Game;
using Game.Components;
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
            D.Err("OnGameIdChanged");
            crafterBuffer.Clear();
        }

        public static void OnLateReady(CrafterComp comp)
        {
            D.Err("OnLateReady");
            
            if (!crafterBuffer.ContainsKey(comp))
            {
                //newly built assembler compatibility
                IngredientBuffer buffer = new IngredientBuffer(comp);
                buffer.IsActive = true;
                crafterBuffer.Add(comp, buffer);
            }
            IngredientBufferComp bufferComp = comp.Entity.GetComponent<IngredientBufferComp>();
            if (bufferComp == null)
            {
                //dynamic CrafterComp support
                bufferComp = new IngredientBufferComp();
                comp.Entity.AddComponent(bufferComp);
            }
            crafterBuffer[comp].wrapper = bufferComp;
            bufferComp.buffer = crafterBuffer[comp];
        }

        public static void OnSave(CrafterComp comp, ComponentData data)
        {
            D.Err("OnSave");
            crafterBuffer[comp].OnSave(data);
        }

        public static void OnLoad(CrafterComp comp, ComponentData data)
        {
            D.Err("OnLoad");
            IngredientBuffer buffer = new IngredientBuffer(comp);
            crafterBuffer.Add(comp, buffer);
            buffer.OnLoad(data);
        }

        public static void RebuildingredientsReq(CrafterComp comp)
        {
            crafterBuffer[comp].RebuildIngredientsReq();
        }

        public static void ProvideRequestedMat(CrafterComp comp, UnstoredMatComp unstoredMat)
        {
            crafterBuffer[comp].ProvideRequestedMat(unstoredMat);
        }

        public static void FillFromBuffer(CrafterComp comp)
        {
            crafterBuffer[comp].FillFromBuffer();
        }

        public static void SwitchToCrafting(CrafterComp comp)
        {
            IngredientBuffer buffer=crafterBuffer[comp];
            //it's not redundant!
            buffer.IsActive = buffer.IsActive;
            buffer.wrapper.OnRecipeChange();
        }

        public static void StopProducing(CrafterComp comp)
        {
            crafterBuffer[comp].wrapper.GetUIBlock().NeedsListRebuild = true;
            crafterBuffer[comp].TryEjectBuffer();
            crafterBuffer[comp].RefillThreshold = 1;
        }

        //cannot detour OnRemove without modifying BaseComponent<T>.OnRemove or other methods
        //TODO impl with ghost comp
        public static void OnRemove(CrafterComp comp)
        {
            D.Err("OnRemove");
        }
    }
}
