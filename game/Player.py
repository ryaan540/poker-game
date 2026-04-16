import random
import time

class Player():

    def __init__(self, type="pc", cards=None, bet=0, name="", amount=0):
        self.name = name
        self.type = type
        self.cards = cards if cards is not None else []
        self._bet = bet
        self.amount = amount

    # -------- BET PROPERTY --------
    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, amount):
        if amount <= 0:
            return
        if amount > self.amount:
            print("Not enough balance")
            return
        self._bet += amount
        self.amount -= amount

    def reset_bet(self):
        self._bet = 0

    # -------- HUMAN ACTIONS --------
    def place_initial_bet(self):
        while True:
            amount = input(f"Place initial bet. Current amount is {self.amount}: ")

            if amount.isdigit():
                n = int(amount)
                if 0 < n <= self.amount:
                    return n

            print(f"Enter a valid number between 1 and {self.amount}")

    def call_fold_raise(self, player):
        choice = input("Press 1 to call\nPress 2 to fold\nPress 3 to raise\n")

        if choice == '1':
            return self.call(player)
        elif choice == '2':
            return self.fold()
        elif choice == '3':
            return self.raise_stake(player)

        print("Wrong choice")
        return self.call_fold_raise(player)

    def call(self, player):
        diff = player.bet - self.bet

        if diff <= 0:
            print("No need to call")
            return True

        if diff > self.amount:
            print("Can't call — not enough money")
            return "l"

        self.bet = diff
        print(f"I call. I bet {diff}")
        return True

    def fold(self):
        print("I Fold")
        return "l"

    def raise_stake(self, player):
        raise_amount = input(f"Enter raise amount (max {self.amount}): ")

        if not raise_amount.isdigit():
            print("Invalid input")
            return self.raise_stake(player)

        raise_amount = int(raise_amount)

        if raise_amount > self.amount:
            print("Too high")
            return self.raise_stake(player)

        self.bet = raise_amount
        print(f"I raise by {raise_amount}")
        return raise_amount

    # -------- AI ACTIONS --------
    def auto_call_raise(self, player, round_num):
        print("PC thinking...")
        time.sleep(2)

        diff = player.bet - self.bet
        print("Human bet:", player.bet)
        print("PC bet:", self.bet)

        if diff < 0:
            print("I call your bet")
            return self.call(player)

        if diff > self.amount:
            print("I fold (too expensive)")
            return "l"

        raise_amount = diff + random.randint(1, 30)

        if raise_amount > self.amount or round_num >= 3:
            self.bet = diff
            print(f"I call your bet: {diff}")
            return True

        self.bet = raise_amount
        print(f"I raise by {raise_amount}")
        return raise_amount

    def auto_match_or_raise(self, amount):
        print("PC thinking...")
        time.sleep(2)

        to_do = random.randint(1, 2)
        raise_amount = amount + random.randint(10, 250)

        if raise_amount > self.amount:
            to_do = 1

        if to_do == 1:
            if self.amount >= amount:
                self.amount -= amount
                print(f"Matching bet: {amount}")
                return amount
            else:
                print("Can't match — folding")
                return "l"

        self._bet += raise_amount
        self.amount -= raise_amount
        print(f"Raising by {raise_amount}")
        return raise_amount