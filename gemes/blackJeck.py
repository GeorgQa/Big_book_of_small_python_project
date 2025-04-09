"""Бдек-джекб (с) Эл Свейгарт
Классическая карточная игра, изветная также как "двадцать одно"
В этой версии нет стразования или разбиения
Теги: большая, игра, каротчная игра"""

import random
import sys

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

        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDecr():
    #Возвращаем список кортежей для 52 карт
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return  deck

def displayHands(playerHand, dealerHand, showDealerHand):
    #Отображаем карты игрока и диллера. скрываем первую карту дилера если showDealerHand = False
    print()
    if showDealerHand:
        print("DEALER:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        #скрываем первую карту диллера
        displayCards([BACKSIDE] + dealerHand[1:])

    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    #Возвращаем стоимость карт. Где фигурные карты стоят 10 , туз 11 или 1 (функция подбирает стоимость)
    value = 0
    numberOfAces = 0

    #добалвяем стоимость карт не туза
    for card in  cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K","Q","J"): #Эти стоят по 10 баллов
            value += 10
        else:
            value += int(rank) #стоимость равна номиналу

    #А сейчас для тузов
    value += numberOfAces #Добавляем 1 для каждого туза.
    for i in range(numberOfAces):
        #Если можно добавить ещё 10 с перебором, добавимЖ
        if value + 10 <= 21:
            value += 10
        return  value

def displayCards(cards):
    #Отображаем все карты их списка карт
    rows = ["", "", "", "", ""]

    for i ,cards in enumerate(cards):
        rows[0] += " __ " #Выводим верхнюю строку карты
        if card == BACKSIDE: #Выводим рубашку картыЖ
            rows[1] += "|## |"
            rows[2] += "|###|"
            rows[3] += "|_##|"
        else:
        #выводим лицевую сторону карты
            rank, suit = card #Карта - структура данных тип кортеж
            rows[1] += "|{} |"
            rows[2] += "| {} |"
            rows[3] += "|_{}|"

    for row in rows:
        print(row)

def getMove(playerHand, money):
    """Справиваем, какой ход хочет сделать игрок и возвращаем "H"
    , если он хочет взять ещё карту, "S", если ему хватит, и "D", если он удваивае"""
    while True:#Продолжаем итерации цикла пока игрок не сделает ход
        #определяем какой ход делает игрок
        moves = ['(H)it', '(s)tand']

        #Игрок может увоить при первом ходеб это ясно из того, что у игрока ровно две картыЖ
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        #Получаем ход игрока:
        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return  move
        if move == "D" and "(D)ouble down' in moves":
            return  move


#Если программа не импортируется, а запускается производим запуск:
if __name__ == "__main__":
    main()