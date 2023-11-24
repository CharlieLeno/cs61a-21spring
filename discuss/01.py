"""Q1: Jacket Weather?"""
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining == True:
        print('True')
    else:
        print('False')


"""Q2: (Tutorial) Warm Up: Case Conundrum"""
def square(x):
    print("here!")
    return x * x

"""Q3: Square So Slow"""
def so_slow(num):
    x = num
    while x > 0:
        x=x+1
    return x / 0
square(so_slow(5))

"""Q4: (Tutorial) Is Prime?"""
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

"""Q5: (Tutorial) Fizzbuzz"""
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        i = i + 1

