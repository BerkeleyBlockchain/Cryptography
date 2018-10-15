'''utils.py'''

from math import sqrt
from random import getrandbits
import random

def gcd(x, y):
    '''Computes the greatest common divisor of x and y.

    >>> gcd(16, 10)
    2
    >>> gcd(3, 3)
    3
    >>> gcd(35, 12)
    1
    '''
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def div(x, y):
    '''Returns the number of times a number y divides x.

    >>> div(5, 4)
    1
    >>> div(28, 5)
    5
    '''
    return (x - x % y) // y

def extended_gcd(x, y):
    '''Computes d, the greatest common divisor as well as integers
    a and b such that gcd(x, y) = ax + by. Returns (d,a,b).

    >>> extended_gcd(35, 12)
    (1, -1, 3)
    >>> extended_gcd(16, 10)
    (2, 2, -3)
    '''
    if y == 0:
        return x, 1, 0
    else:
        d, a, b = extended_gcd(y, x % y)
        return d, b, a - div(x, y) * b

def is_coprime(a, b):
    '''Returns whether or not two integers are coprime
    (which means that a and b only share 1 as a common divisor).

    >>> is_coprime(2, 3)
    True
    >>> is_coprime(16, 10)
    False
    '''
    return gcd(a, b) == 1

def find_inverse(m, x):
    '''Find the inverse of x mod m, if m and x are coprime.

    >>> find_inverse(35, 12)
    3
    >>> print(find_inverse(16, 10))
    None
    '''
    if not is_coprime(m, x):
        return None
    d, _, inv = extended_gcd(m, x)
    while inv < 0:
        inv += m
    return inv

def is_prime(n, k=50):
    '''Returns whether a number is prime or not using the Miller-Rabin
    primality check.

    >>> is_prime(100005091)
    True
    >>> is_prime(3)
    True
    '''
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def is_prime_naive(x):
    '''Returns whether or not a number x is prime. O(sqrt(n)).

    >>> is_prime_naive(2)
    True
    >>> is_prime_naive(89)
    True
    >>> is_prime_naive(100)
    False
    '''
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def generate_prime(bits=512):
    '''Returns a random prime number with a specified number of bits.

    >>> is_prime(generate_prime(2))
    True
    '''
    prime = int(getrandbits(bits))
    while not is_prime(prime):
        prime = int(getrandbits(bits))
    return prime

def generate_coprime(x, max_num=None):
    '''Returns a number that is relatively prime to x.
    '''

    check_num = generate_prime()
    while not is_coprime(x, check_num):
        if max_num and check_num > max_num:
            return None
        else:
            check_num = generate_prime()
    return check_num
