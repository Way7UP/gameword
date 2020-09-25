import random
# исправить код: за словом необходимо обратиться к Алисе
# do you want to play with Alis?

words_list = ('кошка', 'корова', 'свинья', 'огород',
              'курица', 'пастух', 'лошадь', 'трактор', 'колодец')

secret_word = random.choice(words_list)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
    letter = input('введите ОДНУ букву: ').strip().lower()
    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        for position, symbol in enumerate(secret_word):
            # print(position, symbol)
            if symbol == letter:
                gamer_word[position] = symbol
        if '*' not in gamer_word:
            print('вы выиграли!!!')
            print('\tбыло загадно слово:', secret_word.upper())
            break
    else:
        errors_counter += 1
        print('\tошибок допущено:', errors_counter)
        if errors_counter == 8:
            print('вы проиграли ;(')
            break

    print(''.join(gamer_word))

print('игра окончена')
