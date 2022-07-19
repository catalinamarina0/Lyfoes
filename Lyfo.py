import Queue

class lyfo:
    def __init__(self,tube):
        self.storage = Queue.lifo(4)
        for ball in tube:
            self.storage.Put(ball)
        tube_set = set(self.storage.queue)
        self.nrColors = len(tube_set)
        self.finished = False
        self.Finished()
    
    def CanGetFrom(self):
        if self.storage.Empty():
            return False
        elif self.finished:
            return False
        else:
            return True

    #TODO: Kees vindt single point of return beter.
    def CanPutInto(self,ball):
        if self.storage.Full():
            return False
        elif ball == self.storage.Peek():
            return True
        elif self.storage.Empty():
            return True
        else:
            return False

    def MoveBall(frm,to):
        if frm.finished:
            raise Exception("Illegal move: Lyfo is finished.")
        ball = frm.storage.Get()
        if not to.CanPutInto(ball):
            raise Exception(f"Illegal move: Can't put ball '{ball}' in lyfo '{to.Show()}'.")
        else:
            to.storage.Put(ball)
        if to.nrColors == 0:
            to.nrColors += 1
        if not ball in frm.storage.Show():
            frm.nrColors -= 1
        to.Finished()

    def Finished(self):
        if self.nrColors == 1 and self.storage.Full():
            self.finished = True
        return self.finished
    
    def Peek(self):
        return self.storage.Peek()

    def Show(self):
        lst = self.storage.Show()
        string = ""
        for element in lst:
            string += element
        return string

    def Equals(self,other):
        return self.storage.Equals(other.storage)