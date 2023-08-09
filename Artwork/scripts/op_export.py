import bpy
from sprite_defs import *
from mathutils import Vector
from math import radians
import os
from time import sleep
from threading import Timer
import copy

TILE_RES = 256

def output_path(path):
    blender_dir = os.path.dirname(bpy.data.filepath)
    artwork_dir = os.path.dirname(blender_dir)
    mod_dir = os.path.dirname(artwork_dir)
    graphics_dir = os.path.join(mod_dir, "Graphics/")
    if path.endswith("_"):
        path = path[:-1]
    return os.path.join(graphics_dir, path.replace('.', '/'))

class StardeusExportAllOperator(bpy.types.Operator):
    bl_idname = "object.stardeusexportall"
    bl_label = "Export All"
    bl_description = "Exports all objects as sprites"

    def execute(self, context):
        exit_edit_mode()
        for col_name in SPRITES:
            col = SPRITES[col_name]
            activate_model(self, col)
            export_model(self, col)
        return {'FINISHED'}

class StardeusExportActiveOperator(bpy.types.Operator):
    bl_idname = "object.stardeusexportactive"
    bl_label = "Export Active"
    bl_description = "Exports active collection as sprites"

    def execute(self, context):
        exit_edit_mode()
        col_name = bpy.context.view_layer.active_layer_collection.name
        if col_name in SPRITES:
            col = SPRITES[col_name]
            activate_model(self, col)
            export_model(self, col)
        else:
            self.report({'ERROR'}, "Not found in SPRITES: " + col_name)

        return {'FINISHED'}

class StardeusActivateActiveOperator(bpy.types.Operator):
    bl_idname = "object.stardeusactivateactive"
    bl_label = "Activate Active"
    bl_description = "Activates selected collection"

    def execute(self, context):
        exit_edit_mode()
        col_name = bpy.context.view_layer.active_layer_collection.name
        if col_name in SPRITES:
            col = SPRITES[col_name]
            activate_model(self, col)
        else:
            self.report({'ERROR'}, "Not found in SPRITES: " + col_name)
        return {'FINISHED'}

class StardeusExportSelectedOperator(bpy.types.Operator):
    bl_idname = "object.stardeusexportselected"
    bl_label = "Export Selected"
    bl_description = "Exports selected object as sprites"

    selection: bpy.props.StringProperty()

    def execute(self, context):
        exit_edit_mode()
        col = SPRITES[self.selection]
        activate_model(self, col)
        export_model(self, col)
        return {'FINISHED'}

class StardeusActivateModelOperator(bpy.types.Operator):
    bl_idname = "object.stardeusactivatemodel"
    bl_label = "Activate Model"
    bl_description = "Activates selected object"

    selection: bpy.props.StringProperty()

    def execute(self, context):
        col = SPRITES[self.selection]
        activate_model(self, col, False)
        return {'FINISHED'}

def exit_edit_mode():
    if bpy.context.object is not None:
        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")

def activate_model(operator, sprite, select_contents=True):
    report(operator, "Activating: " + sprite.path)
    collection = sprite.path
    for obj in bpy.context.selected_objects:
        obj.select_set(False)

    names = collection.split("/")
    final_name = names[-1]
    names.append(sprite.lights)

    # Enable the right collections in outliner
    vl = bpy.context.view_layer
    vl.use_freestyle = sprite.with_outline
    for ls in vl.freestyle_settings.linesets:
        ls.show_render = ls.name in sprite.line_sets

    # print("Enable in outliner: " + names)
    enable_in_outliner(names, vl.layer_collection.children)

    # Toggle the right collections for rendering
    for col in bpy.data.collections:
        if select_contents:
            sel_children = col.name == final_name and sprite.subset == []
        else:
            sel_children = False
        toggle_collection(col, col.name in names, sel_children)

    activate_camera(sprite, 'd')

def activate_camera(sprite, direction):
    scene = bpy.context.scene

    if direction == 'd' or direction == 'u':
        width = sprite.width_du
        height = sprite.height_du
        camera_name = sprite.camera_du
        cam = f'Camera{camera_name}{width}x{height}'
    else:
        width = sprite.width_lr
        height = sprite.height_lr
        if sprite.camera_lr == "flat":
            # Exactly same camera that we used for DU (battery case)
            camera_name = sprite.camera_du
            cam = f'Camera{camera_name}{height}x{width}'
        else:
            camera_name = sprite.camera_lr
            cam = f'Camera{camera_name}{width}x{height}'

    scene.render.resolution_x = width * TILE_RES
    scene.render.resolution_y = height * TILE_RES
    cam_obj = bpy.data.objects[cam]

    scene.camera = cam_obj


def export_model(operator, sprite):
    # Handle subsets
    if len(sprite.subset) > 0:
        root_name = sprite.path.split("/")[-1]
        for sub in sprite.subset:
            sprite_copy = copy.deepcopy(sprite)
            sprite_copy.subset = []
            sprite_copy.path = f'{sprite.path}/{root_name}{sub}'
            print("Will export subsprite: " + sprite_copy.path)
            activate_model(operator, sprite_copy)
            export_model(operator, sprite_copy)
        return

    scene = bpy.context.scene
    path = output_path(sprite.path)

    if not sprite.is_rotatable:
        render_scene(operator, path + ".png")
        return

    scene.cursor.location = Vector((0.0, 0.0, 0.0))
    scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))

    prev_pivot = scene.tool_settings.transform_pivot_point
    scene.tool_settings.transform_pivot_point = "CURSOR"

    # Down
    if 'D' not in sprite.skip_rotations:
        activate_camera(sprite, 'd')
        render_scene(operator, path + "_D.png")
    rotate_selected(-90)
    if 'L' not in sprite.skip_rotations:
        activate_camera(sprite, 'l')
        render_scene(operator, path + "_L.png")
    rotate_selected(-90)
    if 'U' not in sprite.skip_rotations:
        activate_camera(sprite, 'u')
        render_scene(operator, path + "_U.png")
    rotate_selected(-90)
    if 'R' not in sprite.skip_rotations:
        activate_camera(sprite, 'r')
        render_scene(operator, path + "_R.png")
    # Rotate back
    rotate_selected(270)

    activate_camera(sprite, 'd')
    report(operator, "Done rendering " + path)

    scene.tool_settings.transform_pivot_point = prev_pivot

def get_override(area_type, region_type):
    for area in bpy.context.screen.areas:
        if area.type == area_type:
            for region in area.regions:
                if region.type == region_type:
                    override = {'area': area, 'region': region}
                    return override
    #error message if the area or region wasn't found
    raise RuntimeError("Wasn't able to find", region_type," in area ", area_type,
                        "\n Make sure it's open while executing script.")


def rotate_selected(deg, axis='Z', constraint=(False, False, True)):
    rads = radians(deg)
    override = get_override("VIEW_3D", "WINDOW")
    bpy.ops.transform.rotate(override, value=rads, orient_axis=axis, orient_type='GLOBAL',
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        orient_matrix_type='GLOBAL',
        constraint_axis=constraint,
        mirror=True)

def render_scene(operator, path):
    report(operator, "Rendering: " + path)
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)

def report(operator, what):
    operator.report({'INFO'}, what)
    sleep(0.1)


def enable_in_outliner(names, children):
    if len(children) == 0:
        return
    for item in children:
        excl = not item.name in names
        item.exclude = excl
        item.hide_viewport = excl
        enable_in_outliner(names, item.children)


def toggle_collection(col, on, sel_children):
    col.hide_viewport = not on
    col.hide_render = not on
    if not sel_children:
        return
    for obj in col.all_objects:
        if not obj.hide_viewport:

            obj.select_set(True)
