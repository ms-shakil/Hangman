# Make Hangman game with python !
import random
import string
from words_arr import words

# This function return valid word

def Valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word.upper()

# This is main function ! . This function work how to play hangman !

def Hangman():
    word = Valid_word(words)
    word_letter = set(word)
    alpa = set(string.ascii_uppercase)
    used_letter = set()
    live = 7
    
    while len(word_letter) > 0 and live > 0:
        print(f"You have {live} lives left and  you have used these letters:"," ".join(used_letter))
        word_list = [val  if val in used_letter else "_" for val in word] 
        print("Cureent word:"," ".join(word_list))
        user_input = input("Guess a letter:").upper()
        
        if user_input in alpa - used_letter:
            used_letter.add(user_input)
            if user_input in  word_letter:
                word_letter.remove(user_input)
            else:
                live = live -1            
        elif  user_input in used_letter:            
            print("you have already used that character, Please try again.")    
        else:
            print("invallid character. Please try again.")        
    
    if live == 0:
        print(f"Sorry , You died  this word is {word}")
    else:
        print(f"You win , You guess the word {word}!!")    
    
Hangman()    ## call hangman function