# Stardeus Modding Concepts

Most of Stardeus components are self-registering using the game's own `[SelfInit]` attribute (see `Game.Utils.SelfInitAttribute`). Mod DLLs are loaded before any `[SelfInit]` stage runs, so it works the same way inside a mod as it does in the core game — this template uses it throughout. Unity's `[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]` is also a valid, simpler entry point if you don't need stage/order control. Either way, you won't need hacks like Harmony for things like creating new components, systems, AI actions, etc. There may be some limitations to what can be achieved through code, but you can always visit Stardeus Discord's #stardeus-modding channel and get some help. It is likely that what you need can be exposed easily.

We are using strings instead of enums in most situations where enum would be a reasonable choice, because strings give more flexibility to create new types of parameters that could be hard to introduce as a new enum value, especially if multiple mods would want to touch the same enum.

Best way to figure how to create the code is to decompile Stardeus DLL files and analyze them. There are some free decompilers available: JetBrains DotPeek, dnSpy.

Note that everything that uses `RuntimeInitializeOnLoadMethod` will be `sealed` to prevent attempts of extending classes with custom implementations. This is intended, inheritence is bad design in general, composition should be preferred. Also, `RuntimeInitializeOnLoadMethod` will not work with inheritence. Easiest way to modify some component is to create a new component that interacts with existing component. For example, see `Bullet` and `EnergyBullet` - these are separate components and `EnergyBullet` extends the functionality of `Bullet`.

## What's in this template

- `ExampleModComp.cs` — a self-registering `BaseComponent`, attached to the `ModTest`
  device (`Definitions/Objects/Devices/ModTest.json`). Shows config reading,
  save/load, the electricity hookup, and AI goal callbacks.
- `ExampleTab.cs` — the entity-panel UI for `ExampleModComp`, using the
  `BaseEntityTab` + `UISpawn` widget system (the current UI system; the older
  UDB/`IUIDataProvider` system has been removed from the game).
- `ExampleModSys.cs` — a minimal self-registering `GameSystem` with save/load,
  showing signal listeners and a tick handler. Has no UI of its own; see
  `ExampleTab.cs` for the UI example.

**Note:** mod DLLs are loaded before any `[SelfInit]` stage runs, so `[SelfInit]`
works the same inside a mod as it does in the core game. `ExampleTab.cs` registers
with plain `[SelfInit]`, exactly like the in-game `HeaterTab.cs` and the
`ExampleModComp.cs`/`ExampleModSys.cs` registrations elsewhere in this mod. See
`Docs/Architecture/SelfInit.md` (the "Mods" section) in the main project for the
underlying mechanism and a couple of minor caveats (assembly-name blacklist,
referencing the game's `Game.Utils` assembly).

## Debugging in Visual Studio with breakpoints

*WARNING: this guide is possibly outdated*

For simple C# mods you can always use `KL.Utils.D.Err("LOG SOMETHING")` to debug your mod with logging statements, but in cases when you need more complex debugging, if you are working on a big mod, etc, here are the steps you can take to use Visual Studio and add breakpoints in your mods, also step through core game code.

1. Acquire development build from spajus. Note: spajus will not give the development build to strangers. There may be a possiblity to do this without the development build, but I couldn't get this to work. [Read this](https://ludeon.com/forums/index.php?topic=51589.0) if you want to try it, process should be similar to RimWorld.
2. Put your mod into `Stardeus_Data/StreamingAssets/Mods/YourMod`. Copy and edit Template if needed.
3. Make sure contents of `Stardeus_Data/boot.config` are as follows:
   ```
   wait-for-managed-debugger=1
   player-connection-debug=1
   ```
   Do not append this to existing file, replace all contents!
   If everything is done correctly, after you run Stardeus.exe you should see a dialog saying "You can attach a managed debugger now if you want".
4. Run Visual Studio Installer, click Modify on your VS (mine was 2019) and make sure that in Workloads tab "Game Development with Unity" is included (the optional Editor 2018 is not needed)
5. Launch Visual Studio 2019 (or your version) and choose Open Project or Solution
6. Select `Stardeus_Data/StreamingAssets/Mods/YourMod/.vscode/mod.csproj`
7. Go to Project > mod Properties
8. Go to Build > Advanced
9. In Output section set Debugging Information to Portable. Save and close the properties.
10. Do Build > Build Solution to produce your mod's DLL file and PDB. They should appear in `Stardeus_Data/StreamingAssets/Mods/YourMod/Libraries/YourMod.{dll,pdb}`
11. Run `Stardeus.exe` outside of Visual Studio, do not click OK on the "You can now attach a managed debugger" popup.
12. Switch to Visual Studio and select Debug > Attach Unity Debugger
13. Select the instance of type Player and click OK
14. Switch back to Stardeus "You can now attached debugger" popup and click OK to attach the debugger
15. Wait for game to boot completely and load everything, until you see "press any key" or the main menu
16. Switch back to Visual Studio, open Debug > Windows > Modules and try to find `YourMod.dll`. If it is in the list, you can debug it.
17. Right click Game.dll in the Modules list and select Load Symbols. After this, modules should say that symbols are loaded for Game, KLUnityUtils, etc, and YourMod too.
18. Open any .cs file in YourMod and add breakpoints. Make sure when you hover the breakpoint you just added, there is no tooltip saying "Breakpoint will not currently be hit. No symbols are loaded".
19. Now the breakpoint should get triggered.