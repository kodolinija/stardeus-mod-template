using System.Collections.Generic;
using Game.Constants;
using Game.Data;
using Game.Utils;
using Game.CodeGen;
using UnityEngine;
using Game.Systems.AI;
using KL.Utils;

namespace Game.Components {
    /// <summary>
    /// WARNING Don't forget to replace BaseComponent<ExampleComp>
    /// with correct component class name
    /// </summary>
    public sealed class ExampleModComp : BaseComponent<ExampleModComp>, IUIDataProvider,
            IUIContextMenuProvider, IAIGoalProvider, IUIMultiSelectable, IUISubmenuProvider {

        /// <summary>
        /// Add the following with correct class name to register
        /// the component at runtime when mod loads:
        /// AddComponentPrototype(new ExampleModComp());
        /// </summary>
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.
            SubsystemRegistration)]
        private static void Register() {
            AddComponentPrototype(new ExampleModComp());
        }

        private int energyCost;
        // If you want this to be an electric device
        private ElectricNodeComp elNode;
        private UDB dataBlock;
        public string CommonActionId => "See other common actions";
        public bool IsReachableForCommonAction => true;
        public bool HasSubmenuNow => true;
        public string SubmenuTitle => "submenu.title".T();


        protected override void OnConfig() {
            energyCost = Config.GetInt(PropertyIdH.EnergyCost);
        }

        public override void OnSave() {
            var data = GetOrCreateData();
            data.SetInt("EnergyCost", energyCost);
        }

        protected override void OnLoad(ComponentData data) {
            energyCost = data.GetInt("EnergyCost", 0);
        }

        public override void OnReady(bool wasLoaded) {
            // Usually it's safer to use OnLateReady, because all other components
            // will be configured by then
        }

        public override void OnLateReady(bool wasLoaded) {
            // This is where you would put code that executes after the device
            // is placed with the build tool (but won't be built yet),
            // or after the game was loaded for the first time
        }

        public override void Receive(IComponent sender, int message) {
            // This is the right way to hook into the electricity system
            if (message == MsgIdH.ElectricNodeAdded) {
                if (sender is ElectricNodeComp elNode) {
                    this.elNode = elNode;
                    // This device will attempt to consume the defined energy cost when plugged in
                    elNode.SetConsumerWantedInput(energyCost);
                    elNode.AddAfterTick(this, AfterTickGrid);
                }
            }
            if (message == MsgIdH.ConstructionFinished) {
                D.Warn("The example device was constructed");
            }
            // See MsgId / MsgIdH classes to find out what other signals you can receive
        }

        //This runs every 10 ticks.
        private void AfterTickGrid() {
            if (!elNode.IsPowerable) {
                // The device is disconnected or turned off
            }
            if (elNode.IsConsuming) {
                // device is consuming power, it can now perform something.
            }

            // NEVER ship your mods with such logs, as they would be very noisy
            // and would clog the game log files!
            // Logging in frequently called methods should only be used during
            // development!
            // D.Warn("Tick in component: {0}", this);
        }

        public override void OnRemove() {
            D.Warn("The example device was removed: {0}", this);
        }

        public void OnGoalChange(AIGoal goal, AIGoalState from, AIGoalState to) {
            // This will be called whenever a goal state transitions
        }

        public void OnGoalLoad(AIGoal goal) {
            // When game loads, the AI system will call this method with the goal
            // for this device if such goal exists.
        }

        public UDB GetUIBlock() {
            // If it's not an energy enabled device, remove the isReachable check
            if (!Tile.IsConstructed || !Tile.ENode.IsReachable) {
                return null;
            }
            dataBlock ??= UDB.Create(this, UDBT.IText, IconId.CQuestion,
                "some.title".T()).WithGroupId(UDBGH.Management);
            UpdateUIBlock(false);
            return dataBlock;
        }

        private void UpdateUIBlock(bool wasUpdated) {
            if (wasUpdated && dataBlock?.IsShowing != true) { return; }
            // TODO implement

            dataBlock.UpdateTitle("some.title".T());
        }

        public void GetUIDetails(List<UDB> res) {
            res.Add(UDB.Create(this,
                    UDBT.DText,
                    IconId.CMissing,
                    "item.name".T())
                        // In translations item.text = "Foo bar {0} {1}"
                        // would output "Foo bar 1 2"
                        .WithText("item.text".T(1, 2)));
        }

        public void ContextActions(List<UDB> res) {
            // You can add different items in the context menu, the
            // following will show info panel details submenu as the context menu
            GetUIDetails(res);
        }

        public override string ToString() {
            return $" * Example [EnergyCost: {energyCost}. Entity: {entity}]";
        }
    }
}