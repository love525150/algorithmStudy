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

    def put(self, key, value):
        node = self.Node(key, value)
        if self.is_empty():
            self.root = node
            return

        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
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

    def delete(self, key):
        self.root = self._delete_node(key, self.root)

    def _delete_node(self, key, node):
        """节点删除的实现异常难理解：
        这个方法本身是递归调用的，方法返回被删除节点的位置替代节点（因为涉及被删节点子树保留的问题，不能单纯把被删节点置空），
        如果入参节点不是被删节点，则返回入参节点自身（相当于不是被删节点，就用自己代替自己）
        当入参是被删节点时，有以下几种情况：
        1. 被删节点左右子树都没有，则用“空”作为替代节点
        2. 被删节点只有左（或右）子树，则用左（或右）子树作为替代节点
        3. 被删节点左右子树都存在，这个时候是最trick的：
            第一步：从左子树从找出最大值的节点，其值作为用于替代节点的值
            第二步：把入参节点的值改为第一步中找到的值，（注意了，这时整棵树里需删节点的值已经没了，而替代值的节点有2个，一个是本节点，另一个在左子树里）
            第三步：递归调用本方法，在左子树中把替代值的节点删除（把多出来的那个节点删掉）
            这里可以看出，实际上并没有直接用左子树中最大的节点去代替被删节点，而是把那个节点的值覆盖到该位置的节点，然后把多余另一个节点删除，
            因为直接代替会导致原位置子树的错乱，所以只是进行了值的拷贝来替代
            （使用右子树的最小值去代替也是可以的）
        """
        replacement = node
        if node is None:
            return replacement

        if key < node.key:
            node.left = self._delete_node(key, node.left)
        elif key > node.key:
            node.right = self._delete_node(key, node.right)
        else:
            if node.left is None and node.right is None:
                replacement = None
            elif node.left is not None and node.right is None:
                replacement = node.left
            elif node.right is not None and node.left is None:
                replacement = node.right
            else:
                replaced_delete_node = self._find_max_node(node.left)
                replacement.key = replaced_delete_node.key
                replacement.value = replaced_delete_node.value
                node.left = self._delete_node(replaced_delete_node.key, node.left)

        return replacement

    def get(self, key):
        node = self._get_node(key)
        return node.value if node is not None else None

    def _get_node(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return current_node

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None

    def max_key(self):
        max_node = self._find_max_node(self.root)
        return max_node.key if max_node is not None else None

    def _find_max_node(self, node):
        """右子树上最右的节点就是值最大的节点"""
        if node is None:
            return None

        max_node = node
        while max_node.right is not None:
            max_node = max_node.right

        return max_node

    def _find_min_node(self, node):
        """左子树上最左的节点就是值最小的节点"""
        if node is None:
            return None

        min_node = node
        while min_node.left is not None:
            min_node = min_node.left

        return min_node

    def min_key(self):
        min_node = self._find_min_node(self.root)
        return min_node.key if min_node is not None else None

    def is_empty(self):
        return self.root is None

    def range(self, lo, high):
        result = []
        self._range(self.root, lo, high, result)
        return result

    def _range(self, node, lo, high, _list):
        """使用中序遍历，这样可以保证节点值进入列表时是按序的"""
        if node is None:
            return
        
        if node.key > lo: #如果node <= lo，则node的左子树都比lo小，不用再去左子树里面遍历了，这里是取反了
            self._range(node.left, lo, high, _list)
        
        if node.key >= lo and node.key <= high:
            _list.append(node.key)
        
        if node.key < high:
            self._range(node.right, lo, high, _list)

    class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None


class RedBlackTree(BinarySearchTree):
    """红黑树，也是标准的二叉搜索树，树中的链接分为两种，红链接将两个2-节点连接起来构成一个3-节点，黑连接则是2-3树中的普通链接
    满足下列条件：
    1. 红链接均为左链接
    2. 没有任何一个节点同时和两条红链接相连
    3. 该树是完美黑色平衡的，即任意空链接到根节点的路径上的黑链接数量相同
    
    实现的理论来源是2-3树，是用二叉搜索树模拟2-3的实现。
    因为是标准的二叉搜索树，所以，二叉树的所有api实现都是能够使用的（除了插入删除时逻辑不同）
    """
    RED = "RED"
    BLACK = "BLACK"

    def __init__(self):
        BinarySearchTree.__init__(self)

    class Node:
        def __init__(self, key, value, color):
            self.key = key
            self.value = value
            self.color = color
            self.left = None
            self.right = None

    def is_red(self, node):
        if node is None:
            return False
        return node.color == RedBlackTree.RED

    def rotate_left(self, node):
        """左旋转，将右边的红链接转到左边"""
        replacement = node.right
        node.right = replacement.left
        replacement.left = node
        replacement.color = node.color
        node.color = RedBlackTree.RED
        # 下面是精髓，把replacement node作为返回值返回，这样指向node的那个引用在本方法结束之后就能指向replacement node
        return replacement

    def rotate_right(self, node):
        """右旋转，将左边的红链接转到右边"""
        replacement = node.left
        node.left = replacement.right
        replacement.right = node
        replacement.color = node.color
        node.color = RedBlackTree.RED
        # 下面是精髓，把replacement node作为返回值返回，这样指向node的那个引用在本方法结束之后就能指向replacement node
        return replacement

    def flip_colors(self, node):
        """当节点左右两边链接都是红色的时候调用"""
        node.color = RedBlackTree.RED
        node.left.color = RedBlackTree.BLACK
        node.right.color = RedBlackTree.BLACK

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = RedBlackTree.BLACK

    def _put(self, node, key, value):
        replacement = node
        if node is None:
            # 新插入节点是红链接
            return self.Node(key, value, RedBlackTree.RED)

        if key < node.key:
            # 在node的左边
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            # 在node的右边
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        # 插入完后递归向上检查父节点，看看是否需要作出调整，这里是红黑树保持平衡的关键
        # 三个判断的顺序不能乱，因为是有可能连续满足的
        if self.is_red(node.right) and not self.is_red(node.left):
            replacement = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            replacement = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        # 返回一个替代的节点给父节点引用，没有发生旋转的话就是原来的节点
        return replacement



# tree = BinarySearchTree()
# tree.put(2, "tow")
# tree.put(1, "one")
# tree.put(3, "three")
# tree.put(0, "zero")
# tree.put(1.5, "tow.five")
#
# print(tree.get(0))
# print(tree.get(8))
# print(tree.max_key())
# print(tree.min_key())
#
# tree.delete(2)
# print(tree.min_key())
# tree.delete(0)
# print(tree.min_key())
# tree.delete(1)
# print(tree.min_key())

tree = RedBlackTree()
tree.put(1, "1")
tree.put(2, "2")
tree.put(3, "3")
tree.put(4, "4")
tree.put(5, "5")
tree.put(6, "6")
tree.put(7, "7")
tree.put(8, "8")

print(tree.get(1))
print(tree.get(9))
print(tree.max_key())
print(tree.min_key())
print(tree.root.key)
