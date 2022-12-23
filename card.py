from enum import Enum

class Card:
    suit:str
    rank:str

    def __init__(self, suit:str, rank:str):
        self.suit=suit
        self.rank=rank

    def to_int(self):
        return

    def to_str(self):
        return self.suit+self.rank

    @classmethod
    def from_str(cls, string):
        cls(suit=string[:-1], rank=string[-1])

    def to_special_str(self):

        return {'D':"\u2666", "H":"\u2665", "C":"\u2663", "S":"\u2660"}[self.suit]+self.rank

    def rank_to_int(self):
        if self.rank in {str(i) for i in range(2,10)}:
            return int(self.rank)
        elif self.rank=='T':
            return 10
        elif self.rank=='J':
            return 11
        elif self.rank=='Q':
            return 12
        elif self.rank=='K':
            return 13
        elif self.rank=='A':
            return 14

    @staticmethod
    def int_to_rank(rank: int):
        if rank in {i for i in range(2, 10)}:
            return str(rank)
        elif rank == 10:
            return 'T'
        elif rank == 11:
            return 'J'
        elif rank == 12:
            return 'Q'
        elif rank == 13:
            return 'K'
        elif rank == 14:
            return 'A'
        else:
            print(rank)


if __name__=="__main__":
    my_card = Card("H", "A")
    print(my_card.to_str())