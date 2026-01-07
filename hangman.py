import random

word_list=["kpn", "apple", "banana"]
print(word_list)

chosen_word = random.choice(word_list)
print(chosen_word)

placeHolder  = ""
for each_letter in range(len(chosen_word)):
   placeHolder += "_"
print(placeHolder)
game_over = False

correct_guesses_letters = []

while not game_over:
    guessed_letter = input("Guess a word: letter ").lower()
    print(guessed_letter)

    display= ""

    for each_letter in chosen_word:
        if each_letter == guessed_letter:
           display += each_letter
           correct_guesses_letters.append(guessed_letter)
        elif guessed_letter in correct_guesses_letters:
           display += guessed_letter
        else:
           display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")