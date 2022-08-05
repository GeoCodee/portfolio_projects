#Step 1
import random
import hangman_art
import hangman_words
from replit import clear
# from replit import clear

word_list = hangman_words.word_list
stages = hangman_art.stages

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

print(hangman_art.logo)
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

display = []
for char in chosen_word:
    display.append('_')

wrong_guess = []

end_game = False
lives = 6
while not end_game:
    guess = input("Guess a letter: ").lower()

    clear()
    if guess in display:
        print(f"You already guessed the letter, try another one. \n Wrong Guesses: {','.join(wrong_guess)}")

    print(stages[lives])
    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess

    if guess not in chosen_word:
        
        lives -= 1
        wrong_guess += guess
        print(
            f"You have {lives} guesses left. Wrong guesses: {','.join(wrong_guess)}"
        )
        if lives == 0:
            
            end_game = True

    print(' '.join(display))

    if '_' not in display:
        end_game = True


if lives > 0:
    print("You win!")
else:
    print(stages[lives])
    print("You Lose!")
