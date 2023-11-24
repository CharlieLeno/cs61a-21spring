"""Q1: Keep Ints"""
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <= n:
        if cond(i) == True:
            print(i)
        i = i + 1

"""Q2: (Tutorial) Make Keeper"""
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.
        >>> def is_even(x):
        ...     # Even numbers have remainder 0 when divided by 2.
        ...     return x % 2 == 0
        >>> make_keeper(5)(is_even)
        2
        4
    """
    def func(cond):
        i = 1
        while i <= n:
            if cond(i) == True:
                print(i)
            i = i + 1
        return None
    return func

"""Q7: (Tutorial) Warm Up: Make Keeper Redux"""
def make_keeper_redux(n):
    """Returns a function. This function takes one parameter <cond> and prints out
       all integers 1..i..n where calling cond(i) returns True. The returned
       function returns another function with the exact same behavior.

        >>> def multiple_of_4(x):
        ...     return x % 4 == 0
        >>> def ends_with_1(x):
        ...     return x % 10 == 1
        >>> k = make_keeper_redux(11)(multiple_of_4)
        4
        8
        >>> k = k(ends_with_1)
        1
        11
        >>> k
        <function do_keep>
    """
    def do_keep(cond):
        i = 1
        while i <= n:
            if cond(i) == True:
                print(i)
            i = i + 1
        return do_keep
    return do_keep

"""Q8: Print Delayed"""
def print_delayed(x):
    """Return a new function. This new function, when called, will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi") # a function is returned
    5
    <function delay_print>
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

"""Q9: (Tutorial) Print N"""
def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print