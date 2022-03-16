import random
words = ['friday', 'electronis', 'engineering', 'nagpur', 

         'technology', 'mathematics', 'computer', 'condition', 

         'reverse', 'coronavirus', 'python', 'students'] 
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 14
while turns > 0:
    failed = 0
    for char in word: 
        if char in guesses: 
             print(char)
        else: 
             print("_")
             failed += 1

    if failed == 0:
        print("You Won the game")
        print("The word is: ", word)
        break
    guess = input("guess a character:")
    guesses += guess 
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
              print("You Lost the game!!Better luck next time")
