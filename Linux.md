## Linux Prerequisites

| Linux Distro | Install Instruction |
| --- | --- |
| Arch Linux | pacman -S dotnet-sdk dotnet-host dotnet-runtime |
| Red Hat | yum install dotnet dotnet-host dotnet-sdk-6.0 |
| Debian | [Please refer to this documentation](https://learn.microsoft.com/en-us/dotnet/core/install/linux-debian) |
| Fedora | [Please refer to this documentation](https://learn.microsoft.com/en-us/dotnet/core/install/linux-fedora) |
| OpenSUSE | [Please refer to this documentation](https://learn.microsoft.com/en-us/dotnet/core/install/linux-opensuse) |
| SLES | [Please refer to this documentation](https://learn.microsoft.com/en-us/dotnet/core/install/linux-sles) |
| Ubuntu | apt-get install dotnet6 dotnet-runtime-6.0 |
| CentOS | [Please refer to this documentation](https://learn.microsoft.com/en-us/dotnet/core/install/linux-centos) |

## Visual Studio Code is Recommended
[You can install Visual Studio Code from this instruction](https://code.visualstudio.com/docs/setup/linux)

## Ensure you have correct paths

Generally if you have installed Steam on your Linux Distro, you may have a ".steam" directory symbolic link in your home folder IE `/home/user/.steam`.

Depending on which version of the game you have, you may either have the actual Stardeus copy or the Stardeus Demo, so you will have to make a distinction here.

Your game folder may be in the following path, if not, please let us know which Linux distro you're on and where can it actually be found:

`/home/{Your Username}/.steam/steam/steamapps/common/Stardeus/`

Also for where you're going to put your mod folder at, it'll likely be under this folder:

`/home/{Your Username}/.config/unity3d/Kodo Linija/Stardeus/Mods/`

## How to compile a mod DLL with your code

1. `git clone https://github.com/kodolinija/stardeus-mod-template.git {Enter name of your mod with spaces replaced with underscores}` into your project folder.
2. Edit `ModInfo.json` and change the `Id`, `Name`, `Description` and other fields.
3. Remove the `SteamWorkshopItemId` file.
4. Edit `.vscode/mod.csproj` line 14 to set the name of the DLL file your mod will produce.
5. Edit `.vscode/mod.csproj` line 31 to work with your system.
6. Edit `.vscode/mod.csproj` to change the following lines:

`<Reference Include="/home/{Your Username}/.local/share/Steam/steamapps/common/Stardeus/Stardeus_Data/Managed/Game.dll">`

and

`<Reference Include="/home/{Your Username}/.local/share/Steam/steamapps/common/Stardeus/Stardeus_Data/Managed/*.dll">`

7. Open the folder with your favorite editor.
8. When done writing your mod program, brings up a terminal with mod folder set as current directory and run `dotnet build .vscode`, or pick `Tasks: Run Build Task` from Command Palette in Visual Studio Code editor.

Warning: If you attempt to modify `launch.json` to have it run Stardeus executable after pressing `F5` to compile the DLL file and run Stardeus, it may crash your window manager depending on the circumstances with Steam Runtime, it is a containerization for game applications. So it is advised to instead run Stardeus directly from Steam application. If debugging is needed, you can attach the debugger to the running Stardeus executable.

9. Make a symbolic link of your mod folder in Stardeus mod folder which can be done as followed:
`ln -sv "/home/{Your Username}/{Your Mod Folder Name}" "/home/{Your Username}/.config/unity3d/Kodo Linija/Stardeus/Mods/{Your Mod Folder Name}"`

10. Now run Stardeus from Steam.

11. Once Stardeus starts, you should see your mod listed and enabled in `Main Menu > Mods`.

## How to upload your mod to Steam Workshop

The instruction is the same in [README.md](README.md#how-to-upload-your-mod-to-steam-workshop)
