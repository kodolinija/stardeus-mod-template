# Stardeus Mod Template

This is a mod template for [Stardeus](https://store.steampowered.com/app/1380910/Stardeus/).

It should be the definitive example for anything moddable in this game, and will be
extended over time to contain at least one example of any moddable aspect.

See subfolders for more readme files on how to create Artwork, and Definitions.

Best place to ask questions about modding Stardeus is on [Stardeus Discord](https://discord.com/invite/89amEwP), #stardeus-modding channel.

## Empty Mod

If you want to create a simple mod, this empty mod project may be a better starting point:
https://github.com/kodolinija/stardeus-mod-empty

## GitHub Repository

IMPORTANT! If you downloaded this mod from [Stardeus Steam Workshop](https://steamcommunity.com/app/1380910/workshop/),
please check the official GitHub Repository instead. It will most likely have a newer, more up to date version of the mod template.

The repository is here: https://github.com/kodolinija/stardeus-mod-template

## Stardeus Modding Series on YouTube

Here's a playlist of the official Stardeus Modding series on YouTube:
https://www.youtube.com/playlist?list=PLvm1mLYInibc8n0Q5_caRql5nEUiBwvTC

Subscribe to https://www.youtube.com/@KodoLinija and use the bell icon to get notified about new videos.


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
10. Once Stardeus starts, you should see your mod listed and enabled in `Main Menu > Mods`.

You may need to examine what's in .vscode directory and modify / create new
scripts there accordingly to what would work on your OS.

## How to upload your mod to Steam Workshop

Before uploading, please read the `STARDEUS MOD CREATOR AGREEMENT` part in Stardeus `EULA`:
https://stardeusgame.com/eula/ - you must agree to these terms if are publishing your mod on Steam Workshop, or anywhere else.

When your mod is ready, you can share it with the world by uploading it to the Steam Workshop.

### Initial Upload

0. Make sure you have removed any unnecessary files and folders from the mod, including, .vscode, .git, Artwork, Blender files, any unused files from the mod template, etc
1. Make sure your mod is not next to `Core` mod, but instead is in the user mod directory. You can open that directory via `Main Menu` > `Mods` > `About Mods`
2. Remove the `SteamWorkshopItemId` file.
1. Edit the `ModInfo.json` and change the `SteamWorkshop` from `false` to `true`.
2. Make sure you have changed the `ModCover.jpg` and removed any unnecessary files that were in the template.
3. Run Stardeus through Steam and open `Main Menu > Mods > Your Mod`.
4. Press the `Upload to Steam Workshop` button.
5. A confirmation popup will appear shortly.

### Troubleshooting

- If upload fails with `k_EResultLimitExceeded`, it's possible that the ModCover.jpg is too large. Try reducing the cover size to < 150Kb.

### Updating Your Mod

0. Do not delete or change the `SteamWorkshopItemId` file, it has your mod steam id
1. Make changes to the mod, rebuild the DLL if necessary
2. Run Stardeus through Steam
3. Go to `Main Menu > Mods > Your Mod` and press the `Upload to Steam Workshop` button
4. A confirmation popup will appear shortly.

You can only update the mod if your Steam user is the creator and if the mod is inside the User mods folder, not downloaded through Steam Workshop.
