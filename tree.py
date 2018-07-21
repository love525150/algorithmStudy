# -*- coding: utf-8 -*-


class MinHeap:
    """最小堆
    是一个完全二叉树，树及子树的根一定是树里面最小的元素
    添加或删除元素会通过上浮或下沉调整节点使得保持堆的定义
    由于是完全二叉树，使用数组实现会比较简单，数组索引0位置留空，从1开始使用，
    若节点的索引是k，则此节点的父节点是k/2，两个子节点是2k和2k+1"""

    def __init__(self, init_list=None):
        self.priority_queue = []
        self.priority_queue.append(None)
        if init_list is not None:
            for i in init_list:
                self.add(i)

    def add(self, element):
        self.priority_queue.append(element)
        self._swim(element, len(self.priority_queue) - 1)

    def _swim(self, element, current_index):
        parent_index = int(current_index / 2)
        while current_index != 1 and element < self.priority_queue[parent_index]:
            _switch_list_value(self.priority_queue, current_index, parent_index)
            current_index = parent_index
            parent_index = int(current_index / 2)

    def pop(self):
        pop_element = self.priority_queue[1]
        _switch_list_value(self.priority_queue, 1, len(self.priority_queue) - 1)
        self.priority_queue.pop()  # pop方法默认删除最后一个元素
        self._sink(1)
        return pop_element

    def _sink(self, current_index):
        child_index_1 = current_index * 2
        child_index_2 = current_index * 2 + 1
        last_index = len(self.priority_queue) - 1
        while child_index_1 <= last_index:
            if child_index_2 > last_index:
                smaller_child_index = child_index_1
            else:
                smaller_child_index = child_index_1 if self.priority_queue[child_index_1] < self.priority_queue[
                    child_index_2] else child_index_2

            if self.priority_queue[smaller_child_index] < self.priority_queue[current_index]:
                _switch_list_value(self.priority_queue, smaller_child_index, current_index)
                current_index = smaller_child_index
                child_index_1 = current_index * 2
                child_index_2 = current_index * 2 + 1
            else:
                break

    def size(self):
        return len(self.priority_queue) - 1


def _switch_list_value(list_, p1, p2):
    temp = list_[p1]
    list_[p1] = list_[p2]
    list_[p2] = temp


class BinarySearchTree:
    """二叉搜索树
    左子树的所有节点都比根节点小
    右子树的所有节点都比根节点大"""

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        self.size += 1
        node = self.Node(key, value)
        if self.root is None:
            self.root = node
            return

        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                self.size -= 1
                current_node.value = value
            elif key < current_node.key:
                if current_node.left is None:
                    current_node.left = node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = node
                    break
                else:
                    current_node = current_node.right

    def get(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return current_node.value

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None

    class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None


tree = BinarySearchTree()
tree.put(2, "tow")
tree.put(1, "one")
tree.put(3, "three")
tree.put(0, "zero")
tree.put(1.5, "tow.five")

print(tree.size)
print(tree.get(0))
print(tree.get(8))