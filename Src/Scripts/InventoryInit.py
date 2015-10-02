import bge, Rasterizer

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()
text = bge.logic.globalDict["Text"]

# Get the objects
inventoryView = curScene.objects["InventoryView"]
inventoryBackground = curScene.objects["InventoryBackground"]
inventoryItem = curScene.objects["InventoryItem"]

# Add the mouse pointer if needed
Rasterizer.showMouse(True)

inventoryItem.resolution = 4
inventoryItem["Text"] = scenes[0].objects["Player"]["Inventory"]