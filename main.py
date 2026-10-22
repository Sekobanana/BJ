import random

#CREATE THE DECK
deck = []
face_cards = {"J": 10, "Q": 10, "K": 10}

for i in range(11): #put every number from 1-10 in the deck
    if i == 0: #don't put 0 in the deck
        continue

    else:
        for _ in range(4): #put every number 4x in the deck for 4 suits
            deck.append(i)

for face_card in face_cards: #put every face card (= J, Q, K) in the deck
    for _ in range(4):
        deck.append(face_card)

#CREATE FUNCTIONS FOR DEALING A HAND AND CALCULATING THE SUM OF A HAND
def deal(hand=list, deck=list, amount=int):
    for _ in range(amount):
        dealing_card = deck.pop(random.randint(0, (len(deck) - 1))) #take so many random cards from the deck as specified and put them in the hand
        hand.append(dealing_card)

def hand_sum(hand=list):
    card_sum = 0

    for card in hand:
        if card in face_cards:
            card_sum += face_cards[card]

        else:
            card_sum += card

    return card_sum

#INITIALISE THE PLAYER AND DEALER HANDS
dealer = []
player = []

deal(player, deck, 2)
deal(dealer, deck, 2)

player_sum = hand_sum(player)
dealer_sum = hand_sum(dealer)

if 1 in player & player_sum == 11:
    print("BLACKJACK")