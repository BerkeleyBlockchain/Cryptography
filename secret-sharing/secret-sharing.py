"""secret-sharing.py"""

import sys
sys.path.append('../utils')

from primes import *
from mod import *

def generate_random_shares(secret, minimum, num_shares):

    assert minimum < shares, "Minimum shares must be less than total shares)"
    poly = [secret] + [generate_prime() for i in range(minimum)]

    shares = [(i, poly_eval(poly, i)) for i in range(1, num_shares + 1)]

    return shares

def poly_eval(poly, x):
    '''Evaluate a polynomial (represented as a list) at x

    >>> poly_eval([1, 2, 3], 4)
    57

    >>> poly_eval([50, 60, 70], 2)
    450

    '''
    total, i = 0, 0
    for coef in poly:
        total += coef * pow(x, i)
        i += 1
    return total
