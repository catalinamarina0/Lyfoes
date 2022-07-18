import Status
#from Lyfo import lyfo

def Config():
    printAll = 0
    tubes = TestTubes5_1()
    return printAll,tubes

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

def TestTubes4_1():     #42 turns
    t1 = "dayw"
    t2 = "aygb"
    t3 = "bpgr"
    t4 = "rypg"
    t5 = "arop"
    t6 = "dwwo"
    t7 = "bdol"
    t8 = "olap"
    t9 = "lgdl"
    t10 = "rbyw"
    t11 = ""
    t12 = ""
    return t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12

def TestTubes5_1():     #70 turns
    t1 = "lmpm"
    t2 = "lggm"
    t3 = "xpbe"
    t4 = "aorl"
    t5 = "zdwb"
    t6 = "rboy"
    t7 = "dwao"
    t8 = "otpz"
    t9 = "zbwx"
    t10 = "xyyp"
    t11 = "ltda"
    t12 = "edgy"
    t13 = "meae"
    t14 = "zxtr"
    t15 = "rwgt"
    t16 = ""
    t17 = ""
    return t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17

def CheckValidityTubes(tubes):
    nrBalls = {}
    for tube in tubes:
        for color in tube:
            if color in nrBalls:
                nrBalls[color] += 1
            else:
                nrBalls[color] = 1
    for color in nrBalls:
        if nrBalls[color] != 4:
            raise Exception(f"Wrong setup: {nrBalls[color]} balls have color '{color}'.")

def MakeStatus(tubes):
    stat = Status.status(tubes)
    return stat

#TODO: Clean up
def Run(lst: list,f: Status.field):
    turn = 0
    won = 0
    while won == False and len(lst[turn]) > 0:
        lst.append([])
        for stat in lst[turn]:
            if stat.HasWon():
                won = True
            stat.LegalMoves()
            stat.Moves()
    #        stats.add(stat)
        #for stat in stats:
            lst[turn + 1] += f.AddNewStatuses(stat)
        print(len(lst[turn + 1]))
        turn += 1
    return turn - 1

def PrintStatuses(turn,lst):
    print(f"\nStatuses after {turn} turns:")
    turnNr = turn
    for index in range(len(lst[turnNr])):
        print(lst[turnNr][index].Show())


#TODO: Clean up
def main():
    printAll, tubes = Config()
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
    print(f"Finished in {turn} turns.")

    if printAll:
        for turnNr in range(turn + 1):
            PrintStatuses(turnNr,lst)
    else:
        PrintStatuses(turn,lst)

if __name__ == "__main__":
    main()
