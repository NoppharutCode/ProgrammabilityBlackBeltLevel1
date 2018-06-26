# Guess the number: 4
# Wrong, try again! 

# Guess the number: 8
# Correct! 
import random

number = random.randint(1, 10)
ans = None

while True:
    print("Guess the number: ", end="")
    ans = int(input())

    if(ans == number):
        print("Correct!")
        break
    else:
        print("Wrong, try again!")
