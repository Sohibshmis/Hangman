import random
# list
from words_list import word_list

# stages and logo
from hangmanr_art import logo, stages
# lives
lives = 6
# the logo
print(logo)
# randomly choose a word
chosen_word = random.choice(word_list)
# to know the word uncomment this line of code
# print(f'solution is {chosen_word}.')

# display the empty spaces as many letters there is in the chosen_word
display = []
for letter in chosen_word:
    display += '_'
print(display)

# Keep looping the game
end_of_game = False
while not end_of_game:
    # taking a letter from the user
    guess = input("Guess a letter:").lower()
    # checking if the letter is correct and replacing it, if it is
    correct_letter = False
    if guess in display:
        print(f'You have already guessed {guess}.')
    else:
        count = 0
        for letter in chosen_word:
            if letter == guess:
                display[count] = guess
                correct_letter = True
            count += 1
        print(display)

        if not correct_letter:
            lives -= 1
            print(f'Wrong! the letter {guess} is not in the word!\nYou have {lives} lives left.')
            print(stages[lives])
        elif lives < 6:
            print(f'Correct! You have {lives} lives left.')
            print(stages[lives])
        else:
            print(f'Correct! You have {lives} lives left.')

    if '_' not in display:
        print(f'Guess the word correctly {chosen_word}.')
        print('You won, Goodjob you saved the man!')
        end_of_game = True
    if lives == 0:
        print(f'The word was{chosen_word}.')
        print('You lost, the man died :(')
        end_of_game = True
