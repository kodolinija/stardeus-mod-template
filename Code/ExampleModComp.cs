using System.Collections.Generic;
using Game.AI;
using Game.Components;
using Game.Constants;
using Game.Data;
using Game.Utils;
using UnityEngine;

namespace ExampleMod.Components {
    // WARNING Don't forget to replace BaseComponent<ExampleModComp>
    // with correct component class name
    public sealed class ExampleModComp : BaseComponent<ExampleModComp>, IUIDataProvider,
            IUIContextMenuProvider, IAdvertProvider, IUIMultiSelectable {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.
            SubsystemRegistration)]
        private static void Register() {
            // Uncomment the following with correct class name to register
            // the component at runtime when mod loads
            AddComponentPrototype(new ExampleModComp());
        }

        private int stuff;

        protected override void OnConfig() {
            stuff = Config.GetInt("stuff");
        }

        public override void OnSave() {
            var data = GetOrCreateData();
            data.SetInt("Stuff", stuff);
        }

        protected override void OnLoad(ComponentData data) {
            stuff = data.GetInt("Stuff", 0);
        }

        public override string ToString() {
            return $" * Example [Stuff {stuff}]";
        }

        public override void OnLateReady(bool wasLoaded) {
        }

        public override void OnReady(bool wasLoaded) {
        }

        public override void Receive(IComponent sender, int message) {
        }

        public override void OnRemove() {
        }

        private UDB dataBlock;
        private Advert ad;

        public bool HasCancellableAd => Advert.IsActive(ad);

        public Advert CurrentAdvert => ad;

        public string CommonActionId => "See other common actions";

        public bool IsReachableForCommonAction => true;

        public UDB GetUIBlock() {
            // If it's not an energy enabled device, remove the isReachable check
            if (!Tile.IsConstructed || !Tile.EnergyNode.IsConnected) {
                return null;
            }
            dataBlock ??= UDB.Create(this,
                UDBT.IText,
                IconId.CQuestion,
                "some.title".T());
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
        }

        public void CancelAdvert(string why) {
            if (HasCancellableAd) {
                S.Adverts.Cancel(ad, why);
            }
        }

        public void OnAdvertLoad(Advert ad) {
            this.ad = ad;
        }

        public void OnAdvertCancelled(Advert ad) {
            this.ad = null;
        }

        public void OnAdvertComplete(Advert ad) {
            this.ad = null;
        }
    }
}