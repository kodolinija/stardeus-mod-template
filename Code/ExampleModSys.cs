using Game.Components;
using Game.Data;
using Game.Systems;
using Game.Utils;
using KL.Utils;

namespace ExampleMod.Systems {
    public sealed class ExampleModSys : GameSystem, ISaveable {
        // The convention is that all systems end with Sys, and SysId is equal to the class name
        public const string SysId = "ExampleModSys";
        public override string Id => SysId;
        // If your system can work in sandbox too, set this to false
        public override bool SkipInSandbox => true;

        // Mod DLLs are loaded before any [SelfInit] stage runs, so plain [SelfInit]
        // (default stage CoreDefs) works here exactly like it does for core systems
        // (e.g. LightSys.Register()) -- see Docs/Architecture/SelfInit.md.
        [SelfInit]
        private static void Register() {
            GameSystems.Register(SysId, () => new ExampleModSys());
        }

        // If your system adds some mechanic that may not be compatible with
        // old saves, you have to set the MinRequiredVersion
        //public override string MinRequiredVersion => "0.6.89";

        // Public so that the UI can use it. See ExampleTab.cs for the entity-panel
        // UI that exposes mod state; this system has no overlay/center-panel UI of
        // its own (the old UDB-based overlay example was removed -- if you need a
        // system-level overlay button, implement IOverlayProvider; see
        // Assets/Scripts/Game/Systems/Light/LightSys.cs in the main project for a
        // current, minimal example).
        public int SomeVariable;

        protected override void OnInitialize() {
            S.Sig.AfterLoadState.AddListener(OnLoadSave);
            S.Sig.AreasInitialized.AddListener(OnAreasInit);
        }

        private void OnLoadSave(GameState state) {
            state.Clock.OnTick.AddListener(OnTick);
        }

        // If your system depends on AreasSys, for example, you may want to
        // start ticking your system only after initial areas have been built
        private void OnAreasInit() {
            D.Warn("Areas initialized");
        }

        private void OnTick(long ticks) {
            D.Warn("Ticking synchronously. Tick: {0}", ticks);
            D.Err("PLEASE REMOVE Clock.OnTick LISTENER IF YOU DON'T NEED IT IN YOUR MOD");
        }

        public override void Unload() {
            // Release the resources here
        }

        public string GetName() {
            return Id;
        }

        // We use ComponentData for saving entity components, but it can be
        // used in systems as well, if the system is marked ISaveable
        private ComponentData data;

        public ComponentData Save() {
            data ??= new ComponentData(0, SysId);
            data.SetInt("SomeVariable", SomeVariable);
            return data;
        }

        public void Load(ComponentData data) {
            this.data = data;
            SomeVariable = data.GetInt("SomeVariable", 0);
        }
    }
}
