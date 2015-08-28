import bge

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()

def countSceneVerts(scene):
    sum = 0
    for obj in curScene.objects:
        sum += countObjectVerts(obj)
    return sum

def countObjectVerts(obj):
    sum = 0
    for mesh in obj.meshes:
        sum += countMeshVerts(mesh)
    return sum

def countMeshVerts(mesh):
    sum = 0
    for material in range(mesh.numMaterials):
        sum += mesh.getVertexArrayLength(material)
    return sum

sum = countSceneVerts(curScene)
curCont.owner["AllVerts"] = sum