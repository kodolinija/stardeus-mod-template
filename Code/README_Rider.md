# Stardeus Modding Concepts

Most of Stardeus components are self-registering using Unity's `[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]`. This means you won't need hacks like Harmony for things like creating new components, systems, AI actions, etc. There may be some limitations to what can be achieved through code, but you can always visit Stardeus Discord's #stardeus-modding channel and get some help. It is likely that what you need can be exposed easily.

We are using strings instead of enums in most situations where enum would be a reasonable choice, because strings give more flexibility to create new types of parameters that could be hard to introduce as a new enum value, especially if multiple mods would want to touch the same enum.

Best way to figure how to create the code is to decompile Stardeus DLL files and analyze them. There are some free decompilers available: JetBrains DotPeek, dnSpy.

Note that everything that uses `RuntimeInitializeOnLoadMethod` will be `sealed` to prevent attempts of extending classes with custom implementations. This is intended, inheritence is bad design in general, composition should be preferred. Also, `RuntimeInitializeOnLoadMethod` will not work with inheritence. Easiest way to modify some component is to create a new component that interacts with existing component. For example, see `Bullet` and `EnergyBullet` - these are separate components and `EnergyBullet` extends the functionality of `Bullet`.

## Debugging in Rider with breakpoints

For simple C# mods you can always use `KL.Utils.D.Err("LOG SOMETHING")` to debug your mod with logging statements, but in cases when you need more complex debugging, if you are working on a big mod, etc, here are the steps you can take to use Visual Studio and add breakpoints in your mods, also step through core game code.

1. Download this template and copy it into `Stardeus_Data/StreamingAssets/Mods/` and rename it to whatever name you'd like.
2. Go inside of your mod's folder and look for `modinfo.json`. Change the field "Id" to something unique. For example `"Spajus.MyMod"`.
3. You may need to setup manual references to the game's source code, see step 6 on how to access the game files. Look for a Managed folder, which should be full of .dll files. Import them, and make sure Copy Local is not ticked in their options.
4. Ensure your project builds. You can create a new project using Rider and import all of the .cs source files.
5. Download [DoorStop](https://github.com/NeighTools/UnityDoorstop), which allows setting up a debugger.
6. Extract the content of the 64bit version in Stardeus' folder. If you've bought the game through Steam, you can right click on Stardeus => Manage => Browse Local Files.
7. If you're on Windows, open `doorstop_config.ini` with any text editor. On Linux, open `run.sh`.
8. On Linux, look for `executable_name` and set it to "Stardeus"
9. Set `debug_enabled` to `true` (`1` on Linux)
10. Note down the `debug_adress`, you will need it later.
11. Open the game normally. On Linux, open the game through the shell script `sh run.sh`
12. Go into Rider, go click on the 4 horizontal bars in the top left => `Run` => `Edit Configurations`
13. Create a new `Mono Remote` configuration by clicking on the +.
14. Set your `Host` to `127.0.0.1` and the `Port` to what you wrote down earlier at step 10.
15. Press OK. You should now have a new button next to the run button at the top of the interface.
16. Press it, and the debugger should attach.
17. You should be able to set breakpoints in your project. You can also set breakpoints in the decompiled code Rider provides when inspecting game classes.
