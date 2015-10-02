import bge, math, random, Rasterizer

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()

forwardSpeed = bge.logic.globalDict["Settings"]["ForwardSpeed"]
backwardSpeed = bge.logic.globalDict["Settings"]["BackwardSpeed"]
leftSpeed = bge.logic.globalDict["Settings"]["LeftSpeed"]
rightSpeed = bge.logic.globalDict["Settings"]["RightSpeed"]
jumpForce = bge.logic.globalDict["Settings"]["JumpForce"]

# Get the objects
fpView = curScene.objects["FpView"]
player = curScene.objects["Player"]

# Remove the mouse pointer if needed
Rasterizer.showMouse(False)

# Get keyboard input
aKeyDown = bge.logic.keyboard.events[bge.events.AKEY] == bge.logic.KX_INPUT_ACTIVE
aKeyJustDown = bge.logic.keyboard.events[bge.events.AKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED
aKeyJustUp = bge.logic.keyboard.events[bge.events.AKEY] == bge.logic.KX_INPUT_JUST_RELEASED

dKeyDown = bge.logic.keyboard.events[bge.events.DKEY] == bge.logic.KX_INPUT_ACTIVE
dKeyJustDown = bge.logic.keyboard.events[bge.events.DKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED
dKeyJustUp = bge.logic.keyboard.events[bge.events.DKEY] == bge.logic.KX_INPUT_JUST_RELEASED

eKeyDown = bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_ACTIVE
eKeyJustDown = bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED
eKeyJustUp = bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_JUST_RELEASED

gKeyJustDown = bge.logic.keyboard.events[bge.events.GKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

qKeyDown = bge.logic.keyboard.events[bge.events.QKEY] == bge.logic.KX_INPUT_ACTIVE
qKeyJustDown = bge.logic.keyboard.events[bge.events.QKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

sKeyDown = bge.logic.keyboard.events[bge.events.SKEY] == bge.logic.KX_INPUT_ACTIVE
sKeyJustDown = bge.logic.keyboard.events[bge.events.SKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED
sKeyJustUp = bge.logic.keyboard.events[bge.events.SKEY] == bge.logic.KX_INPUT_JUST_RELEASED

vKeyJustDown = bge.logic.keyboard.events[bge.events.VKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

wKeyDown = bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_ACTIVE
wKeyJustDown = bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED
wKeyJustUp = bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_JUST_RELEASED

accentGraveKeyJustDown = bge.logic.keyboard.events[bge.events.ACCENTGRAVEKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

escKeyJustDown = bge.logic.keyboard.events[bge.events.ESCKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

shiftKeyDown = bge.logic.keyboard.events[bge.events.LEFTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE

spaceKeyDown = bge.logic.keyboard.events[bge.events.SPACEKEY] == bge.logic.KX_INPUT_ACTIVE
spaceKeyJustDown = bge.logic.keyboard.events[bge.events.SPACEKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED


# Get mouse input
lMouseDown = bge.logic.mouse.events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_ACTIVE
lMouseUp = bge.logic.mouse.events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_JUST_RELEASED

# Movement logic

curCont.actuators["Move"].reference = curCont.sensors["GroundCollision"].hitObject

# Move forwards
if wKeyDown and shiftKeyDown:
    curCont.actuators["Move"].linV = (0.0, forwardSpeed*2, 0.0)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, False)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, True)
    curCont.activate("Move")
elif wKeyDown:
    curCont.actuators["Move"].linV = (0.0, forwardSpeed, 0.0)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, False)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, True)
    curCont.activate("Move")
    
# Move backwards
if sKeyDown and shiftKeyDown:
    curCont.actuators["Move"].linV = (0.0, -backwardSpeed*2, 0.0)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, False)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, True)
    curCont.activate("Move")
elif sKeyDown:
    curCont.actuators["Move"].linV = (0.0, -backwardSpeed, 0.0)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, False)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, True)
    curCont.activate("Move")

# Move left
if aKeyDown and shiftKeyDown:
    curCont.actuators["Move"].linV = (-leftSpeed*2, 0.0, 0.0)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, False)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, True)
    curCont.activate("Move")
elif aKeyDown:
    curCont.actuators["Move"].linV = (-leftSpeed, 0.0, 0.0)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, False)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, True)
    curCont.activate("Move")

# Move right
if dKeyDown and shiftKeyDown:
    curCont.actuators["Move"].linV = (rightSpeed*2, 0, 0)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, False)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, True)
    curCont.activate("Move")
elif dKeyDown:
    curCont.actuators["Move"].linV = (rightSpeed, 0, 0)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, False)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, True)
    curCont.activate("Move")

# Jump
if spaceKeyDown and curCont.sensors["GroundCollision"].positive:
    curCont.actuators["Move"].linV = (0.0, 0.0, jumpForce)
    curCont.actuators["Move"].forceLimitX = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitY = (0.0, 0.0, True)
    curCont.actuators["Move"].forceLimitZ = (0.0, 0.0, False)
    curCont.activate("Move")  

# Deactivate current movement
curCont.deactivate("Move")

# Open the console
if accentGraveKeyJustDown:
    curCont.activate("Console")

# Open the inventory
if eKeyJustDown:
    curCont.activate("Inventory")

# Open the ESC menu ( for testing it is now the "q" key )
if qKeyJustDown:
    print("q")

# Add a bit of Hunger/Thirst every frame bge.logic.globalDict["GameData"]
if bge.logic.globalDict["GameData"]["Player"]["Hunger"] <= 100.0:
    bge.logic.globalDict["GameData"]["Player"]["Hunger"] += 0.002

if bge.logic.globalDict["GameData"]["Player"]["Thirst"] <= 100.0:
    bge.logic.globalDict["GameData"]["Player"]["Thirst"] += 0.008