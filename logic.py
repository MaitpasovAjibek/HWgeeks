import random


class GameLogic:
    def check_win(self, bet, slot):
        slots = list(range(1, 31))
        win_slot = random.choice(slots)

        if slot == win_slot:
            return bet * 2
        else:
            return -bet

