using System.Collections.Generic;
using Game.Constants;
using Game.Data;
using Game.Utils;
using KL.I18N;
using UnityEngine;

namespace Game.Components {
    // WARNING Don't forget to replace BaseComponent<ExampleComp> 
    // with correct component class name
    public sealed class ExampleModComp : BaseComponent<ExampleModComp>, IUIDataProvider {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.
            SubsystemRegistration)]
        static void Register() {
            AddComponentPrototype(new ExampleModComp());
        }

        private int stuff;

        protected override void OnConfig() {
            stuff = Config.GetInt("Stuff");
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

        public override void Receive(IComponent sender, string message) {

        }

        public override void OnRemove() {

        }

        private UDB dataBlock;
        public UDB GetUIBlock() {
            if (!Tile.IsConstructed) { return null; }
            if (dataBlock == null) {
                dataBlock = UDB.Create(this, 
                    UDBT.IText, 
                    IconId.CQuestion,
                    "some.title".T());
            }
            UpdateUIBlock(false);
            return dataBlock;
        }

        private void UpdateUIBlock(bool wasUpdated) {
            if (wasUpdated) {
                if (dataBlock == null || !dataBlock.IsShowing) { return; }
            }
            // TODO implement

            dataBlock.WasUpdated = wasUpdated;
        }

        public List<UDB> GetUIDetails() {
            var res = new List<UDB>();
            res.Add(UDB.Create(this, 
                    UDBT.DText,
                    IconId.CMissing,
                    "item.name".T())
                        // In translations item.text = "Foo bar {0} {1}" 
                        // would output "Foo bar 1 2"
                        .WithText("item.text".T(1, 2)));
            return res;
        }
    }
}