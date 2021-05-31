class Sprite:
    def __init__(self, path, 
            width_du = 1, height_du = 1, 
            # Zero == same as du
            width_lr = 0, height_lr = 0, 
            camera_du= "" , camera_lr = "same_as_du", 
            is_rotatable=True, with_outline=True, 
            lights="Object Lights",
            line_sets=["Object"],
            subset=[]):
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


SPRITES = {
    # Devices

    "ModTest": Sprite("Objects/Devices/ModTest", 2, 2, 1, 3),

    "Battery": Sprite("Objects/Devices/Battery", 2, 1, 1, 2, camera_lr="flat"),
    "PlanterMini": Sprite("Objects/Devices/PlanterMini"),
    "SolarPanel": Sprite("Objects/Devices/SolarPanel", camera_du="TD", is_rotatable=False),
    "SolarPanelArray": Sprite("Objects/Devices/SolarPanelArray", 2, 2, camera_du="TD", is_rotatable=False),
    "MatterReactor": Sprite("Objects/Devices/MatterReactor", 2, 3),
    "CloningPod": Sprite("Objects/Devices/CloningPod", 2, 3),
    "Loom": Sprite("Objects/Devices/Loom", 2, 3),
    "FluidCannon": Sprite("Objects/Devices/FluidCannon", 2, 3),
    "MatterReactorMini": Sprite("Objects/Devices/MatterReactorMini", 2, 2, 1, 3),
    "StasisArray": Sprite("Objects/Devices/StasisArray", 5, 6, is_rotatable=True),
    "Storage": Sprite("Objects/Devices/Storage", 3, 4),
    "NutrientExtractor": Sprite("Objects/Devices/NutrientExtractor", 3, 4),
    "ChargeStation": Sprite("Objects/Devices/ChargeStation"),
    "Switch": Sprite("Objects/Devices/Switch"),
    "CleaningBotDock": Sprite("Objects/Devices/CleaningBotDock"),
    "EnergyConnector": Sprite("Objects/Devices/EnergyConnector", 1, 2),
    "DirectionalTurret": Sprite("Objects/Devices/DirectionalTurret", 1, 3, 2, 2),
    "EmergencySiren": Sprite("Objects/Devices/EmergencySiren", 1, 2),
    "RepairStation": Sprite("Objects/Devices/RepairStation", 1, 2),
    "EnergyConnectorBig": Sprite("Objects/Devices/EnergyConnectorBig", 1, 2),
    "MemoryModule": Sprite("Objects/Devices/MemoryModule", 1, 2),
    "MemoryModuleMini": Sprite("Objects/Devices/MemoryModuleMini", 1, 2),
    "ShipComputer": Sprite("Objects/Devices/ShipComputer", 2, 3, is_rotatable=True),
    "HeatSink": Sprite("Objects/Devices/HeatSink", 1, 2, is_rotatable=False),
    "StardeusLogo": Sprite("FX/StardeusLogo", 12, 3, is_rotatable=False),
    "StorageModule": Sprite("Objects/Devices/StorageModule", 1, 2),
    "StorageModuleMini": Sprite("Objects/Devices/StorageModuleMini", 1, 2),
    "Engine": Sprite("Objects/Devices/Engine", 3, 3),
    "Thruster": Sprite("Objects/Devices/Thruster"),
    "BridgeControls": Sprite("Objects/Devices/BridgeControls", 3, 2, 2, 3, camera_lr="flat"),
    "Shuttle": Sprite("Objects/Devices/Shuttle", 3, 5, 4, 4),
    "ShuttleFlying": Sprite("Objects/Devices/ShuttleFlying", 3, 5, 4, 4),
    "ShuttlePad": Sprite("Objects/Devices/ShuttlePad", 3, 5, 4, 4),
    "OxygenPump": Sprite("Objects/Devices/OxygenPump", 2, 2, 1, 3),
    "Heater": Sprite("Objects/Devices/Heater", 1, 2),
    "Fridge": Sprite("Objects/Devices/Fridge", 1, 2),
    "Toilet": Sprite("Objects/Devices/Toilet", 1, 2),
    "Shower": Sprite("Objects/Devices/Shower", 1, 2),
    "Assembler": Sprite("Objects/Devices/Assembler", 2, 2, 1, 3),
    "Disassembler": Sprite("Objects/Devices/Disassembler", 3, 4),
    "AutoKitchen": Sprite("Objects/Devices/AutoKitchen", 2, 2, 1, 3),
    "SleepingPod": Sprite("Objects/Devices/SleepingPod", 2, 2, 1, 3),
    "Radar": Sprite("Objects/Devices/Radar", 3, 4),
    "Furnace": Sprite("Objects/Devices/Furnace", 3, 4),
    "Grinder": Sprite("Objects/Devices/Grinder", 3, 4),
    "Recycler": Sprite("Objects/Devices/Recycler", 3, 4),
    "Communicator": Sprite("Objects/Devices/Communicator", 2, 2, 1, 3),
    "ParticleCollector": Sprite("Objects/Devices/ParticleCollector", 2, 3, 3, 2, camera_lr="flat"),

    # Furniture
    "WardrobeSteel": Sprite("Objects/Furniture/WardrobeSteel", 1, 2, 1, 2),
    "ChairCaptain": Sprite("Objects/Furniture/ChairCaptain"),
    "ChairSteel": Sprite("Objects/Furniture/ChairSteel"),
    "ChairWood": Sprite("Objects/Furniture/ChairWood"),
    "TableSteel1x2": Sprite("Objects/Furniture/TableSteel1x2", 2, 1, 1, 2, camera_lr="flat"),
    "TableSteel1x3": Sprite("Objects/Furniture/TableSteel1x3", 3, 1, 1, 3, camera_lr="flat"),
    "TableWood1x2": Sprite("Objects/Furniture/TableWood1x2", 2, 1, 1, 2, camera_lr="flat"),
    "TableWood1x3": Sprite("Objects/Furniture/TableWood1x3", 3, 1, 1, 3, camera_lr="flat"),
    "BedSteel": Sprite("Objects/Furniture/BedSteel", 1, 2, 2, 1, camera_du="F", camera_lr="flat"),
    "BedWood": Sprite("Objects/Furniture/BedWood", 1, 2, 2, 1, camera_du="F", camera_lr="flat"),

    # Structure
    "Frame01": Sprite("Structure/Floors/Frame01", camera_du="TD", is_rotatable=False, with_outline=False),
    "Frame02": Sprite("Structure/Floors/Frame02", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor01": Sprite("Structure/Floors/Floor01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorGlass01": Sprite("Structure/Floors/FloorGlass01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorGlass01Angle": Sprite("Structure/Floors/FloorGlass01Angle", camera_du="TD", is_rotatable=True, with_outline=False),
    "FloorGlass01Lit": Sprite("Structure/Floors/FloorGlass01Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor01Lit": Sprite("Structure/Floors/Floor01Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor01Angle": Sprite("Structure/Floors/Floor01Angle", camera_du="TD", is_rotatable=True, with_outline=False),
    "Floor02": Sprite("Structure/Floors/Floor02", camera_du="TD", is_rotatable=False, with_outline=False),
    "Floor02Angle": Sprite("Structure/Floors/Floor02Angle", camera_du="TD", is_rotatable=True, with_outline=False),
    "Floor02Lit": Sprite("Structure/Floors/Floor02Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced01": Sprite("Structure/Floors/FloorReinforced01", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced01Angle": Sprite("Structure/Floors/FloorReinforced01Angle", camera_du="TD", is_rotatable=True, with_outline=False),
    "FloorReinforced01Lit": Sprite("Structure/Floors/FloorReinforced01Lit", camera_du="TD", is_rotatable=False, with_outline=False),
    "FloorReinforced02": Sprite("Structure/Floors/FloorReinforced02", camera_du="TD", is_rotatable=True, with_outline=False),
    "FloorReinforced02Angle": Sprite("Structure/Floors/FloorReinforced02Angle", camera_du="TD", is_rotatable=True, with_outline=False),
    "FloorReinforced02Lit": Sprite("Structure/Floors/FloorReinforced02Lit", camera_du="TD", is_rotatable=False, with_outline=False),

    # Walls
    "Wall01": Sprite("Structure/Walls/Wall01", 4, 4, camera_du="TD", is_rotatable=False, lights="Wall Lights", line_sets=["Wall"]),
    "Wall02": Sprite("Structure/Walls/Wall02", 4, 4, camera_du="TD", is_rotatable=False, lights="Wall Lights", line_sets=["Wall"]),
    "WallReinforced01": Sprite("Structure/Walls/WallReinforced01", 4, 4, camera_du="TD", is_rotatable=False, lights="Wall Lights", line_sets=["Wall"]),

    # Vents
    "Vent01": Sprite("Structure/Walls/Vent01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),
    "Vent02": Sprite("Structure/Walls/Vent02", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], subset=["_R", "_D"]),

    # Doors
    "Door01": Sprite("Structure/Doors/Door01", 1, 1, camera_du="TD", lights="Wall Lights", is_rotatable=False, line_sets=["Wall"], 
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
    # Underscore in the end will be removed, so this will become a preview version
    "Human.[F]Hat01_": Sprite("Beings/Hats/Human.[F]Hat01_", is_rotatable=False),
    "Human.[F]Hat01": Sprite("Beings/Hats/Human.[F]Hat01"),
    "Human.[F]Hat01_H": Sprite("Beings/Hats/Human.[F]Hat01_H"),
    "Human.[F]Clothing01_": Sprite("Beings/Clothing/Human.[F]Clothing01_", is_rotatable=False),
    "Human.[F]Clothing01": Sprite("Beings/Clothing/Human.[F]Clothing01"),
    "Human.[F]Clothing01_H": Sprite("Beings/Clothing/Human.[F]Clothing01_H"),

    "Human.[M]Body01": Sprite("Beings/Bodies/Human.[M]Body01"),
    "Human.[M]Body01_H": Sprite("Beings/Bodies/Human.[M]Body01_H"),
    "Human.[M]Head01": Sprite("Beings/Heads/Human.[M]Head01"),
    "Human.[M]Head01_H": Sprite("Beings/Heads/Human.[M]Head01_H"),
    "Human.[M]Hair01": Sprite("Beings/Hair/Human.[M]Hair01"),
    "Human.[M]Hair01_H": Sprite("Beings/Hair/Human.[M]Hair01_H"),
    "Human.[M]Hat01_": Sprite("Beings/Hats/Human.[M]Hat01_", is_rotatable=False),
    "Human.[M]Hat01": Sprite("Beings/Hats/Human.[M]Hat01"),
    "Human.[M]Hat01_H": Sprite("Beings/Hats/Human.[M]Hat01_H"),
    "Human.[M]Clothing01_": Sprite("Beings/Clothing/Human.[M]Clothing01_", is_rotatable=False),
    "Human.[M]Clothing01": Sprite("Beings/Clothing/Human.[M]Clothing01"),
    "Human.[M]Clothing01_H": Sprite("Beings/Clothing/Human.[M]Clothing01_H"),

    "CleaningBot.[N]Body01": Sprite("Beings/Bodies/CleaningBot.[N]Body01"),

    "Drone.[N]Body01": Sprite("Beings/Bodies/Drone.[N]Body01"),
    "Drone.[N]Shadow01": Sprite("Beings/Shadows/Drone.[N]Shadow01", with_outline=False),
    "Robot.[N]Body01": Sprite("Beings/Bodies/Robot.[N]Body01"),
    "Robot.[N]Head01": Sprite("Beings/Heads/Robot.[N]Head01"),
    
    "Crawler.[N]Body01": Sprite("Beings/Bodies/Crawler.[N]Body01"),
    "Crawler.[N]Body01_1": Sprite("Beings/Bodies/Crawler.[N]Body01_1"),

    # Attached Crawler Hat
    "Human.[N]Crawler01": Sprite("Beings/Hats/Human.[N]Crawler01"),
    "Human.[N]Crawler01_": Sprite("Beings/Hats/Human.[N]Crawler01_", is_rotatable=False),
    "Human.[N]Crawler01_H": Sprite("Beings/Hats/Human.[N]Crawler01_H"),

    # Plants
    "Wheat": Sprite("Obj/Plants/Wheat", is_rotatable=False, 
        subset=["_", "_Growing1", "_Growing2", "_Seed", "_Harvested"]),

    # Asteroids
    "Asteroid01": Sprite("Obj/Asteroids/Asteroid01", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Asteroid02": Sprite("Obj/Asteroids/Asteroid02", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Asteroid03": Sprite("Obj/Asteroids/Asteroid03", is_rotatable=False, line_sets=["ObjectBorder"]),

    # Bullet
    "EnergyBullet": Sprite("Obj/Misc/EnergyBullet", is_rotatable=False),
    "WaterBullet": Sprite("Obj/Misc/WaterBullet", is_rotatable=False, with_outline=False),

    # Eggs
    "Egg01": Sprite("Obj/Eggs/Egg01", is_rotatable=False),

    # Misc
    "StorageCapsule": Sprite("Obj/Misc/StorageCapsule", is_rotatable=False),
    "StorageCapsule_Open": Sprite("Obj/Misc/StorageCapsule_Open", is_rotatable=False),

    # Meals
    "SoyBurger": Sprite("Obj/Meals/SoyBurger", is_rotatable=False),
    "SurvivalMeal": Sprite("Obj/Meals/SurvivalMeal", is_rotatable=False),

    # Materials
    "Steel": Sprite("Obj/Materials/Steel", is_rotatable=False),
    "CopperPlate": Sprite("Obj/Materials/CopperPlate", is_rotatable=False),
    "Glass": Sprite("Obj/Materials/Glass", is_rotatable=False),
    "Rock": Sprite("Obj/Materials/Rock", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Protein": Sprite("Obj/Materials/Protein", is_rotatable=False),
    "PlantFiber": Sprite("Obj/Materials/PlantFiber", is_rotatable=False),
    "Coal": Sprite("Obj/Materials/Coal", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Carbon": Sprite("Obj/Materials/Carbon", is_rotatable=False),
    "CarbonFiber": Sprite("Obj/Materials/CarbonFiber", is_rotatable=False),
    "Copper": Sprite("Obj/Materials/Copper", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Iron": Sprite("Obj/Materials/Iron", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Silicon": Sprite("Obj/Materials/Silicon", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Lithium": Sprite("Obj/Materials/Lithium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Soil": Sprite("Obj/Materials/Soil", is_rotatable=False),
    "Titanium": Sprite("Obj/Materials/Titanium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Uranium": Sprite("Obj/Materials/Uranium", is_rotatable=False, line_sets=["ObjectBorder"]),
    "Wood": Sprite("Obj/Materials/Wood", is_rotatable=False),
    "Biowaste": Sprite("Obj/Materials/Biowaste", is_rotatable=False),
    "Water": Sprite("Obj/Materials/Water", is_rotatable=False),
    "Biomass": Sprite("Obj/Materials/Biomass", is_rotatable=False),
}