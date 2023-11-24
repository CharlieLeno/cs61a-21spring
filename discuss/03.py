"""Q2: Merge Numbers"""
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        if n1 % 10 > n2 % 10:
            return merge(n1, n2 // 10) * 10 + n2 % 10
        else:
            return merge(n1 // 10, n2) * 10 + n1 % 10
        
"""Q3: Is Prime"""
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        else:
            return helper(i + 1)
    return helper(2)

"""Q4: (Tutorial) Warm Up: Recursive Multiplication"""
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    elif m == 1:
        return n
    elif m >= n:
        return multiply(m, n - 1) + m
    else:
        return multiply(m - 1, n) + n
    
"""Q5: (Tutorial) Recursive Hailstone"""
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(n * 3 + 1) + 1

"""Q6: Count Stair Ways"""
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 0 or n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)
    
"""Q7: (Tutorial) Count K"""
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs 
    when taking up to and including k steps at a time. 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif k == 1:
        return 1
    else:
        sum = 0
        for i in range(1, k+1):
            sum += count_k(n - i, k)
        return sum
