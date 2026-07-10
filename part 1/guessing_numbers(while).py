import random

answer = random.randint(1,100)
status = False

while status == False:
    guess = int(input("Insert your guess: "))

    if guess > answer:
        print("Clue: Lower")
    elif guess < answer:
        print("Clue: Higher")
    else:
        print(f"The answer is {answer}, Congratulation you are correct!")
        print("Thank you for playing the game")
        status = True
        
    