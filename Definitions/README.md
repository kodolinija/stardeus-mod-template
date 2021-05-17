# Stardeus Mod Definitions

Definitions are a powerful tool that glues the game pieces together. Anything buildable, any object or being has to have a definition. Through definitions, you can introduce new Research Tree branches, modify any existing device, create new devices, create new being species, tune a lot of exposed game balancing parameters, create procedural generation templates, create new Skills, Needs, Materials, Twitch Roles - you name it.

Best way to figure out how to create your own definitions is to explore the Core mod Definitions folder.

A definition is plain JSON file that defines a set of components and their properties. There is limited inheritence support, so you can create a definition that is based on another object, and only change what has to be overridden. For example, see Core mod's Definitions: `Structure/Walls/BaseWall.json`, `Structure/Walls/Wall01.json` that inherits from BaseWall, and `Structure/Walls/WallReinforced01.json` that inherits from Wall01.

A note about `TileTransform` and `TileGraphics` components.  `TileTransform`'s `Width` and `Height` properties are defining the base size, While `TileGraphics` `HasHeight` property tells if sprite has one extra row on top, that is rendered in the "above" layer. For example, `ShipComputer`'s tile transform is 2x2, it's graphics `HasHeight` is `true`, and it's sprite size in `sprite_defs.py` (see README of `Artwork` directory) is 2x3.