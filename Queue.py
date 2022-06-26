class lifo:
    def __init__(self,maxsize):
        self.queue = []
        self.maxsize = maxsize

    def qsize(self):
        return len(self.queue)

    def put(self, item):
        if not self.full():
            self.queue.append(item)
        else:
            print("Error: Queue is full.")

    def get(self):
        if not self.empty():
            return self.queue.pop()
        else:
            print("Error: Queue is empty.")

    def empty(self):
        return self.qsize() == 0

    def full(self):
        return self.qsize() == self.maxsize
    
    def peek(self):
        return self.queue[-1]