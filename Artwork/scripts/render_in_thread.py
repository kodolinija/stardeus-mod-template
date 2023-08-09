
# report back to operator
def separate_thread(self):
    from time import sleep
    for i in range(100):
        sleep(0.1)
        self.report({'INFO'}, f"{i}%")
    self.report({'INFO'}, "100% - Finished")
    self.finished = True

class WM_OT_dummy_progress(bpy.types.Operator):
    bl_idname = "wm.dummy_progress"
    bl_label = "Dummy Progress"
    
    # keep operator alive using modal while function runs
    def modal(self, context, event):
        if self.finished:
            return {'FINISHED'}
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        self.finished = False
        
        from threading import Timer
        Timer(0, separate_thread, (self,)).start()

        wm = context.window_manager
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
def register():
    bpy.utils.register_class(WM_OT_dummy_progress)

if __name__ == '__main__':
    register()
    
    bpy.ops.wm.dummy_progress('INVOKE_DEFAULT')