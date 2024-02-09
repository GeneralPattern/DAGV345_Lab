import maya.cmds as cmds

sequenceName = str(input("Sequence Name: "))

def SeqRenamer(txt):
    sel = cmds.ls(sl=True)
    count = txt.count("#")

    poundFind = txt.find("#" * count)
    if poundFind < 0:
        print("Enter the sequence with all the pound signs together")
        return

    for i in range(1, len(sel)):
        newName = txt.replace("#" * count, str(i).zfill(count))
        cmds.rename(sel[i], newName)6

SeqRenamer(sequenceName)
