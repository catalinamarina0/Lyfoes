from Lyfo import lyfo
import copy
import operator

class status:
    def __init__(self,tubes):
        self.lyfoes = [lyfo(tube) for tube in tubes]
        self.Sort()
        self.nrLyfoes = len(self.lyfoes)
    
    def IsLegalMove(self,frmIndex,toIndex):
        return (frmIndex != toIndex 
                and self.lyfoes[frmIndex].CanGetFrom() 
                and self.lyfoes[toIndex].CanPutInto(self.lyfoes[frmIndex].Peek()))

    def LegalMoves(self):
        self.moves = {(frmIndex,toIndex) for frmIndex in range(len(self.lyfoes)) 
                    for toIndex in range(len(self.lyfoes)) 
                    if self.IsLegalMove(frmIndex,toIndex)}

    def Move(self,move: tuple):
        "move = (frmIndex,toIndex)"
        frmIndex = move[0]
        toIndex = move[1]
        self.lyfoes[frmIndex].MoveBall(self.lyfoes[toIndex])
    
    def Copy(self):
        return copy.deepcopy(self)
        
    def Moves(self):
        "Generates all statuses one move away from the current status."
        self.newStatuses = []
        for move in self.moves:
            stat = self.Copy()
            stat.Move(move)
            stat.Sort()
            self.newStatuses.append(stat)

    def NewStatuses(self):
        return self.newStatuses

    def Sort(self):
        self.lyfoes.sort(key=operator.attrgetter('storage.queue'))  #TODO: Private

    def Equals(self,other):
        for lyfoIndex in range(len(self.lyfoes)):
            if not self.lyfoes[lyfoIndex].Equals(other.lyfoes[lyfoIndex]):
                return False
        return True
            
    def HasWon(self):
        for lyfoe in self.lyfoes:
            if lyfoe.CanGetFrom():
                return False
        return True
    
    def Show(self):
        lst = []
        for lyfoe in self.lyfoes:
            lst.append(lyfoe.Show())
        return lst

class field:
    "A field is a collection of all statuses thusfar encountered."
    def __init__(self,stat: status):
        self.statuses = {stat}

    def AddStatus(self,stat: status):
        self.statuses.add(stat)

    def IsNewStatus(self,newStat: status):
        for stat in self.statuses:
            if stat.Equals(newStat):
                return False
        return True

    def AddNewStatuses(self,stat: status):
        lst = []
        newStatuses = stat.NewStatuses()
        for newStatus in newStatuses:
            if self.IsNewStatus(newStatus):
                self.AddStatus(newStatus)
                lst.append(newStatus)
        return lst

    


