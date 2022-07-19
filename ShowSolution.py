from typing import Counter


def FindPreviousStatus(allStatuses: list,status,turn):
    for previousStatus in allStatuses[turn - 1]:
        if status in previousStatus.newStatuses:
            return previousStatus
    if status in allStatuses[turn]:
        raise Exception(f"Previous status not found: turn {turn}.")
    else:
        raise Exception(f"Current status not found: turn {turn}.")

def FindUnsortedMove(unsortedStat,nextStat):
    unsortedStatShow = unsortedStat.Show()
    c1 = Counter(unsortedStatShow)
    c2 = Counter(nextStat.Show())
    oldLyfoes = list((c1 - c2).elements())
    newLyfoes = list((c2 - c1).elements())
    if len(oldLyfoes) != 2:
        raise Exception("Difference between old and new status is wrong.")
    if oldLyfoes[0][:-1] in newLyfoes:
        frm = oldLyfoes[0]
        to = oldLyfoes[1]
    else:
        frm = oldLyfoes[1]
        to = oldLyfoes[0]
    for index in range(len(unsortedStatShow)):
        if frm == unsortedStatShow[index]:
            frmIndex = index
        elif to == unsortedStatShow[index]:       #TODO: fails if frm == to
            toIndex = index
    return frmIndex,toIndex
        

def FindNextUnsortedStatus(unsortedStat,move):
    unsortedStat.Move(move)
