import random
import string
from Word import words

def Get_valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def Hangman():
    word = Get_valid_word(words)
    word_letter = set(word)
    alpa = set(string.ascii_uppercase)
    used_letter = set()
    print(word_letter)
    while len(word_letter) > 0:
        print("you have used these letters:"," ".join(used_letter))
        
        word_list = [val  if val in used_letter else "_" for val in word] 
        print("cureent word:"," ".join(word_list))
        user_input_letter = input("Guess a letter::").upper()
        if user_input_letter in alpa - used_letter:
            used_letter.add(user_input_letter)
            if user_input_letter in  word_letter:
                word_letter.remove(user_input_letter)
        elif  user_input_letter in used_letter:
            print("you have already used that character, Please try again.")    
        else:
            print("invallid character. Please try again.")        
   
    
Hangman()    