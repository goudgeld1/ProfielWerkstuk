import bge, Rasterizer

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()

# Get the objects
startMenuView = curScene.objects["StartMenuView"]
continueObj = curScene.objects["Continue"]
newGame = curScene.objects["NewGame"]
options = curScene.objects["Options"]
quit = curScene.objects["Quit"]
continueSensor = curScene.objects["ContinueSensor"]
newGameSensor = curScene.objects["NewGameSensor"]
optionsSensor = curScene.objects["OptionsSensor"]
quitSensor = curScene.objects["QuitSensor"]

if continueSensor["Selected"] == False and continueSensor.sensors["MouseOver"].positive:
    continueSensor["Selected"] = True
    continueObj["Text"] = "> "+continueObj["Text"]
elif continueSensor["Selected"] == True and (not continueSensor.sensors["MouseOver"].positive):
    continueSensor["Selected"] = False    
    continueObj["Text"] = continueObj["Text"][2:]
elif continueSensor.sensors["MouseOver"].positive and startMenuView.sensors["LeftMouseDown"].positive:
    curScene.replace("HUD")
    curCont.activate("StartMainGame")


if newGameSensor["Selected"] == False and newGameSensor.sensors["MouseOver"].positive:
    newGameSensor["Selected"] = True
    newGame["Text"] = "> "+newGame["Text"]
elif newGameSensor["Selected"] == True and (not newGameSensor.sensors["MouseOver"].positive):
    newGameSensor["Selected"] = False    
    newGame["Text"] = newGame["Text"][2:]


if optionsSensor["Selected"] == False and optionsSensor.sensors["MouseOver"].positive:
    optionsSensor["Selected"] = True
    options["Text"] = "> "+options["Text"]
elif optionsSensor["Selected"] == True and (not optionsSensor.sensors["MouseOver"].positive):
    optionsSensor["Selected"] = False    
    options["Text"] = options["Text"][2:]


if quitSensor["Selected"] == False and quitSensor.sensors["MouseOver"].positive:
    quitSensor["Selected"] = True
    quit["Text"] = "> "+quit["Text"]
elif quitSensor["Selected"] == True and (not quitSensor.sensors["MouseOver"].positive):
    quitSensor["Selected"] = False    
    quit["Text"] = quit["Text"][2:]
elif quitSensor.sensors["MouseOver"].positive and startMenuView.sensors["LeftMouseDown"].positive:
    bge.logic.endGame()