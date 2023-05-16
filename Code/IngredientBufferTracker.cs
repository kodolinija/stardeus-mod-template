using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Game;
using Game.AI;
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
                buffer.testvalue = UnityEngine.Random.Range(0, 1000);
                buffer.IsActive = true;
                crafterBuffer.Add(comp, buffer);
            }
        }

        public static void OnSave(CrafterComp comp, ComponentData data)
        {
            D.Err("OnSave");
            data.SetInt("test_rand", crafterBuffer[comp].testvalue);
            crafterBuffer[comp].OnSave(data);
        }

        public static void OnLoad(CrafterComp comp, ComponentData data)
        {
            D.Err("OnLoad");
            IngredientBuffer buffer = new IngredientBuffer(comp);
            buffer.testvalue = data.GetInt("test_rand", UnityEngine.Random.Range(0, 1000));
            buffer.OnLoad(data);
            crafterBuffer.Add(comp, buffer);
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

        //cannot detour OnRemove without modifying BaseComponent<T>.OnRemove or other methods
        //TODO impl with ghost comp
        public static void OnRemove(CrafterComp comp)
        {
            D.Err("OnRemove");
        }

        [Obsolete]
        public static int getInt(CrafterComp comp)
        {
            return crafterBuffer[comp].testvalue;
        }
        [Obsolete]
        public static void incInt(CrafterComp comp)
        {
            crafterBuffer[comp].testvalue += 1;
        }
        [Obsolete]
        public static string peekBuffer(CrafterComp comp)
        {
            IngredientBuffer buffer=crafterBuffer[comp];
            StringBuilder sb=new StringBuilder();
            sb.Append("isActive: ").Append(buffer.IsActive).AppendLine();
            sb.Append("fillCompletelyBeforeCrafting: ").Append(buffer.fillCompletelyBeforeCrafting).AppendLine();
            sb.Append("ingredients: ").AppendLine();
            if(buffer.ingredients==null)
                return sb.Append("null").ToString();
            foreach (Mat mat in buffer.ingredients)
                sb.Append(mat.StackSize).Append("/").Append(mat.MaxStackSize).Append(" ").Append(mat.Type.NameT).AppendLine();
            return sb.ToString();
        }
        [Obsolete]
        public static void toggleActive(CrafterComp comp)
        {
            crafterBuffer[comp].IsActive = !crafterBuffer[comp].IsActive;
        }
    }
}
