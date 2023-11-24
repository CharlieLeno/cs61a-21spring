# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def change_abstraction(change):
    change_abstraction.changed = change


change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])







"""Q1: Perfectly Balanced and Pruned"""
def sum_tree(t):
    """
    Add all elements in a tree.

    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    if is_leaf(t):
        return label(t)
    return label(t) + sum([sum_tree(branch) for branch in branches(t)])

def balanced(t):
    """
    Checks if each branch has same sum of all elements,
    and each branch is balanced.

    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(t, [t, tree(1)])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if len(branches(t)) <= 1:
        return True
    sum_list = [sum_tree(branch) for branch in branches(t)]
    if len(set(sum_list)) == 1:
        return True
    return False
    

def prune_tree(t, predicate):
    """
    Returns a new tree where any branch that has the predicate of the label
    of the branch returns True has its branches pruned.

    >>> prune_tree(tree(1, [tree(2)]), lambda x: x == 1) # prune at root
    [1]
    >>> prune_tree(tree(1, [tree(2)]), lambda x: x == 2) # prune at leaf
    [1, [2]]
    >>> prune_tree(test_tree, lambda x: x >= 3) # prune at 3, 4, and 5
    [1, [2, [4], [5]], [3]]
    >>> sum_tree(prune_tree(test_tree, lambda x: x > 10)) # prune nothing, add 1 to 9
    45
    >>> prune_tree(test_tree, lambda x: x > 10) == test_tree # prune nothing
    True
    """
    "*** YOUR CODE HERE ***"
    if predicate(label(t)):
        return tree(label(t))
    return tree(label(t), [prune_tree(branch, predicate) for branch in branches(t)])


test_tree = tree(1,
                [tree(2,
                    [tree(4,
                        [tree(8),
                            tree(9)]),
                    tree(5)]),
                tree(3,
                    [tree(6),
                    tree(7)])])
#TBD draw(test_tree)


"""Q2: Closest - Spring 2015 Midterm 2 Q3(c)"""
def closest(t):
    """ Return the smallest difference between an entry and the sum of the
    root entries of its branches .
    >>> t = tree(8 , [tree(4), tree(3)])
    >>> closest(t) # |8 - (4 + 3)| = 1
    1
    >>> closest(tree(5, [t])) # Same minimum as t
    1
    >>> closest(tree(10, [tree(2), t])) # |10 - (2 + 8)| = 0
    0
    >>> closest(tree(3)) # |3 - 0| = 3
    3
    >>> closest(tree(8, [tree(3, [tree(1, [tree(5)])])])) # 3 - 1 = 2
    2
    >>> sum([])
    0
    """
    diff = abs(label(t) - sum([label(branch) for branch in branches(t)]))
    return min([diff] + [closest(branch) for branch in branches(t)])



"""Q3: Recursion on Tree ADT - Summer 2014 Midterm 1 Q7"""
def dejavu(t, n):
    """
    >>> my_tree = tree(2, [tree(3, [tree(5), tree(7)]), tree(4)])
    >>> dejavu(my_tree, 12) # 2 -> 3 -> 7
    True
    >>> dejavu(my_tree, 5) # Sums of partial paths like 2 -> 3 don ’t count
    False
    """
    if is_leaf(t):
        return label(t) == n
    for branch in branches(t):
        if dejavu(branch, n - label(t)):
            return True
    return False



"""Q4: Forest Path - Fall 2015 Final Q3 (a)(b)(d)"""
def reduce(f, s, initial):
    """Combine elements of s pairwise
    using f, starting with initial.

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [2, 3, 1], 2)
    64
    """
    for x in s:
        initial = f(initial, x)
    return initial

# The one function defined below is used in the questions below 
# to convert truthy and falsy values into the numbers 1 and 0, respectively.
def one(b):
    if b:
        return 1
    else:
        return 0

def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    3
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    if is_leaf(t):
        return one(label(t) >= n)
    return sum([bigpath(branch, n - label(t)) for branch in branches(t)])

def allpath(t, f, g, s):
    """ Return the number of paths p in t for which f(reduce(g, p, s)) is truthy.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> even = lambda x: x % 2 == 0
    >>> allpath(t, even, max, 0) # Path maxes are 2, 4, and 5
    2
    >>> allpath(t, even, pow, 2) # E.g., pow(pow(2, 1), 2) is even
    3
    >>> allpath(t, even, pow, 1) # Raising 1 to any power is odd
    0
    """
    if is_leaf(t):
        return one(f(reduce(g, t, s)))
    return sum([allpath(branch, f, g, s) for branch in branches(t)])

from operator import add , mul

def bigpath_allpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath_allpath(t, 3)
    3
    >>> bigpath_allpath(t, 6)
    2
    >>> bigpath_allpath(t, 9)
    1
    """
    return allpath(t, lambda x: label(t) >= x, lambda x, y: x - y, n + label(t))






