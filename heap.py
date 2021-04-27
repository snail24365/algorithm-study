class Heap:
    def __init__(self):
        self.data = []

    @staticmethod
    def parent_idx(index):
        return (index - 1) // 2

    def print(self):
        for datum in self.data:
            print(datum)

    def pop_heap(self):
        if len(self.data) == 0:
            return None
        ret = self.data[0]
        min_idx = len(self.data) - 1
        self.data[min_idx] = ret

    def insert(self, node):
        self.data.append(node)
        self.normalize(len(self.data)-1)

    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp

    def normalize(self, idx):
        p_idx = Heap.parent_idx(idx)
        while idx > 0 and self.data[p_idx] < self.data[idx]:
            self.swap(idx, p_idx)
            idx = p_idx
            p_idx = Heap.parent_idx(idx)


heap = Heap()
line = [23,73,34,8,28,14,24,65,1]
for item in line:
    heap.insert(item)
heap.print()