import bge

# Frequently used variables
curCont = bge.logic.getCurrentController()

# Get the objects
player = curScene.objects["Player"]

if curCont.owner.getDistanceTo(player) >= 64:
    curCont.replaceMesh("ObjEmpty", True, True)
else:
    curCont.replaceMesh("Tree1", True, True)