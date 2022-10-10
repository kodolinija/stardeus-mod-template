# Stardeus Mod Template

This is a mod template for [Stardeus](https://store.steampowered.com/app/1380910/Stardeus/).

It should be the definitive example for anything moddable in this game, and will be
extended over time to contain at least one example of any moddable aspect.

See subfolders for more readme files on how to create Artwork, and Definitions.

Best place to ask questions about modding Stardeus is on [Stardeus Discord](https://discord.com/invite/89amEwP), #stardeus-modding channel.


## How to compile a mod DLL with your code

If you're on Linux, please refer to [Linux Build Instruction instead.](Linux.md)

1. Make a copy of "stardeus-mod-template" folder, rename it to something else.
2. Edit `ModInfo.json` and change the `Id`, `Name`, `Description` and other fields.
3. Remove the `SteamWorkshopItemId` file.
4. Edit `.vscode/mod.csproj` line 14 to set the name of the DLL file your mod will produce.
5. Edit `.vscode/mod.csproj` line 31 to work with your system.
6. Edit `.vscode/launch.json` line 15 to work with your system.
7. Move the folder to the `Mods` directory near your `Saves`. You can open the folder from Stardeus itself, through `Main Menu > Mods > About Mods > Open User Mods Directory`.
8. Open the folder with `Visual Studio Code`.
9. Press `F5` to compile the DLL file and run Stardeus.
10. Note that Steam will automatically restart Stardeus executable to run it through appropriate Steam facilities, so if you will want to debug the project, you will have to attach the debugger after the executable is restarted (it will have a different PID, etc).
11. Once Stardeus starts, you should see your mod listed and enabled in `Main Menu > Mods`.

You may need to examine what's in .vscode directory and modify / create new
scripts there accordingly to what would work on your OS.

Video tutorial: https://www.youtube.com/watch?v=oUttUN2Khp8

More tutorials will follow!

Happy modding!

## How to upload your mod to Steam Workshop

Before uploading, please read the `STARDEUS MOD CREATOR AGREEMENT` part in Stardeus `EULA`:
https://stardeusgame.com/eula/ - you must agree to these terms if are publishing your mod on Steam Workshop, or anywhere else.

When your mod is ready, you can share it with the world by uploading it to the Steam Workshop.

1. Edit the `ModTemplate.json` and change the `SteamWorkshop` from `false` to `true`.
2. Make sure you have changed the `ModCover.jpg` and removed any unnecessary files that were in the template.
3. Restart Stardeus and open `Main Menu > Mods > Your Mod`.
4. Click the `Upload to Steam Workshop` button.
5. A browser page should open, where you can finish adding descriptions, etc.
