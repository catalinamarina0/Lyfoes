import queue
import DefineGame
import copy
from collections import deque
import Queue

def NewField(allFields,field):
    if field in allFields:
        return False
    else:
        allFields.append(field)
        return True

def Turn(getFrom,putInto):
    if DefineGame.LegalTurn(getFrom,putInto):
        print(getFrom.queue,"->",putInto.queue)
        putInto.put(getFrom.get())
    else:
        print("Error: Illegal turn:",getFrom.queue,"->",putInto.queue)

def FindNextTurns(status):
    newTurns = []
    nrLyfoes = len(status)
    for getFromIndex in range(nrLyfoes):
        for putIntoIndex in range(nrLyfoes):
            if getFromIndex == putIntoIndex:
                continue
            elif DefineGame.LegalTurn(status[getFromIndex],status[putIntoIndex]):
                newTurns.append( ((getFromIndex,putIntoIndex)))
    return newTurns

def PlayNextTurns(status,newTurns):
    newStatuses = []
    for turn in newTurns:
        statusCopy = copy.deepcopy(list(status))
        statusCopy[turn[1]].put(statusCopy[turn[0]].get())
        newStatuses.append(tuple(statusCopy))
    return newStatuses

def CreateWinCondition(field):
    colors = set()
    for tube in field:
        for color in tube:
            colors.add(color)
    winCondition = {""}
    for color in colors:
        winCondition.add(color+color+color+color)
    return winCondition


def Win(winCondition,field):
    for tube in field:
        if not tube in winCondition:
            return False
    return True

def Flow(allFields,winCondition,status):
    field = DefineGame.Field(status)
    if Win(winCondition,field):
        print("Congrats!")
        SystemExit
    if field in allFields:
        print("Heb ik al:",field)
    NewField(allFields,field)
    
    newTurns = FindNextTurns(status)
    newStatuses = PlayNextTurns(status,newTurns)
    return newStatuses
    


def main():
    t1 = "ryby"
    t2 = "rrbb"
    t3 = "bryy"
    t4 = ""
    t5 = ""

#    winCondition = {"rrrr","bbbb","yyyy",""}
    
    tubes = [t1,t2,t3,t4,t5]
    lyfo1 = DefineGame.CreateLyfo(t1)
    lyfo2 = DefineGame.CreateLyfo(t2)
    lyfo3 = DefineGame.CreateLyfo(t3)
    lyfo4 = DefineGame.CreateLyfo(t4)
    lyfo5 = DefineGame.CreateLyfo(t5)

    status = DefineGame.CreateStatus(lyfo1,lyfo2,lyfo3,lyfo4,lyfo5)
    field = DefineGame.Field(status)
    winCondition = CreateWinCondition(field)
    allFields = []
    NewField(allFields,field)
    newTurns = FindNextTurns(status)
    newStatuses = PlayNextTurns(status,newTurns)
    newStatusesCopy = copy.deepcopy(newStatuses)
    newStatuses = []
    for status in newStatusesCopy:
        newStatuses += Flow(allFields,winCondition,status)

    
    print(newTurns)

    print(allFields)

    newStatusesCopy = copy.deepcopy(newStatuses)
    for status in newStatusesCopy:
        newStatuses = Flow(allFields,winCondition,status)

    print(newTurns)

    print(allFields)






if __name__ == "__main__":
    main()
"""
    t1 = "ryby"
    t2 = "rrbb"
    t3 = "bryy"
    t4 = ""
    t5 = ""

    tube1 = DefineGame.CreateLyfo(t1)
    tube2 = DefineGame.CreateLyfo(t2)
    tube3 = DefineGame.CreateLyfo(t3)
    tube4 = DefineGame.CreateLyfo(t4)
    tube5 = DefineGame.CreateLyfo(t5)
    status = DefineGame.CreateStatus(tube1,tube2,tube3,tube4,tube5)

    newTurns = [tuple((0,4)),tuple((0,4))]
    PlayNextTurns(status,newTurns)

    newTurns = FindNextTurns(status)
    newStatuses = PlayNextTurns(status,newTurns)
"""