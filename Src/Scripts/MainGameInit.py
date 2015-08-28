import bge, math, random, Rasterizer

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()

# Get the objects
fpView = curScene.objects["FpView"]
player = curScene.objects["Player"]
OPE = curScene.objectsInactive["ObjectPlacementEmpty"]


random.seed(256)


# Add mist to the world
curScene.world.mistEnable = True

# Set the camera to the fpView
curScene.active_camera = fpView

# Add trees
def addTree():
    OPEPosition = [random.uniform(-512, 512), random.uniform(-512, 512), 512]
    
    OPE.position = OPEPosition
    
    hit, point, normal = OPE.rayCast([OPEPosition[0], OPEPosition[1], 499], OPEPosition, 16)

    if hit:
        if hit.name == "TreePlacementPlane":
            OPEPosition[2] = 499
            hit, point, normal = OPE.rayCast([OPEPosition[0], OPEPosition[1], 0], OPEPosition, 512)
            
            if hit.name == "Ground":
                OPE.position = point
                OPE.orientation = (0, 0, random.randint(0, 360))
                curScene.addObject("ObjTree1", OPE, 0)
    else:
        addTree()
    
for x in range(2048):
    addTree()