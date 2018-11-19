# Problem Set 2, hangman.py
# Name: Razikh Shaik

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "Problem Set 2/words.txt"


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
    for i in set(secret_word):
      if i not in letters_guessed:
        return False

    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for i in secret_word:
      if i in letters_guessed:
        guessed_word = guessed_word + i
      else:
        guessed_word = guessed_word + "_ "

    return guessed_word    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    remaining_letters = ""
    for i in list(all_letters):
      if i not in letters_guessed:
        remaining_letters += i

    return remaining_letters
    
def is_validate_the_input(guessed_letter):
  if (not str.isalpha(guessed_letter)) or (len(guessed_letter) > 1):
    return False
  else:
    return True

def calculate_guesses_warnings(num_of_guesses, num_of_warnings, warn_flag = False, message= "", is_vowel = False):
  if warn_flag:
    if num_of_warnings > 0:
      num_of_warnings -= 1
      print(message,"you have",num_of_warnings,"warnings left. ", end="")
    else:
      num_of_guesses -= 1
      print(message,"you have no warnings left, you lose a guess. ", end="")
  else:
    if not is_vowel:
      num_of_guesses -= 1
    else:
      num_of_guesses -= 2
    print(message, end = "")
  return (num_of_guesses,num_of_warnings)

def get_input_eval_metrics(secret_word, letters_guessed, num_of_guesses, num_of_warnings, with_hints = False, hints_identifier="*"):
  skip = False
  warn_flag = False
  correct_flag = False
  dm = ""
  vowels = ['a', 'e', 'i', 'o', 'u']
  is_vowel = False

  guessed_letter = input("Please guess a letter:")
  if is_validate_the_input(guessed_letter):
    if guessed_letter in letters_guessed:
      warn_flag= True
      dm  = "Oops! You've already guessed that letter."
    elif guessed_letter not in secret_word:
      letters_guessed.append(guessed_letter)
      dm = "Oops! That letter is not in my word: "
      if guessed_letter in vowels:
        is_vowel = True
    elif guessed_letter in secret_word:
      letters_guessed.append(guessed_letter)
      skip = True
      correct_flag = True
      dm = "Good guess."
  elif with_hints == True and guessed_letter == hints_identifier:
    print("possible matches: ", show_possible_matches(get_guessed_word(secret_word, letters_guessed)), "\n Try it now! ", end="")
    skip = True
  else:
    dm = "Oops! That is not a valid letter."
    warn_flag= True

  if not skip:
    num_of_guesses, num_of_warnings = calculate_guesses_warnings(num_of_guesses, num_of_warnings, warn_flag= warn_flag, message= dm, is_vowel=is_vowel)
  if correct_flag:
    print(dm,end="") 
    
  print(get_guessed_word(secret_word, letters_guessed))
  
  return (letters_guessed, num_of_guesses, num_of_warnings)
      

def hangman(secret_word, with_hints = False, hints_identifier="*"):
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long. ")
    print("-------------")
    letters_guessed = []
    num_of_guesses = 6
    num_of_warnings = 3
    while num_of_guesses > 0:
      print("You have "+str(num_of_guesses)+" guesses left.")
      print("Available letters:", get_available_letters(letters_guessed))
      letters_guessed, num_of_guesses, num_of_warnings = get_input_eval_metrics(secret_word, letters_guessed, num_of_guesses, num_of_warnings, with_hints = with_hints, hints_identifier=hints_identifier)
      if is_word_guessed(secret_word, letters_guessed):
        break     
    
    if num_of_guesses > 0:
      print("------------")
      print("Congratulations, you won!")
      print("Your total score for this game is:",num_of_guesses * len(set(secret_word)))
    else:
      print("------------")
      print("Sorry, you ran out of guesses. The word was:", secret_word)






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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] == "_":
            other_word = other_word.replace(other_word[i], "_")
        
    return my_word.strip() == other_word.strip()



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_words = []
    for i in wordlist:
      if match_with_gaps(my_word, i):
        possible_words.append(i)
    if len(possible_words) > 0:
      return " ".join(possible_words)
    else:
      return "No matches found"



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    hangman(secret_word, with_hints = True)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


def initiate(func):
    #print(match_with_gaps("_ _ _ _ ", "appl"))
    #print(show_possible_matches("_ _ _ _ "))
    secret_word = choose_word(wordlist)
    #print(secret_word)
    func(secret_word)