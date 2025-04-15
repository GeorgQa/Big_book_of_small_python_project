import random

input(random)


HEADS  ="heads"
TAILS = "tails"
COIN_VALUES = [ HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUES)

def play_martingale(*, starting_funds:int, min_bet: int, max_bet:int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet  = min_bet

    while current_funds > 0:
        steps_to_loose += 1
        current_funds -= current_bet
        flipped_coin_value =flip_coin()

        if flipped_coin_value == HEADS:
            win = current_bet * 2
            current_funds += win
            current_bet = min_bet
        else:
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds

    return  steps_to_loose

def  simulatre_martingale_for_nplayers(*, starting_bet: int, min_bet: int, max_bet: int, count_games: int) -> float:
    total_steps_to_loose = 0
    for i in range(count_games):
        step_to_loose = play_martingale(starting_funds= starting_bet, min_bet=min_bet, max_bet= max_bet)
        total_steps_to_loose += step_to_loose

    return  total_steps_to_loose / count_games


print(simulatre_martingale_for_nplayers(starting_bet=1000 , min_bet= 1, max_bet= 100, count_games= 10))