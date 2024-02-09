import maya.cmds as cmds

def set_rig_color(color_number):
	sel = cmds.ls(sl=True)

	shape = cmds.listRelatives (sel, shapes = True )

	for node in shape:
		cmds. setAttr (node + ".overrideEnabled" ,True)
		cmds. setAttr (node + ".overrideColor" ,color_number)

set_rig_color(8)