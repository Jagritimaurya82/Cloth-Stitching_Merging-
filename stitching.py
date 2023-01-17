# sewing the t-shirts with alignment
import bpy
from mathutils import *
from math import *
import os


 
file_loc_1 = r'C:\Users\acer\Desktop\blender_scripting\Salwar\Avatar_SDK bodies_35'
Files = os.listdir(file_loc_1)
for File_1 in Files:
    body_path = os.path.join(file_loc_1,File_1)
    name1 = File_1.rsplit('.', 1)[0]
   
     
    
    file_loc_2 = r'C:\Users\acer\Desktop\blender_scripting\Salwar\salwar_templates_14'
    Files = os.listdir(file_loc_2)
    for File_2 in Files:
        cloth_path = os.path.join(file_loc_2,File_2)
        name2 = File_2.rsplit('.', 1)[0]
        
        
        #import cloth
        imported_object_cloth = bpy.ops.import_scene.obj(filepath=cloth_path)
        obj_object_cloth = bpy.context.selected_objects[0]  
        
        #import body
        imported_object_body = bpy.ops.import_scene.fbx(filepath=body_path)
        obj_object_body = bpy.context.selected_objects[1]
      
        
        if( File_2 == '1.obj' or File_2 == '2.obj'  or File_2 =='3.obj' or File_2 == '6.obj' or File_2 == '7.obj' or File_2 =='8.obj' or File_2 == '11.obj' or File_2 == '12.obj' or File_2 == '13.obj'): 
               
        # for XS, S, M
            #select cloth
            bpy.context.view_layer.objects.active = obj_object_cloth
            #add cloth properties
            bpy.ops.object.modifier_add(type='CLOTH')
            bpy.context.object.modifiers["Cloth"].settings.quality = 7
            bpy.context.object.modifiers["Cloth"].settings.mass = 0.08
            bpy.context.object.modifiers["Cloth"].settings.tension_stiffness = 8
            bpy.context.object.modifiers["Cloth"].settings.compression_stiffness = 8
            bpy.context.object.modifiers["Cloth"].settings.shear_stiffness = 4
            bpy.context.object.modifiers["Cloth"].settings.bending_stiffness = 2
            bpy.ops.object.modifier_add(type='COLLISION')
            bpy.context.object.modifiers["Cloth"].collision_settings.collision_quality = 5
            bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True
            
            #add stitching operation
            bpy.context.object.modifiers["Cloth"].settings.use_sewing_springs = True

            #select body
            bpy.context.view_layer.objects.active = obj_object_body

            #add collision properties to body
            bpy.ops.object.modifier_add(type='COLLISION')
             

            #run simulator
            bpy.context.scene.frame_set(1) 
            for k in range(45):
                bpy.context.scene.frame_set(bpy.context.scene.frame_current + 1)
             
            #rename selected object
            for obj in bpy.context.scene.objects:
                if obj.type == 'MESH':
                    obj.name = "body"   



            # delete SMPL body
            object_to_delete = bpy.data.objects['body']
            bpy.data.objects.remove(object_to_delete, do_unlink=True)
 
            #export tshirt
            file_loc_3 = f'C:/Users/acer/Desktop/blender_scripting/Salwar/stitched_salwar/{name1}_{name2}.obj'
            bpy.ops.export_scene.obj(filepath=file_loc_3 , use_materials=False )

            #rename selected object
            for obj in bpy.context.scene.objects:
                if obj.type == 'MESH':
                    obj.name = "tshirt"   

            # delete cloth
            object_to_delete = bpy.data.objects['tshirt']
            bpy.data.objects.remove(object_to_delete, do_unlink=True)
            
            
            
        if( File_2 == '4.obj' or File_2 == '5.obj' or File_2 =='9.obj' or File_2 == '10.obj' or File_2 == '14.obj' or File_2 =='15.obj'):
            bpy.context.view_layer.objects.active = obj_object_cloth
            #add cloth properties
            bpy.ops.object.modifier_add(type='CLOTH')
            bpy.context.object.modifiers["Cloth"].settings.quality = 7
            bpy.context.object.modifiers["Cloth"].settings.mass = 0.1
            bpy.context.object.modifiers["Cloth"].settings.tension_stiffness = 15
            bpy.context.object.modifiers["Cloth"].settings.compression_stiffness = 15
            bpy.context.object.modifiers["Cloth"].settings.shear_stiffness = 5
            bpy.context.object.modifiers["Cloth"].settings.bending_stiffness = .5
            bpy.ops.object.modifier_add(type='COLLISION')
            bpy.context.object.modifiers["Cloth"].collision_settings.collision_quality = 5
            bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True
                
            #add stitching operation
            bpy.context.object.modifiers["Cloth"].settings.use_sewing_springs = True

            #select body
            bpy.context.view_layer.objects.active = obj_object_body

            #add collision properties to body
            bpy.ops.object.modifier_add(type='COLLISION')
                 

            #run simulator
            bpy.context.scene.frame_set(1) 
            for k in range(45):
                bpy.context.scene.frame_set(bpy.context.scene.frame_current + 1)
                 
            #rename selected object
            for obj in bpy.context.scene.objects:
                if obj.type == 'MESH':
                    obj.name = "body"   

                # delete SMPL body
            object_to_delete = bpy.data.objects['body']
            bpy.data.objects.remove(object_to_delete, do_unlink=True)
 
            #export tshirt
            file_loc_3 = f'C:/Users/acer/Desktop/blender_scripting/Salwar/stitched_salwar/{name1}_{name2}.obj'
            bpy.ops.export_scene.obj(filepath=file_loc_3 , use_materials=False )

            #rename selected object
            for obj in bpy.context.scene.objects:
                if obj.type == 'MESH':
                    obj.name = "bottomware"   

            # delete cloth
            object_to_delete = bpy.data.objects['bottomware']
            bpy.data.objects.remove(object_to_delete, do_unlink=True)
                
            
            
        


            








        
   
        
        
 