import random

def create_deck(deck=list):
    for i in range(10):
        if i == 0:
            continue

        else:
            for _ in range(4):
                deck.append(i)

    for _ in range(16):
        deck.append(10)

    return deck

deck = []
deck = create_deck(deck)
#print(deck)

