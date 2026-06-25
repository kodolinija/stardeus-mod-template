using Game.Components;
using Game.Constants;
using Game.Data;
using Game.Utils;

namespace Game.Systems.UIUX {
    /// <summary>
    /// Demonstrates the current entity-panel UI system: a BaseEntityTab spawning
    /// UISpawn widgets directly. This replaces the removed UDB / IUIDataProvider /
    /// IUISubmenuProvider system that older versions of this template used.
    ///
    /// See Assets/Scripts/Game/Systems/UIUX/Handlers/EntityTabs/HeaterTab.cs in the
    /// main project for another small reference tab, and
    /// Assets/Scripts/Game/Systems/UIUX/Helpers/UISpawnExamples.cs for the full
    /// UIPrefabId -> widget catalog.
    /// </summary>
    public sealed class ExampleTab : BaseEntityTab {
        public const string TabId = "ExampleTab";

        /// <summary>
        /// Mod DLLs are loaded before any [SelfInit] stage runs, so plain [SelfInit]
        /// works here exactly like it does for in-game tabs (e.g. HeaterTab.cs) and
        /// for the component/system registration elsewhere in this mod -- see
        /// </summary>
        [SelfInit]
        private static void Register() {
            RegisterTab(new ExampleTab());
        }

        private Tile tile;
        private ExampleModComp comp;
        private GameState S;

        public override string Id => TabId;
        public override int Order => -10;
        public override string TabName => "example.tab.name".T();

        public override bool ShowFor(GameState s, Tile tile) {
            if (!tile.IsConstructed) { return false; }
            if (tile.ENode?.IsReachable == false) { return false; }
            if (!tile.TryGetComponent<ExampleModComp>(out var c)) { return false; }
            this.tile = tile;
            comp = c;
            S = s;
            return true;
        }

        public override bool LoadContent(WGroup group) {
            var block = UISpawn.Block(lifetime, group, 0);
            int idx = 0;

            // Light/dark background convention: WContent2* prefabs use the darker,
            // interactable-block background. See UISpawnExamples.cs for details.
            var infoRow = UISpawn.Widget<WIconText2>(lifetime,
                UIPrefabId.WContent2Text2, block.Container, idx++);
            infoRow.Load(IconId.CInfo, "example.tab.energy_cost".T(),
                Units.XNum(comp.EnergyCost));

            var toggleRow = UISpawn.Widget<WToggleWithIconText2>(lifetime,
                UIPrefabId.WContent2Text2Toggle, block.Container, idx++);
            toggleRow.Item.Load(IconId.CCog, "example.tab.demo_flag".T(),
                comp.DemoFlag ? "example.tab.demo_flag.on".T() : "example.tab.demo_flag.off".T());
            toggleRow.Toggle.Load(comp.DemoFlag, isOn => {
                comp.DemoFlag = isOn;
                // No persistent widget state in this system (unlike the old UDB
                // dataBlock) -- ReloadTab() disposes the lifetime and re-calls
                // LoadContent/LoadFooter so the row reflects the new value.
                ReloadTab();
            });

            return true;
        }

        public override bool LoadFooter(WGroup group) {
            var resetBtn = UISpawn.Widget<WButtonIconText2>(lifetime,
                UIPrefabId.WContent4Button, group.Container, 0);
            resetBtn.Load(IconId.CCog, T.Reset, null, () => {
                comp.DemoFlag = false;
                ReloadTab();
            });
            return true;
        }

        protected override void Cleanup() {
            tile = null;
            comp = null;
            S = null;
        }
    }
}
