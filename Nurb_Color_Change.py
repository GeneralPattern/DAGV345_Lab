import maya.cmds as cmds

def color_change(color):
	sel = cmds.ls(sl=True)

	shape =cmds.listRelatives(sel, shapes = True )


	for selection in shape:
		cmds. setAttr(selection + ".overrideEnabled", True)
		cmds. setAttr(selection + ".overrideColor", color)

color_change(4)