'''
    Calculate fibonacci numbers using a dictionary
'''


def fib(number, computed_fib=None):
    '''
        number: int, nth fibonacci number to be computed
        computed_fib: dict, contains memoization for previously computed fib numbers
    '''
    # If it's the first time the function is called, let's add
    # our first two base cases: 1 and 2
    if computed_fib is None:
        computed_fib = {1: 1, 2: 1}

    # If the number was already computed, return the value
    # associated with it
    if number in computed_fib:
        return computed_fib[number]

    # It's a new number for fibonacci sequence, so we have to
    # actually calculate it
    else:
        ans = fib(number - 1, computed_fib) + fib(number - 2, computed_fib)
        computed_fib[number] = ans
        return ans


print(fib(6))
# 13
print(fib(20))
# 6765
print(fib(100))
# 354224848179261915075
print(fib(160))
# 1226132595394188293000174702095995
