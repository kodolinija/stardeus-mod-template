# This is compatible with Blender 4.5 LTS
import bpy
from sprite_defs import *
from mathutils import Vector
from math import radians
import os
from time import sleep
from threading import Timer
import copy

TILE_RES = 256

def ensure_collection(path):
    collections = path.split('/')
    parent = bpy.context.scene.collection

    for collection_name in collections:
        # Check if the collection exists within the parent
        found = False
        for child in parent.children:
            if child.name == collection_name:
                found = True
                parent = child  # Update the parent to the current collection
                break

        if not found:
            # Create the collection if it doesn't exist
            new_collection = bpy.data.collections.new(collection_name)
            parent.children.link(new_collection)
            parent = new_collection  # Update the parent to the new collection


def output_path(path):
    artwork_dir = os.path.dirname(bpy.data.filepath) # ./ModName/Artwork/ because blend file is located in Artwork by default
    mod_dir = os.path.dirname(artwork_dir) # ./ModName/
    graphics_dir = os.path.join(mod_dir, "Graphics/") # ./ModName/Graphics/
    if path.endswith("_"):
        path = path[:-1]
    return os.path.join(graphics_dir, path.replace('.', '/'))

class StardeusExportAllOperator(bpy.types.Operator):
    bl_idname = "object.stardeusexportall"
    bl_label = "Export All"
    bl_description = "Exports all objects as sprites"

    def execute(self, context):
        bpy.ops.wm.save_mainfile()
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
        bpy.ops.wm.save_mainfile()
        exit_edit_mode()
        col_name = bpy.context.view_layer.active_layer_collection.name
        if col_name in SPRITES:
            col = SPRITES[col_name]
            activate_model(self, col)
            export_model(self, col)
        else:
            self.report({'ERROR'}, "Not found in SPRITES: " + col_name)

        return {'FINISHED'}

class StardeusExportHeadForwardOperator(bpy.types.Operator):
    bl_idname = "object.stardeusexportheadforward"
    bl_label = "Export Head Forward"
    bl_description = "Exports active collection as head or hair in forward direction"

    def execute(self, context):
        bpy.ops.wm.save_mainfile()
        exit_edit_mode()
        col_name = bpy.context.view_layer.active_layer_collection.name
        is_horizontal = col_name.endswith("_H")
        if col_name in SPRITES:
            col = SPRITES[col_name]
            activate_model(self, col)
            if is_horizontal:
                export_model_head_horizontal_fw(self, col)
            else:
                export_model_head_fw(self, col)
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
        bpy.ops.wm.save_mainfile()
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
    ensure_collection(sprite.path)
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
        if col.name == final_name and sprite.activate_filter is not None:
            select_filter(col, sprite.activate_filter)


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

def export_model_head_fw(operator, sprite):
    scene = bpy.context.scene
    path = output_path(sprite.output)
    scene.cursor.location = Vector((0.0, 0.0, 0.2))
    scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))
    scene.tool_settings.transform_pivot_point = "CURSOR"
    bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'

    # Down
    rotate_selected(-20, axis='X', constraint=(True, False, False))
    activate_camera(sprite, 'd')
    render_scene(operator, path + "_D.png", sprite)
    rotate_selected(20, axis='X', constraint=(True, False, False))

    scene.cursor.location = Vector((0.0, 0.0, 0.0))

def export_model_head_horizontal_fw(operator, sprite):
    scene = bpy.context.scene
    path = output_path(sprite.output)
    scene.cursor.location = Vector((0.0, 0.0, 0.0))
    scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))
    scene.tool_settings.transform_pivot_point = "CURSOR"
    bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'

    # Left
    activate_camera(sprite, 'l')
    rotate_selected(-90)
    # Turn head towards camera
    rotate_selected(30, axis='X', constraint=(True, False, False))
    render_scene(operator, path + "_L.png", sprite)
    # Unrotate
    rotate_selected(-30, axis='X', constraint=(True, False, False))
    rotate_selected(90)

    # Right
    activate_camera(sprite, 'l')
    rotate_selected(90)
    # Turn head towards camera
    rotate_selected(30, axis='X', constraint=(True, False, False))
    render_scene(operator, path + "_R.png", sprite)
    # Unrotate
    rotate_selected(-30, axis='X', constraint=(True, False, False))
    rotate_selected(-90)


def export_model(operator, sprite):
    # Handle subsets
    if len(sprite.subset) > 0:
        root_name = sprite.path.split("/")[-1]
        for sub in sprite.subset:
            sprite_copy = copy.deepcopy(sprite)
            sprite_copy.subset = []
            sprite_copy.path = f'{sprite.path}/{root_name}{sub}'
            sprite_copy.output = f'{sprite.output}/{root_name}{sub}'
            print("Will export subsprite: " + sprite_copy.output)
            activate_model(operator, sprite_copy)
            export_model(operator, sprite_copy)
        return

    scene = bpy.context.scene
    path = output_path(sprite.output)

    if not sprite.is_rotatable:
        render_scene(operator, path + ".png", sprite)
        return

    scene.cursor.location = Vector((0.0, 0.0, 0.0))
    scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))

    prev_pivot = scene.tool_settings.transform_pivot_point
    prev_ori = bpy.context.scene.transform_orientation_slots[0].type
    scene.tool_settings.transform_pivot_point = "CURSOR"
    bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'

    skip_rots = list(sprite.skip_rotations)

    # Export special head rotations first
    if sprite.is_head:
        if path.endswith("_H"):
            skip_rots.append('L')
            skip_rots.append('R')
        else:
            skip_rots.append('D')

    report(operator, "Skip rots: " + str(skip_rots))

    if sprite.num_rotations == 0:
        # Down
        if 'D' not in skip_rots:
            activate_camera(sprite, 'd')
            render_scene(operator, path + "_D.png", sprite)
        rotate_selected(-90)
        if 'L' not in skip_rots:
            activate_camera(sprite, 'l')
            render_scene(operator, path + "_L.png", sprite)
        rotate_selected(-90)
        if 'U' not in skip_rots:
            activate_camera(sprite, 'u')
            render_scene(operator, path + "_U.png", sprite)
        rotate_selected(-90)
        if 'R' not in skip_rots:
            activate_camera(sprite, 'r')
            render_scene(operator, path + "_R.png", sprite)

        # Rotate back
        rotate_selected(270)
    else:
        # Turret / anim mode
        deg = (360 / sprite.num_rotations)
        activate_camera(sprite, 'd')
        for i in range(sprite.num_rotations):
            if sprite.stop_at_rotation == 0 or sprite.stop_at_rotation > i:
                render_scene(operator, path + "_R" + str(i) + ".png", sprite)
            rotate_selected(-deg)
        # Rotate back
        rotate_selected(360)


    # Export special head rotations
    if sprite.is_head:
        if path.endswith("_H"):
            report(operator, "Exporting special horizontal head rotations for " + sprite.path)
            export_model_head_horizontal_fw(operator, sprite)
        else:
            report(operator, "Exporting special head rotation for " + sprite.path)
            export_model_head_fw(operator, sprite)

    activate_camera(sprite, 'd')
    report(operator, "Done rendering " + path)

    scene.tool_settings.transform_pivot_point = prev_pivot
    bpy.context.scene.transform_orientation_slots[0].type = prev_ori

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
    # Blender 4.0+ uses context.temp_override instead of passing override as first argument
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == 'WINDOW':
                    with bpy.context.temp_override(area=area, region=region):
                        bpy.ops.transform.rotate(value=rads, orient_axis=axis, orient_type='GLOBAL',
                            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                            orient_matrix_type='GLOBAL',
                            constraint_axis=constraint,
                            mirror=True)
                    # Force depsgraph update so rotation is applied before rendering
                    bpy.context.view_layer.update()
                    return
    raise RuntimeError("Wasn't able to find VIEW_3D area with WINDOW region")

def render_scene(operator, path, sprite):
    report(operator, "Rendering: " + path)
    bpy.context.scene.render.filepath = path

    if sprite.anim_frames > 0:
        # anim_speed_pct works like the old frame_map_new: higher percentage = slower animation = more frames
        # 100% = normal speed (anim_frames frames), 200% = half speed (double the frames), 50% = double speed (half the frames)
        original_frame_start = bpy.context.scene.frame_start
        original_frame_end = bpy.context.scene.frame_end

        # Calculate total output frames: higher percentage = more frames
        num_output_frames = int(sprite.anim_frames * (sprite.anim_speed_pct / 100.0))
        bpy.context.scene.frame_start = 0
        bpy.context.scene.frame_end = sprite.anim_frames - 1

        # Render each output frame, sampling from the source animation
        for output_frame in range(0, num_output_frames):
            # Map output frame to source frame (slower playback = lower source frame number)
            source_frame = int(output_frame / (sprite.anim_speed_pct / 100.0))
            bpy.context.scene.frame_set(source_frame)
            if path.endswith(".png"):
                path = path[:-4]
            frame_path = f"{path}_F{output_frame}.png"
            bpy.context.scene.render.filepath = frame_path
            bpy.ops.render.render(write_still=True)

        # Restore original frame settings
        bpy.context.scene.frame_start = original_frame_start
        bpy.context.scene.frame_end = original_frame_end
    else:
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

def select_filter(col, filter):
    for obj in col.all_objects:
        if obj.name.startswith(filter):
            obj.select_set(True)
        else:
            obj.select_set(False)
