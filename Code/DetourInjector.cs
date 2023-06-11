using System;
using System.Linq;
using System.Reflection;
using System.Collections;
using Game.UI;
using Game.Rendering;
using Game.Components;
using KL.Utils;
using KL.Randomness;
using UnityEngine;

namespace IngredientBuffer
{
    internal static class DetourInjector
    {
        private static string AssemblyName => Assembly.GetAssembly(typeof(DetourInjector)).FullName.Split(new char[] { ',' }).First<string>();

        public static void Info(string text)
        {
            GetCoroutines().StartCoroutine(DelayedPopup("Icons/Color/Info", Game.Constants.T.Information, text));
        }
        public static void Warning(string text)
        {
            GetCoroutines().StartCoroutine(DelayedPopup("Icons/Color/Warning", Game.Constants.T.Warning, text));
        }

        static FieldInfo coroutineField = typeof(Coroutines).GetField("instance", BindingFlags.Static | BindingFlags.NonPublic);
        private static Coroutines GetCoroutines()
        {
            return (Coroutines)coroutineField.GetValue(null);
        }

        public static IEnumerator DelayedPopup(string icon, string title, string text)
        {
            while (!RenderingService.Sprites.Contains(icon))
            {
                yield return (object)new WaitForSecondsRealtime(1f);
            }
            yield return (object)new WaitForSecondsRealtime(Rng.URange(0.5f, 1f));
            UIPopupWidget.Spawn(icon, title, text);
        }

        [RuntimeInitializeOnLoadMethod]
        private static void init()
        {
            Inject();
        }

        public static void Inject()
        {
            try
            {
                if (!DoInject())
                {
                    Warning("[" + AssemblyName + "] Failed to inject properly: method not found");
                }
                else
                {
                    Info("[" + AssemblyName + "] Detour complete.");
                }
            }
            catch (Exception e)
            {
                D.Err("[" + AssemblyName + "] Injection failed!");
                D.Err(e.StackTrace);
                Warning("[" + AssemblyName + "] Failed to inject properly, see Player.log for error message.");
            }
        }

        private static bool DoInject()
        {
            System.Collections.Generic.List<MethodInfo> source = new System.Collections.Generic.List<MethodInfo>();
            System.Collections.Generic.List<MethodInfo> method = new System.Collections.Generic.List<MethodInfo>();
            BindingFlags Public = BindingFlags.Instance | BindingFlags.Public;
            BindingFlags NonPublic = BindingFlags.NonPublic | BindingFlags.Instance;
            BindingFlags Any = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;

            Type ts = typeof(CrafterComp);
            Type tm = typeof(CrafterCompModding);

            source.Add(ts.GetMethod("OnLateReady", Public));
            method.Add(tm.GetMethod("OnLateReady", Any));

            source.Add(ts.GetMethod("OnSave", Public));
            method.Add(tm.GetMethod("OnSave", Any));

            source.Add(ts.GetMethod("OnLoad", NonPublic));
            method.Add(tm.GetMethod("OnLoad", Any));

            source.Add(ts.GetMethod("RebuildIngredientsReq", NonPublic));
            method.Add(tm.GetMethod("RebuildIngredientsReq", Any));

            source.Add(ts.GetMethod("ProvideRequestedMat", Public));
            method.Add(tm.GetMethod("ProvideRequestedMat", Any));

            source.Add(ts.GetMethod("SpawnCraftable", NonPublic));
            method.Add(tm.GetMethod("SpawnCraftable", Any));

            source.Add(ts.GetMethod("SwitchToCrafting", Public));
            method.Add(tm.GetMethod("SwitchToCrafting", Any));

            source.Add(ts.GetMethod("StopProducing", Public));
            method.Add(tm.GetMethod("StopProducing", Any));

            source.Add(ts.GetMethod("RelocateTo", Public));
            method.Add(tm.GetMethod("RelocateTo", Any));

            source.Add(ts.GetMethod("CheckMissingIngredients", NonPublic));
            method.Add(tm.GetMethod("CheckMissingIngredients", Any));


            if (source.Count != method.Count)
                return false;
            for (int i = 0; i < source.Count; i++)
            {
                MethodInfo s = source[i];
                MethodInfo m = method[i];
                if (s == null || m == null)
                    return false;
                DoDetour(s, m);
            }

            return true;
        }

        public unsafe static void DoDetour(MethodInfo source, MethodInfo destination)
        {
            if (IntPtr.Size == 8)
            {
                byte* arg_136_0 = (byte*)source.MethodHandle.GetFunctionPointer().ToInt64();
                long num = destination.MethodHandle.GetFunctionPointer().ToInt64();
                byte* ptr = arg_136_0;
                long* ptr2 = (long*)(ptr + 2);
                *ptr = 72;
                ptr[1] = 184;
                *ptr2 = num;
                ptr[10] = 255;
                ptr[11] = 224;
            }
            else
            {
                int num2 = source.MethodHandle.GetFunctionPointer().ToInt32();
                int arg_1A6_0 = destination.MethodHandle.GetFunctionPointer().ToInt32();
                byte* ptr3 = (byte*)num2;
                int* ptr4 = (int*)(ptr3 + 1);
                int num3 = arg_1A6_0 - num2 - 5;
                *ptr3 = 233;
                *ptr4 = num3;
            }
        }
    }
}
