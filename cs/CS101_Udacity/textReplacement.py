marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

occurrence = line.find(marker)
replaced = line[:occurrence] + replacement + line[occurrence + len(marker):]

print (replaced)