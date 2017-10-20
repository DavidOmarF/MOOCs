'''
    Calculate fibonacci numbers using a dictionary
'''


def fib(number):
    '''
        number: int, nth fibonacci number to be computed
    '''
    if number == 1 or number == 2:
        return 1

    return fib(number - 1) + fib(number - 2)
