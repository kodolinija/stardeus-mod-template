using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using Game;
using Game.AI;
using Game.Commands;
using Game.Components;
using Game.Data;
using Game.UI;
using KL.Randomness;
using KL.Utils;
using UnityEngine;

namespace IngredientBuffer
{
    public static class CrafterCompModding
    {
		static FieldInfo extraInfo = typeof(CrafterComp).GetField("extraInfo", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo tuneCraftSpeed = typeof(CrafterComp).GetField("tuneCraftSpeed", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo tuneCraftEnergyCost = typeof(CrafterComp).GetField("tuneCraftEnergyCost", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo deficitEv = typeof(CrafterComp).GetField("deficitEv", BindingFlags.NonPublic | BindingFlags.Instance);
		static MethodInfo UpdateExtraInfo = typeof(CrafterComp).GetMethod("UpdateExtraInfo", BindingFlags.NonPublic | BindingFlags.Instance);

		static MethodInfo GetOrCreateData = typeof(CrafterComp).GetMethod("GetOrCreateData", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo craftPriority = typeof(CrafterComp).GetField("craftPriority", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo isIdleWarningsOn = typeof(CrafterComp).GetField("isIdleWarningsOn", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo ingredients = typeof(CrafterComp).GetField("ingredients", BindingFlags.NonPublic | BindingFlags.Instance);

		static MethodInfo SetIngredients = typeof(CrafterComp).GetMethod("SetIngredients", BindingFlags.NonPublic | BindingFlags.Instance);
		static MethodInfo VerifyIngredients = typeof(CrafterComp).GetMethod("VerifyIngredients", BindingFlags.NonPublic | BindingFlags.Instance);

		static FieldInfo currentAd = typeof(CrafterComp).GetField("currentAd", BindingFlags.NonPublic | BindingFlags.Instance);
		static MethodInfo HideIcon = typeof(CrafterComp).GetMethod("HideIcon", BindingFlags.NonPublic | BindingFlags.Instance);

		static FieldInfo amountBlock = typeof(CrafterComp).GetField("amountBlock", BindingFlags.NonPublic | BindingFlags.Instance);

		public static Mat[] GetIngredients(this CrafterComp This)
        {
			return (Mat[])ingredients.GetValue(This);
        }
		public static Advert GetCurrentAd(this CrafterComp This)
        {
			return (Advert)currentAd.GetValue(This);
        }

		public static void OnLateReady(this CrafterComp This, bool wasLoaded)
		{
			extraInfo.SetValue(This,This.Entity.GetRequiredComponent<ExtraInfoComp>(This));
			tuneCraftSpeed.SetValue(This,Tunable.Float(783785663));
			tuneCraftEnergyCost.SetValue(This,Tunable.Float(-974012108));
			if (wasLoaded)
			{
				((MatDeficitEventHolder)deficitEv.GetValue(This)).OnLateReady();
				UpdateExtraInfo.Invoke(This,null);
			}

			IngredientBufferTracker.OnLateReady(This);
		}

		public static void OnSave(this CrafterComp This)
		{
			ComponentData orCreateData = (ComponentData)GetOrCreateData.Invoke(This,null);
			orCreateData.SetFloat("Progress", This.Progress);
			orCreateData.SetInt("Priority", (int)craftPriority.GetValue(This));
			orCreateData.SetInt("TotalProd", This.TotalProduced);
			orCreateData.SetBool("IdleWarn", (bool)isIdleWarningsOn.GetValue(This));
			CraftingDemand.Save(This.Demand, orCreateData);
			if (This.Demand != null)
			{
				((MatDeficitEventHolder)deficitEv.GetValue(This)).Save(orCreateData);
			}
			orCreateData.SetMats("Ingredients", (Mat[])ingredients.GetValue(This));

			IngredientBufferTracker.OnSave(This, orCreateData);
		}

		public static void OnLoad(this CrafterComp This, ComponentData data)
		{
			This.Demand = CraftingDemand.Load(data);
			if (This.Demand != null)
			{
				((MatDeficitEventHolder)deficitEv.GetValue(This)).Load(data);
				ingredients.SetValue(This, data.GetMats("Ingredients", null));
				if (ingredients == null)
				{
					SetIngredients.Invoke(This, null);
				}
				else
				{
					VerifyIngredients.Invoke(This, null);
				}
			}
			isIdleWarningsOn.SetValue(This, data.GetBool("IdleWarn", (bool)isIdleWarningsOn.GetValue(This)));
			craftPriority.SetValue(This, data.GetInt("Priority", (int)craftPriority.GetValue(This)));
			This.TotalProduced = data.GetInt("TotalProd", 0);
			This.Progress = data.GetFloat("Progress", 0f);

			IngredientBufferTracker.OnLoad(This, data);
		}

		public static bool RebuildIngredientsReq(this CrafterComp This)
		{
			This.MissingMats.Clear();
			Mat[] array = (Mat[])ingredients.GetValue(This);
			for (int i = 0; i < array.Length; i++)
			{
				Mat mat = array[i];
				if (mat.Diff >= 1)
				{
					This.MissingMats.Add(new MatRequest
					{
						Type = mat.Type,
						Amount = mat.Diff,
						IsAmountOptional = true,
						Requester = This
					});
				}
			}

			IngredientBufferTracker.RebuildingredientsReq(This);

			return This.MissingMats.Count == 0;
		}

		public static bool ProvideRequestedMat(this CrafterComp This, UnstoredMatComp unstoredMat, Being worker)
		{
			D.Ass(ingredients != null, "Crafter taking ingredients from being while having null ingredients");
			Mat[] array=(Mat[])ingredients.GetValue(This);
			for (int i = 0; i < array.Length; i++)
			{
				Mat mat = array[i];
				if (mat.Type == unstoredMat.Type)
				{
					int diff = mat.Diff;
					if (diff > 0)
					{
						int wantedAmount = Mathf.Min(diff, unstoredMat.StackSize);
						wantedAmount = unstoredMat.Take(mat.Type, null, wantedAmount, (Advert)currentAd.GetValue(This));
						mat.StackSize += wantedAmount;
						array[i] = mat;
						if (mat.StackSize == mat.MaxStackSize)
						{
							((MatDeficitEventHolder)deficitEv.GetValue(This)).ClearIf(mat.Type);
						}
					}
				}
			}

			IngredientBufferTracker.ProvideRequestedMat(This, unstoredMat);

			bool num = This.RebuildIngredientsReq();
			if (num)
			{
				HideIcon.Invoke(This,null);
			}
			return num;
		}

		public static void SpawnCraftable(this CrafterComp This, Craftable craftable)
		{
			Def def = craftable.ProductDef;
			This.Tile.Damageable.AddWear(1f);
			if (def.HasVariations)
			{
				if (This.Demand.ColorId != null)
				{
					foreach (Def variation in def.Variations)
					{
						if (variation.ColorId == This.Demand.ColorId)
						{
							def = variation;
							break;
						}
					}
				}
				if (def.HasVariations)
				{
					def = This.S.Rng.From(def.Variations);
				}
			}
			if (def.IsBeing)
			{
				CmdSpawnBeing cmdSpawnBeing = new CmdSpawnBeing(EntityUtils.CenterOf(This.Tile.Transform.WorkSpot) + Rng.UInsideUnitCircle() * 0.25f, def, false, null, 0f, "Physical", false, null);
				cmdSpawnBeing.Execute(This.S);
				Persona persona = cmdSpawnBeing.Being.Persona.Persona;
				persona.IsClone = persona.Species.IsBiological;
				persona.Age = 0;
				persona.BirthTick = This.S.Ticks;
				if (persona.Species.Type == "Human")
				{
					The.AchievementTracker.Unlock("CloneHuman");
				}
			}
			else if (def.MatType != null)
			{
				int num = craftable.OutputMultiplier;
				if (num < 1)
				{
					num = 1;
				}
				MatStorageComp materialStorage = This.Tile.MaterialStorage;
				if (materialStorage != null && !materialStorage.IsFull)
				{
					This.Tile.MaterialStorage.Store(def.MatType, null, num, null);
				}
				else
				{
					This.S.CmdQ.Enqueue(new CmdSpawnMatByType(def.MatType, num, This.Tile.Transform.WorkSpot, 0f, true, true));
				}
			}
			else
			{
				This.S.CmdQ.Enqueue(new CmdSpawnObj(EntityUtils.CenterOf(This.Tile.Transform.WorkSpot) + Rng.UInsideUnitCircle() * 0.25f, def, true, true));
			}
			This.Progress = 0f;
			Mat[] array = (Mat[])ingredients.GetValue(This);
			for (int i = 0; i < array.Length; i++)
			{
				Mat mat = array[i];
				mat.StackSize = 0;
				array[i] = mat;
			}

			IngredientBufferTracker.FillFromBuffer(This);

			if (((UDB)amountBlock.GetValue(This))?.IsShowing ?? false)
			{
				((UDB)amountBlock.GetValue(This)).NeedsListRebuild = true;
			}
			This.S.Sig.EntityProduced.Send(This.Demand.Product, 1);
			This.Demand.AmountProduced++;
			This.Demand.AmountProducedThis++;
			This.TotalProduced++;
		}

		//TODO move this into ghost comp
		public static void ContextActions(this CrafterComp This, List<UDB> res)
		{
			if (This.Tile.IsConstructed && This.Tile.EnergyNode.IsReachable)
			{
				This.GetUIDetails(res);
			}

			
			res.Add(UDB.Create(This, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "isActive")
				.WithText2("Toggle")
				.WithClickFunction(delegate { IngredientBufferTracker.toggleActive(This); }));
			res.Add(UDB.Create(This, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "buffer")
				.WithText2("Peek")
				.WithClickFunction(delegate { UIPopupWidget.Spawn("Icons/Color/Warning", "Buffer", IngredientBufferTracker.peekBuffer(This)); }));
			res.Add(UDB.Create(This, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "progress to 99%")
				.WithText2("Set")
				.WithClickFunction(delegate { This.Progress = 0.99f; }));
			res.Add(UDB.Create(This, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "missing mats")
				.WithText2("Peek")
				.WithClickFunction(delegate { StringBuilder sb = new StringBuilder();
					foreach(MatRequest mr in This.MissingMats)
						sb.Append(mr.Amount).Append(mr.Type.NameT).AppendLine();
					UIPopupWidget.Spawn("Icons/Color/Warning", "MissingMats",sb.ToString());
				}));


			res.Add(UDB.Create(This, Game.Constants.UDBT.DTextBtn, "Icons/Color/Count", "test value")
				.WithText2(IngredientBufferTracker.getInt(This).ToString())
				.WithClickFunction(delegate { IngredientBufferTracker.incInt(This); }));
		}
	}
}
