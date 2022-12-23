```mermaid
flowchart TD

A[Deal 5 cards]
B[Discard up to 5 cards]
B0[Fold]
B1[Bet]
C[Replace discarded]
D0[Fold]
D1[Bet]
E[Best Hand Wins]


A-->B
B-->B0
B-->B1
B1-->C
C-->D0
C-->D1
D1-->E

```

```mermaid
classDiagram
    class Game {
        +deal_phase()
        +discard_phase()
        +replace_phase()
        +asses_phase()
    }

    class Card{
        +int suit
        +int value        
    }

    class CardDeck{
        -List~Card~ cards
        + draw(n) Card
    }

    class PlayerBank{
        +int bet
        +int total

        +change_bet(int)
    }

    class PlayerHand{
        +List~Card~ hand
        +List~Card~ holding

        +add_to_holding(int index)
        +receive_cards(List~Card~)
    }

    class HandAssesor {
        +asses(List~Card~)
    }

    Game --* Player
    Game --* CardDeck
    Game --* HandAssesor

    class Player

    Player --* PlayerHand
    Player --* PlayerBank

    CardDeck -- Card
    PlayerHand -- Card
    HandAssesor -- Card
```

Royal Flush - 10 J Q K A of same suit

Straight Flush - 5 cards of the same suit

Four of a kind - 4 cards of the same value

Full house - 2 cards of the same value, and 3 of a different but same value

Three of a kind - 3 cards of the same value

Two pair - 2, 2 pairs

pair - two cards of the same value

```mermaid
flowchart TD

Flush{Flush?}
Straight{Straight?}
Royal{Royal Flush?}
counts[get counts]

Flush --> Straight
Straight -- 11 --> Royal
Royal --1--> royal[/royal flush/]
Royal --0--> str_fl[/straight flush/]
Straight -- 10 --> fl[/flush/]
Straight -- 01 --> str[/straight/]

Straight -- 00 --> counts

counts --> count_counts{three 3's, two 2's, 4 2's}
count_counts -- 110 --> fh[/full house/]
count_counts -- 100 --> 3[/three of a kind/]
count_counts -- 001 --> 2p[/two pair/]
count_counts -- 010 --> p[/pair/]
count_counts -- 000 --> hc[/high_card/]

```
pocket poker

Straight - 20
3 of a kind - 15
2 pair - 10
jacks or better - 5

striaght flush - 250
4 of a kind - 125
full house - 40
flush - 25

to play costs 5 points