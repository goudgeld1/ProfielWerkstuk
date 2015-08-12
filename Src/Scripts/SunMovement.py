import bge, math

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()

# Get the Objects
sunPath = curScene.objects["SunPath"]
ambient = curScene.objects["Ambient"]

xyz = sunPath.localOrientation.to_euler()
xyz[1] = math.radians(math.degrees(xyz[1])-1/5)
sunPath.localOrientation = xyz.to_matrix()

# make the sky color change
if(math.degrees(xyz[1]) < 80 and math.degrees(xyz[1]) > -80):
    ambient.energy = 0.4
    ambient.color = [1, 1, 1]
    bge.render.setBackgroundColor([0, .4, .65, 0])
elif(math.degrees(xyz[1]) > 100 or math.degrees(xyz[1]) < -100):
    ambient.energy = 0.2
    ambient.color = [.4, .4, .8]
    bge.render.setBackgroundColor([0, 0, .1, 0])
else:
    ambient.energy = 0.3
    ambient.color = [.6, .15, .05]
    bge.render.setBackgroundColor([.4, .3, .6, 0])
    
    
#ambient.energy = math.sin((xyz[1]/2 + math.pi/4) + 1) / 10 + 0.1
print(math.degrees(xyz[1]))
#print(ambient.energy)