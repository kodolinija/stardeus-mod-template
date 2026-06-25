using Game.Constants;
using Game.Data;
using Game.Utils;
using Game.CodeGen;
using Game.Systems.AI;
using KL.Utils;

namespace Game.Components {
    /// <summary>
    /// WARNING Don't forget to replace BaseComponent<ExampleComp>
    /// with correct component class name
    /// </summary>
    public sealed class ExampleModComp : BaseComponent<ExampleModComp>, IAIGoalProvider {

        /// <summary>
        /// Add the following with correct class name to register
        /// the component at runtime when mod loads:
        /// AddComponentPrototype(new ExampleModComp());
        /// Mod DLLs are loaded before any [SelfInit] stage runs, so plain
        /// [SelfInit] (default stage CoreDefs) works here exactly like it
        /// does for core components (e.g. LightSourceComp, WithFuseComp) --
        /// </summary>
        [SelfInit]
        private static void Register() {
            AddComponentPrototype(new ExampleModComp());
        }

        private int energyCost;
        // Exposed for ExampleTab.cs, which displays this in the entity panel.
        public int EnergyCost => energyCost;

        // A small piece of mutable, saved state, just so ExampleTab.cs has
        // something to read AND write (and demonstrate ReloadTab()).
        private bool demoFlag;
        public bool DemoFlag {
            get => demoFlag;
            set => demoFlag = value;
        }

        // If you want this to be an electric device
        private ElectricNodeComp elNode;

        protected override void OnConfig() {
            energyCost = Config.GetInt(PropertyIdH.EnergyCost);
        }

        public override void OnSave() {
            var data = GetOrCreateData();
            data.SetInt("EnergyCost", energyCost);
            data.SetBool("DemoFlag", demoFlag);
        }

        protected override void OnLoad(ComponentData data) {
            energyCost = data.GetInt("EnergyCost", 0);
            demoFlag = data.GetBool("DemoFlag", false);
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

        // Entity-panel UI for this component lives in ExampleTab.cs (see
        // Assets/Scripts/Game/Systems/UIUX/Handlers/EntityTabs/ in the main project
        // for the BaseEntityTab API this mod targets). The old IUIDataProvider /
        // IUISubmenuProvider / IUIContextMenuProvider / UDB system has been removed.

        public override string ToString() {
            return $" * Example [EnergyCost: {energyCost}. Entity: {entity}]";
        }
    }
}
