import random
from Word import words

def Get_valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word

def Hangman():
    print(Get_valid_word(words))
    
Hangman()    