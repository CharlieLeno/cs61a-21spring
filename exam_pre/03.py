"""Q1: 'Tis it?"""
def is_palindrome(s):
    """
    >>> is_palindrome("tenet")
    True
    >>> is_palindrome("tenets")
    False
    >>> is_palindrome("raincar")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("ab")
    False
    """
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1: -1])

"""Q2: Greatest Pals"""

def greatest_pal1(s):
    """
    >>> greatest_pal1("tenet")
    'tenet'
    >>> greatest_pal1("tenets")
    'tenet'
    >>> greatest_pal1("stennet")
    'tennet'
    >>> greatest_pal1("25 racecars")
    'racecar'
    >>> greatest_pal1("abc")
    'a'
    >>> greatest_pal1("")
    ''
    """
    """TBD"""
    if is_palindrome(s):
        return s
    left, right = s[0: -1], s[1:]
    if is_palindrome(left) == False:
        return greatest_pal1(right)
    return greatest_pal1(left)




def greatest_pal2(s):
    """
    >>> greatest_pal2("tenet")
    'tenet'
    >>> greatest_pal2("tenets")
    'tenet'
    >>> greatest_pal2("stennet")
    'tennet'
    >>> greatest_pal2("25 racecars")
    'racecar'
    >>> greatest_pal2("abc")
    'a'
    >>> greatest_pal2("")
    ''
    """
    def helper(a, b, c):
        "print(a, b, s[b: b + a], c)"
        if a > len(s):
            return c
        elif a + b > len(s):
            return helper(a + 1, 0, c)
        elif is_palindrome(s[b: b + a]):
            return helper(a + 1, 0, s[b: b + a])
        return helper(a, b + 1, c)
    return helper(1, 0, "")

def greatest_pal3(s):
    """
    >>> greatest_pal3("tenet")
    'tenet'
    >>> greatest_pal3("tenets")
    'tenet'
    >>> greatest_pal3("stennet")
    'tennet'
    >>> greatest_pal3("25 racecars")
    'racecar'
    >>> greatest_pal3("abc")
    'a'
    >>> greatest_pal3("")
    ''
    """
    def helper(a, b):
        if is_palindrome(s[b: b + a]):
            return s[b: b + a]
        elif a + b == len(s):
            return helper(a - 1, 0)
        return helper(a, b + 1)
    return helper(len(s), 0)

"""TBD"""
Y = lambda f: (lambda x: x(x))(lambda x: f(lambda z: x(x)(z)))
fib_maker = lambda f: lambda r: ________________________________________________________________
is_pal_maker = lambda f: lambda r: _____________________________________________________________

fib = Y(fib_maker)
is_pal = Y(is_pal_maker)

# This code sets up doctests for fib and is_pal. Run test(fib) and test(is_pal) to check your implementation

fib.__name__ = 'fib'
fib.__doc__="""Given n, returns the nth Fibonacci nuimber.

>>> fib(0)
0
>>> fib(1)
1
>>> fib(2)
1
>>> fib(3)
2
>>> fib(4)
3
>>> fib(5)
5
"""

is_pal.__name__ = 'is_pal'
is_pal.__doc__="""Returns whether or not an input string s is a palindrome.

>>> is_pal('tenet')
True
>>> is_pal('tenets')
False
>>> is_pal('ab')
False
>>> is_pal('')
True
>>> is_pal('a')
True
"""

