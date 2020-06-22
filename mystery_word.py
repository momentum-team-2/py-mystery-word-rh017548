import random

new_list = [line.rstrip() for line in open("words.txt", "r")]
easy_words = [e_text for e_text in new_list if len(e_text) >=4 and len(e_text) <=6 ]
normal_words = [n_text for n_text in new_list if len(n_text) >=6 and len(n_text) <=8 ]
hard_words = [h_text for h_text in new_list if len(h_text) >=8]

print('***Lets Play!***')
print('***You Have 8 Guesses***')

difficulty_choice = input('Choose difficulty: (E)asy, (N)ormal or (H)ard')
if difficulty_choice == 'E':
    mystery_word = random.choice(easy_words)
elif difficulty_choice == 'N':
    mystery_word = random.choice(normal_words)
elif difficulty_choice == 'H':
    mystery_word = random.choice(hard_words)
else:
    print('Choose E, N or H')
print(f" The word has {len(mystery_word)} letters")
print(mystery_word)
guessed_letters = []
correct_guess = []
tries = 0
def display_word(mystery_word, correct_guess):
    return (letter if letter in correct_guess else '_' for letter in mystery_word)

wrong_guesses = 0
while (wrong_guesses <= 8): 
    guess = input('**** Guess A Letter ****')
    tries = tries + 1
    if len(guess) != 1:
        print('Choose only one letter')
    elif guess.isalpha() != True:
        print('Pick A Letter Only')
    guessed_letters.append(guess)
    if guess in guessed_letters:
        print('You have already picked this letter')
    

    if guess in mystery_word:
        correct_guess.append(guess)
        print(f"Great Guess! This word does have a(n) {guess}. You have {8 - wrong_guesses } guesses left")
    elif guess not in mystery_word and guess.isalpha() == True:
        wrong_guesses = wrong_guesses + 1
        print(f"Sorry! This word does not have a(n) {guess}. You have {8 - wrong_guesses} guesses left")
    
    print(f'Mystery Word: {" ".join(display_word(mystery_word, correct_guess))}')
    if '_' not in display_word(mystery_word, correct_guess):
        print(f"You Win! The word was {mystery_word}! You guessed it in {tries} tries!")
        exit(0)
    if wrong_guesses == 8:
        print(f"Game Over! The word was {mystery_word}!")
        exit(0)

   
              

                                    


        


    
    
    




