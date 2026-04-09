class Card:
    RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    SUITES=["HEARTS", "DIAMONDS", "SPADES", "CLUBS", "JOKER"]
    def __init__(self, suite, rank):
        

        if not isinstance(suite, str):
            raise TypeError(f'Suite expected to be a string, got {type(suite).__name__}')
        if not isinstance(rank, str):
            raise TypeError(f'Rank expected to be a string, got {type(rank).__name__}')

        suiteUpper = suite.upper()
        rankUpper = rank.upper()

        if suiteUpper == "JOKER":
            self.rank = "JOKER"
            self.suite = suiteUpper
            return

        if rankUpper not in Card.RANKS:
            raise ValueError(f'Invalid rank: {rank}')
        if suiteUpper not in Card.SUITES:
            raise ValueError(f'Invalid suit: {suite}')

        self.rank = rank
        self.suite = suite

    def printCard(self):
        print("Rank:", self.rank)
        print("Suite:", self.suite)


if __name__ == "__main__":
    card1 = Card(suite="Joker", rank="A")  # Joker card
    card1.printCard()

    card2 = Card(suite="Clubs", rank="3")
    card2.printCard()
