import maya.cmds as cmds

# Get selected joints
selected_joints = cmds.ls(selection=True, type="joint")

# Loop through each joint and print correct Python command format
for joint in selected_joints:
    rotation = cmds.getAttr(joint + ".rotate")[0]  # Get rotation values
    command = f'cmds.setAttr("{joint}.rotate", {rotation[0]}, {rotation[1]}, {rotation[2]})'
    print(command)
