'''
    Compares two different algorithms:
        recursive and memoization
    for computing Fib sequence.
'''
import time


def fib_rec(number):
    global num_calls
    num_calls += 1
    if number == 1 or number == 2:
        return 1

    return fib_rec(number - 1) + fib_rec(number - 2)


def fib_dict(number, computed_fib=None):
    # For benchmark purposes:
    global num_calls
    num_calls += 1

    if computed_fib is None:
        computed_fib = {1: 1, 2: 1}

    if number in computed_fib:
        return computed_fib[number]

    nth_fib = fib_dict(number - 1, computed_fib) + fib_dict(number - 2, computed_fib)
    computed_fib[number] = nth_fib
    return nth_fib


# i = 10
def dict_measure(i):
    start = time.time()
    fib_dict(i)
    end = time.time()
    return str(i) + "," + str(num_calls) + "," + format(end - start, '.32f')

def rec_measure(i):
    start = time.time()
    fib_rec(i)
    end = time.time()
    return str(i) + "," + str(num_calls) + "," + format(end - start, '.32f')


dict_stats = open("dict_stats.csv", "w")
rec_stats = open("rec_stats.csv", "w")

for i in range(1, 41):
    num_calls = 0
    dict_stats.write(dict_measure(i) + "\n")
    num_calls = 0
    rec_stats.write(rec_measure(i) + "\n")
