class lifo:
    def __init__(self,maxsize):
        self.queue = []
        self.maxsize = maxsize

    def Qsize(self):
        return len(self.queue)

    def Put(self, item):
        if not self.Full():
            self.queue.append(item)
        else:
            print("Error: Queue is full.")      #TODO: Exception

    def Get(self):
        if not self.Empty():
            return self.queue.pop()
        else:
            print("Error: Queue is empty.")     #TODO: Exception

    def Empty(self):
        return self.Qsize() == 0

    def Full(self):
        return self.Qsize() == self.maxsize
    
    def Peek(self):
        if not self.Empty():
            return self.queue[-1]
        else:
            return None
    
    def Show(self):
        return self.queue

    def Equals(self,other):
        return self.queue == other.queue