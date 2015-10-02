import bge, Rasterizer, json

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()

isLastPlayedGameSet = False

# Get the objects
continueObj = curScene.objects["Continue"]
continueSensor = curScene.objects["ContinueSensor"]
newGame = curScene.objects["NewGame"]
options = curScene.objects["Options"]
quit = curScene.objects["Quit"]

# Show the default mouse cursor
Rasterizer.showMouse(True)

# Load the global game settings
file = open("Data\\Settings.ksg", "r")
data = file.read().replace('\n', '')
content = json.loads(data)
bge.logic.globalDict["Settings"] = content
#print(content)

# Load the language file of the current language
file = open("Src\\Lang\\"+bge.logic.globalDict["Settings"]["Language"]+".txt", "r")
data = file.read().replace('\n', '')
content = json.loads(data)
bge.logic.globalDict["Text"] = content
#print(content)

# Check if save file is set
if not bge.logic.globalDict["Settings"]["LastPlayedGame"] == "":
    isLastPlayedGameSet = True


text = bge.logic.globalDict["Text"]

continueObj["Text"] = text["continue"]
continueObj.resolution = 4
if not isLastPlayedGameSet:
    continueObj.color = (0.05, 0.1, 0.25, 1)
    continueSensor["Active"] = False

newGame["Text"] = text["newGame"]
newGame.resolution = 4

options["Text"] = text["options"]
options.resolution = 4

quit["Text"] = text["quit"]
quit.resolution = 4