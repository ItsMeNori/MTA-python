import random
answer = random.randint(1,10)
while True:
    guess = int(input("Guess a number."))
    if answer == guess:
        print("correct.")
        break
    else:
        print("retard.")