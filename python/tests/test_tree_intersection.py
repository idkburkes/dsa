import pytest
from code_challenges.trees.trees import BinaryTree
from code_challenges.trees.trees import Node
from code_challenges.tree_intersection.tree_intersection import tree_intersection



def test_tree_intersection(tree_populated1, tree_populated2):

    actual = tree_intersection(tree_populated1, tree_populated2)
    expected = {5, 200, 75} 
    diff = actual.difference(expected)
    assert len(diff) == 0


def test_empty_tree(tree_populated1):

    empty_tree = BinaryTree()
    actual = tree_intersection(tree_populated1, empty_tree)
    expected = {}
    assert actual == expected


@pytest.fixture
def tree_populated1():
    tree = BinaryTree(100)
    #
    #           (100)
    #          /      \
    #       (50)     (200)
    #      /    \     /   
    #    (25)  (75) (5)
    #

    # Left Subtree
    tree.root.left = Node(50)
    tree.root.left.left = Node(25)
    tree.root.left.right = Node(75)

    # Right Subtree
    tree.root.right = Node(200)
    tree.root.right.left = Node(5)
    return tree

@pytest.fixture
def tree_populated2():
    tree = BinaryTree(2)
    #
    #           (2)
    #         /     \
    #       (7)      (5)
    #     /    \        \   
    #   (200)    (6)       (9)
    #         /   \     /
    #       (5)  (11)  (75)

    # Left Subtree
    tree.root.left = Node(7)
    tree.root.left.left = Node(200)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)

    # Right Subtree
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(75)
    return tree