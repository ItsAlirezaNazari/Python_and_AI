import random

computer_number = random.randint(10, 40)
guess_counter = 0

for i in range(10):
    user_number = int(input("Guess: "))
    guess_counter += 1

    if computer_number == user_number:
        print("You win 🎉")
        print("The number of your guesses", guess_counter)
        break

    elif computer_number > user_number:
        print("go up")
    
    elif computer_number < user_number:
        print("go down")

