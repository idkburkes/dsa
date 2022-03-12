
class Node:
    def __init__(self, val, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self,root=None):
        if root is not None:
            self.root = Node(root)
        else:
            self.root = None

    def pre_order(self):
        if not self.root:
            raise Exception('There is no root node in this tree.')
        def traverse(root, list):
            if root:
                list.append(root.val)
                traverse(root.left, list)
                traverse(root.right, list)
        res = []
        traverse(self.root, res)
        return res
             
    def post_order(self):
        if not self.root:
            raise Exception('There is no root node in this tree.')
        def traverse(root, list):
            if root:
                traverse(root.left, list)
                traverse(root.right, list)
                list.append(root.val)        
        res = []
        traverse(self.root, res)
        return res

    def in_order(self):
        if not self.root:
            raise Exception('There is no root node in this tree.')
        def traverse(root, list):
            if root:
                traverse(root.left, list)
                list.append(root.val)
                traverse(root.right, list)        
        res = []
        traverse(self.root, res)
        return res

    # This is my iterative in-order traversal solution
    def find_max(self):
        if self.root is None: 
            raise Exception('Tree has no root node.')
        stack, node, maxnum = [], self.root, float('-inf')
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            maxnum = max(node.val, maxnum)
            node = node.right
        return maxnum

    def breadth_first(tree):
        if tree.root is None:
            raise Exception('Tree has no root node.')
        queue, res = [tree.root], []
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                res.append(node.val)
        return res
    
                 
class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        BinaryTree.__init__(self, root)

    def add(self, new_val):
        if self.root is None:
            self.root = Node(new_val)
            return

        node = self.root
        while node.val != new_val:
            if node.left is None and new_val < node.val:
                node.left = Node(new_val)
                node = node.left
            elif node.right is None and new_val > node.val:
                node.right = Node(new_val)
                node = node.right
            elif node.left and new_val < node.val:
                node = node.left
            elif node.right and new_val > node.val:
                node = node.right



    def contains(self, target):
        if target is None:
            raise Exception('Target can\'t be None')
        node = self.root
        while node:
            if node.val == target:
                return True
            elif node.val > target:
                node = node.left
            else:
                node = node.right
        return False        

    

    
    


