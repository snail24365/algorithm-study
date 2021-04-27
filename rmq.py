"""
구간 트리 (range minimum query, RMQ)
minimum을 maximum 등등으로 바꿀 수 있음. 합병이 가능한 모든 함수
"""


class RMQ:
    def __init__(self, lst):
        n = len(lst)
        self.n = n
        self.lst = lst
        self.range_min = [0] * (n * 4)
        self.init(0, n-1, 1)

    def init(self, left, right, node):
        if left == right:
            self.range_min[node] = self.lst[left]
            return self.range_min[node]
        mid = (left + right) // 2
        left_min = self.init(left, mid, node * 2)
        right_min = self.init(mid + 1, right, node * 2 + 1)
        self.range_min[node] = min(left_min, right_min)
        return self.range_min[node]

    def query(self, left, right):
        return self.query(left, right, 1, 0, self.n - 1)

    def query(self, left, right, node, node_left, node_right):
        if left == node_left and right == node_right:
            return self.range_min[node]
        if node_left > right or node_right < left:
            return float('inf')
        mid = (node_left + node_right) // 2
        return min(self.query(left, right, node * 2, node_left, mid),
                   self.query(left, right, node * 2 + 1, mid + 1, node_right))

    def update(self, index, new_value):
        return self.update(index, new_value, 1, 0, self.n-1)

    def update(self, index, new_value, node, node_left, node_right):
        if index < node_left or node_right < index:
            return self.range_min[node]

        if node_left == node_right:
            self.range_min[node] = new_value
            return self.range_min[node]

        mid = (node_left + node_right) // 2
        self.range_min[node] = min(self.update(index, new_value, node*2, node_left, mid),
                                   self.update(index, new_value, node*2+1, mid + 1, node_right))
        return self.range_min[node]

