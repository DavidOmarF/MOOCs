# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

## Number Number Number -> Number
## Returns the lowest of three numbers received
## def lowest(a, b, c): return 0                #stub
def lowest (a, b, c): 
    return lower(lower(a, b), lower(b, c))
    
## Number Number -> Number
## Returns the lower of two numbers received
## def lower(a, b): return 0                    #stub
def lower (a, b):
    if(a < b):
        return a
    else:
        return b

## Number Number -> Number
## Returns the bigger number between two numbers received
## def bigger (a, b): return 0                  #stub
def bigger (a, b):
    return a + b - lower(a, b)

## Number Number Number -> Number
## Returns the biggest number between three received
## def biggest(a, b, c): return 0               #stub
def biggest(a, b, c): 
    return bigger(bigger(a, b), bigger(b, c))


## Number Number Number -> Number
## Returns the median value (the one in the middle (if sorted))
## def median (a, b, c): return 0               #stub
def median(a, b, c):
    return a + b + c - lowest (a, b, c) - biggest (a, b, c)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7