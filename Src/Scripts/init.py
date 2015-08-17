import bge

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()

# Get the objects
fpView = curScene.objects["FpView"]
player = curScene.objects["Player"]

# Add the HeadsUpDisplay (HUD) to the view
if player["HUD"]:
    Scene = player.actuators["HUD"]
    Scene.scene = "HUD"
    curCont.activate("HUD")