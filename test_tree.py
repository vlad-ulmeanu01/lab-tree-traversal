from tree import Tree
import pytest
import random

def test_hi():
    assert(1 + 1 == 2)

def test_find1():
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)

    assert(not tree.find(69))
    assert(tree.find(2))
    assert(not tree.find(5))

def test_find2():
    tree = Tree()

    n = 10**4
    v = [i for i in range(1, n+1)]
    random.shuffle(v)
    
    for i in range(int(n // 2)):
        tree.add(v[i])

    for i in range(int(n // 2)):
        assert(tree.find(v[i]))

    for i in range(int(n // 2), n):
        assert(not tree.find(v[i]))
