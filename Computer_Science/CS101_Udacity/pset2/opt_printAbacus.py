#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    line = ['|00000*****   |',
            '|00000****   *|',
            '|00000***   **|',
            '|00000**   ***|',
            '|00000*   ****|',
            '|00000   *****|',
            '|0000   0*****|',
            '|000   00*****|',
            '|00   000*****|',
            '|0   0000*****|',
            '|   00000*****|',]
    val = str(value).zfill(10)
    for i in range(0, 10): print (line[int(val[i])])