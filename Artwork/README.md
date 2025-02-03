# Stardeus Artwork Template

All Stardeus in-game art (with exception for icons) is exported from
3D models using Blender. The file that is provided here (StardeusMod.blend)
contains some objects from the game, so you can explore it and see how everything
is done.

Warning! Do not activate collections manually. Do not touch or modify lights or
cameras. Do not change any scene settings, freestyle outlines, etc by hand, ever!
Everything is done through automation and scripts. Changing something manually
will most likely make things look not coherent with the rest of game art!

# Artwork Workflow

1. Add a new sprite definition to `Scripts/sprite_defs.py`. Easiest way is to just
   copy an existing definition from a sprite that is of the same size and properties
   that you want to create, and just change it's name. For example:
   `"ModTest": Sprite("Objects/Devices/ModTest", 2, 2, 1, 3),`
   Here 2, 2 is 2x2 tiles when object is facing down and up, and 1, 3 is 1x3
   tiles when object is facing left and right. Note that in game pump is 1x2 tiles,
   but it has "height", meaning 1x2 is base size, but actual sprite height is +1.
2. Open StardeusMod.blend with blender 3.6 or newer. Then create a collection
   using exactly same hierarchy and name (`Objects > Devices > ModTest`). You
   will have to put your model in this collection. But before your do anything
   else, move to step 3 now.
3. Activate "Scripting" tab and run the active script (stardeus_menu). It will load
   all sprite definitions and export scripts. This step is absolutely necessary,
   otherwise you will be going through hell trying to enable the right collections
   and manually exporting all 4 rotations of a sprite, for all it's versions.
   If you modify `sprite_defs.py`, you can do `Render > Stardeus > Reload Scripts`
   to apply changes (regular Blender "reload scripts" is not enough!).
4. Activate "Layout" tab, move mouse over 3D viewport, press space to open the
   Quick Search menu, then start typing "activate modtest" until you will see
   `Render > Stardeus > Activate > ModTest` option. Select it and magic will
   happen - the script will select and activate the right collection, right camera,
   enable lights, etc. If you don't see `Render > Stardeus > ...` options, double
   check if you have successfully completed step 2.
5. Work on your model. Refer to preview in top-left, or press Numpad 0 to show
   camera preview. Your object should fit, and it should be placed on zero
   coordinate, with 0 on Z axis being the ground level. Press F12 to quick-render
   a preview in bottom-left corner.
6. To create a small shadow below your object, you will have to create a "shadow
   catcher" by checking "shadow catcher" in object properties, then editing that
   object, selecting all faces and doing "Mark Freestyle Face" from Quick Search.
   Also applying "ShadowCatcher" material on this object. Or just copy a shadow
   catcher from another object. Put the shadow catcher slightly below and adjust
   the distance + use F12 to find a nice result.
7. When you are happy with your model, hit spacebar to access Quick Search and
   type "export modtest" and hit enter. Blender will become unresponsive for the
   duration of the export, but you can open `Graphics/Objects/Devices` folder
   and see how exported PNG files will start appearing there.
8. When you have your PNG files exported, you can proceed to `Definitions` folder
   readme, to see how to define a new device and link the new graphics to it.

There will be video tutorials about this! Subscribe to
[Kodo Linija on YouTube](https://www.youtube.com/channel/UCYRe2i1dSAXCr6a6TYsQawQ)
to get notified.