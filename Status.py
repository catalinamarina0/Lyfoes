from Lyfo import lyfo
import copy
import operator

class status:
    def __init__(self,tubes):
        self.lyfoes = [lyfo(tube) for tube in tubes]
        self.ConvertToString()
#        self.nrLyfoes = len(self.lyfoes)        #TODO: What is this for?
    
    #TODO: Refer to SameColorDifferentLyfo?
    def IsLegalMove(self,frmIndex,toIndex):
        return (frmIndex != toIndex 
                and self.lyfoes[frmIndex].CanGetFrom() 
                and self.lyfoes[toIndex].CanPutInto(self.lyfoes[frmIndex].Peek()))

    def LegalMoves(self):
        "Generate a set of all legal moves."
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
        
    def SameColorDifferentLyfo(self, move: tuple):
        if self.lyfoes[move[1]].storage.Empty():    #TODO: Private
            ball = self.lyfoes[move[0]].Peek()
            for lyfoe in self.lyfoes:
                if lyfoe.nrColors == 1:     #TODO: Private
                    if ball == lyfoe.Peek():
                        return True
        return False

    def Moves(self):
        "Generates all statuses one move away from the current status."
        newStatuses = []
        for move in self.moves:
            if not self.SameColorDifferentLyfo(move):
                stat = self.Copy()
                stat.Move(move)
                stat.Sort()
                stat.ConvertToString()      #TODO? Is copied to new statuses, but subsequently overwritten.
                newStatuses.append(stat)
        self.newStatuses = newStatuses

    def NewStatuses(self):
        return self.newStatuses

    def Sort(self):
        self.lyfoes.sort(key=operator.attrgetter('storage.queue'))  #TODO: Private

    def ConvertToString(self):
        string = ""
        for lyfoe in self.lyfoes:
            s = lyfoe.Show()
            string += s + (4 - len(s)) * " "
        self.string = string

    def String(self):
        return self.string

#TODO: No longer used
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
        self.statuses = {stat.String()}
        stat.Sort()

    def AddStatus(self,stat: status):
        self.statuses.add(stat.String())

    def IsNewStatus(self,newStat: status):
        return not newStat.String() in self.statuses

    #TODO: Make comprehensive
    def AddNewStatuses(self,stat: status):
        lst = []
        newStatuses = stat.NewStatuses()
        for newStatus in newStatuses:
            if self.IsNewStatus(newStatus):
                self.AddStatus(newStatus)
                lst.append(newStatus)
        return lst
