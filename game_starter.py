
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import os
import random
import string

clear = lambda: os.system('cls')
WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for secret_letter in secret_word:
        if (not secret_letter in letters_guessed): return False
    return True


### Testcases
assert is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']) == False
assert is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']) == True
assert is_word_guessed('carrot', ['b', 'g', 'd', 'z', 'w', 'y', 'v', 'm', 'i', 'k']) == False
assert is_word_guessed('lettuce', ['k', 'v', 'a', 'e', 'n', 'd', 'b', 'f', 'u', 'c']) == False
assert is_word_guessed ('pineapple', []) == False
assert is_word_guessed ('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']) == True
print('is_word_guessed Test passed!')



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    return ''.join([secret_letter if secret_letter in letters_guessed else "_ " for secret_letter in secret_word]).strip()
    
      
### Testcases
assert get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']) == '_ pp_ e'
assert get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']) == 'durian'
assert get_guessed_word('grapefruit', ['k', 'm', 'b', 'j', 'e', 'w', 's', 'z', 'u', 'x']) == '_ _ _ _ e_ _ u_ _'
assert get_guessed_word('coconut', ['w', 'l', 'i', 'p', 'c', 'u', 'j', 'h', 'v', 'z']) == 'c_ c_ _ u_'
assert get_guessed_word('banana', []) == '_ _ _ _ _ _'
assert get_guessed_word('broccoli', ['e', 'c', 'g', 'u', 'r', 'x', 's', 'a', 'p', 'j']) == '_ r_ cc_ _ _'
assert get_guessed_word('', ['e']) == ''
print('get_guessed_word Test passed!')



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join([letter for letter in string.ascii_lowercase if not letter in letters_guessed])


### Testcases 
assert get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) == 'abcdfghjlmnoqtuvwxyz'
assert get_available_letters([]) == 'abcdefghijklmnopqrstuvwxyz'
assert get_available_letters(['r', 'y', 'd', 'u', 't']) == 'abcefghijklmnopqsvwxz'
assert get_available_letters(['t', 'w', 'v', 'b', 'k', 'n']) == 'acdefghijlmopqrsuxyz'
assert get_available_letters(['a']) == 'bcdefghijklmnopqrstuvwxyz'
assert get_available_letters(['p', 'r', 'f', 'd', 'k', 'h', 'c', 'a', 'i', 'y', 'w', 'b']) == 'egjlmnoqstuvxz'
print('get_available_letters Test passed!')



def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Let the game begin!')
    print(f'I am thinking of a word with {len(secret_word)} letters.')

    max_wrong_guess = 8

    wrong_guess_count = 0
    letters_guessed = []
    while True:
        print()

        if wrong_guess_count >= max_wrong_guess:
            print('You Lose!!! L + Ratio')
            print(f'Reason: Your guess wrong more than {max_wrong_guess} letters!')
            print(f'The word is: {secret_word}')
            break

        if is_word_guessed(secret_word, letters_guessed):
            print(f'You Win!!! The word is: {get_guessed_word(secret_word, letters_guessed)}')
            break

        print(f'You have {max_wrong_guess - wrong_guess_count} guesses remaining.')
        print(f'Letters available to you: {get_available_letters(letters_guessed)}')
        guess = input('Guess a letter: ').lower()

        if guess in letters_guessed:
            print(f'You dumb****! You already try \'{guess}\': {get_guessed_word(secret_word, letters_guessed)}')
        elif guess not in secret_word:
            letters_guessed.append(guess)
            print(f'Wrong! The letter \'{guess}\' is not in the word: {get_guessed_word(secret_word, letters_guessed)}')
            wrong_guess_count += 1
        else:
            letters_guessed.append(guess)
            print(f'Correct: {get_guessed_word(secret_word, letters_guessed)}')



def main():
    clear()
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()