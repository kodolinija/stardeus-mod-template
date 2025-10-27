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
            skip_rotations=[],
            output=None,
            is_head=False,
            num_rotations=0,
            stop_at_rotation=0,
            activate_filter=None,
            anim_frames=0,
            anim_speed_pct=100):
        self.path = path
        if (output == None):
            output = path
        self.output = output
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
        self.is_head = is_head
        self.skip_rotations = skip_rotations
        self.num_rotations = num_rotations
        self.stop_at_rotation = stop_at_rotation
        self.activate_filter = activate_filter
        self.anim_frames = anim_frames
        self.anim_speed_pct = anim_speed_pct

def add_hat(sprites, species, name):
    # Preview
    sprites["{}_".format(name)] = Sprite(
        "Beings/Hats.{}/{}/{}_".format(species, name, name), is_rotatable=False, is_head=True)
    sprites["{}".format(name)] = Sprite(
        path="Beings/Hats.{}/{}/[N]{}".format(species, name, name),
        output="Beings/Hats.{}/{}/{}".format(species, name, name),
        is_head=True)
    sprites["{}_H".format(name)] = Sprite(
        path="Beings/Hats.{}/{}/[N]{}_H".format(species, name, name),
        output="Beings/Hats.{}/{}/{}_H".format(species, name, name),
        is_head=True)

def add_hair(sprites, species, sex, num):
    sprites["{}.[{}]Hair{}".format(species, sex, num)] = Sprite(
        "Beings/Hair/{}.[{}]Hair{}".format(species, sex, num),
        is_head=True
    )
    sprites["{}.[{}]Hair{}_H".format(species, sex, num)] = Sprite(
        "Beings/Hair/{}.[{}]Hair{}_H".format(species, sex, num),
        is_head=True
    )

def add_clothing(sprites, species, name):
    # Preview
    sprites["{}_".format(name)] = Sprite("Beings/Clothing.{}/{}/{}_".format(species, name, name), is_rotatable=False)

    # Body Types
    body_types = ["[F]", "[M]", "[T]", "[L]"]
    for body_type in body_types:
        sprites["{}{}".format(body_type, name)] = Sprite(
            path="Beings/Clothing.{}/{}/{}{}".format(species, name, body_type, name),
            output="Beings/Clothing/{}/{}/{}/{}{}".format(species, name, body_type, body_type, name)
        )
        sprites["{}{}_H".format(body_type, name)] = Sprite(
            path="Beings/Clothing.{}/{}/{}{}_H".format(species, name, body_type, name),
            output="Beings/Clothing/{}/{}/{}/{}{}_H".format(species, name, body_type, body_type, name)
        )


SPRITES = {
    "Logo" : Sprite("Logo", 4, 1, is_rotatable=False, with_outline=False, camera_du="Logo"),
    "KLLogo" : Sprite("KLLogo", 4, 1, is_rotatable=False, with_outline=False, camera_du="Logo"),
    "Wallpaper" : Sprite("Wallpaper", 10, 10, is_rotatable=False, with_outline=False, camera_du="Wallpaper"),
    # Devices
    "AssemblyHub": Sprite("Objects/Devices/AssemblyHub", 2, 3),
    "SurgeryHub": Sprite("Objects/Devices/SurgeryHub", 2, 3),
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
    "BotDock": Sprite("Objects/Devices/BotDock"),
    "CleaningBotDock": Sprite("Objects/Devices/CleaningBotDock"),
    "CoffeeMaker": Sprite("Objects/Devices/CoffeeMaker", 1, 2),
    "IceMaker": Sprite("Objects/Devices/IceMaker", 1, 2, is_rotatable=False),
    "Communicator": Sprite("Objects/Devices/Communicator", 2, 2, 1, 3),
    "CookingStation": Sprite("Objects/Devices/CookingStation", 2, 2, 1, 3),
    "CPUModule": Sprite("Objects/Devices/CPUModule", 1, 2),
    "CPUModuleMini": Sprite("Objects/Devices/CPUModuleMini", 1, 2),
    "DirectionalTurret": Sprite("Objects/Devices/DirectionalTurret", 1, 3, 2, 2),
    "Disassembler": Sprite("Objects/Devices/Disassembler", 3, 4),
    "Mechuary": Sprite("Objects/Devices/Mechuary", 3, 3, 2, 4, camera_du="L", camera_lr=""),
    "Morgue": Sprite("Objects/Devices/Morgue", 3, 3, 2, 4, camera_du="L", camera_lr=""),
    "DiskModule": Sprite("Objects/Devices/DiskModule", 1, 2),
    "DiskModuleMini": Sprite("Objects/Devices/DiskModuleMini", 1, 2),
    "EmergencySiren": Sprite("Objects/Devices/EmergencySiren", 1, 2),
    "EnergyConnector": Sprite("Objects/Devices/EnergyConnector", 1, 2),
    "EnergyConnectorBig": Sprite("Objects/Devices/EnergyConnectorBig", 1, 2),
    "Fabricator": Sprite("Objects/Devices/Fabricator", 3, 4),
    "FloorSocket": Sprite("Objects/Devices/FloorSocket"),
    "FluidCannon": Sprite("Objects/Devices/FluidCannon", 2, 3),
    "TractorBeam": Sprite("Objects/Devices/TractorBeam", 2, 3),
    "Fridge": Sprite("Objects/Devices/Fridge", 1, 2),
    "FTLDrive": Sprite("Objects/Devices/FTLDrive", 3, 3),
    "Furnace": Sprite("Objects/Devices/Furnace", 3, 4),
    "FusionDrive": Sprite("Objects/Devices/FusionDrive", 3, 3),
    "WarpDriveMini": Sprite("Objects/Devices/WarpDriveMini", 2, 3),
    "WarpDrive": Sprite("Objects/Devices/WarpDrive", 3, 4),
    "EmergencyJumpDrive": Sprite("Objects/Devices/EmergencyJumpDrive", 2, 2),
    "Jukebox": Sprite("Objects/Devices/Jukebox", 1, 2),
    "Heater": Sprite("Objects/Devices/Heater", 1, 2),
    "PentagramStatue": Sprite("Objects/Devices/PentagramStatue", 1, 2),
    "HeaterMini": Sprite("Objects/Devices/HeaterMini", 1, 1),
    "HeatSink": Sprite("Objects/Devices/HeatSink", 1, 2, is_rotatable=False),
    "LightBlock": Sprite("Objects/Devices/LightBlock", is_rotatable=False),
    "MatterReactor": Sprite("Objects/Devices/MatterReactor", 2, 3),
    "MinerMini": Sprite("Objects/Devices/MinerMini", 2, 3),
    "MatterReactorMini": Sprite("Objects/Devices/MatterReactorMini", 2, 2, 1, 3),
    "CapsuleLauncher": Sprite("Objects/Devices/CapsuleLauncher", 2, 2, 1, 3),
    "TradePortal": Sprite("Objects/Devices/TradePortal", 1, 2, is_rotatable=False),
    "MemoryModule": Sprite("Objects/Devices/MemoryModule", 1, 2),
    "MemoryModuleMini": Sprite("Objects/Devices/MemoryModuleMini", 1, 2),
    "MLBooth": Sprite("Objects/Devices/MLBooth", 1, 2),
    "Replicator": Sprite("Objects/Devices/Replicator", 2, 2, 1, 3),
    "SuicideBooth": Sprite("Objects/Devices/SuicideBooth", 1, 2),
    "NuclearReactor": Sprite("Objects/Devices/NuclearReactor", 3, 4),
    "OxygenPump": Sprite("Objects/Devices/OxygenPump", 2, 2, 1, 3),
    "Planter": Sprite("Objects/Devices/Planter", 2, 2, camera_du="F", camera_lr="flat"),
    "PlanterMini": Sprite("Objects/Devices/PlanterMini"),
    "Probe": Sprite("Objects/Devices/Probe", 1, 2, is_rotatable=False),
    "Probe_Flying": Sprite("Objects/Devices/Probe_Flying", 1, 3, 3, 1, camera_lr="flat"),
    "Probe_Launching": Sprite("Objects/Devices/Probe_Launching", 1, 3, is_rotatable=False),
    "ReturnBeacon": Sprite("Objects/Devices/ReturnBeacon", 2, 3, is_rotatable=False),
    "QuantumBarrier": Sprite("Objects/Devices/QuantumBarrier", 3, 4),
    "Radiator": Sprite("Objects/Devices/Radiator", 1, 2),
    "Converter": Sprite("Objects/Devices/Converter", 2, 2, 1, 3),
    "Recycler": Sprite("Objects/Devices/Recycler", 3, 4),
    "Refinery": Sprite("Objects/Devices/Refinery", 3, 4),
    "ResearchStation": Sprite("Objects/Devices/ResearchStation", 2, 2, 1, 3), #, camera_lr="flat"),
    "SecurityControls": Sprite("Objects/Devices/SecurityControls", 2, 2, 1, 3),
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
    "StasisArrayMini": Sprite("Objects/Devices/StasisArrayMini", 3, 4, is_rotatable=False),
    "StasisArrayMiniMatrix": Sprite("Objects/Devices/StasisArrayMiniMatrix", 3, 4, is_rotatable=False),
    "StasisArray": Sprite("Objects/Devices/StasisArray", 5, 6, is_rotatable=False),
    "StasisArrayMatrix": Sprite("Objects/Devices/StasisArrayMatrix", 5, 6, is_rotatable=False),
    "StasisPod": Sprite("Objects/Devices/StasisPod", 2, 2),
    "StasisPod_Flying": Sprite("Objects/Devices/StasisPod_Flying", 2, 2),
    "Storage": Sprite("Objects/Devices/Storage", 3, 4),
    "StorageMini": Sprite("Objects/Devices/StorageMini", 2, 3),
    "Freezer": Sprite("Objects/Devices/Freezer", 2, 3),
    "PartStorage": Sprite("Objects/Devices/PartStorage", 2, 3),
    "OrganStorage": Sprite("Objects/Devices/OrganStorage", 2, 2, 1, 3, skip_rotations=["U", "L"]),
    "Switch": Sprite("Objects/Devices/Switch"),
    "Teleporter": Sprite("Objects/Devices/Teleporter"),
    "NanobotHive": Sprite("Objects/Devices/NanobotHive", is_rotatable=False),
    "TerraformControls": Sprite("Objects/Devices/TerraformControls", 3, 2, 2, 3, camera_lr="flat"),
    "TerraformerAqua": Sprite("Objects/Devices/TerraformerAqua", 4, 5, skip_rotations=["U", "L"]),
    "TerraformerAtmo": Sprite("Objects/Devices/TerraformerAtmo", 4, 5),
    "TerraformerBio": Sprite("Objects/Devices/TerraformerBio", 4, 5),
    "TerraformerTerrain": Sprite("Objects/Devices/TerraformerTerrain", 4, 5),
    "Thruster": Sprite("Objects/Devices/Thruster"),
    "PrecisionThruster": Sprite("Objects/Devices/PrecisionThruster"),
    "Toilet": Sprite("Objects/Devices/Toilet", 1, 2),
    "TubeFeeder": Sprite("Objects/Devices/TubeFeeder", 1, 2),
    "WinchAnchor": Sprite("Objects/Devices/WinchAnchor"),
    "WinchHook": Sprite("Objects/Devices/WinchHook"),

    "KaraokeMachine": Sprite("Objects/Devices/KaraokeMachine", 1, 2),
    "ArcadeCabinet": Sprite("Objects/Devices/ArcadeCabinet", 1, 2),


    # Decorations
    "PumpkinHead01": Sprite("Objects/Cosmetics/PumpkinHead01"),
    "PumpkinHead02": Sprite("Objects/Cosmetics/PumpkinHead02"),
    "PumpkinHead03": Sprite("Objects/Cosmetics/PumpkinHead03"),
    "PumpkinHead04": Sprite("Objects/Cosmetics/PumpkinHead04"),
    "Skull01": Sprite("Objects/Cosmetics/Skull01"),
    "Skull02": Sprite("Objects/Cosmetics/Skull02"),
    "Skull03": Sprite("Objects/Cosmetics/Skull03"),
    "GhostStatue": Sprite("Objects/Cosmetics/GhostStatue", 1, 2),
    "Coffin01": Sprite("Objects/Cosmetics/Coffin01", 1, 1, is_rotatable=True),
    "Coffin02": Sprite("Objects/Cosmetics/Coffin02", 1, 1, is_rotatable=True),
    "TombStone01": Sprite("Objects/Cosmetics/TombStone01", skip_rotations=["U", "L"]),
    "TombStone02": Sprite("Objects/Cosmetics/TombStone02"),
    "TombStone03": Sprite("Objects/Cosmetics/TombStone03"),

    # Furniture
    "Sign": Sprite("Objects/Furniture/Sign", 1, 1, is_rotatable=False),
    "Pantry": Sprite("Objects/Furniture/Pantry", 1, 2),
    "LargePantry": Sprite("Objects/Furniture/LargePantry", 2, 2, 1, 3),
    "Cabinet": Sprite("Objects/Furniture/Cabinet", 1, 2, 1, 2),
    "WardrobeSteel": Sprite("Objects/Furniture/WardrobeSteel", 1, 2, 1, 2),
    "WeaponsLocker": Sprite("Objects/Furniture/WeaponsLocker", 1, 2, 1, 2),
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
    "PetBedNew": Sprite("Objects/Furniture/PetBedNew"),
    "Vase01": Sprite("Objects/Furniture/Vase01", is_rotatable=False),
    "Vase02": Sprite("Objects/Furniture/Vase02", is_rotatable=False),
    "Urn": Sprite("Objects/Furniture/Urn", is_rotatable=False),
    "BedSteel": Sprite("Objects/Furniture/BedSteel", 1, 2, 2, 1, camera_du="F", camera_lr="flat"),
    "BedWood": Sprite("Objects/Furniture/BedWood", 1, 2, 2, 1, camera_du="F", camera_lr="flat"),
    "BedSteelDouble": Sprite("Objects/Furniture/BedSteelDouble", 2, 2, camera_du="F", camera_lr="flat"),
    "BedWoodDouble": Sprite("Objects/Furniture/BedWoodDouble", 2, 2, camera_du="F", camera_lr="flat"),
    "PingPongTable": Sprite("Objects/Furniture/PingPongTable", 2, 2, 1, 3),

    # Chess
    "ChessPawnW": Sprite("Objects/Cosmetics/Chess/ChessPawnW", 1, 2, is_rotatable=False),
    "ChessPawnB": Sprite("Objects/Cosmetics/Chess/ChessPawnB", 1, 2, is_rotatable=False),
    "ChessRookW": Sprite("Objects/Cosmetics/Chess/ChessRookW", 1, 2, is_rotatable=False),
    "ChessRookB": Sprite("Objects/Cosmetics/Chess/ChessRookB", 1, 2, is_rotatable=False),
    "ChessBishopW": Sprite("Objects/Cosmetics/Chess/ChessBishopW", 1, 2, is_rotatable=False),
    "ChessBishopB": Sprite("Objects/Cosmetics/Chess/ChessBishopB", 1, 2, is_rotatable=False),
    "ChessQueenW": Sprite("Objects/Cosmetics/Chess/ChessQueenW", 1, 2, is_rotatable=False),
    "ChessQueenB": Sprite("Objects/Cosmetics/Chess/ChessQueenB", 1, 2, is_rotatable=False),
    "ChessKingW": Sprite("Objects/Cosmetics/Chess/ChessKingW", 1, 2, is_rotatable=False),
    "ChessKingB": Sprite("Objects/Cosmetics/Chess/ChessKingB", 1, 2, is_rotatable=False),
    "ChessKnightW": Sprite("Objects/Cosmetics/Chess/ChessKnightW", 1, 2, is_rotatable=True),
    "ChessKnightB": Sprite("Objects/Cosmetics/Chess/ChessKnightB", 1, 2, is_rotatable=True),

    # Structure
    "TractorBeamTarget": Sprite("Structure/Floors/TractorBeamTarget", camera_du="TD", is_rotatable=False, with_outline=False),
    "TractorBeamTarget_1": Sprite("Structure/Floors/TractorBeamTarget_1", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorVent01": Sprite("Structure/Floors/FloorVent01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorVent01_1": Sprite("Structure/Floors/FloorVent01_1", camera_du="TD", is_rotatable=False, with_outline=False),
    "TrapFloor01": Sprite("Structure/Floors/TrapFloor01", camera_du="TD", is_rotatable=True, with_outline=False, skip_rotations=["U", "L"]),
    "TrapFloor01_1": Sprite("Structure/Floors/TrapFloor01_1", camera_du="TD", is_rotatable=True, with_outline=False, skip_rotations=["U", "L"]),
    "Frame01": Sprite("Structure/Floors/Frame01", camera_du="TD", is_rotatable=False, with_outline=False),
    "Frame02": Sprite("Structure/Floors/Frame02", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor01": Sprite("Structure/Floors/Floor01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorWood01": Sprite("Structure/Floors/FloorWood01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorMarble01": Sprite("Structure/Floors/FloorMarble01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorMarble02": Sprite("Structure/Floors/FloorMarble02", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorGlass01": Sprite("Structure/Floors/FloorGlass01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorGlass01Angle": Sprite("Structure/Floors/FloorGlass01Angle", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorGlass01Lit": Sprite("Structure/Floors/FloorGlass01Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor01t": Sprite("Structure/Floors/Floor01Lit", camera_du="TD", is_rotatable=False, with_outline=False),
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

    # Vents
    "Vent01": Sprite("Structure/Walls/Vent01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "Vent02": Sprite("Structure/Walls/Vent02", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "VentReinforced01": Sprite("Structure/Walls/VentReinforced01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),

    # Wall devices
    "WallSocket01": Sprite("Structure/Walls/WallSocket01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "WallSocket02": Sprite("Structure/Walls/WallSocket02", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "WallSocketReinforced01": Sprite("Structure/Walls/WallSocketReinforced01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),

    # Windows
    "Window01": Sprite("Structure/Walls/Window01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "Window02": Sprite("Structure/Walls/Window02", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "WindowReinforced01": Sprite("Structure/Walls/WindowReinforced01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),

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

    "Human.[N]Body01": Sprite("Beings/Bodies/Human.[N]Body01"),
    "Human.[N]Body01_H": Sprite("Beings/Bodies/Human.[N]Body01_H"),

    "Human.[NL]Body01": Sprite("Beings/Bodies/Human.[NL]Body01"),
    "Human.[NL]Body01_H": Sprite("Beings/Bodies/Human.[NL]Body01_H"),

    "Human.[FL]Body01": Sprite("Beings/Bodies/Human.[FL]Body01"),
    "Human.[FL]Body01_H": Sprite("Beings/Bodies/Human.[FL]Body01_H"),

    "Human.[L]Body01": Sprite("Beings/Bodies/Human.[L]Body01"),
    "Human.[L]Body01_H": Sprite("Beings/Bodies/Human.[L]Body01_H"),

    "Human.[L]Body02": Sprite("Beings/Bodies/Human.[L]Body02"),
    "Human.[L]Body02_H": Sprite("Beings/Bodies/Human.[L]Body02_H"),

    "Human.[ML]Body01": Sprite("Beings/Bodies/Human.[ML]Body01"),
    "Human.[ML]Body01_H": Sprite("Beings/Bodies/Human.[ML]Body01_H"),

    "Human.[F]Body01": Sprite("Beings/Bodies/Human.[F]Body01"),
    "Human.[F]Body01_H": Sprite("Beings/Bodies/Human.[F]Body01_H"),
    "Human.[F]Head01": Sprite("Beings/Heads/Human.[F]Head01", is_head=True),
    "Human.[F]Head01_H": Sprite("Beings/Heads/Human.[F]Head01_H", is_head=True),

    # Weapons
    "EnergyRifle01_": Sprite("Obj/Weapons/EnergyRifle01/EnergyRifle01_", is_rotatable=False),
    "EnergyRifle01": Sprite("Obj/Weapons/EnergyRifle01/EnergyRifle01"),
    "Handgun01_": Sprite("Obj/Weapons/Handgun01/Handgun01_", is_rotatable=False),
    "Handgun01": Sprite("Obj/Weapons/Handgun01/Handgun01"),
    "Knife01_": Sprite("Obj/Weapons/Knife01/Knife01_", is_rotatable=False),
    "Knife01": Sprite("Obj/Weapons/Knife01/Knife01"),

    "Human.[M]Body01": Sprite("Beings/Bodies/Human.[M]Body01"),
    "Human.[M]Body01_H": Sprite("Beings/Bodies/Human.[M]Body01_H"),
    "Human.[M]Head01": Sprite("Beings/Heads/Human.[M]Head01", is_head=True),
    "Human.[M]Head01_H": Sprite("Beings/Heads/Human.[M]Head01_H", is_head=True),
    # Chad
    "Human.[M]Head02": Sprite("Beings/Heads/Human.[M]Head02", is_head=True),
    "Human.[M]Head02_H": Sprite("Beings/Heads/Human.[M]Head02_H", is_head=True),

    "CleaningBot.[N]Body01": Sprite("Beings/Bodies/CleaningBot.[N]Body01"),
    "CleaningBot.[N]Shadow01": Sprite("Beings/Shadows/CleaningBot.[N]Shadow01"),

    "Mindjar.[N]Body01": Sprite("Beings/Bodies/Mindjar.[N]Body01"),
    "Mindjar.[N]Shadow01": Sprite("Beings/Shadows/Mindjar.[N]Shadow01"),
    "Mindjar_Empty.[N]Body01": Sprite("Beings/Bodies/Mindjar_Empty.[N]Body01"),

    "Carrier.[N]Body01": Sprite("Beings/Bodies/Carrier.[N]Body01"),
    "Carrier_Tracks.[N]Body01": Sprite("Beings/Bodies/Carrier_Tracks.[N]Body01"),
    "Carrier.[N]Shadow01": Sprite("Beings/Shadows/Carrier.[N]Shadow01", with_outline=False),

    "Orbotron.[N]Body01": Sprite("Beings/Bodies/Orbotron.[N]Body01"),
    "Orbotron_Tracks.[N]Body01": Sprite("Beings/Bodies/Orbotron_Tracks.[N]Body01"),
    "Orbotron.[N]Shadow01": Sprite("Beings/Shadows/Orbotron.[N]Shadow01", with_outline=False),

    "Drone.[N]Body01": Sprite("Beings/Bodies/Drone.[N]Body01"),
    "Drone_Tracks.[N]Body01": Sprite("Beings/Bodies/Drone_Tracks.[N]Body01"),
    "Drone_NoMobilizer.[N]Body01": Sprite("Beings/Bodies/Drone_NoMobilizer.[N]Body01"),
    "Drone.[N]Shadow01": Sprite("Beings/Shadows/Drone.[N]Shadow01", with_outline=False),

    "Sentry.[N]Body01": Sprite("Beings/Bodies/Sentry.[N]Body01"),
    "Sentry_Tracks.[N]Body01": Sprite("Beings/Bodies/Sentry_Tracks.[N]Body01"),
    "Sentry.[N]Shadow01": Sprite("Beings/Shadows/Sentry.[N]Shadow01", with_outline=False),

    "Robot.[N]Body01": Sprite("Beings/Bodies/Robot.[N]Body01"),
    "Robot.[N]Shadow01": Sprite("Beings/Shadows/Robot.[N]Shadow01", with_outline=False),
    "Robot_NoTracks.[N]Body01": Sprite("Beings/Bodies/Robot_NoTracks.[N]Body01"),
    "Robot_NoMobilizer.[N]Body01": Sprite("Beings/Bodies/Robot_NoMobilizer.[N]Body01"),
    "Robot.[N]Head01": Sprite("Beings/Heads/Robot.[N]Head01"),

    "Cerebrant.[N]Body01": Sprite("Beings/Bodies/Cerebrant.[N]Body01"),
    "Cerebrant.[N]Head01": Sprite("Beings/Heads/Cerebrant.[N]Head01"),

    "Crawler.[N]Body01": Sprite("Beings/Bodies/Crawler.[N]Body01"),
    "Crawler.[N]Body01_1": Sprite("Beings/Bodies/Crawler.[N]Body01_1"),
    "Crawler.[N]Body01_H": Sprite("Beings/Bodies/Crawler.[N]Body01_H"),

    "UnCrawler.[N]Body01": Sprite("Beings/Bodies/UnCrawler.[N]Body01"),
    "UnCrawler.[N]Body01_1": Sprite("Beings/Bodies/UnCrawler.[N]Body01_1"),
    "UnCrawler.[N]Body01_H": Sprite("Beings/Bodies/UnCrawler.[N]Body01_H"),

    "Cat.[N]Body01": Sprite("Beings/Bodies/Cat.[N]Body01"),
    "Cat.[N]Body02": Sprite("Beings/Bodies/Cat.[N]Body02"),
    "Cat.[N]Body03": Sprite("Beings/Bodies/Cat.[N]Body03"),
    "Cat.[N]Body01_H": Sprite("Beings/Bodies/Cat.[N]Body01_H"),
    "Cat.[N]Body02_H": Sprite("Beings/Bodies/Cat.[N]Body02_H"),
    "Cat.[N]Body03_H": Sprite("Beings/Bodies/Cat.[N]Body03_H"),

    "Sheep.[N]Body01": Sprite("Beings/Bodies/Sheep.[N]Body01"),
    "Sheep.[N]Body01_H": Sprite("Beings/Bodies/Sheep.[N]Body01_H"),
    "Sheep_Shaved.[N]Body01": Sprite("Beings/Bodies/Sheep_Shaved.[N]Body01"),
    "Sheep_Shaved.[N]Body01_H": Sprite("Beings/Bodies/Sheep_Shaved.[N]Body01_H"),

    "Chic.[N]Body01": Sprite("Beings/Bodies/Chic.[N]Body01"),
    "Chic.[N]Body01_H": Sprite("Beings/Bodies/Chic.[N]Body01_H"),

    "Hen.[N]Body01": Sprite("Beings/Bodies/Hen.[N]Body01"),
    "Hen.[N]Body01_H": Sprite("Beings/Bodies/Hen.[N]Body01_H"),

    "Rooster.[N]Body01": Sprite("Beings/Bodies/Rooster.[N]Body01"),
    "Rooster.[N]Body01_H": Sprite("Beings/Bodies/Rooster.[N]Body01_H"),

    "Cow.[N]Body01": Sprite("Beings/Bodies/Cow.[N]Body01"),
    "Cow.[N]Body01_H": Sprite("Beings/Bodies/Cow.[N]Body01_H"),

    "Pig.[N]Body01": Sprite("Beings/Bodies/Pig.[N]Body01"),
    "Pig.[N]Body01_H": Sprite("Beings/Bodies/Pig.[N]Body01_H"),

    "Dog.[N]Body01": Sprite("Beings/Bodies/Dog.[N]Body01"),
    "Dog.[N]Body01_H": Sprite("Beings/Bodies/Dog.[N]Body01_H"),

    "Dog.[N]Body02": Sprite("Beings/Bodies/Dog.[N]Body02"),
    "Dog.[N]Body02_H": Sprite("Beings/Bodies/Dog.[N]Body02_H"),

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
    "PumpkinPlant": Sprite("Obj/Plants/PumpkinPlant", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),
    "ArtilleryFungus": Sprite("Obj/Plants/ArtilleryFungus", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),
    # Trees
    "Oak": Sprite("Obj/Plants/Oak", 2, 2, camera_du="F", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),
    "RubberTree": Sprite("Obj/Plants/RubberTree", 2, 2, camera_du="F", is_rotatable=False,
        subset=["_", "_Growing1", "_Growing2", "_Seed"]),

    # Animated Tiles
    "Loom": Sprite("Objects/Devices/Loom", 1, 1),
    "Loom_Base": Sprite("Objects/Devices/Loom_Base", 1, 1),
    "Loom_Anim": Sprite("Objects/DeviceAnims/Loom_Anim", 1, 1, anim_frames=24),

    "OxyMaticFloor": Sprite("Structure/Floors/OxyMaticFloor", camera_du="TD", is_rotatable=False, with_outline=False),
    "OxyMaticFloor_Anim": Sprite("Objects/DeviceAnims/OxyMaticFloor_Anim", camera_du="TD", is_rotatable=False, with_outline=False, anim_frames=4),

    "Treadmill": Sprite("Objects/Devices/Treadmill", 2, 1, 1, 2, camera_lr="flat"),
    "Treadmill_Anim": Sprite("Objects/DeviceAnims/Treadmill_Anim", 1, 1, camera_lr="flat", anim_frames=4),

    "AutoDoc": Sprite("Objects/Devices/AutoDoc", 2, 2, 1, 3),
    "AutoDoc_Base": Sprite("Objects/Devices/AutoDoc_Base", 2, 2, 1, 3),
    "AutoDoc_Anim": Sprite("Objects/DeviceAnims/AutoDoc_Anim", 1, 1, anim_frames=24),

    "ParticleCollector": Sprite("Objects/Devices/ParticleCollector", 2, 3, 3, 2, camera_lr="flat"),
    "ParticleCollector_Base": Sprite("Objects/Devices/ParticleCollector_Base", 2, 3, 3, 2, camera_lr="flat"),
    "ParticleCollector_Anim": Sprite("Objects/DeviceAnims/ParticleCollector_Anim", 1, 1, is_rotatable=False, anim_frames=24),

    "Assembler": Sprite("Objects/Devices/Assembler", 2, 2, 1, 3),
    "Assembler_Base": Sprite("Objects/Devices/Assembler_Base", 2, 2, 1, 3, skip_rotations=['L', 'R']),
    "Assembler_Anim": Sprite("Objects/DeviceAnims/Assembler_Anim", 1, 1, is_rotatable=False, anim_frames=24),

    "DataHarvesterQuantum": Sprite("Objects/Devices/DataHarvesterQuantum", 2, 3, is_rotatable=False),
    "DataHarvesterQuantum_Base": Sprite("Objects/Devices/DataHarvesterQuantum_Base", 2, 3, is_rotatable=False),
    "DataHarvesterQuantum_Anim": Sprite("Objects/DeviceAnims/DataHarvesterQuantum_Anim", 1, 1, is_rotatable=False, anim_frames=24),

    "RepairStation": Sprite("Objects/Devices/RepairStation", 1, 2),
    "RepairStation_Base": Sprite("Objects/Devices/RepairStation_Base", 1, 2),
    "RepairStation_Anim": Sprite("Objects/DeviceAnims/RepairStation_Anim", 1, 1, anim_frames=24),

    "CloningPod": Sprite("Objects/Devices/CloningPod", 2, 3),
    "CloningPod_Base": Sprite("Objects/Devices/CloningPod_Base", 2, 3),
    "CloningPod_Anim": Sprite("Objects/DeviceAnims/CloningPod_Anim", 1, 1, is_rotatable=False, anim_frames=25, anim_speed_pct=200),

    "CraftingStation": Sprite("Objects/Devices/CraftingStation", 2, 2, 1, 3),
    "CraftingStation_Base": Sprite("Objects/Devices/CraftingStation_Base", 2, 2, 1, 3),
    "CraftingStation_Anim": Sprite("Objects/DeviceAnims/CraftingStation_Anim", 1, 1, is_rotatable=True, anim_frames=25),

    "VoidRipper": Sprite("Objects/Devices/VoidRipper", 3, 4, is_rotatable=False),
    "VoidRipper_Base": Sprite("Objects/Devices/VoidRipper_Base", 3, 4, is_rotatable=False),
    "VoidRipper_Anim": Sprite("Objects/DeviceAnims/VoidRipper_Anim", 1, 1, anim_frames=49, is_rotatable=False),

    "Telescope": Sprite("Objects/Devices/Telescope", 2, 3, is_rotatable=False),
    "Telescope_Base": Sprite("Objects/Devices/Telescope_Base", 2, 3, is_rotatable=False),
    "Telescope_Anim": Sprite("Objects/DeviceAnims/Telescope_Anim", 1, 1, anim_frames=49, is_rotatable=False),

    "NutrientExtractor": Sprite("Objects/Devices/NutrientExtractor", 2, 3),
    "NutrientExtractor_Anim": Sprite("Objects/DeviceAnims/NutrientExtractor_Anim", 1, 1,
        anim_frames=12, is_rotatable=True, skip_rotations=['U', 'L']),

    "Grinder": Sprite("Objects/Devices/Grinder", 2, 3),
    "Grinder_Anim": Sprite("Objects/DeviceAnims/Grinder_Anim", 1, 1, num_rotations=64, stop_at_rotation=8, activate_filter="ROT_"),

    "FluxCapacitor": Sprite("Objects/Devices/FluxCapacitor", 2, 2, is_rotatable=False),
    "FluxCapacitor_Base": Sprite("Objects/Devices/FluxCapacitor_Base", 2, 2, is_rotatable=False),
    "FluxCapacitor_Anim": Sprite("Objects/DeviceAnims/FluxCapacitor_Anim", 1, 1, num_rotations=72, stop_at_rotation=24, activate_filter="ROT_"),

    "OxygenPumpMini": Sprite("Objects/Devices/OxygenPumpMini", 1, 1, is_rotatable=True),
    "OxygenPump_Anim": Sprite("Objects/DeviceAnims/OxygenPump_Anim", 1, 1, num_rotations=64, stop_at_rotation=8, activate_filter="ROT_"),

    "ShipComputer": Sprite("Objects/Devices/ShipComputer", 2, 3, is_rotatable=False),
    "ShipComputer_Base": Sprite("Objects/Devices/ShipComputer_Base", 2, 3, is_rotatable=False),
    "ShipComputer_Anim": Sprite("Objects/DeviceAnims/ShipComputer_Anim", 1, 1, num_rotations=240, stop_at_rotation=48),

    "Centrifuge": Sprite("Objects/Devices/Centrifuge", 2, 3, is_rotatable=True),
    "Centrifuge_Anim": Sprite("Objects/DeviceAnims/Centrifuge_Anim", 1, 1, num_rotations=128, stop_at_rotation=8, activate_filter="ROT_"),

    "BeamDrill": Sprite("Objects/Devices/BeamDrill", 2, 3, is_rotatable=False),
    "BeamDrill_Anim": Sprite("Objects/DeviceAnims/BeamDrill_Anim", 1, 2, num_rotations=32, stop_at_rotation=8, activate_filter="ROT_"),

    "BreachCapsule_Drill_Anim": Sprite("Objects/DeviceAnims/BreachCapsule_Drill_Anim", 1, 1, num_rotations=32, stop_at_rotation=8, activate_filter="ROT_"),

    "Radar": Sprite("Objects/Devices/Radar", 2, 3, is_rotatable=False),
    "Radar_Base": Sprite("Objects/Devices/Radar_Base", 2, 3, is_rotatable=False),
    "Radar_Anim": Sprite("Objects/DeviceAnims/Radar_Anim", 1, 1, num_rotations=128),

    "SystemScanner": Sprite("Objects/Devices/SystemScanner", 2, 3, is_rotatable=False),
    "SystemScanner_Base": Sprite("Objects/Devices/SystemScanner_Base", 2, 3, is_rotatable=False),
    "SystemScanner_Anim": Sprite("Objects/DeviceAnims/SystemScanner_Anim", 1, 1, num_rotations=128, stop_at_rotation=64),

    # Ship facilities
    "ShieldEmitter": Sprite("Objects/Devices/ShieldEmitter", 2, 3, is_rotatable=False),
    "ShieldEmitter_Base": Sprite("Objects/Devices/ShieldEmitter_Base", 2, 3, is_rotatable=False),
    "ShieldEmitter_Anim": Sprite("Objects/DeviceAnims/ShieldEmitter_Anim", 1, 1, is_rotatable=False, anim_frames=24, anim_speed_pct=200),

    # Turrets
    "MiniTurret": Sprite("Objects/Devices/MiniTurret", is_rotatable=False),
    "MiniTurret_Base": Sprite("Objects/Devices/MiniTurret_Base", is_rotatable=False),
    "MiniTurret_Head": Sprite("Objects/TurretHeads/MiniTurret_Head", num_rotations=128),

    "InterceptorTurret": Sprite("Objects/Devices/InterceptorTurret", is_rotatable=False),

    "InterceptorTurret": Sprite("Objects/Devices/InterceptorTurret", 1, 1, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "InterceptorTurret_Base": Sprite("Objects/Devices/InterceptorTurret_Base", 1, 1, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "InterceptorTurret_Head": Sprite("Objects/TurretHeads/InterceptorTurret_Head", 1, 1,
        camera_du="F", camera_lr="flat", num_rotations=128, stop_at_rotation=43),

    "ShredderCannon": Sprite("Objects/Devices/ShredderCannon", 2, 2, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "ShredderCannon_Base": Sprite("Objects/Devices/ShredderCannon_Base", 2, 2, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "ShredderCannon_Head": Sprite("Objects/TurretHeads/ShredderCannon_Head", 1, 1,
        camera_du="F", camera_lr="flat", num_rotations=128),
    "ShredderCannon_Top": Sprite("Objects/Devices/ShredderCannon_Top", 2, 2, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "ShredderCannon_ZoneView": Sprite("Objects/Devices/ShredderCannon_ZoneView", 1, 1,
        camera_du="F", camera_lr="flat"),

    "GaussStriker": Sprite("Objects/Devices/GaussStriker", 2, 2, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "GaussStriker_Base": Sprite("Objects/Devices/GaussStriker_Base", 2, 2, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "GaussStriker_Head": Sprite("Objects/TurretHeads/GaussStriker_Head", 1, 1,
        camera_du="F", camera_lr="flat", num_rotations=128),
    "GaussStriker_Top": Sprite("Objects/Devices/GaussStriker_Top", 2, 2, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "GaussStriker_ZoneView": Sprite("Objects/Devices/GaussStriker_ZoneView", 1, 1,
        camera_du="F", camera_lr="flat"),

    "RocketPod": Sprite("Objects/Devices/RocketPod", 2, 2, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "RocketPod_Base": Sprite("Objects/Devices/RocketPod_Base", 2, 2, is_rotatable=False,
        camera_du="F", camera_lr="flat"),
    "RocketPod_Head": Sprite("Objects/TurretHeads/RocketPod_Head", 1, 1,
        camera_du="F", camera_lr="flat", num_rotations=128),
    "RocketPod_ZoneView": Sprite("Objects/Devices/RocketPod_ZoneView", 1, 1,
        camera_du="F", camera_lr="flat"),

    "HeavyLaser": Sprite("Objects/Devices/HeavyLaser", 2, 2, is_rotatable=True,
        camera_du="F", camera_lr="flat"),
    "HeavyLaser_Base": Sprite("Objects/Devices/HeavyLaser_Base", 2, 2, is_rotatable=True,
        camera_du="F", camera_lr="flat"),
    "HeavyLaser_Head": Sprite("Objects/TurretHeads/HeavyLaser_Head", 1, 1,
        camera_du="F", camera_lr="flat", num_rotations=128),
    "HeavyLaser_ZoneView": Sprite("Objects/Devices/HeavyLaser_ZoneView", 1, 1,
        camera_du="F", camera_lr="flat"),

    # Asteroids
    "Asteroid01": Sprite("Obj/Asteroids/Asteroid01", 3, 3, is_rotatable=False, line_sets=["ObjectBorder"]),
    "Asteroid02": Sprite("Obj/Asteroids/Asteroid02", 3, 3, is_rotatable=False, line_sets=["ObjectBorder"]),
    "Asteroid03": Sprite("Obj/Asteroids/Asteroid03", 3, 3, is_rotatable=False, line_sets=["ObjectBorder"]),
    "Asteroid04": Sprite("Obj/Asteroids/Asteroid04", 3, 3, is_rotatable=False, line_sets=["ObjectBorder"]),
    "Asteroid05": Sprite("Obj/Asteroids/Asteroid05", 3, 3, is_rotatable=False, line_sets=["ObjectBorder"]),

    # Ships
    "SpaceStation01": Sprite("SpaceObjects/Stations/SpaceStation01", 4, 4, is_rotatable=False),
    # Unclassified – A generic ship that doesn't fit into any other category.
    "ShipUnclassified01": Sprite("SpaceObjects/Ships/ShipUnclassified01", 3, 3, 3, 3),
    "ShipUnclassified01_Derelict": Sprite("SpaceObjects/Derelicts/ShipUnclassified01_Derelict", 3, 3, 3, 3),
    # Fighter – Small, fast, one or two crew, dogfighting, scouting.
    "ShipFighter01": Sprite("SpaceObjects/Ships/ShipFighter01", 3, 3, 3, 3),
    "ShipFighter01_Derelict": Sprite("SpaceObjects/Derelicts/ShipFighter01_Derelict", 3, 3, 3, 3),
    # Corvette – Slightly bigger than a fighter, light armament, escort, or recon.
    "ShipCorvette01": Sprite("SpaceObjects/Ships/ShipCorvette01", 3, 3, 3, 3),
    "ShipCorvette01_Derelict": Sprite("SpaceObjects/Derelicts/ShipCorvette01_Derelict", 3, 3, 3, 3),
    # Frigate – Medium-sized, versatile, good firepower, often a patrol or escort ship.
    "ShipFrigate01": Sprite("SpaceObjects/Ships/ShipFrigate01", 3, 3, 3, 3),
    "ShipFrigate01_Derelict": Sprite("SpaceObjects/Derelicts/ShipFrigate01_Derelict", 3, 3, 3, 3),
    # Destroyer – Fast, heavily armed, used for fleet defense or offense.
    "ShipDestroyer01": Sprite("SpaceObjects/Ships/ShipDestroyer01", 3, 3, 3, 3),
    "ShipDestroyer01_Derelict": Sprite("SpaceObjects/Derelicts/ShipDestroyer01_Derelict", 3, 3, 3, 3),
    # Cruiser – Larger, well-rounded, can act as a fleet command or heavy hitter.
    "ShipCruiser01": Sprite("SpaceObjects/Ships/ShipCruiser01", 3, 3, 3, 3),
    "ShipCruiser01_Derelict": Sprite("SpaceObjects/Derelicts/ShipCruiser01_Derelict", 3, 3, 3, 3),
    # Battlecruiser – Heavily armed but more mobile than a battleship.
    "ShipBattlecruiser01": Sprite("SpaceObjects/Ships/ShipBattlecruiser01", 3, 3, 3, 3),
    "ShipBattlecruiser01_Derelict": Sprite("SpaceObjects/Derelicts/ShipBattlecruiser01_Derelict", 3, 3, 3, 3),
    # Battleship – Massive, slow, bristling with weapons and defenses.
    "ShipBattleship01": Sprite("SpaceObjects/Ships/ShipBattleship01", 3, 3, 3, 3),
    "ShipBattleship01_Derelict": Sprite("SpaceObjects/Derelicts/ShipBattleship01_Derelict", 3, 3, 3, 3),
    # Carrier – Deploys smaller craft, supports fleets logistically.
    "ShipCarrier01": Sprite("SpaceObjects/Ships/ShipCarrier01", 3, 3, 3, 3),
    "ShipCarrier01_Derelict": Sprite("SpaceObjects/Derelicts/ShipCarrier01_Derelict", 3, 3, 3, 3),
    # Dreadnought – The ultimate warship, extreme firepower and armor.
    "ShipDreadnought01": Sprite("SpaceObjects/Ships/ShipDreadnought01", 3, 3, 3, 3),
    "ShipDreadnought01_Derelict": Sprite("SpaceObjects/Derelicts/ShipDreadnought01_Derelict", 3, 3, 3, 3),
    # Titan – Gigantic, game-changing, superweapon potential.
    "ShipTitan01": Sprite("SpaceObjects/Ships/ShipTitan01", 3, 3, 3, 3),
    "ShipTitan01_Derelict": Sprite("SpaceObjects/Derelicts/ShipTitan01_Derelict", 3, 3, 3, 3),
    "ShipSpaceStation01_Derelict": Sprite("SpaceObjects/Derelicts/ShipSpaceStation01_Derelict", 3, 3, 3, 3, is_rotatable=False),

    # Space Objects
    "HyperjumpRelay01": Sprite("SpaceObjects/Misc/HyperjumpRelay01", 4, 4, is_rotatable=False),
    "ReturnBeacon01": Sprite("SpaceObjects/Misc/ReturnBeacon01", 1, 1, is_rotatable=False),

    # Bullet
    "EnergyBullet": Sprite("Obj/Misc/EnergyBullet", is_rotatable=False),
    "WaterBullet": Sprite("Obj/Misc/WaterBullet", is_rotatable=False, with_outline=False),
    "BiowasteBullet": Sprite("Obj/Misc/BiowasteBullet", is_rotatable=False, with_outline=False),

    # Eggs
    "Egg01": Sprite("Obj/Eggs/Egg01", is_rotatable=False),

    # Body Parts
    "BodyPartRobotic": Sprite("Obj/BodyParts/Robotic", is_rotatable=False),
    "BodyPartRobotic1": Sprite("Obj/BodyParts/Robotic1", is_rotatable=False),
    "BodyPartRobotic2": Sprite("Obj/BodyParts/Robotic2", is_rotatable=False),
    "BodyPartRobotic3": Sprite("Obj/BodyParts/Robotic3", is_rotatable=False),
    "BodyPartOrganic": Sprite("Obj/BodyParts/Organic", is_rotatable=False),
    "BodyPartOrganic1": Sprite("Obj/BodyParts/Organic1", is_rotatable=False),
    "BodyPartOrganic2": Sprite("Obj/BodyParts/Organic2", is_rotatable=False),
    "BodyPartOrganic3": Sprite("Obj/BodyParts/Organic3", is_rotatable=False),

    # Misc
    "C42": Sprite("Obj/Misc/C42", is_rotatable=False),
    "C42_Armed": Sprite("Obj/Misc/C42_Armed", is_rotatable=False),

    # Containers
    "QuestPackage": Sprite("Obj/Containers/QuestPackage", is_rotatable=False),
    "QuestPackage_Open": Sprite("Obj/Containers/QuestPackage_Open", is_rotatable=False),
    "StorageCapsule": Sprite("Obj/Containers/StorageCapsule", is_rotatable=False),
    "StorageCapsule_Open": Sprite("Obj/Containers/StorageCapsule_Open", is_rotatable=False),
    "Hullpiercer": Sprite("Obj/Containers/Hullpiercer", is_rotatable=False),
    "Hullpiercer_Open": Sprite("Obj/Containers/Hullpiercer_Open", is_rotatable=False),

    # Meals
    "SoyBurger": Sprite("Obj/Meals/SoyBurger", is_rotatable=False),
    "PumpkinSoup": Sprite("Obj/Meals/PumpkinSoup", is_rotatable=False),
    "Bread": Sprite("Obj/Meals/Bread", is_rotatable=False),
    "SurvivalMeal": Sprite("Obj/Meals/SurvivalMeal", is_rotatable=False),

    # Materials
    "Aerolith": Sprite("Obj/Materials/Aerolith", is_rotatable=False),
    "Terranite": Sprite("Obj/Materials/Terranite", is_rotatable=False),
    "Hydronium": Sprite("Obj/Materials/Hydronium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Edenium": Sprite("Obj/Materials/Edenium", is_rotatable=False, line_sets=["ObjectBorder"]),

    "Nanobots": Sprite("Obj/Materials/Nanobots", is_rotatable=False),
    "SteelPlate": Sprite("Obj/Materials/SteelPlate", is_rotatable=False),
    "LeadPlate": Sprite("Obj/Materials/LeadPlate", is_rotatable=False),
    "CopperPlate": Sprite("Obj/Materials/CopperPlate", is_rotatable=False),
    "TitaniumPlate": Sprite("Obj/Materials/TitaniumPlate", is_rotatable=False),
    "Microchip": Sprite("Obj/Materials/Microchip", is_rotatable=False),
    "Microchip2": Sprite("Obj/Materials/Microchip2", is_rotatable=False),
    "Microchip3": Sprite("Obj/Materials/Microchip3", is_rotatable=False),
    "Glass": Sprite("Obj/Materials/Glass", is_rotatable=False),
    "BatteryCell": Sprite("Obj/Materials/BatteryCell", is_rotatable=False),
    "Rock": Sprite("Obj/Materials/Rock", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Protein": Sprite("Obj/Materials/Protein", is_rotatable=False),
    "StemCells": Sprite("Obj/Materials/StemCells", is_rotatable=False),
    "PlantFiber": Sprite("Obj/Materials/PlantFiber", is_rotatable=False),
    "PoppyHeads": Sprite("Obj/Materials/PoppyHeads", is_rotatable=False),
    "Pumpkin": Sprite("Obj/Materials/Pumpkin", is_rotatable=False),
    "PoppyPetals": Sprite("Obj/Materials/PoppyPetals", is_rotatable=False),
    "CornflowerPetals": Sprite("Obj/Materials/CornflowerPetals", is_rotatable=False),
    "Coal": Sprite("Obj/Materials/Coal", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Quartz": Sprite("Obj/Materials/Quartz", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Ashes": Sprite("Obj/Materials/Ashes", is_rotatable=False),
    "Carbon": Sprite("Obj/Materials/Carbon", is_rotatable=False),
    "CarbonFiber": Sprite("Obj/Materials/CarbonFiber", is_rotatable=False),
    "Copper": Sprite("Obj/Materials/Copper", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Gold": Sprite("Obj/Materials/Gold", is_rotatable=False, line_sets=["ObjectBorder"]),
    "GoldIngot": Sprite("Obj/Materials/GoldIngot", is_rotatable=False),
    "Silver": Sprite("Obj/Materials/Silver", is_rotatable=False, line_sets=["ObjectBorder"]),
    "SilverIngot": Sprite("Obj/Materials/SilverIngot", is_rotatable=False),
    "Platinum": Sprite("Obj/Materials/Platinum", is_rotatable=False, line_sets=["ObjectBorder"]),
    "PlatinumIngot": Sprite("Obj/Materials/PlatinumIngot", is_rotatable=False),
    "Iron": Sprite("Obj/Materials/Iron", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Lead": Sprite("Obj/Materials/Lead", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Silicon": Sprite("Obj/Materials/Silicon", is_rotatable=False, line_sets=["ObjectBorder"]),
    "SiliconWafer": Sprite("Obj/Materials/SiliconWafer", is_rotatable=False),
    "Lithium": Sprite("Obj/Materials/Lithium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Soil": Sprite("Obj/Materials/Soil", is_rotatable=False),
    "Titanium": Sprite("Obj/Materials/Titanium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Uranium": Sprite("Obj/Materials/Uranium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Wood": Sprite("Obj/Materials/Wood", is_rotatable=False),

    "Phasium": Sprite("Obj/Materials/Phasium", is_rotatable=False),
    "FusionCell": Sprite("Obj/Materials/FusionCell", is_rotatable=False),
    "FusionCellHeavy": Sprite("Obj/Materials/FusionCellHeavy", is_rotatable=False),

    "Missile": Sprite("Obj/Ammo/Missile", is_rotatable=False),
    "InterceptorDart": Sprite("Obj/Ammo/InterceptorDart", is_rotatable=False),

    "Biowaste": Sprite("Obj/Materials/Biowaste", is_rotatable=False),
    "Water": Sprite("Obj/Materials/Water", is_rotatable=False),
    "Ice": Sprite("Obj/Materials/Ice", is_rotatable=False, line_sets=["ObjectBorder"]),
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
    "GoldWire": Sprite("Obj/Materials/GoldWire", is_rotatable=False),
    "OpticalFiber": Sprite("Obj/Materials/OpticalFiber", is_rotatable=False),
    "BioEnrichedWater": Sprite("Obj/Materials/BioEnrichedWater", is_rotatable=False),
    "OrganicTurf": Sprite("Obj/Materials/OrganicTurf", is_rotatable=False),
    "AtmosphereMix": Sprite("Obj/Materials/AtmosphereMix", is_rotatable=False),
    "MultiFertilizer": Sprite("Obj/Materials/MultiFertilizer", is_rotatable=False),
    "PigmentRed": Sprite("Obj/Materials/PigmentRed", is_rotatable=False),
    "PigmentGreen": Sprite("Obj/Materials/PigmentGreen", is_rotatable=False),
    "PigmentBlue": Sprite("Obj/Materials/PigmentBlue", is_rotatable=False),

    # Upgrades
    "ReactorEfficiencyUpgrade": Sprite("Obj/Upgrades/ReactorEfficiencyUpgrade", is_rotatable=False),
    "ProcessorEfficiencyUpgrade": Sprite("Obj/Upgrades/ProcessorEfficiencyUpgrade", is_rotatable=False),
    "AsimovOverrideUpgrade": Sprite("Obj/Upgrades/AsimovOverrideUpgrade", is_rotatable=False),
    "StarcredsMiningUpgrade": Sprite("Obj/Upgrades/StarcredsMiningUpgrade", is_rotatable=False),
    "ShuttleStorageUpgrade": Sprite("Obj/Upgrades/ShuttleStorageUpgrade", is_rotatable=False),
    "AutoConnectUpgrade": Sprite("Obj/Upgrades/AutoConnectUpgrade", is_rotatable=False),
    "DiskCompressionUpgrade": Sprite("Obj/Upgrades/DiskCompressionUpgrade", is_rotatable=False),
    "MemoryCompressionUpgrade": Sprite("Obj/Upgrades/MemoryCompressionUpgrade", is_rotatable=False),
    "AutoPilotUpgrade": Sprite("Obj/Upgrades/AutoPilotUpgrade", is_rotatable=False),
    "FuseUpgrade": Sprite("Obj/Upgrades/FuseUpgrade", is_rotatable=False),
    "WinchRangeUpgrade": Sprite("Obj/Upgrades/WinchRangeUpgrade", is_rotatable=False),
}

add_hat(SPRITES, "Human", "Hat01")
add_hat(SPRITES, "Human", "BaseballCap01")
add_hat(SPRITES, "Human", "CrawlerFacehug")
add_hat(SPRITES, "Human", "UnCrawlerFacehug")
add_hat(SPRITES, "Human", "SpaceHelmet01")
add_hat(SPRITES, "Human", "SpaceHelmet02")
add_hat(SPRITES, "Human", "JesterHat")
add_clothing(SPRITES, "Human", "Uniform01")
add_clothing(SPRITES, "Human", "Uniform02")
add_clothing(SPRITES, "Human", "Uniform03")
add_clothing(SPRITES, "Human", "SpaceSuit01")
add_clothing(SPRITES, "Human", "SpaceSuit02")
add_clothing(SPRITES, "Human", "Tracksuit01")
add_clothing(SPRITES, "Human", "Tracksuit02")

# Increase range end to add more sprites
for i in range(1, 30):
    add_hair(SPRITES, "Human", "F", f"{i:02d}")

# Increase range end to add more sprites
for i in range(1, 20):
    add_hair(SPRITES, "Human", "M", f"{i:02d}")