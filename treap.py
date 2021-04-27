import random


class Treap:
    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.size = 1
        self.value = value
        self.priority = random.random()

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, val):
        self.__right = val
        self.calc_size()

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, val):
        self.__left = val
        self.calc_size()

    def calc_size(self):
        left_size = self.left.size if self.left else 0
        right_size = self.right.size if self.right else 0
        self.size = 1 + left_size + right_size

    def print_priority(self):
        print(self.priority)
        if self.left:
            self.left.print_priority()
        if self.right:
            self.right.print_priority()

    def print_preorder(self):
        print(self.value)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.value)
        if self.right:
            self.right.print_inorder()

    def insert(self, treap):
        if treap.priority > self.priority:
            less, greater = self.split(treap.value)
            treap.left = less
            treap.right = greater
            return treap

        if treap.value <= self.value:
            self.left = self.left.insert(treap) if self.left else treap
        else:
            self.right = self.right.insert(treap) if self.right else treap

        return self

    def split(self, priority):
        if self.priority <= priority:
            right_less, right_greater = self.right.split(priority) if self.right else (None, None)
            self.right = right_less
            return self, right_greater

        left_less, left_greater = self.left.split(priority) if self.left else (None, None)
        self.left = left_greater
        return left_less, self

    @classmethod
    def erase(cls, node, key):
        if not node:
            return None

        if node.value == key:
            new_node = cls.merge(node.left, node.right)
            del node
            return new_node

        if key < node.value:
            node.left = cls.erase(node.left, key)
        else:
            node.right = cls.erase(node.right, key)
        return node

    @classmethod
    def merge(cls, treap1, treap2):
        if not treap1:
            return treap2

        if not treap2:
            return treap1

        if treap1.priority < treap2.priority:
            treap2.left = treap1
            treap2.right = cls.merge(treap2.left, treap2.right)
            return treap2

        treap1.right = treap2
        treap1.left = cls.merge(treap1.left, treap1.right)
        return treap1

    def kth(self, k):
        left_size = self.left.size if self.left else 0
        if k == left_size + 1:
            return self
        if k <= left_size:
            return self.left.kth(k)
        return self.right.kth(k - left_size - 1)

    def count_less_than(self, key):
        if not self:
            return 0
        if self.value < key:
            left_size = self.left.size if self.left else 0
            return 1 + left_size + self.right.count_less_than(key)
        return self.left.count_less_than(key)


root = Treap(1)
for i in range(2, 10):
    root = root.insert(Treap(i))

root.print_preorder()
print("=" * 20)
#new_root = Treap.erase(root, 5)
#new_root.print_preorder()
print(root.kth(4).value)

