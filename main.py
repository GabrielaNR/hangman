import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

from hangman_words import word_list

#TODO-2: - Import the stages from hangman_art.py and make this error go away.
from hangman_art import stages

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

from hangman_art import logo
print(logo)
print("Welcome to hangman game!")
chosen_word = random.choice(word_list)
end_game = False
display = []
not_display = []
lives = 6

#lista palavra
for letra in chosen_word:
  not_display.append(letra)
#print(not_display)

#lista a ser mostrada
for letra in chosen_word:
  display.append("#") 
print(f"The word is {''.join(display)}.")
print(stages[6])
while not end_game:
#pedindo entrada do usuário 
  user_choice = input("Guess a letter: ").lower()
  
#checando se a letra já foi usada
  if user_choice in display:
    print(f"You've already guessed {user_choice}")
    
#checando a entrada do usuário:    
  if user_choice in not_display:
    for i in range(len(display)):
      if not_display[i] == user_choice:
        display[i] = user_choice
        
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.   
        print(f"Current position: {(i + 1)}\nGuessed letter: {user_choice}")
        if display == not_display:
          end_game = True
          print(f"You win!\nThe word is {chosen_word}!")
  elif user_choice not in not_display:
    lives -= 1
    
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    print(f"You guessed {user_choice}, that's not in the word. You lose a life.\nNow you have {lives} lives.")
    if lives == 0:
      end_game = True
      print(f"You lose!\nThe word is {chosen_word}.")
     
  print(f"{''.join(display)}")
  print(stages[lives])
    
