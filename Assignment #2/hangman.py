# Problem Set 2, hangman.py
# Name: Vladimir Trotsenko
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = load_words()  

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    result = True        
    for e in secret_word:
        if e not in letters_guessed:
            result = False
    return result

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    g_word = ''
    for e in secret_word:
        if e in letters_guessed:
            g_word += e
        else:
            g_word += '_ '
    return g_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    for e in letters_guessed:
        if e in alphabet:
            alphabet.remove(e)
    return ''.join(alphabet)        

def unic_letters(secret_word):
    """
    secret_word : string; The word the user is guessing
    Returns : length of the secret word
    """
    unic_letters = []
    for e in secret_word:
        if e not in unic_letters:
            unic_letters += e
    return len(unic_letters)
                      
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a', 'o', 'e', 'i', 'u']
    global letters_guessed                
    letters_guessed = []                  
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word) , 'letters long.')
    print('You have', warnings_remaining, 'warnings left.')
    while guesses_remaining > 0 or warnings_remaining > 0:
        print('------------------')
        print('You have', guesses_remaining, 'guesses left.')
        print('Available letters: ', get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ')
        guess.lower()
        if not guess.isalpha():
            if warnings_remaining > 1:
                warnings_remaining -= 1
                print('Incorrect input. You have', warnings_remaining, 'warnings left: ', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                if guesses_remaining == 0:
                        break
                print('Incorrect input. You have no warnings: ', get_guessed_word(secret_word, letters_guessed))
        else:
            if guess not in letters_guessed:
                letters_guessed += guess
                if guess not in secret_word:
                    print('This letter not in my word: ', get_guessed_word(secret_word, letters_guessed))
                    if guess not in vowels:
                        guesses_remaining -= 1
                        if guesses_remaining == 0:
                           break
                    else:
                        guesses_remaining -= 2
                        if guesses_remaining == 0:
                            break
                else:
                    print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            else:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print('Used before. You have', warnings_remaining, 'warnings left: ', get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses_remaining -= 1
                    print('Used before. You have no warnings left: ', get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            print('------------------')
            print('You won. It was', get_guessed_word(secret_word, letters_guessed) + '.')
            print('Your score:', unic_letters(secret_word)*guesses_remaining)
            break
    if not is_word_guessed(secret_word, letters_guessed):
        print('------------------')
        print('You lost. It was', secret_word + '.')  
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    result = True
    my_word = list(my_word)
    for e in my_word:
        if e == ' ':                       # <-- removing all the spaces from guessed word
            my_word.remove(e)              # because we needed them only for convenience in 
    if len(my_word) == len(other_word):    # reading the guesses in Console
        for i in range(len(my_word)):
            if my_word[i] != '_':                                        # <--- if there is an underscore but the related letter 
                if my_word[i] != other_word[i]:                          # of possible word is in guessed_letters means that word  
                    result = False                                       # could not be our secret word
            elif my_word[i] == '_' and other_word[i] in letters_guessed:
                result = False                              
    else:
        result = False
    return result

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    count = 0
    for e in wordlist:
        other_word = e
        if match_with_gaps(my_word, other_word):
             print(other_word, end = ' ')
        else:
            count += 1
    if count == len(wordlist):
        print('No matches found.')     # <-- only for the preparation because logically
    return                             # the answer would be at least one - secret_word

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses.
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a', 'o', 'e', 'i', 'u']
    global letters_guessed                
    letters_guessed = []                  
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word) , 'letters long.')
    print('You have', warnings_remaining, 'warnings left.')
    while guesses_remaining > 0 or warnings_remaining > 0:
        print('-------------------------')
        print('You have', guesses_remaining, 'guesses left.')
        print('Available letters: ', get_available_letters(letters_guessed), end = '')
        guess = input('Please guess a letter: ')
        guess.lower()
        if guess == '*':
            my_word = get_guessed_word(secret_word, letters_guessed)
            print('Possible matches are: ')    
            show_possible_matches(my_word)
        elif not guess.isalpha():
            if warnings_remaining > 1:
                warnings_remaining -= 1
                print('Incorrect input. You have', warnings_remaining, 'warnings left: ', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                if guesses_remaining <= 0:
                        break
                print('Incorrect input. You have no warnings: ', get_guessed_word(secret_word, letters_guessed))
        else:
            if guess not in letters_guessed:
                letters_guessed += guess
                if guess not in secret_word:
                    print('This letter not in my word: ', get_guessed_word(secret_word, letters_guessed))
                    if guess not in vowels:
                        guesses_remaining -= 1
                        if guesses_remaining <= 0:
                           break
                    else:
                        guesses_remaining -= 2
                        if guesses_remaining <= 0:
                            break
                else:
                    print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            else:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print('Used before. You have', warnings_remaining, 'warnings left: ', get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses_remaining -= 1
                    print('Used before. You have no warnings left: ', get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            print('-------------------------')
            print('You won. It was', get_guessed_word(secret_word, letters_guessed) + '.')
            print('Your score:', unic_letters(secret_word)*guesses_remaining)
            break
    if not is_word_guessed(secret_word, letters_guessed):
        print('-------------------------')
        print('You lost. It was', secret_word + '.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
