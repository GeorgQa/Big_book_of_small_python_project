"""Бейглз
Дедуктивная логическая инра на угадывание числа по подсказкам.
Теги:короткая, игра, головоломка"""


import random

NUM_DUGITS = 3 #Попробуйте задать эту константу от 1 до  10
MAX_GUESSES = 10  #Попробуйте задать эту константу от 1 до  100

def main():
    print('''Bagels, a deductive logic game.\nBy AL Sweingart al@inventwithpython.com\nI am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:\nWhen I say:  That means:
    Pico    One digit is correct but in the worng position.
    Fermi   One digpt os correct and in the ringht position.
    Bagels  No digit is correct.\nFor example, if the secret number was 248 and yiur auess was 843, the\n
clues would be Fermi Pico.'''.format(NUM_DUGITS))
    while True:
        secretNum = getSecretNum()
        print ('I gave thought up a number.')
        print (' Yoy have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess)!= NUM_DUGITS or not guess.isdecimal():
                print ('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess,secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answe was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> '.lower().startswith("y")):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum= ''
    for i in range(NUM_DUGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess,secretNum):
    """Возвращает строку с подсказками pico, fermi и bagels
    для полученной на входе пары из догадки и секретного числа."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        #Сортируем подсказки в алфавином порядке, чтобы их исходный
        #порядок ничего не выдал.
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()