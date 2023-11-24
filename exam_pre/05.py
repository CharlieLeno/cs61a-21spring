"""Q1: Node Printer"""
def node_printer(t):
    """
    >>> t1 = tree(1, [tree(2,
    ...                   [tree(5),
    ...                    tree(6, [tree(8)])]),
    ...               tree(3),
    ...               tree(4, [tree(7)])])
    >>> printer = node_printer(t1)
    >>> for _ in range(8):
    ...     printer()
    1
    2
    3
    4
    5
    6
    7
    8
    """
    to_explore = [t]
    def step():
        node = to_explore.pop(0)
        print(label(node))
        for branch in branches(node):
            if branch:
                to_explore.append(branch)
    return step


"""Q2: Fibonacci Generator"""
def fib_gen():
    """
    >>> fg = fib_gen()
    >>> for _ in range(7):
    ...     print(next(fg))
    0
    1
    1
    2
    3
    5
    8
    """
    def helper(m, n):
        a = m + n
        yield m
        yield from helper(n, a)
    yield from helper(0, 1)
    """TBD
    yield from __________________________________
    a = __________________________________________
    ______________________________________________
    for x, y in __________________________________:
        ___________________________________________
    """
    
    """iterative function"""
    """
    a, b = 0, 1
    while True:
        yield a
        temp = a + b
        a = b
        b = temp
    """

"""Q3: Partition Generator"""
def partition_gen(n):
    """
    >>> for partition in partition_gen(4): # note: order doesn't matter
    ...     print(partition)
    [4]
    [3, 1]
    [2, 2]
    [2, 1, 1]
    [1, 1, 1, 1]
    """
    def yield_helper(j, k):
        if j == 0:
            yield []
        elif j > 0 and k > 0:
            for small_part in yield_helper(j - k, k):
                yield [k] + small_part
            yield from yield_helper(j, k - 1)

    yield from yield_helper(n, n)


"""Q4: Apply That Again"""
def amplify(f, x):
    """Yield the longest sequence x, f(x), f(f(x)), ... that are all true values

    >>> list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    """
    "*** YOUR CODE HERE ***"
    if not x:
        return
    yield x
    yield from amplify(f, f(x))




# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
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
