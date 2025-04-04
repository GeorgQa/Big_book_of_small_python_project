"""Бдек-джекб (с) Эл Свейгарт
Классическая карточная игра, изветная также как "двадцать одно"
В этой версии нет стразования или разбиения
Теги: большая, игра, каротчная игра"""

import random, sys

#Значения карт (масти) константы
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
# список chr можно глянуть на сайте hhtps://inventwithpython.com/charactermap)
BACKSIDE  = "backside"


def main():
    print("""Blackjeck, by AL Sweigart
    
    Reles: 
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H) it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can  (D)ouble down to increase your bet
    but must hit exactly one mort time before standing.
    In case of a tie, the bet is returned to player.
    The dealer stop hitting at 17.""")

    money  = 5000
    while True:
        #Проверяем не закончились ли деньги у игрока
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("thanks for playing!")
            sys.exit()


   #Делаем возможность поставить на следующий раунд
    print("Money:", money)
    bet = getBet(money)

    #Сдаём дилеру и игроку карты из колоды:
    deck = getDeck()
    delerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    #Обработка действий игрока:
    print('Bet:', bet)
    #цикл до тех пор пока player не скипнет
    while True:
        displayHands(playerHand,delerHand,False)
        print()
        #Проверка на перебор
        if getHandValue(playerHand)>21:
            break
        #Получаем ход игрока: H,S and D)
        move = getMove(playerHand, money - bet)

        # обработка действий игрока
        if move == 'D':
            #Игрок удваивает, он может увеличить ставку:
            additionalBet = getBet(min(bet, (money - bet)))
            bet += additionalBet
            print(f"Bet increased to {bet}.")
            print('Bet:', bet)

        if move in ('H', "D"):
            #Еще или удваиваю игрок берет ещё одну карту
            newCard = decl.pop()
            rank, suit  = newCard
            print(f"You drew a {rank} of {suit}.")
            playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                #Если перебор то пропускается ход игрока
                continue

        if getHandValue(playerHand) <= 21:
            while getHandValue(delerHand) < 21:
                #дилер берет ещё карту:
                print("Dealer hits...")
                delerHand.append(deck.pop())
                delerHands(playerHand, delerHand, False)

                if getHandValue(delerHand) >21:
                    break #перебор у диллера
                input("Press Enter to continue...")
                print('\n\n')

        #обображает итоговые карты на руках:
        delerHand(playerHand, delerHand,True)

        playerValue = getHandValue(playerHand)
        delerValue = getHandValue(delerHand)
        #Проверяем, игрок выиграл, проиграл или сыграл вничью:
        if delerValue > 21:
            print("Dealer busts! You win {}!".format(bet))
            money += bet
        elif playerValue > delerValue:
            print("You won {}!".format(bet))
            money == bet
        elif (playerValue > 21) or (playerValue < delerValue):
            print("You lost")
            money += bet
        elif playerValue== delerValue:
            print("It a tie, the bet is returned to you.")
        input("Press Enter to continue...")
        print('\n\n')

def getBet(maxBet):
    """спрашиваем у игрока сколько он ставит за раунд"""
    while True:
        print(f"How much do you bet? (1-{maxBet}, or QUIT)")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("THanks for playing!")
            sys.exit()

        if not bet.isdecimal()