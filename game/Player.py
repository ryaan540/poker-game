class Player():
    def __init__(self, type="pc", cards=[], amount=0, total_amount_bet=0, name=""):
        self.name = name
        self.type = type
        self.cards = cards
        self.total_amount_bet = total_amount_bet
        self.amount = amount