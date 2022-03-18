from code_challenges.hashtable.hashtable import HashTable
from code_challenges.trees.trees import BinaryTree



def tree_intersection(tree1: BinaryTree, tree2: BinaryTree) -> set:    
    if tree1.root is None or tree2.root is None:
        # There is no intersection if either tree is empty
        return set()

    hashtable = HashTable()
    intersection = set()
    # Traverse first tree and place all values in hashtable
    stack = []
    node = tree1.root
    # iterative in-order traversal
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        # implementation only currently handles strings as a key
        hashtable.set(str(node.val), node)
        node = node.right
    
    stack = []
    node = tree2.root
    # iterative in-order traversal
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if hashtable.contains(str(node.val)):
            intersection.add(node.val)
        node = node.right
    
    return intersection

    


    


