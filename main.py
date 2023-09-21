#Step 1 
import random 
import hangman_art
import hangman_words

from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

chosen_word = random.choice(word_list)
len_chosen_word = len(chosen_word)
display = ["_" for _ in chosen_word]  # Initialize display with underscores for each letter in chosen_word
end_of_game = False
lives = 6
guessed_letters = [] 

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len_chosen_word):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    if lives == 0:
        end_of_game = True
        print("You lose")
        print(f'The answer was {chosen_word}.')

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])