from Lyfo import lyfo
import copy

class status:
    def __init__(self,tubes):
        self.lyfoes = [lyfo(tube) for tube in tubes]
        self.nrLyfoes = len(self.lyfoes)
    
    def Removable(self):
        self.removable = [frm for frm in self.lyfoes if frm.CanGetFrom()]

    def MovableTo(self,ball):
        return [to for to in self.lyfoes if to.CanPutInto(ball)]

    def IsLegalMove(self,frmIndex,toIndex):
        return (frmIndex != toIndex 
                and self.lyfoes[frmIndex].CanGetFrom() 
                and self.lyfoes[toIndex].CanPutInto(self.lyfoes[frmIndex].Peek()))

    #TODO: Bypasses the functions Removable() and MovableTo(). Delete?
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
            self.newStatuses.append(stat)

    #TODO: Not exactly what I want, but it'll do for now.
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
        for newStatus in stat.newStatuses:    #TODO: Private
            if self.IsNewStatus(newStatus):
                self.AddStatus(newStatus)
                lst.append(newStatus)
        return lst

    


