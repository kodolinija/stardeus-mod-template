# Stardeus Code Modding

Most of Stardeus components are self-registering using Unity's `[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.  SubsystemRegistration)]`. This means you won't need hacks like Harmony for things like creating new components, systems, AI actions, etc. There may be some limitations to what can be achieved through code, but you can always visit Stardeus Discord's #stardeus-modding channel and get some help. It is likely that what you need can be exposed easily.

We are using strings instead of enums in most situations where enum would be a reasonable choice, because strings give more flexibility to create new types of parameters that could be hard to introduce as a new enum value, especially if multiple mods would want to touch the same enum.

Best way to figure how to create the code is to decompile Stardeus DLL files and analyze them. 

Note that everything that uses `RuntimeInitializeOnLoadMethod` will be `sealed` to prevent attempts of extending classes with custom implementations. This is intended, inheritence is bad design in general, composition should be preferred. Also, `RuntimeInitializeOnLoadMethod` will not work with inheritence. Easiest way to modify some component is to create a new component that interacts with existing component. For example, see `Bullet` and `EnergyBullet` - these are separate components and `EnergyBullet` extends the functionality of `Bullet`.