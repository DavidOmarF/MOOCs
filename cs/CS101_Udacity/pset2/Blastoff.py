# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

## Number -> __NOTHING__
## Takes a number n and prints from n to 1, and then "Blastoff!"

## def countdown(n): return                 #stub
def countdown(n):
    if n == 0:
        print ("Blastoff!")
        return
    else:
        print (n)
        countdown(n-1)

countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!
