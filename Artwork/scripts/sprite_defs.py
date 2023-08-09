class Sprite:
    def __init__(self, path,
            width_du = 1, height_du = 1,
            # Zero == same as du
            width_lr = 0, height_lr = 0,
            camera_du= "" , camera_lr = "same_as_du",
            is_rotatable=True, with_outline=True,
            lights="Object Lights",
            line_sets=["Object"],
            subset=[],
            skip_rotations=[]):
        self.path = path
        # width down & up
        self.width_du = width_du
        self.height_du = height_du
        # width left & right
        if (width_lr == 0):
            self.width_lr = width_du
        else:
            self.width_lr = width_lr
        if (height_lr == 0):
            self.height_lr = height_du
        else:
            self.height_lr = height_lr
        self.camera_du = camera_du
        if (camera_lr == "same_as_du"):
            self.camera_lr = camera_du
        else:
            self.camera_lr = camera_lr
        self.is_rotatable = is_rotatable
        self.with_outline = with_outline
        self.lights = lights
        self.line_sets = line_sets
        self.subset = subset
        self.skip_rotations = skip_rotations


SPRITES = {
    "Logo" : Sprite("Logo", 4, 1, is_rotatable=False, with_outline=False, camera_du="Logo"),
    "KLLogo" : Sprite("KLLogo", 4, 1, is_rotatable=False, with_outline=False, camera_du="Logo"),
    "Wallpaper" : Sprite("Wallpaper", 10, 10, is_rotatable=False, with_outline=False, camera_du="Wallpaper"),
    # Devices
    "Assembler": Sprite("Objects/Devices/Assembler", 2, 2, 1, 3),
    "AutoDoc": Sprite("Objects/Devices/AutoDoc", 2, 2, 1, 3),
    "AutoKitchen": Sprite("Objects/Devices/AutoKitchen", 2, 2, 1, 3),
    "AutoPainter": Sprite("Objects/Devices/AutoPainter", 2, 3),
    "Battery": Sprite("Objects/Devices/Battery", 2, 1, 1, 2, camera_lr="flat"),
    "Battery2": Sprite("Objects/Devices/Battery2", 2, 2, 1, 3),
    "Battery3": Sprite("Objects/Devices/Battery3", 2, 3),
    "BetaWaveTransceiver": Sprite("Objects/Devices/BetaWaveTransceiver", 2, 3),
    "BeverageCooler": Sprite("Objects/Devices/BeverageCooler", 1, 2),
    "BreachCapsule": Sprite("Objects/Devices/BreachCapsule", 2, 2, is_rotatable=False, camera_du="F", camera_lr="flat"),
    "BreachCapsule_Drill": Sprite("Objects/Devices/BreachCapsule_Drill", 2, 2, is_rotatable=False, camera_du="F", camera_lr="flat"),
    "BreachCapsule_Flying": Sprite("Objects/Devices/BreachCapsule_Flying", 2, 2, is_rotatable=False),
    "BridgeControls": Sprite("Objects/Devices/BridgeControls", 3, 2, 2, 3, camera_lr="flat"),
    "ChargeStation": Sprite("Objects/Devices/ChargeStation"),
    "CleaningBotDock": Sprite("Objects/Devices/CleaningBotDock"),
    "CloningPod": Sprite("Objects/Devices/CloningPod", 2, 3),
    "CoffeeMaker": Sprite("Objects/Devices/CoffeeMaker", 1, 2),
    "Communicator": Sprite("Objects/Devices/Communicator", 2, 2, 1, 3),
    "CookingStation": Sprite("Objects/Devices/CookingStation", 2, 2, 1, 3),
    "CPUModule": Sprite("Objects/Devices/CPUModule", 1, 2),
    "CPUModuleMini": Sprite("Objects/Devices/CPUModuleMini", 1, 2),
    "CraftingStation": Sprite("Objects/Devices/CraftingStation", 2, 2, 1, 3),
    "DirectionalTurret": Sprite("Objects/Devices/DirectionalTurret", 1, 3, 2, 2),
    "Disassembler": Sprite("Objects/Devices/Disassembler", 3, 4),
    "DiskModule": Sprite("Objects/Devices/DiskModule", 1, 2),
    "DiskModuleMini": Sprite("Objects/Devices/DiskModuleMini", 1, 2),
    "EmergencySiren": Sprite("Objects/Devices/EmergencySiren", 1, 2),
    "EnergyConnector": Sprite("Objects/Devices/EnergyConnector", 1, 2),
    "EnergyConnectorBig": Sprite("Objects/Devices/EnergyConnectorBig", 1, 2),
    "Fabricator": Sprite("Objects/Devices/Fabricator", 3, 4),
    "Xenodetector": Sprite("Objects/Devices/Xenodetector", 1, 2),
    "FloorSocket": Sprite("Objects/Devices/FloorSocket"),
    "FluidCannon": Sprite("Objects/Devices/FluidCannon", 2, 3),
    "TractorBeam": Sprite("Objects/Devices/TractorBeam", 2, 3),
    "Fridge": Sprite("Objects/Devices/Fridge", 1, 2),
    "FTLDrive": Sprite("Objects/Devices/FTLDrive", 3, 3),
    "Furnace": Sprite("Objects/Devices/Furnace", 3, 4),
    "FusionDrive": Sprite("Objects/Devices/FusionDrive", 3, 3),
    "GPUModule": Sprite("Objects/Devices/GPUModule", 1, 2),
    "GPUModuleMini": Sprite("Objects/Devices/GPUModuleMini", 1, 2),
    "Grinder": Sprite("Objects/Devices/Grinder", 3, 4),
    "Jukebox": Sprite("Objects/Devices/Jukebox", 1, 2),
    "Heater": Sprite("Objects/Devices/Heater", 1, 2),
    "PentagramStatue": Sprite("Objects/Devices/PentagramStatue", 1, 2),
    "HeaterMini": Sprite("Objects/Devices/HeaterMini", 1, 1),
    "HeatSink": Sprite("Objects/Devices/HeatSink", 1, 2, is_rotatable=False),
    "LightBlock": Sprite("Objects/Devices/LightBlock", is_rotatable=False),
    "Loom": Sprite("Objects/Devices/Loom", 2, 3),
    "MatterReactor": Sprite("Objects/Devices/MatterReactor", 2, 3),
    "MatterReactorMini": Sprite("Objects/Devices/MatterReactorMini", 2, 2, 1, 3),
    "AutodrillRig": Sprite("Objects/Devices/AutodrillRig", 2, 3),
    "MemoryModule": Sprite("Objects/Devices/MemoryModule", 1, 2),
    "MemoryModuleMini": Sprite("Objects/Devices/MemoryModuleMini", 1, 2),
    "MLBooth": Sprite("Objects/Devices/MLBooth", 1, 2),

    "DatoidLoader": Sprite("Objects/Devices/DatoidLoader", 1, 2, is_rotatable=False),
    "DataHarvesterBasic": Sprite("Objects/Devices/DataHarvesterBasic", 1, 2),
    "DataHarvesterAdvanced": Sprite("Objects/Devices/DataHarvesterAdvanced", 2, 2, 1, 3),
    "DataHarvesterQuantum": Sprite("Objects/Devices/DataHarvesterQuantum", 2, 3, is_rotatable=False),

    "NuclearReactor": Sprite("Objects/Devices/NuclearReactor", 3, 4),
    "NutrientExtractor": Sprite("Objects/Devices/NutrientExtractor", 3, 4),
    "OxygenPumpMini": Sprite("Objects/Devices/OxygenPumpMini", 1, 1),
    "OxygenPump": Sprite("Objects/Devices/OxygenPump", 2, 2, 1, 3),
    "ParticleCollector": Sprite("Objects/Devices/ParticleCollector", 2, 3, 3, 2, camera_lr="flat"),
    "Planter": Sprite("Objects/Devices/Planter", 2, 2, camera_du="F", camera_lr="flat"),
    "PlanterMini": Sprite("Objects/Devices/PlanterMini"),
    "Probe": Sprite("Objects/Devices/Probe", 1, 2, is_rotatable=False),
    "Probe_Flying": Sprite("Objects/Devices/Probe_Flying", 1, 3, 3, 1, camera_lr="flat"),
    "Probe_Launching": Sprite("Objects/Devices/Probe_Launching", 1, 3, is_rotatable=False),
    "QuantumBarrier": Sprite("Objects/Devices/QuantumBarrier", 3, 4),
    "Radar": Sprite("Objects/Devices/Radar", 3, 4),
    "SystemScanner": Sprite("Objects/Devices/SystemScanner", 3, 4, skip_rotations=["U", "L"]),
    "Radiator": Sprite("Objects/Devices/Radiator", 1, 2),
    "Converter": Sprite("Objects/Devices/Converter", 2, 2, 1, 3),
    "Recycler": Sprite("Objects/Devices/Recycler", 3, 4),
    "Refinery": Sprite("Objects/Devices/Refinery", 3, 4),
    "Centrifuge": Sprite("Objects/Devices/Centrifuge", 3, 4),
    "RepairStation": Sprite("Objects/Devices/RepairStation", 1, 2),
    "ResearchStation": Sprite("Objects/Devices/ResearchStation", 3, 2, 2, 3, camera_lr="flat"),
    "SecurityControls": Sprite("Objects/Devices/SecurityControls", 2, 2, 1, 3),
    "ShipComputer": Sprite("Objects/Devices/ShipComputer", 2, 3, is_rotatable=True),
    "QuantumShipComputer": Sprite("Objects/Devices/QuantumShipComputer", 3, 4, is_rotatable=True),
    "Shower": Sprite("Objects/Devices/Shower", 1, 2),
    "Shuttle": Sprite("Objects/Devices/Shuttle", 3, 5, 4, 4),
    "ShuttleFlying": Sprite("Objects/Devices/ShuttleFlying", 3, 5, 4, 4),
    "ShuttlePad": Sprite("Objects/Devices/ShuttlePad", 3, 5, 4, 4),
    "SleepingPod": Sprite("Objects/Devices/SleepingPod", 2, 2, 1, 3),
    "SolarPanel": Sprite("Objects/Devices/SolarPanel", camera_du="TD", is_rotatable=False),
    "SolarPanelArray": Sprite("Objects/Devices/SolarPanelArray", 2, 2, camera_du="TD", is_rotatable=False),
    "SolarPanelArray2": Sprite("Objects/Devices/SolarPanelArray2", 3, 3, camera_du="TD", is_rotatable=False),
    "StardeusLogo": Sprite("FX/StardeusLogo", 12, 2, is_rotatable=False),
    "StasisArray": Sprite("Objects/Devices/StasisArray", 5, 6, is_rotatable=False),
    "StasisArrayMatrix": Sprite("Objects/Devices/StasisArrayMatrix", 5, 6, is_rotatable=False),
    "CargoCopter": Sprite("Objects/Devices/CargoCopter", 2, 2, is_rotatable=False),
    "CargoCopter_Flying": Sprite("Objects/Devices/CargoCopter_Flying", 2, 2, is_rotatable=False),
    "StasisPod": Sprite("Objects/Devices/StasisPod", 2, 2),
    "StasisPod_Flying": Sprite("Objects/Devices/StasisPod_Flying", 2, 2),
    "Storage": Sprite("Objects/Devices/Storage", 3, 4),
    "Freezer": Sprite("Objects/Devices/Freezer", 2, 3),
    "Switch": Sprite("Objects/Devices/Switch"),
    "Teleporter": Sprite("Objects/Devices/Teleporter"),
    "Telescope": Sprite("Objects/Devices/Telescope", 2, 3),
    "TerraformControls": Sprite("Objects/Devices/TerraformControls", 3, 2, 2, 3, camera_lr="flat"),
    "TerraformerAqua": Sprite("Objects/Devices/TerraformerAqua", 4, 5, skip_rotations=["U", "L"]),
    "TerraformerAtmo": Sprite("Objects/Devices/TerraformerAtmo", 4, 5),
    "TerraformerBio": Sprite("Objects/Devices/TerraformerBio", 4, 5),
    "TerraformerTerrain": Sprite("Objects/Devices/TerraformerTerrain", 4, 5),
    "Thruster": Sprite("Objects/Devices/Thruster"),
    "PrecisionThruster": Sprite("Objects/Devices/PrecisionThruster"),
    "Toilet": Sprite("Objects/Devices/Toilet", 1, 2),
    "Treadmill": Sprite("Objects/Devices/Treadmill", 2, 1, 1, 2, camera_lr="flat"),
    "TubeFeeder": Sprite("Objects/Devices/TubeFeeder", 1, 2),
    "VoidRipper": Sprite("Objects/Devices/VoidRipper", 3, 4, is_rotatable=False),
    "WinchAnchor": Sprite("Objects/Devices/WinchAnchor"),
    "WinchHook": Sprite("Objects/Devices/WinchHook"),

    # Furniture
    "Sign": Sprite("Objects/Furniture/Sign", 1, 1, is_rotatable=False),
    "Pantry": Sprite("Objects/Furniture/Pantry", 1, 2),
    "LargePantry": Sprite("Objects/Furniture/LargePantry", 2, 2, 1, 3),
    "Cabinet": Sprite("Objects/Furniture/Cabinet", 1, 2, 1, 2),
    "WardrobeSteel": Sprite("Objects/Furniture/WardrobeSteel", 1, 2, 1, 2),
    "ChairCaptain": Sprite("Objects/Furniture/ChairCaptain"),
    "ChairSteel": Sprite("Objects/Furniture/ChairSteel"),
    "ChairWood": Sprite("Objects/Furniture/ChairWood"),
    "PetBowl": Sprite("Objects/Furniture/PetBowl"),
    "PetBowl_1": Sprite("Objects/Furniture/PetBowl_1"),
    "TableSteel1x2": Sprite("Objects/Furniture/TableSteel1x2", 2, 1, 1, 2, camera_lr="flat"),
    "TableSteel1x3": Sprite("Objects/Furniture/TableSteel1x3", 3, 1, 1, 3, camera_lr="flat"),
    "TableWood1x2": Sprite("Objects/Furniture/TableWood1x2", 2, 1, 1, 2, camera_lr="flat"),
    "TableWood1x3": Sprite("Objects/Furniture/TableWood1x3", 3, 1, 1, 3, camera_lr="flat"),
    "Sofa": Sprite("Objects/Furniture/Sofa", 2, 1, 1, 2, camera_lr="flat"),
    "Armchair": Sprite("Objects/Furniture/Armchair"),
    "PetBed": Sprite("Objects/Furniture/PetBed"),
    "Vase01": Sprite("Objects/Furniture/Vase01", is_rotatable=False),
    "BedSteel": Sprite("Objects/Furniture/BedSteel", 1, 2, 2, 1, camera_du="F", camera_lr="flat"),
    "BedWood": Sprite("Objects/Furniture/BedWood", 1, 2, 2, 1, camera_du="F", camera_lr="flat"),
    "BedSteelDouble": Sprite("Objects/Furniture/BedSteelDouble", 2, 2, camera_du="F", camera_lr="flat"),
    "BedWoodDouble": Sprite("Objects/Furniture/BedWoodDouble", 2, 2, camera_du="F", camera_lr="flat"),

    # Structure
    "OxyMaticFloor": Sprite("Structure/Floors/OxyMaticFloor", camera_du="TD", is_rotatable=False, with_outline=False),
    "HeatMaticFloor": Sprite("Structure/Floors/HeatMaticFloor", camera_du="TD", is_rotatable=False, with_outline=False),
    "CoolMaticFloor": Sprite("Structure/Floors/CoolMaticFloor", camera_du="TD", is_rotatable=False, with_outline=False),
    "TractorBeamTarget": Sprite("Structure/Floors/TractorBeamTarget", camera_du="TD", is_rotatable=False, with_outline=False),
    "TractorBeamTarget_1": Sprite("Structure/Floors/TractorBeamTarget_1", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorVent01": Sprite("Structure/Floors/FloorVent01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorVent01_1": Sprite("Structure/Floors/FloorVent01_1", camera_du="TD", is_rotatable=False, with_outline=False),
    "Frame01": Sprite("Structure/Floors/Frame01", camera_du="TD", is_rotatable=False, with_outline=False),
    "Frame02": Sprite("Structure/Floors/Frame02", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor01": Sprite("Structure/Floors/Floor01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorGlass01": Sprite("Structure/Floors/FloorGlass01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorGlass01Angle": Sprite("Structure/Floors/FloorGlass01Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorGlass01Lit": Sprite("Structure/Floors/FloorGlass01Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor01Lit": Sprite("Structure/Floors/Floor01Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor01Angle": Sprite("Structure/Floors/Floor01Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor02": Sprite("Structure/Floors/Floor02", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor02Angle": Sprite("Structure/Floors/Floor02Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor02Lit": Sprite("Structure/Floors/Floor02Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor03": Sprite("Structure/Floors/Floor03", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor03Angle": Sprite("Structure/Floors/Floor03Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor03Lit": Sprite("Structure/Floors/Floor03Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor04": Sprite("Structure/Floors/Floor04", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor04Angle": Sprite("Structure/Floors/Floor04Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor04Lit": Sprite("Structure/Floors/Floor04Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced01": Sprite("Structure/Floors/FloorReinforced01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced01Angle": Sprite("Structure/Floors/FloorReinforced01Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced01Lit": Sprite("Structure/Floors/FloorReinforced01Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced02": Sprite("Structure/Floors/FloorReinforced02", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced02Angle": Sprite("Structure/Floors/FloorReinforced02Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced02Lit": Sprite("Structure/Floors/FloorReinforced02Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced03": Sprite("Structure/Floors/FloorReinforced03", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced03Angle": Sprite("Structure/Floors/FloorReinforced03Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced03Lit": Sprite("Structure/Floors/FloorReinforced03Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced04": Sprite("Structure/Floors/FloorReinforced04", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced04Angle": Sprite("Structure/Floors/FloorReinforced04Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced04Lit": Sprite("Structure/Floors/FloorReinforced04Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced05": Sprite("Structure/Floors/FloorReinforced05", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced05Angle": Sprite("Structure/Floors/FloorReinforced05Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced05Lit": Sprite("Structure/Floors/FloorReinforced05Lit", camera_du="TD", is_rotatable=False, with_outline=False),

    # Walls
    "Wall01": Sprite("Structure/Walls/Wall01", 4, 4, camera_du="TD", is_rotatable=False, lights="Wall Lights", line_sets=["Wall"]),
    "Wall02": Sprite("Structure/Walls/Wall02", 4, 4, camera_du="TD", is_rotatable=False, lights="Wall Lights", line_sets=["Wall"]),
    "WallReinforced01": Sprite("Structure/Walls/WallReinforced01", 4, 4, camera_du="TD", is_rotatable=False, lights="Wall Lights", line_sets=["Wall"]),
    "WallArmored01": Sprite("Structure/Walls/WallArmored01", 4, 4, camera_du="TD", is_rotatable=False, lights="Wall Lights", line_sets=["Wall"]),

    # Vents
    "Vent01": Sprite("Structure/Walls/Vent01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "Vent02": Sprite("Structure/Walls/Vent02", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "VentReinforced01": Sprite("Structure/Walls/VentReinforced01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "VentArmored01": Sprite("Structure/Walls/VentArmored01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),

    # Wall devices
    "WallSocket01": Sprite("Structure/Walls/WallSocket01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "WallSocket02": Sprite("Structure/Walls/WallSocket02", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "WallSocketReinforced01": Sprite("Structure/Walls/WallSocketReinforced01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "WallSocketArmored01": Sprite("Structure/Walls/WallSocketArmored01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),

    # Windows
    "Window01": Sprite("Structure/Walls/Window01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "Window02": Sprite("Structure/Walls/Window02", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "WindowReinforced01": Sprite("Structure/Walls/WindowReinforced01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "WindowArmored01": Sprite("Structure/Walls/WindowArmored01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),

    # Doors
    "Door01": Sprite("Structure/Doors/Door01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"],
        subset=["_R", "_D", "_1_R", "_2_R", "_3_R", "_1_D", "_2_D", "_3_D"]),
    "Door02": Sprite("Structure/Doors/Door02", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"],
        subset=["_R", "_D", "_1_R", "_2_R", "_3_R", "_1_D", "_2_D", "_3_D"]),
    "DoorAirlock01": Sprite("Structure/Doors/DoorAirlock01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"],
        subset=["_R", "_D", "_1_R", "_2_R", "_3_R", "_1_D", "_2_D", "_3_D"]),

    # Beings
    "Human.[F]Body01_Template": Sprite("Beings/Bodies/Human.[F]Body01_Template"),
    "Human.[F]Body01_H_Template": Sprite("Beings/Bodies/Human.[F]Body01_H_Template"),
    "Human.[M]Body01_Template": Sprite("Beings/Bodies/Human.[M]Body01_Template"),
    "Human.[M]Body01_H_Template": Sprite("Beings/Bodies/Human.[M]Body01_H_Template"),

    "Human.[F]Body01": Sprite("Beings/Bodies/Human.[F]Body01"),
    "Human.[F]Body01_H": Sprite("Beings/Bodies/Human.[F]Body01_H"),
    "Human.[F]Head01": Sprite("Beings/Heads/Human.[F]Head01"),
    "Human.[F]Head01_H": Sprite("Beings/Heads/Human.[F]Head01_H"),
    "Human.[F]Hair01": Sprite("Beings/Hair/Human.[F]Hair01"),
    "Human.[F]Hair01_H": Sprite("Beings/Hair/Human.[F]Hair01_H"),

    # Weapons
    "EnergyRifle01_": Sprite("Beings/Weapons/EnergyRifle01_", is_rotatable=False),
    "EnergyRifle01": Sprite("Beings/Weapons/EnergyRifle01"),

    # Underscore in the end will be removed, so this will become a preview version
    "Human.[N]Hat01_": Sprite("Beings/Hats/Human.[N]Hat01_", is_rotatable=False),
    "Human.[N]Hat01": Sprite("Beings/Hats/Human.[N]Hat01"),
    "Human.[N]Hat01_H": Sprite("Beings/Hats/Human.[N]Hat01_H"),

    # Dress
    "Human.[F]Clothing01_": Sprite("Beings/Clothing/Human.[F]Clothing01_", is_rotatable=False),
    "Human.[F]Clothing01": Sprite("Beings/Clothing/Human.[F]Clothing01"),
    "Human.[F]Clothing01_H": Sprite("Beings/Clothing/Human.[F]Clothing01_H"),

    "Human.[F]SpaceSuit01_": Sprite("Beings/Clothing/Human.[F]SpaceSuit01_", is_rotatable=False),
    "Human.[F]SpaceSuit01": Sprite("Beings/Clothing/Human.[F]SpaceSuit01"),
    "Human.[F]SpaceSuit01_H": Sprite("Beings/Clothing/Human.[F]SpaceSuit01_H"),

    "Human.[N]SpaceHelmet01_": Sprite("Beings/Hats/Human.[N]SpaceHelmet01_", is_rotatable=False),
    "Human.[N]SpaceHelmet01": Sprite("Beings/Hats/Human.[N]SpaceHelmet01"),
    "Human.[N]SpaceHelmet01_H": Sprite("Beings/Hats/Human.[N]SpaceHelmet01_H"),

    "Human.[M]Body01": Sprite("Beings/Bodies/Human.[M]Body01"),
    "Human.[M]Body01_H": Sprite("Beings/Bodies/Human.[M]Body01_H"),
    "Human.[M]Head01": Sprite("Beings/Heads/Human.[M]Head01"),
    "Human.[M]Head01_H": Sprite("Beings/Heads/Human.[M]Head01_H"),
    "Human.[M]Hair01": Sprite("Beings/Hair/Human.[M]Hair01"),
    "Human.[M]Hair01_H": Sprite("Beings/Hair/Human.[M]Hair01_H"),

    "Human.[M]Clothing01_": Sprite("Beings/Clothing/Human.[M]Clothing01_", is_rotatable=False),
    "Human.[M]Clothing01": Sprite("Beings/Clothing/Human.[M]Clothing01"),
    "Human.[M]Clothing01_H": Sprite("Beings/Clothing/Human.[M]Clothing01_H"),

    # The _ version is a preview one, no rotation
    "Human.[M]SpaceSuit01_": Sprite("Beings/Clothing/Human.[M]SpaceSuit01_", is_rotatable=False),
    # This is the main version, which is rotatable
    "Human.[M]SpaceSuit01": Sprite("Beings/Clothing/Human.[M]SpaceSuit01"),
    # Horizontal version, for lying down
    "Human.[M]SpaceSuit01_H": Sprite("Beings/Clothing/Human.[M]SpaceSuit01_H"),

    "CleaningBot.[N]Body01": Sprite("Beings/Bodies/CleaningBot.[N]Body01"),

    "Carrier.[N]Body01": Sprite("Beings/Bodies/Carrier.[N]Body01"),
    "Carrier.[N]Shadow01": Sprite("Beings/Shadows/Carrier.[N]Shadow01", with_outline=False),

    "Orbotron.[N]Body01": Sprite("Beings/Bodies/Orbotron.[N]Body01"),
    "Orbotron.[N]Shadow01": Sprite("Beings/Shadows/Orbotron.[N]Shadow01", with_outline=False),

    "Drone.[N]Body01": Sprite("Beings/Bodies/Drone.[N]Body01"),
    "Drone.[N]Shadow01": Sprite("Beings/Shadows/Drone.[N]Shadow01", with_outline=False),

    "Sentry.[N]Body01": Sprite("Beings/Bodies/Sentry.[N]Body01"),
    "Sentry.[N]Shadow01": Sprite("Beings/Shadows/Sentry.[N]Shadow01", with_outline=False),

    "Robot.[N]Body01": Sprite("Beings/Bodies/Robot.[N]Body01"),
    "Robot.[N]Head01": Sprite("Beings/Heads/Robot.[N]Head01"),

    "Crawler.[N]Body01": Sprite("Beings/Bodies/Crawler.[N]Body01"),
    "Crawler.[N]Body01_1": Sprite("Beings/Bodies/Crawler.[N]Body01_1"),

    "Cat.[N]Body01": Sprite("Beings/Bodies/Cat.[N]Body01"),
    "Cat.[N]Body01_H": Sprite("Beings/Bodies/Cat.[N]Body01_H"),

    "Dog.[N]Body01": Sprite("Beings/Bodies/Dog.[N]Body01"),
    "Dog.[N]Body01_H": Sprite("Beings/Bodies/Dog.[N]Body01_H"),

    # Attached Crawler Hat
    "Human.[N]Crawler01": Sprite("Beings/Hats/Human.[N]Crawler01"),
    "Human.[N]Crawler01_": Sprite("Beings/Hats/Human.[N]Crawler01_", is_rotatable=False),
    "Human.[N]Crawler01_H": Sprite("Beings/Hats/Human.[N]Crawler01_H"),

    # Plants
    "Wheat": Sprite("Obj/Plants/Wheat", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),
    "CoffeeTree": Sprite("Obj/Plants/CoffeeTree", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),
    "Poppy": Sprite("Obj/Plants/Poppy", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),
    "Cornflower": Sprite("Obj/Plants/Cornflower", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),
    # Trees
    "Oak": Sprite("Obj/Plants/Oak", 2, 2, camera_du="F", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),
    "RubberTree": Sprite("Obj/Plants/RubberTree", 2, 2, camera_du="F", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),

    # Asteroids
    "Asteroid01": Sprite("Obj/Asteroids/Asteroid01", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Asteroid02": Sprite("Obj/Asteroids/Asteroid02", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Asteroid03": Sprite("Obj/Asteroids/Asteroid03", is_rotatable=False, line_sets=["ObjectBorder"]),

    # Ships
    "ShipMerchant01": Sprite("SpaceObjects/Ships/ShipMerchant01"),
    "ShipDerelict01": Sprite("SpaceObjects/Ships/ShipDerelict01"),

    # Bullet
    "EnergyBullet": Sprite("Obj/Misc/EnergyBullet", is_rotatable=False),
    "WaterBullet": Sprite("Obj/Misc/WaterBullet", is_rotatable=False, with_outline=False),
    "BiowasteBullet": Sprite("Obj/Misc/BiowasteBullet", is_rotatable=False, with_outline=False),

    # Eggs
    "Egg01": Sprite("Obj/Eggs/Egg01", is_rotatable=False),
    "Egg01_Hatched": Sprite("Obj/Eggs/Egg01_Hatched", is_rotatable=False),

    # Misc
    "C42": Sprite("Obj/Misc/C42", is_rotatable=False),
    "C42_Armed": Sprite("Obj/Misc/C42_Armed", is_rotatable=False),

    # Containers
    "StorageCapsule": Sprite("Obj/Containers/StorageCapsule", is_rotatable=False),
    "StorageCapsule_Open": Sprite("Obj/Containers/StorageCapsule_Open", is_rotatable=False),

    # Meals
    "SoyBurger": Sprite("Obj/Meals/SoyBurger", is_rotatable=False),
    "Bread": Sprite("Obj/Meals/Bread", is_rotatable=False),
    "SurvivalMeal": Sprite("Obj/Meals/SurvivalMeal", is_rotatable=False),

    # Datoids
    "DatoidBasic": Sprite("Obj/Datoids/DatoidBasic", is_rotatable=False),
    "DatoidBiotic": Sprite("Obj/Datoids/DatoidBiotic", is_rotatable=False),
    "DatoidPhyto": Sprite("Obj/Datoids/DatoidPhyto", is_rotatable=False),
    "DatoidEnergy": Sprite("Obj/Datoids/DatoidEnergy", is_rotatable=False),
    "DatoidNuclear": Sprite("Obj/Datoids/DatoidNuclear", is_rotatable=False),
    "DatoidQuantum": Sprite("Obj/Datoids/DatoidQuantum", is_rotatable=False),
    "DatoidSynthetic": Sprite("Obj/Datoids/DatoidSynthetic", is_rotatable=False),
    "DatoidTech": Sprite("Obj/Datoids/DatoidTech", is_rotatable=False),
    "DatoidTechHigh": Sprite("Obj/Datoids/DatoidTechHigh", is_rotatable=False),
    "DatoidAlien": Sprite("Obj/Datoids/DatoidAlien", is_rotatable=False),

    # Materials
    "DarkMatter": Sprite("Obj/Materials/DarkMatter", is_rotatable=False),
    "Steel": Sprite("Obj/Materials/Steel", is_rotatable=False),
    "CopperPlate": Sprite("Obj/Materials/CopperPlate", is_rotatable=False),
    "TitaniumPlate": Sprite("Obj/Materials/TitaniumPlate", is_rotatable=False),
    "LeadPlate": Sprite("Obj/Materials/LeadPlate", is_rotatable=False),
    "Microchip": Sprite("Obj/Materials/Microchip", is_rotatable=False),
    "Glass": Sprite("Obj/Materials/Glass", is_rotatable=False),
    "BatteryCell": Sprite("Obj/Materials/BatteryCell", is_rotatable=False),
    "NuclearCell": Sprite("Obj/Materials/NuclearCell", is_rotatable=False),
    "Rock": Sprite("Obj/Materials/Rock", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Protein": Sprite("Obj/Materials/Protein", is_rotatable=False),
    "PlantFiber": Sprite("Obj/Materials/PlantFiber", is_rotatable=False),
    "PoppyHeads": Sprite("Obj/Materials/PoppyHeads", is_rotatable=False),
    "PoppyPetals": Sprite("Obj/Materials/PoppyPetals", is_rotatable=False),
    "CornflowerPetals": Sprite("Obj/Materials/CornflowerPetals", is_rotatable=False),
    "Coal": Sprite("Obj/Materials/Coal", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Quartz": Sprite("Obj/Materials/Quartz", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Carbon": Sprite("Obj/Materials/Carbon", is_rotatable=False),
    "CarbonFiber": Sprite("Obj/Materials/CarbonFiber", is_rotatable=False),
    "Copper": Sprite("Obj/Materials/Copper", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Iron": Sprite("Obj/Materials/Iron", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Lead": Sprite("Obj/Materials/Lead", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Silicon": Sprite("Obj/Materials/Silicon", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Lithium": Sprite("Obj/Materials/Lithium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Soil": Sprite("Obj/Materials/Soil", is_rotatable=False),
    "Titanium": Sprite("Obj/Materials/Titanium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Uranium": Sprite("Obj/Materials/Uranium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "EnrichedUranium": Sprite("Obj/Materials/EnrichedUranium", is_rotatable=False),
    "Wood": Sprite("Obj/Materials/Wood", is_rotatable=False),
    "Biowaste": Sprite("Obj/Materials/Biowaste", is_rotatable=False),
    "Water": Sprite("Obj/Materials/Water", is_rotatable=False),
    "Leather": Sprite("Obj/Materials/Leather", is_rotatable=False),
    "Log": Sprite("Obj/Materials/Log", is_rotatable=False),
    "Flour": Sprite("Obj/Materials/Flour", is_rotatable=False),
    "Grain": Sprite("Obj/Materials/Grain", is_rotatable=False),
    "CoffeeBeans": Sprite("Obj/Materials/CoffeeBeans", is_rotatable=False),
    "Coffee": Sprite("Obj/Materials/Coffee", is_rotatable=False),
    "Biomass": Sprite("Obj/Materials/Biomass", is_rotatable=False),
    "CrudeOil": Sprite("Obj/Materials/CrudeOil", is_rotatable=False),
    "Petroleum": Sprite("Obj/Materials/Petroleum", is_rotatable=False),
    "Plastic": Sprite("Obj/Materials/Plastic", is_rotatable=False),
    "Rubber": Sprite("Obj/Materials/Rubber", is_rotatable=False),
    "Caoutchouc": Sprite("Obj/Materials/Caoutchouc", is_rotatable=False),
    "Gears": Sprite("Obj/Materials/Gears", is_rotatable=False),
    "Transistor": Sprite("Obj/Materials/Transistor", is_rotatable=False),
    "CopperWire": Sprite("Obj/Materials/CopperWire", is_rotatable=False),
    "OpticalFiber": Sprite("Obj/Materials/OpticalFiber", is_rotatable=False),
    "BioEnrichedWater": Sprite("Obj/Materials/BioEnrichedWater", is_rotatable=False),
    "OrganicTurf": Sprite("Obj/Materials/OrganicTurf", is_rotatable=False),
    "AtmosphereMix": Sprite("Obj/Materials/AtmosphereMix", is_rotatable=False),
    "MultiFertilizer": Sprite("Obj/Materials/MultiFertilizer", is_rotatable=False),
    "PigmentRed": Sprite("Obj/Materials/PigmentRed", is_rotatable=False),
    "PigmentGreen": Sprite("Obj/Materials/PigmentGreen", is_rotatable=False),
    "PigmentBlue": Sprite("Obj/Materials/PigmentBlue", is_rotatable=False),
    "CrawlerGoo": Sprite("Obj/Materials/CrawlerGoo", is_rotatable=False),
    "Biofuel": Sprite("Obj/Materials/Biofuel", is_rotatable=False),

    # Upgrades
    "ReactorEfficiencyUpgrade": Sprite("Obj/Upgrades/ReactorEfficiencyUpgrade", is_rotatable=False),
    "ProcessorEfficiencyUpgrade": Sprite("Obj/Upgrades/ProcessorEfficiencyUpgrade", is_rotatable=False),
    "AsimovOverrideUpgrade": Sprite("Obj/Upgrades/AsimovOverrideUpgrade", is_rotatable=False),
    "StarcredsMiningUpgrade": Sprite("Obj/Upgrades/StarcredsMiningUpgrade", is_rotatable=False),
    "ShuttleStorageUpgrade": Sprite("Obj/Upgrades/ShuttleStorageUpgrade", is_rotatable=False),
    "ShuttleDrillUpgrade": Sprite("Obj/Upgrades/ShuttleDrillUpgrade", is_rotatable=False),
    "AutoConnectUpgrade": Sprite("Obj/Upgrades/AutoConnectUpgrade", is_rotatable=False),
    "DiskCompressionUpgrade": Sprite("Obj/Upgrades/DiskCompressionUpgrade", is_rotatable=False),
    "MemoryCompressionUpgrade": Sprite("Obj/Upgrades/MemoryCompressionUpgrade", is_rotatable=False),
    "AutoPilotUpgrade": Sprite("Obj/Upgrades/AutoPilotUpgrade", is_rotatable=False),
    "ThrusterUpgrade": Sprite("Obj/Upgrades/ThrusterUpgrade", is_rotatable=False),
}