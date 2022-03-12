from code_challenges.trees.trees import BinaryTree, BinarySearchTree, Node
import pytest


def test_instantiate_empty_tree():
    tree = BinaryTree()
    assert tree.root is None

def test_tree_with_one_node():
    tree = BinaryTree(5)
    assert tree.root.val == 5

def test_add_left_child_to_bst():
    bst = BinarySearchTree(5)
    bst.add(1)
    assert bst.root.left and bst.root.left.val == 1

def test_add_root_node_to_bst():
    bst = BinarySearchTree()
    bst.add(100)
    actual = bst.root.val
    expected = 100
    assert expected == actual

def test_add_multiple_nodes_to_bst():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(7)
    bst.add(15)
    bst.add(9)
    bst.add(11)
    valid = bst.root.val == 10 and bst.root.left.val == 7 and bst.root.right.val == 15 and bst.root.left.right.val == 9 and bst.root.right.left.val == 11
    assert valid == True

def test_add_right_child_to_bst():
    bst = BinarySearchTree(10)
    bst.add(15)
    assert bst.root.right and bst.root.right.val == 15

def test_preorder_traversal(bst_populated):
    actual = bst_populated.pre_order()
    expected = [100,50,25,75,200,155]
    assert actual == expected

def test_preorder_traversal_on_empty_bst_raises_exception():
    with pytest.raises(Exception):
        bst = BinarySearchTree()
        bst.pre_order()

def test_postorder_traversal(bst_populated):
    actual = bst_populated.post_order()
    expected = [25,75,50,155,200,100]
    assert actual == expected

def test_postorder_traversal_on_empty_bst_raises_exception():
    with pytest.raises(Exception):
        bst = BinarySearchTree()
        bst.post_order()

def test_inorder_traversal(bst_populated):
    actual = bst_populated.in_order()
    expected = [25,50,75,100,155,200]
    assert actual == expected

def test_inorder_traversal_on_empty_bst_raises_exception():
    with pytest.raises(Exception):
        bst = BinarySearchTree()
        bst.in_order()

def test_bst_contains_value_is_present_in_left_subtree(bst_populated):
    actual = bst_populated.contains(75)
    expected = True
    assert actual == expected

def test_bst_contains_value_is_present_in_right_subtree(bst_populated):
    actual = bst_populated.contains(155)
    expected = True
    assert actual == expected

def test_bst_contains_value_is_root(bst_populated):
    actual = bst_populated.contains(100)
    expected = True
    assert actual == expected

def test_bst_contains_value_not_present(bst_populated):
    actual = bst_populated.contains(201)
    expected = False
    assert actual == expected

def test_bst_contains_value_is_none_raises_exception(bst_populated):
    with pytest.raises(Exception):
        actual = bst_populated.contains(None)


def test_tree_find_max(tree_populated):
    actual = tree_populated.find_max()
    expected = 11
    assert actual == expected

def test_tree_find_max_empty_tree():
    with pytest.raises(Exception):
        actual = BinaryTree().find_max()
        expected = 'We should not get this far'

def test_binary_tree_find_max(bst_populated):
    actual = bst_populated.find_max()
    expected = 200
    assert actual == expected

def test_tree_find_max_root_is_max(tree_populated):
    tree = tree_populated
    tree.root.val = 999
    actual = tree.find_max()
    expected = 999
    assert actual == expected

def test_tree_find_max_no_left_subtree(tree_populated):
    tree = tree_populated
    tree.root.left = None
    actual = tree.find_max()
    expected = 9
    assert actual == expected

def test_tree_breadth_first_search(tree_populated):
    tree = tree_populated
    actual = tree.breadth_first()
    expected = [2,7,5,2,6,9,5,11,4]
    assert actual == expected

def test_bst_breadth_first_search(bst_populated):
    tree = bst_populated
    actual = tree.breadth_first()
    expected = [100,50,200,25,75,155]
    assert actual == expected
    
def test_tree_breadth_first_with_no_root_raises_exception():
    with pytest.raises(Exception):
        tree = BinaryTree()
        tree.breadth_first()

def test_tree_breadth_first_with_one_node():
    tree = BinaryTree(5)
    actual = tree.breadth_first()
    expected = [5]
    assert actual == expected

def test_tree_breadth_first_with_two_nodes():
    tree = BinaryTree(5)
    tree.root.left = Node(10)
    actual = tree.breadth_first()
    expected = [5,10]
    assert actual == expected

def test_tree_breadth_first_tree_shaped_liked_linked_list():
    bst = BinarySearchTree(10)
    for i in range(9,4,-1):
        bst.add(i)
    actual = bst.breadth_first()
    expected = [10,9,8,7,6,5]
    assert actual == expected




@pytest.fixture
def bst_populated():
    tree = BinarySearchTree(100)
    #
    #           (100)
    #          /      \
    #       (50)     (200)
    #      /    \     /   
    #    (25)  (75) (155)
    #

    # Left Subtree
    tree.root.left = Node(50)
    tree.root.left.left = Node(25)
    tree.root.left.right = Node(75)

    # Right Subtree
    tree.root.right = Node(200)
    tree.root.right.left = Node(155)
    return tree

@pytest.fixture
def tree_populated():
    tree = BinaryTree(2)
    #
    #           (2)
    #         /     \
    #       (7)      (5)
    #     /    \        \   
    #   (2)    (6)       (9)
    #         /   \     /
    #       (5)  (11)  (4)

    # Left Subtree
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)

    # Right Subtree
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    return tree




    
