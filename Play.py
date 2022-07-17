import Status
#from Lyfo import lyfo

def TestTubes1_1():     #10 turns
    t1 = "ryby"
    t2 = "rrbb"
    t3 = "bryy"
    t4 = ""
    t5 = ""
    return t1,t2,t3,t4,t5

def TestTubes2_1():     #17 turns
    t1 = "grrb"
    t2 = "rypp"
    t3 = "bgby"
    t4 = "yryg"
    t5 = "ppgb"
    t6 = ""
    t7 = ""
    return t1,t2,t3,t4,t5,t6,t7

def TestTubes2_2():     #17 turns
    t1 = "rryb"
    t2 = "bpry"
    t3 = "rypg"
    t4 = "bpgb"
    t5 = "yggp"
    t6 = ""
    t7 = ""
    return t1,t2,t3,t4,t5,t6,t7

def TestTubes3_1():     #23 turns
    t1 = "ggpr"
    t2 = "llgw"
    t3 = "byyw"
    t4 = "prlg"
    t5 = "lwrw"
    t6 = "bpby"
    t7 = "ybpr"
    t8 = ""
    t9 = ""
    return t1,t2,t3,t4,t5,t6,t7,t8,t9

def TestTubes4_1():
    t1 = "dlyw"
    t2 = "lygb"
    t3 = "bpgr"
    t4 = "rypg"
    t5 = "lrop"
    t6 = "dwwo"
    t7 = "bdol"
    t8 = "olap"
    t9 = "lgdl"
    t9 = "rbyw"
    t9 = ""
    t9 = ""
    return t1,t2,t3,t4,t5,t6,t7,t8,t9

def CheckValidityTubes(tubes):
    balls = {}
    for tube in tubes:
        for ball in tube:
            if ball in balls:
                balls[ball] += 1
            else:
                balls[ball] = 1
    for color in balls:
        if balls[color] != 4:
            raise Exception(f"Wrong setup: {balls[color]} balls have color {color}.")

def MakeStatus(tubes):
    stat = Status.status(tubes)
    return stat

#TODO: Clean up
def Run(lst: list,f: Status.field):
    turn = 0
    won = 0
    while won == False and len(lst[turn]) > 0:
        for stat in lst[turn]:
            if stat.HasWon():
                won = True
            lst.append([])
            stat.LegalMoves()
            stat.Moves()
    #        stats.add(stat)
        #for stat in stats:
            lst[turn + 1] += f.AddNewStatuses(stat)
        print(len(lst[turn + 1]))
        turn += 1
    return turn

def PrintStatuses(turn,lst):
    print(f"\nStatuses after {turn} turns:")
    turnNr = turn
    for index in range(len(lst[turnNr])):
        print(lst[turnNr][index].Show())


#TODO: Clean up
def main():
    printAll = 0
    tubes = TestTubes2_1()
    CheckValidityTubes(tubes)
    lst = []
    initialStatus = MakeStatus(tubes)
    f = Status.field(initialStatus)
    lst.append([initialStatus])
    initialStatus.LegalMoves()
    initialStatus.Moves()
    lst.append(f.AddNewStatuses(initialStatus))

#    print(f.statuses)

#    stats = set()
#    for turn in range(13):

    print("Number of new statuses each turn:")
    turn = Run(lst,f)
    #TODO: lst has lots of empty elements
    print(f"Finished in {turn - 1} turns.")

    if printAll:
        for turnNr in range(turn):
            PrintStatuses(turnNr,lst)
    else:
        PrintStatuses(turn - 1,lst)


if __name__ == "__main__":
    main()
