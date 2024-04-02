import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



print(f'{hangman_art.logo}')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print("You have allready guessed" + guess)


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
      print("You guessed "+guess+ ", that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")



    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_art.stages[lives])
