import Status
#from Lyfo import lyfo

def TestTubes():
    t1 = "ryby"
    t2 = "rrbb"
    t3 = "bryy"
    t4 = ""
    t5 = ""
    return t1,t2,t3,t4,t5

def MakeStatus(tubes):
    stat = Status.status(tubes)
    return stat




#TODO: Clean up
def main():
    tubes = TestTubes()
    initialStatus = MakeStatus(tubes)
    initialStatus.LegalMoves()
    initialStatus.Moves()
    f = Status.field(initialStatus)
    lst = []
    lst.append(f.AddNewStatuses(initialStatus))

#    print(f.statuses)

#    stats = set()
#    for turn in range(13):
    turn = 0
    won = 0
    print("Number of new statuses each turn:")
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
    print(f"Finished in {turn} turns.")

#    print(f.statuses)
    print("Statuses of last turn:")
    turnNr = turn - 1
    for index in range(len(lst[turnNr])):
        print(lst[turnNr][index].Show())
    #print(stat.lyfoes[0].storage.queue)


if __name__ == "__main__":
    main()
