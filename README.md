# MayaJointRotations

A Python script for Autodesk Maya that allows users to export and restore joint rotations easily using `setAttr`. This script is useful for saving joint transformations, transferring animations, or debugging rigging setups.

## Features
- **Export Joint Rotations**: Print and save rotation values of selected joints.
- **Generate Executable Python Commands**: The output can be copy-pasted and executed directly in Maya's Script Editor.
- **Easily Restore Rotations**: Apply saved values back to joints effortlessly.

## Installation
No installation required. Simply download the **`maya_joint_rotations.py`** script and run it inside Maya's **Script Editor** under the Python tab.

## Usage
### Export Joint Rotations
1. **Select the joints** you want to export.
2. **Run the script** in the **Python tab** of Maya's **Script Editor**:

```python
import maya.cmds as cmds

# Get selected joints
selected_joints = cmds.ls(selection=True, type="joint")

# Loop through each joint and print correct Python command format
for joint in selected_joints:
    rotation = cmds.getAttr(joint + ".rotate")[0]  # Get rotation values
    command = f'cmds.setAttr("{joint}.rotate", {rotation[0]}, {rotation[1]}, {rotation[2]})'
    print(command)
```

3. **Copy the printed output** and save it for later use.

### Restore Joint Rotations
1. **Copy and paste** the previously saved output back into the **Python tab**.
2. **Run the script** to apply the saved rotations to the joints.

Example output:
```python
cmds.setAttr("Hip.rotate", 0.0, 0.0, 0.0)
cmds.setAttr("LeftArm.rotate", 15.2, -5.4, 3.0)
cmds.setAttr("RightLeg.rotate", -10.0, 8.5, 1.2)
```

## Why Use This Script?
✅ **Saves Time** – No need to manually note joint rotations.
✅ **Portable** – Works across different Maya scenes.
✅ **Flexible** – Useful for debugging rigs and transferring animations.

## License
This project is open-source under the **MIT License**.

## Contributing
Feel free to contribute by submitting pull requests or reporting issues!

## Author
[hsuehyt](https://github.com/hsuehyt) 🚀
