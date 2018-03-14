# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

## String String -> Number
## Takes two strings (s, sub), and returns the last position (sub 0) in a, where b appears
        ## (or -1 if sub doesn't appear)
## def find_last(s, sub): return 0              #stub
def find_last(s, sub):
    if s[::-1].find(sub[::-1]) == -1:
        return -1
    else:
        return len(s) - s[::-1].find(sub[::-1]) - len(sub)

print (find_last('holahola', 'ho'))
#>>> 4

print (find_last('aaaaa', 'aa'))
#>>> 3

print (find_last('aaaa', 'b'))
#>>> -1

print (find_last("111111111", "1"))
#>>> 8

print (find_last("222222222", ""))
#>>> 9

print (find_last("", "3"))
#>>> -1

print (find_last("", ""))
#>>> 0