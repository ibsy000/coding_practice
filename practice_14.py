# Write a program that will calculate the number of trailing zeros in a factorial 
# of a given number.

# N! = 1 * 2 * 3 *  ... * N

# Be careful 1000! has 2568 digits...

# Examples

# zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

import math

def zeros(n):

    # first solution is not efficient enough

    fact_n = math.factorial(n)
    zeros = 0
    idx = -1

    while str(fact_n)[idx] == '0':
        zeros += 1
        idx -= 1
    return zeros


print(zeros(12))