import bge, math

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()

# Get the Objects
sunPath = curScene.objects["SunPath"]
sun = curScene.objects["Sun"]
ambient = curScene.objects["Ambient"]
player = curScene.objects["Player"]

xyz = sunPath.localOrientation.to_euler()
xyz[1] = math.radians(math.degrees(xyz[1])-1/60)
sunPath.localOrientation = xyz.to_matrix()

# make the sky color change
if(math.degrees(xyz[1]) < 75 and math.degrees(xyz[1]) > -75):
    ambient.energy = 0.4
    sun.energy = 1.0
    ambient.color = [1, 1, 1]
    curScene.world.backgroundColor = [0, .4, .65]
    curScene.world.mistColor = [0, .4, .65]
elif(math.degrees(xyz[1]) > 90 or math.degrees(xyz[1]) < -90):
    ambient.energy = 0.2
    sun.energy = 0.0
    ambient.color = [.4, .4, .8]
    curScene.world.backgroundColor = [0, 0, .1]
    curScene.world.mistColor = [0, 0, .1]
else:
    ambient.energy = 0.3
    sun.energy = 0.3
    ambient.color = [.6, .15, .05]
    curScene.world.backgroundColor = [.6, .3, .2]
    curScene.world.mistColor = [.6, .3, .2]

#ambient.energy = math.sin((xyz[1]/2 + math.pi/4) + 1) / 10 + 0.1
#print(math.degrees(xyz[1]))
#print(ambient.energy)