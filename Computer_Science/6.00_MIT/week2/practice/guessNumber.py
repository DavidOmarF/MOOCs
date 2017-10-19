print("Please think of a number between 0 and 100!")
ans = ""
high = 100
low = 0
num = 0
while (ans != 'c'):
    mid = int((high + low) / 2)
    print("Is your number ", mid, "?")
    print("Enter 'h' to indicate the guess is too high. "+
          "Enter 'l' to indicate the guess is too low. "+
          "Enter 'c' to indicate I guessed correctly. " , end='')
    ans = input()

    if ans == 'h':
        high = mid
    elif ans == 'l':
        low = mid
    elif ans == 'c':
        num = mid
        break
    else:
        print ("Sorry, I did not understand your input.")
        continue

print("Game over. Your secret number was:", num)
