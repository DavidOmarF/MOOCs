# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

## String -> String
## Returns the original string with 'U' added at the beginning

# def udacify (string): return ""            #stub

def udacify(string):
    return 'U' + string

print (udacify('dacians'))
#>>> Udacians

print (udacify('turn'))
#>>> Uturn

print (udacify('boat'))
#>>> Uboat