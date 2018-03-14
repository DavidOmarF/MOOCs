###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###


## String String String -> String
## Replaces all markers with replacement in line
## def replaceMarker(marker, replacement, line): return "-"              #stub
def replaceMarker(marker, replacement, line):
    occurrence = line.find(marker)
    replaced = line[:occurrence] + replacement + line[occurrence + len(marker):]
    return replaced

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.

# Example 2 # uncomment this to test with different input
#marker = "EY"
#replacement = "Eyjafjallajokull"
#line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.

print (replaceMarker(marker, replacement, line))
