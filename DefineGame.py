import queue
from collections import deque
import copy
import Queue


def CreateLyfo(t):
    lyfo = Queue.lifo(4)
    for ball in t:
        lyfo.put(ball)
    return lyfo

"""
def Peek(lyfo):
    return lyfo.queue[-1]
"""

def CreateStatus(lyfo1,lyfo2,lyfo3,lyfo4,lyfo5):
    statusList = []
    statusList.append(lyfo1)
    statusList.append(lyfo2)
    statusList.append(lyfo3)
    statusList.append(lyfo4)
    statusList.append(lyfo5)
    status = tuple(statusList)
    return status

def Field(status):
    field = set()
    for lyfo in status:
        tubeCurrent = copy.deepcopy(lyfo)
        t = ""
        for ball in tubeCurrent.queue:
            t += ball
        field.add(t)
    return field

"""
def IsEmpty(lyfo):
    return len(lyfo) == 0

def IsFull(lyfo):
    return len(lyfo) == 4
"""

def LegalTurn(getFrom,putInto):
    if getFrom.empty():
        return False
    if putInto.full():
        return False
    if putInto.empty():
        return True
    if getFrom.peek() == putInto.peek():
        return True
    else: return False

def main():
    tube1 = CreateLyfo(t1)
    tube2 = CreateLyfo(t2)
    tube3 = CreateLyfo(t3)
    tube4 = CreateLyfo(t4)
    tube5 = CreateLyfo(t5)
    status = CreateStatus(tube1,tube2,tube3,tube4,tube5)
    field = Field(status)
    

    print(LegalTurn(tube1,tube3))


if __name__ == "__main__":
    

    t1 = "ryby"
    t2 = "rrbb"
    t3 = "bryy"
    t4 = ""
    t5 = ""
    
    main()