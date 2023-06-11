using System.Collections.Generic;
using System.Reflection;
using Game;
using Game.AI;
using Game.Commands;
using Game.Components;
using Game.Constants;
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

		static FieldInfo showingUnconfiguredIcon = typeof(CrafterComp).GetField("showingUnconfiguredIcon", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo demandBlock = typeof(CrafterComp).GetField("demandBlock", BindingFlags.NonPublic | BindingFlags.Instance);
		static MethodInfo IngredientsFor = typeof(CrafterComp).GetMethod("IngredientsFor", BindingFlags.NonPublic | BindingFlags.Instance);
		//static MethodInfo CheckMissingIngredients = typeof(CrafterComp).GetMethod("CheckMissingIngredients", BindingFlags.NonPublic | BindingFlags.Instance);
		static MethodInfo MaybeHintCraftingTargetInventory = typeof(CrafterComp).GetMethod("MaybeHintCraftingTargetInventory", BindingFlags.NonPublic | BindingFlags.Instance);

		static FieldInfo idleGroupId = typeof(CrafterComp).GetField("idleGroupId", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo idleTitle = typeof(CrafterComp).GetField("idleTitle", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo colChoice = typeof(CrafterComp).GetField("colChoice", BindingFlags.NonPublic | BindingFlags.Instance);
		static MethodInfo CancelHaulingAd = typeof(CrafterComp).GetMethod("CancelHaulingAd", BindingFlags.NonPublic | BindingFlags.Instance);
		static MethodInfo HideIdleNotification = typeof(CrafterComp).GetMethod("HideIdleNotification", BindingFlags.NonPublic | BindingFlags.Instance);
		static FieldInfo ingredientBlocks = typeof(CrafterComp).GetField("ingredientBlocks", BindingFlags.NonPublic | BindingFlags.Instance);

		static FieldInfo showingGoalReachedIcon = typeof(CrafterComp).GetField("showingGoalReachedIcon", BindingFlags.NonPublic | BindingFlags.Instance);
		static MethodInfo CheckOperator = typeof(CrafterComp).GetMethod("CheckOperator", BindingFlags.NonPublic | BindingFlags.Instance);

		public static Mat[] GetIngredients(this CrafterComp This)
        {
			return (Mat[])ingredients.GetValue(This);
        }
		public static Advert GetCurrentAd(this CrafterComp This)
        {
			return (Advert)currentAd.GetValue(This);
        }
		public static bool HasCurrentAd(this CrafterComp This)
        {
			Advert ad=(Advert)currentAd.GetValue(This);
			return ad != null && !ad.IsCancelled && !ad.IsCompleted;
        }
		public static void TriggerHaulingAdNow(this CrafterComp This)
        {
			if (This.MissingMats.Count == 0 || This.HasCurrentAd())
				return;
			Advert ad = This.CreateAdvert("Hauling", "Icons/Color/Store", T.HaulIngredients)
							.WithPromise(NeedIdH.Purpose, 5).MarkAsWork(false)
							.WithPriority(((int)craftPriority.GetValue(This)))
							.AndThen("GatherRawMaterials", T.GatherMaterials, NeedIdH.Purpose, 5)
							.Publish(true);
			currentAd.SetValue(This, ad);
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
				if (ingredients.GetValue(This) == null)
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

			IngredientBufferTracker.RebuildIngredientsReq(This);

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
						if (wantedAmount == 0)
							continue;
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

		public static void SwitchToCrafting(this CrafterComp This, Craftable craftable)
		{
			if (craftable != null)
			{
				if (craftable.ProductDef == null)
				{
					D.Err("Cannot switch to crafting {0}. Product def is not available!", craftable.ProductDefId);
					UIPopupWidget.Spawn("Icons/Color/Warning", "MISCONFIGURED CRAFTABLE", "Cannot craft <b>" + craftable.ProductDefId + "</b> - Definition does not exist. It could be a problem with a mod.");
				}
				else
				{
					if ((bool)showingUnconfiguredIcon.GetValue(This))
					{
						showingUnconfiguredIcon.SetValue(This,false);
						This.HideInfoIcon();
					}
					demandBlock.SetValue(This, null);
					This.Demand = CraftingDemand.CreateFor(craftable);
					ingredients.SetValue(This,IngredientsFor.Invoke(This,new object[] { craftable }));
					This.Progress = 0f;

					IngredientBufferTracker.SwitchToCrafting(This);

					((ExtraInfoComp)extraInfo.GetValue(This))?.ShowInfoIcon(This.Demand.Product.Preview, This.Demand.Product.NameT);
					This.CheckMissingIngredients(true);
					UpdateExtraInfo.Invoke(This,null);
					MaybeHintCraftingTargetInventory.Invoke(This,null);
				}
			}
		}

		public static void StopProducing(this CrafterComp This)
		{
			This.Demand = null;
			idleGroupId.SetValue(This, null);
			idleTitle.SetValue(This, null);
			This.Progress = 0f;
			colChoice.SetValue(This, null);
			CancelHaulingAd.Invoke(This, new object[] { "Stopped production" });
			HideIcon.Invoke(This,null);
			HideIdleNotification.Invoke(This,null);
			UpdateExtraInfo.Invoke(This,null);
			((MatDeficitEventHolder)deficitEv.GetValue(This)).Clear();
			Mat[] array=(Mat[])ingredients.GetValue(This);
			if (!Arrays.IsEmpty(array))
			{
				foreach (Mat mat in array)
				{
					if (mat.StackSize >= 1)
					{
						EntityUtils.SpawnRawMaterial(mat, This.Tile.Transform.WorkSpot, 0.5f, true, true);
					}
				}
				if (demandBlock.GetValue(This) != null)
				{
					((UDB)demandBlock.GetValue(This)).NeedsListRebuild = true;
				}
				ingredients.SetValue(This, null);
				((Dictionary<MatType,UDB>)ingredientBlocks.GetValue(This)).Clear();
			}

			IngredientBufferTracker.StopProducing(This);
		}

		public static void RelocateTo(this CrafterComp This, Entity target)
		{
			This.CopyConfigTo(target.GetComponent<ICopyableComp>());

			IngredientBufferTracker.RelocateTo(This, target);
		}

		public static bool CheckMissingIngredients(this CrafterComp This, bool checkIfProducedEnough)
		{
			if (checkIfProducedEnough && (This.Demand?.HasProducedEnough(This.S) ?? true))
			{
				return false;
			}
			if (((Advert)currentAd.GetValue(This))?.IsCancelled ?? false)
			{
				currentAd.SetValue(This, null);
			}
			//move this check after ingredient check so the crafter can operate while the buffer is being filled
			/*
			Advert advert = (Advert)currentAd.GetValue(This);
			if (advert != null && !advert.IsCompleted)
			{
				return false;
			}*/
			bool flag = false;
			Mat[] array = This.GetIngredients();
			for (int i = 0; i < array.Length; i++)
			{
				Mat mat = array[i];
				if (mat.Diff > 0)
				{
					flag = true;
					break;
				}
			}
			if (!flag)
			{
				if ((bool)showingGoalReachedIcon.GetValue(This))
				{
					This.HideInfoIcon();
					showingGoalReachedIcon.SetValue(This,false);
				}
				return true;
			}

			//moved advert check
			Advert advert = (Advert)currentAd.GetValue(This);
			if (advert != null && !advert.IsCompleted)
			{
				return false;
			}

			This.RebuildIngredientsReq();
			CancelHaulingAd.Invoke(This,new object[] { "Has missing ingredients" });
			CheckOperator.Invoke(This, new object[] { false });
			currentAd.SetValue(This, This.CreateAdvert("Hauling", "Icons/Color/Store", T.HaulIngredients).WithPromise(NeedIdH.Purpose, 5).MarkAsWork(false)
				.WithPriority((int)craftPriority.GetValue(This))
				.AndThen("GatherRawMaterials", T.GatherMaterials, NeedIdH.Purpose, 5)
				.Publish(true));
			return false;
		}
	}
}
