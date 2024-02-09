import maya.cmds as cmds

def create_joints():
    """
    Creates a joint at each selection(s) transform.
    Returns: [Joints]
    """

    selections = cmds.ls(sl=True)
    new_joints = []

    for sel in selections:
        position = cmds.xform(sel, q=True, translation=True, worldSpace=True)
        cmds.select(cl=True)

        jnt = cmds.joint()
        cmds.xform(jnt, worldSpace=True, translation=position)


        new_joints.append(jnt)

    cmds.select(new_joints, r=True)
    return new_joints


create_joints()