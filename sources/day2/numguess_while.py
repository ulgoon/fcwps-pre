import random


answer = random.randint(1,100)
print(answer)

username = input("What's your name? ")

while 1:
    guess = eval(input("Guess the number: "))

    if answer == guess:
        print("Correct!")
        break
    else:
        print("Wrong!")
