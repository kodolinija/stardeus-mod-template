import bpy
import sys
import os
import threading
import time

dir = os.path.dirname(bpy.data.filepath)

if not dir in sys.path:
    sys.path.append(dir + "/scripts")

import op_export
import sprite_defs

# this next part forces a reload in case you edit the source after you first start the blender session
import imp
imp.reload(op_export)
imp.reload(sprite_defs)

# this is optional and allows you to call the functions without specifying the package name
from op_export import *

class StardeusMenu(bpy.types.Menu):
    bl_label = "Stardeus"
    bl_idname = "OBJECT_MT_stardeus"

    def draw(self, context):
        layout = self.layout
        active_col_name = bpy.context.view_layer.active_layer_collection.name
        layout.operator(StardeusReloadScripts.bl_idname)
        layout.separator()
        layout.operator(StardeusActivateActiveOperator.bl_idname, text=f"Activate {active_col_name}")
        layout.menu(StardeusActivateSubmenu.bl_idname)
        layout.separator()
        layout.operator(StardeusExportActiveOperator.bl_idname, text=f"Export {active_col_name}")
        layout.menu(StardeusRenderSubmenu.bl_idname)
        layout.separator()
        layout.operator(StardeusExportAllOperator.bl_idname)

class StardeusRenderSubmenu(bpy.types.Menu):
    bl_label = "Export"
    bl_idname = "OBJECT_MT_stardeus_render_single"

    def draw(self, context):
        layout = self.layout
        for item in sorted(sprite_defs.SPRITES):
            layout.operator(StardeusExportSelectedOperator.bl_idname, text=item).selection = item

class StardeusActivateSubmenu(bpy.types.Menu):
    bl_label = "Activate"
    bl_idname = "OBJECT_MT_stardeus_activate"

    def draw(self, context):
        layout = self.layout
        for item in sorted(sprite_defs.SPRITES):
            layout.operator(StardeusActivateModelOperator.bl_idname, text=item).selection = item

class StardeusReloadScripts(bpy.types.Operator):
    bl_idname = "object.stardeusreloadscripts"
    bl_label = "Reload Scripts"
    bl_description = "Reloads Stardeus scripts"

    def execute(self, context):
        print("starting reload")
        threading.Timer(0, reload_scripts).start()
        return {'FINISHED'}

def reload_scripts():
    print("running reload")
    scr = "scripts/stardeus_menu.py"
    load_script(scr)
    time.sleep(0.2)
    print("loading script")
    bpy.ops.script.reload()
    time.sleep(3)
    print("reloading scripts")
    load_script(scr)
    print("loading script again")


def load_script(filename):
    filepath = os.path.join(os.path.dirname(bpy.data.filepath), filename)
    global_namespace = {"__file__": filepath, "__name__": "__main__"}
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), global_namespace)

# Below is the setup that links shit into blender

def draw_item(self, context):
    layout = self.layout
    layout.separator()
    layout.menu(StardeusMenu.bl_idname, text=StardeusMenu.bl_label)

def draw_collection_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(StardeusExportSelectedOperator.bl_idname, text="Export to Stardeus")

def register():
    bpy.utils.register_class(StardeusExportSelectedOperator)
    bpy.utils.register_class(StardeusReloadScripts)
    bpy.utils.register_class(StardeusActivateModelOperator)
    bpy.utils.register_class(StardeusExportActiveOperator)
    bpy.utils.register_class(StardeusActivateActiveOperator)
    bpy.utils.register_class(StardeusExportAllOperator)
    bpy.utils.register_class(StardeusRenderSubmenu)
    bpy.utils.register_class(StardeusActivateSubmenu)
    bpy.utils.register_class(StardeusMenu)
    bpy.types.TOPBAR_MT_render.append(draw_item)
    bpy.types.OUTLINER_MT_collection.append(draw_item)

def reregister():
    bpy.utils.register_class(StardeusExportSelectedOperator)
    bpy.utils.register_class(StardeusReloadScripts)
    bpy.utils.register_class(StardeusExportActiveOperator)
    bpy.utils.register_class(StardeusActivateModelOperator)
    bpy.utils.register_class(StardeusActivateActiveOperator)
    bpy.utils.register_class(StardeusExportAllOperator)
    bpy.utils.register_class(StardeusRenderSubmenu)
    bpy.utils.register_class(StardeusActivateSubmenu)
    bpy.utils.register_class(StardeusMenu)


def unregister():
    bpy.utils.unregister_class(StardeusMenu)
    bpy.utils.unregister_class(StardeusReloadScripts)
    bpy.utils.unregister_class(StardeusRenderSubmenu)
    bpy.utils.unregister_class(StardeusActivateSubmenu)
    bpy.utils.unregister_class(StardeusExportSelectedOperator)
    bpy.utils.unregister_class(StardeusActivateModelOperator)
    bpy.utils.unregister_class(StardeusActivateActiveOperator)
    bpy.utils.unregister_class(StardeusExportActiveOperator)
    bpy.utils.unregister_class(StardeusExportAllOperator)

if __name__ == "__main__":
    if hasattr(bpy.types, "StardeusMenu"):
        unregister()
        reregister()
    else:
        register()

    # The menu can also be called from scripts
    # bpy.ops.wm.call_menu(name=StardeusMenu.bl_idname)

