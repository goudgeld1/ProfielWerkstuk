import bge, math, random

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()

# Get the objects
fpView = curScene.objects["FpView"]
player = curScene.objects["Player"]

forwardSpeed = player["ForwardSpeed"]    #0.08 m/tick = 0.08*60 = 4.8 m/s
backwardSpeed = player["BackwardSpeed"]  #0.06 m/tick ...
leftSpeed = player["LeftSpeed"]          #0.04 m/tick ...
rightSpeed = player["RightSpeed"]        #0.04 m/tick ...

# Get keyboard input
aKeyDown = bge.logic.keyboard.events[bge.events.AKEY] == bge.logic.KX_INPUT_ACTIVE
aKeyJustUp = bge.logic.keyboard.events[bge.events.AKEY] == bge.logic.KX_INPUT_JUST_RELEASED

dKeyDown = bge.logic.keyboard.events[bge.events.DKEY] == bge.logic.KX_INPUT_ACTIVE
dKeyJustUp = bge.logic.keyboard.events[bge.events.DKEY] == bge.logic.KX_INPUT_JUST_RELEASED

eKeyDown = bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_ACTIVE
eKeyJustUp = bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_JUST_RELEASED

gKeyJustDown = bge.logic.keyboard.events[bge.events.GKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

qKeyDown = bge.logic.keyboard.events[bge.events.QKEY] == bge.logic.KX_INPUT_ACTIVE
qKeyJustDown = bge.logic.keyboard.events[bge.events.QKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

sKeyDown = bge.logic.keyboard.events[bge.events.SKEY] == bge.logic.KX_INPUT_ACTIVE
sKeyJustUp = bge.logic.keyboard.events[bge.events.SKEY] == bge.logic.KX_INPUT_JUST_RELEASED

vKeyJustDown = bge.logic.keyboard.events[bge.events.VKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

wKeyDown = bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_ACTIVE
wKeyJustUp = bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_JUST_RELEASED

shiftKeyDown = bge.logic.keyboard.events[bge.events.LEFTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE

spaceKeyDown = bge.logic.keyboard.events[bge.events.SPACEKEY] == bge.logic.KX_INPUT_ACTIVE
spaceKeyJustDown = bge.logic.keyboard.events[bge.events.SPACEKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

accentGraveKeyJustDown = bge.logic.keyboard.events[bge.events.ACCENTGRAVEKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED


# Get mouse input
lMouseDown = bge.logic.mouse.events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_ACTIVE
lMouseUp = bge.logic.mouse.events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_JUST_RELEASED

# Movement logic
# Move forwards
if wKeyDown and shiftKeyDown:
    player.applyMovement((0, forwardSpeed*2, 0),True)
elif wKeyDown:
    player.applyMovement((0, forwardSpeed, 0),True)

# Move backwards
if sKeyDown and shiftKeyDown:
    player.applyMovement((0, -backwardSpeed*2, 0),True)
elif sKeyDown:
    player.applyMovement((0, -backwardSpeed, 0),True)

# Move left
if aKeyDown and shiftKeyDown:
    player.applyMovement((-leftSpeed*2, 0, 0),True)
elif aKeyDown:
    player.applyMovement((-leftSpeed, 0, 0),True)

# Move right
if dKeyDown and shiftKeyDown:
    player.applyMovement((rightSpeed*2, 0, 0),True)
elif dKeyDown:
    player.applyMovement((rightSpeed, 0, 0),True)

# Jump
if spaceKeyDown and curCont.sensors["GroundCollision"].positive:
    curCont.activate("Jump")
curCont.deactivate("Jump")

# Correct gravity for the player
if curCont.sensors["GroundCollision"].positive:
    player.applyForce([0, 0, 9.8 * player.mass], True)
else:
    player.applyForce([0, 0, -9.8 * player.mass], True)

#Toggle the console
if not player["Console"] and accentGraveKeyJustDown:
    player["Console"] = True
elif player["Console"] and accentGraveKeyJustDown:
    player["Console"] = False