import random
import hangman_art
import hangman_words

print(hangman_art.logo)

word_list = hangman_words.word_list
word = random.choice(word_list)
display = []
stages = hangman_art.stages
for _ in word:
    display.append('_')

flag = True
have_lives = 6
print(''.join(display))
while flag:
    guess = input('Guess a letter: ').lower()
    found_anything = False
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
            found_anything = True
    if not found_anything:
        have_lives -= 1
        print(stages[have_lives])
    print(''.join(display))

    if '_' in display and have_lives:
        continue
    elif not have_lives:
        flag = False
        print('You lost.')
    elif '_' not in display:
        flag = False
        print('You won.')
