"""Сообщение в виде битовой карты
Обображает тестовое сообщение в соответвии с указанной битовой картой.
Теги: Крошечная, для начинающих, графика"""

import sys

bitmap = """
....................................................................
**************   *  *** **  *      ******************************
********************* ** ** *  * ****************************** *
**      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *s
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
...................................................................."""

print('Bitmap Message, by AL Sweigart al@inventwithpython.com')
print('Enter the ,message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

#Проходим в цикле по всем строкам битовой карты
for line in bitmap.splitlines():
    #Проходим в цикле по всем символам строки:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Выводим пустое пространство согласно пробелу в битовой карте:
            print(' ', end ='')
        else:
            #Выводим символ сообщения:
            print(message[i % len(message)], end= '')
    print()#Выводим символ в новой строке

