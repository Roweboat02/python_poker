from typing import List, Dict
from enum import Enum

from card import Card


class Hands(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


def is_flush(cards: List[Card]) -> bool:
    suits = {"H": 0, "C": 0, "D": 0, "S": 0}
    for card in cards:
        suits[card.suit] += 1
    return any([i > 4 for i in suits.values()])


def is_straight(cards: List[Card]) -> bool:
    x = 0
    for card in cards:
        x |= 1 << (card.rank_to_int() - 1)
    checker = 0b11111
    while True:
        if x & checker == checker:
            return True
        elif checker > x:
            return False
        checker = checker << 1


def count_cards(cards: list[Card]) -> Dict[int, int]:
    counts = {k: 0 for k in range(2, 15)}
    for i in [card.rank_to_int() for card in cards]:
        counts[i] += 1
    return counts


def counts_to_hand(counts: Dict[int, int]):
    # 4 of kind =5, full house = 4, three of kind = 3, two pair = 2, pair = 1, none=0
    if any([i == 4 for i in counts.values()]):
        return 5
    if any([i == 3 for i in counts.values()]) and any([i == 2 for i in counts.items()]):
        return 4
    if any([i == 3 for i in counts.values()]):
        return 3
    x = sum([i == 2 for i in counts.values()])
    if x > 0:
        return x if x < 2 else 2
    else:
        return 0

def Assess(cards: list[Card]):
    is_fl=is_flush(cards)
    is_str=is_straight(cards)
    if (is_str and is_fl):
        ranks = set(i.rank_to_int() for i in cards)
        if 14 in ranks and 13 in ranks and 12 in ranks and 11 in ranks and 10 in ranks:
            return Hands.ROYAL_FLUSH
        else:
            return Hands.STRAIGHT_FLUSH
    elif is_fl:
        return Hands.FLUSH
    elif is_str:
        return Hands.STRAIGHT
    else:
        return [Hands.HIGH_CARD,
                Hands.TWO_PAIR,
                Hands.THREE_OF_A_KIND,
                Hands.FULL_HOUSE,
                Hands.FOUR_OF_A_KIND][counts_to_hand(count_cards(cards))]

def HandToPoints(hand):
    return {Hands.HIGH_CARD: 0,
     Hands.PAIR:5,
     Hands.TWO_PAIR:15,
     Hands.THREE_OF_A_KIND:20,
     Hands.STRAIGHT:25,
    Hands.FLUSH:30,
    Hands.FULL_HOUSE:40,
     Hands.FOUR_OF_A_KIND:50,
     Hands.STRAIGHT_FLUSH:75 ,
     Hands.ROYAL_FLUSH:100}[hand]
