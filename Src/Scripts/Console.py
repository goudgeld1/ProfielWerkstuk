import bge, re

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()

# Get the objects
consoleView = curScene.objects["ConsoleView"]
consoleInput = curScene.objects["ConsoleInput"]
consoleOutput = curScene.objects["ConsoleOutput"]

def checkKey(keycode, char, shift):
    if shift:
        if bge.logic.keyboard.events[keycode] == bge.logic.KX_INPUT_JUST_ACTIVATED and (bge.logic.keyboard.events[bge.events.LEFTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE or bge.logic.keyboard.events[bge.events.RIGHTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE):
            consoleInput['Text'] += char
    else:
        if bge.logic.keyboard.events[keycode] == bge.logic.KX_INPUT_JUST_ACTIVATED and not (bge.logic.keyboard.events[bge.events.LEFTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE or bge.logic.keyboard.events[bge.events.RIGHTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE):
            consoleInput['Text'] += char

checkKey(bge.events.ZEROKEY, "0", False)
checkKey(bge.events.ONEKEY, "1", False)
checkKey(bge.events.TWOKEY, "2", False)
checkKey(bge.events.THREEKEY, "3", False)
checkKey(bge.events.FOURKEY, "4", False)
checkKey(bge.events.FIVEKEY, "5", False)
checkKey(bge.events.SIXKEY, "6", False)
checkKey(bge.events.SEVENKEY, "7", False)
checkKey(bge.events.EIGHTKEY, "8", False)
checkKey(bge.events.NINEKEY, "9", False)

checkKey(bge.events.ZEROKEY, ")", True)
checkKey(bge.events.ONEKEY, "!", True)
checkKey(bge.events.TWOKEY, "@", True)
checkKey(bge.events.THREEKEY, "#", True)
checkKey(bge.events.FOURKEY, "$", True)
checkKey(bge.events.FIVEKEY, "%", True)
checkKey(bge.events.SIXKEY, "^", True)
checkKey(bge.events.SEVENKEY, "&", True)
checkKey(bge.events.EIGHTKEY, "*", True)
checkKey(bge.events.NINEKEY, "(", True)

checkKey(bge.events.AKEY, "a", False)
checkKey(bge.events.BKEY, "b", False)
checkKey(bge.events.CKEY, "c", False)
checkKey(bge.events.DKEY, "d", False)
checkKey(bge.events.EKEY, "e", False)
checkKey(bge.events.FKEY, "f", False)
checkKey(bge.events.GKEY, "g", False)
checkKey(bge.events.HKEY, "h", False)
checkKey(bge.events.IKEY, "i", False)
checkKey(bge.events.JKEY, "j", False)
checkKey(bge.events.KKEY, "k", False)
checkKey(bge.events.LKEY, "l", False)
checkKey(bge.events.MKEY, "m", False)
checkKey(bge.events.NKEY, "n", False)
checkKey(bge.events.OKEY, "o", False)
checkKey(bge.events.PKEY, "p", False)
checkKey(bge.events.QKEY, "q", False)
checkKey(bge.events.RKEY, "r", False)
checkKey(bge.events.SKEY, "s", False)
checkKey(bge.events.TKEY, "t", False)
checkKey(bge.events.UKEY, "u", False)
checkKey(bge.events.VKEY, "v", False)
checkKey(bge.events.WKEY, "w", False)
checkKey(bge.events.XKEY, "x", False)
checkKey(bge.events.YKEY, "y", False)
checkKey(bge.events.ZKEY, "z", False)

checkKey(bge.events.AKEY, "A", True)
checkKey(bge.events.BKEY, "B", True)
checkKey(bge.events.CKEY, "C", True)
checkKey(bge.events.DKEY, "D", True)
checkKey(bge.events.EKEY, "E", True)
checkKey(bge.events.FKEY, "F", True)
checkKey(bge.events.GKEY, "G", True)
checkKey(bge.events.HKEY, "H", True)
checkKey(bge.events.IKEY, "I", True)
checkKey(bge.events.JKEY, "J", True)
checkKey(bge.events.KKEY, "K", True)
checkKey(bge.events.LKEY, "L", True)
checkKey(bge.events.MKEY, "M", True)
checkKey(bge.events.NKEY, "N", True)
checkKey(bge.events.OKEY, "O", True)
checkKey(bge.events.PKEY, "P", True)
checkKey(bge.events.QKEY, "Q", True)
checkKey(bge.events.RKEY, "R", True)
checkKey(bge.events.SKEY, "S", True)
checkKey(bge.events.TKEY, "T", True)
checkKey(bge.events.UKEY, "U", True)
checkKey(bge.events.VKEY, "V", True)
checkKey(bge.events.WKEY, "W", True)
checkKey(bge.events.XKEY, "X", True)
checkKey(bge.events.YKEY, "Y", True)
checkKey(bge.events.ZKEY, "Z", True)

checkKey(bge.events.SPACEKEY, " ", False)
checkKey(bge.events.PERIODKEY, ".", False)

if bge.logic.keyboard.events[bge.events.BACKSPACEKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED:
    if len(consoleInput["Text"]) > 3:
        consoleInput["Text"] = consoleInput["Text"][:-1]
elif bge.logic.keyboard.events[bge.events.ENTERKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED:
    
    settings = bge.logic.globalDict["Settings"]
    
    if re.search("SetForwardSpeed|SFS", consoleInput["Text"], re.I):
        if re.search("SetForwardSpeed ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SetForwardSpeed ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["ForwardSpeed"] = float(arg1)
            consoleOutput["Text"] = "<< ForwardSpeed set to %s meter/second" % arg1
        elif re.search("SFS ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SFS ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["ForwardSpeed"] = float(arg1)
            consoleOutput["Text"] = "<< ForwardSpeed set to %s meter/second" % arg1
        else:
            consoleOutput['Text'] = "<< Number expected"
    
    elif re.search("SetBackwardSpeed|SBS", consoleInput["Text"], re.I):
        if re.search("SetBackwardSpeed ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SetBackwardSpeed ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["BackwardSpeed"] = float(arg1)
            consoleOutput["Text"] = "<< BackwardSpeed set to %s meter/second" % arg1
        elif re.search("SBS ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SBS ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["BackwardSpeed"] = float(arg1)
            consoleOutput["Text"] = "<< BackwardSpeed set to %s meter/second" % arg1
        else:
            consoleOutput['Text'] = "<< Number expected"
    
    elif re.search("SetLeftSpeed|SLS", consoleInput["Text"], re.I):
        if re.search("SetLeftSpeed ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SetLeftSpeed ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["LeftSpeed"] = float(arg1)
            consoleOutput["Text"] = "<< LeftSpeed set to %s meter/second" % arg1
        elif re.search("SLS ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SLS ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["LeftSpeed"] = float(arg1)
            consoleOutput["Text"] = "<< LeftSpeed set to %s meter/second" % arg1
        else:
            consoleOutput['Text'] = "<< Number expected"
    
    elif re.search("SetRightSpeed|SRS", consoleInput["Text"], re.I):
        if re.search("SetRightSpeed ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SetRightSpeed ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["RightSpeed"] = float(arg1)
            consoleOutput["Text"] = "<< RightSpeed set to %s meter/second" % arg1
        elif re.search("SRS ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SRS ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["RightSpeed"] = float(arg1)
            consoleOutput["Text"] = "<< RightSpeed set to %s meter/second" % arg1
        else:
            consoleOutput['Text'] = "<< Number expected"
    
    elif re.search("SetJumpForce|SJF", consoleInput["Text"], re.I):
        if re.search("SetJumpForce ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SetJumpForce ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["JumpForce"] = float(arg1)
            consoleOutput["Text"] = "<< JumpForce set to %s" % arg1
        elif re.search("SJF ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I):
            arg1 = re.search("SJF ([-+]?[0-9]*\.?[0-9]*)", consoleInput["Text"], re.I).group(1)
            settings["JumpForce"] = float(arg1)
            consoleOutput["Text"] = "<< JumpForce set to %s" % arg1
        else:
            consoleOutput['Text'] = "<< Number expected"
    
    else:
        consoleOutput['Text'] = "<< Unknown Comand"
    
    consoleInput['Text'] = ">> "
