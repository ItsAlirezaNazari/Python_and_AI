import random

computer_score = 0
user_score = 0
computer_choice = ""
user_choice = ""

for i in range(3):
    x = random.randint(1, 3)

    if x == 1:
        computer_choice = "rock"
    elif x == 2:
        computer_choice = "paper"
    elif x == 3:
        computer_choice = "scissors"

    user_choice = input('Choose one of ("rock", "paper", "scissors"): ')

    if computer_choice == "rock" and user_choice == "paper":
        user_score += 1

    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score += 1

    elif computer_choice == "paper" and user_choice == "rock":
        computer_score += 1

    elif computer_choice == "paper" and user_choice == "scissors":
        user_score += 1

    elif computer_choice == "scissors" and user_choice == "rock":
        user_score += 1

    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score += 1

    print("Your choice: ", user_choice)
    print("Computer choice: ", computer_choice)
    print("+")

print("Computer score: ", computer_score)
print("User score: ", user_score)

if computer_score > user_score:
    print("Computer win")
elif computer_score < user_score:
    print("You win")
else:
    print("equal")

