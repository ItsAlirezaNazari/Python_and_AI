import random

words_bank = ["tree", "book", "train", "fish"]
true_chars = []
false_chars = []
user_mistakes = 0
foundAllChars = False

random_index = random.randint(0, len(words_bank) - 1)
word = words_bank[random_index]

while user_mistakes < 6:
    for i in range(len(word)):
        if word[i] in true_chars:
            print(word[i], end=" ")
        else:
            print("_", end=" ")
    
    print("\n")

    if foundAllChars:
        print("You Win 🎉")
        break

    while True:
        user_guess = input("Guess char: ").lower()
        
        if len(user_guess) == 1:
            break
        else:
            print("Please enter one character")

    if user_guess in word:
        true_chars.append(user_guess)
    else:
        false_chars.append(user_guess)
        user_mistakes += 1
    
    if user_mistakes == 6:
        print("Game Over!")
        break

    foundAllChars = True
    for i in range(len(word)):
        if word[i] not in true_chars:
            foundAllChars = False
            break
    
