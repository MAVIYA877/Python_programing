import random 

secret_number = random.randint(1,10)

print("!========================Welcome to the guessing number games========================!")
print("Guess a number between 1 to 10!")

while True:
    guess = int(input("Enter the guess:"))

    if guess == secret_number:
        print("congratulation you guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low! , try again")
    else:
        print("Too high! , try again")