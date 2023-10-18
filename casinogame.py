from decouple import config
from logic import GameLogic


class CasinoGame:
    def __init__(self):
        self.my_money = config('MY_MONEY', default=1000, cast=int)
        self.game_logic = GameLogic()

    def start_game(self):
        while True:
            print(f"Your money: {self.my_money}")
            if self.my_money <= 0:
                print("You have no money left!")
                break

            slot = int(input("Choose a slot (1-30): "))
            bet = int(input("Place your bet: "))

            if bet > self.my_money:
                print("You don't have enough money for this bet!")
                continue

            result = self.game_logic.check_win(bet, slot)
            self.my_money += result

            print(f"Result: {'Win' if result > 0 else 'Loss'}")
            print(f"Your money: {self.my_money}")

            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != 'y':
                break