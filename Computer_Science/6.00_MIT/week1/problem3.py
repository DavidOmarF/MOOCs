s = "kxnxiixoarjmgutrw"
indexes = [0]
lengths = []
words = []
j = 0
for i in range(1, len(s)):
    if ord(s[i]) < ord(s[i - 1]):
        indexes.append(i)
        lengths.append(i - indexes[j])
        words.append(s[indexes[j]:i])
        j = j + 1
    elif i + 1 == len(s):
        lengths.append(i - indexes[j] + 1)
        words.append(s[indexes[j]:i+1])

longest_i = [i for i, x in enumerate(lengths) if x == max(lengths)]
longest = [words[index] for index in longest_i]
print(longest[0])