using System.Collections.Generic;
using ExampleMod.UI;
using Game.Components;
using Game.Constants;
using Game.Data;
using Game.UI;
using Game.Systems;
using KL.Utils;
using UnityEngine;
using Game.Utils;

namespace ExampleMod.Systems {
    public sealed class ExampleModSys : GameSystem, IOverlayProvider, ISaveable {
        // The convention is that all systems end with Sys, and SysId is equal to the class name
        public const string SysId = "ExampleModSys";
        public override string Id => SysId;
        // If your system can work in sandbox too, set this to false
        public override bool SkipInSandbox => true;

        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
        private static void Register() {
            GameSystems.Register(SysId, () => new ExampleModSys());
        }

        // If your system adds some mechanic that may not be compatible with
        // old saves, you have to set the MinRequiredVersion
        //public override string MinRequiredVersion => "0.6.89";

        // By returning something in the Overlays list, your system can add
        // buttons in the top right section of the game UI.
        // Those buttons will toggle the overlays.
        // Almost always there will be just one OverlayInfo in the list,
        // The only exceptions right now are:
        // - EquilibriumSys (Oxygen, Heat, Airtightness and Insulation)
        // - HiveMindSys (Beings, Tasks)
        public List<OverlayInfo> Overlays => overlays;
        private readonly List<OverlayInfo> overlays = new();

        private ExampleOverlayUI ui;
        // Public so that the UI can use it
        public int SomeVariable;

        protected override void OnInitialize() {
            overlays.Clear();
            overlays.Add(overlayInfo);
            ui = new ExampleOverlayUI(this);

            S.Sig.AfterLoadState.AddListener(OnLoadSave);
            S.Sig.AreasInitialized.AddListener(OnAreasInit);
            S.Sig.ToggleOverlay.AddListener(OnToggleOverlay);
        }

        // You will have to create Graphics/Icons/White/ExampleModIcon.png
        private readonly OverlayInfo overlayInfo = new OverlayInfo(
            OverlayType.Controls, SysId, "Icons/White/ExampleModIcon");

        private void OnToggleOverlay(OverlayInfo info, bool on) {
            D.Err("Toggling overlay: {0} -> {1}", info.Id, on);
            if (!on || info.Id != SysId) {
                ui.HideUI();
            } else {
                ui.ShowUI();
            }
        }

        private void OnLoadSave(GameState state) {
            state.Clock.OnTick.AddListener(OnTick);
            UIPopupWidget.Spawn(IconId.CWarning, "warning".T(),
                "Note for mod developer. ExampleModSys should be removed from your mod.<br>A new overlay button was added to the <b>bottom right</b> of the screen.");
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