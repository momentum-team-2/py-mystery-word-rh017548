import random
new_list = [line.rstrip() for line in open("words.txt", "r")]
easy_words = [e_text for e_text in new_list if len(e_text) >=4 and len(e_text) <=6 ]
normal_words = [n_text for n_text in new_list if len(n_text) >=6 and len(n_text) <=8 ]



print('***Lets Play!***')
print('***You Have 10 Guesses***')
difficulty_choice = input('Choose difficulty: (E)asy or (N)ormal')
#guess_word = random.choice(words)
#for choice_word in guess_word:
if difficulty_choice == 'E':
    guess_word = random.choice(easy_words)
elif difficulty_choice == 'N':
    guess_word = random.choice(normal_words)
else:
    print('Choose E or N')
print(guess_word)


#print(choice_word)  
#new_text = [n_text for n_text in words if len(n_text) >=4 and len(n_text) <=6 ]
#print(new_text)  
#["bob", "cool", "whatup", "lemon", "mango", "banana", "apple", "unexpected", "python", "user", "two"]