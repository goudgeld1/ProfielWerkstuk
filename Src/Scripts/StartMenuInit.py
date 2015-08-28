import bge, Rasterizer, json

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()

# Get the objects
continueObj = curScene.objects["Continue"]
newGame = curScene.objects["NewGame"]
options = curScene.objects["Options"]
quit = curScene.objects["Quit"]


Rasterizer.showMouse(True)


file = open("Data\\Settings.txt", "r")
data = file.read().replace('\n', '')
text = json.loads(data)
bge.logic.globalDict["Settings"] = text
#print(text)

file = open("Src\\Lang\\"+bge.logic.globalDict["Settings"]["Language"]+".txt", "r")
data = file.read().replace('\n', '')
text = json.loads(data)
bge.logic.globalDict["Text"] = text
#print(text)

continueObj["Text"] = text["continue"]
continueObj.resolution = 4
newGame["Text"] = text["newGame"]
newGame.resolution = 4
options["Text"] = text["options"]
options.resolution = 4
quit["Text"] = text["quit"]
quit.resolution = 4