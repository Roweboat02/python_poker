from random import randint
from card import Card

def random_suit():
    return ["H", "C", "D", "S"][randint(0,3)]

def random_rank():
    return Card.int_to_rank(randint(2,14))

def random_cards():
    made = 0
    out = []
    while made<21:
        c= Card(random_suit(), random_rank()).to_special_str()
        if c not in set(out):
            out.append(c)
            made+=1
    return out
