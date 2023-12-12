import random


class CreateDeck:
    def __init__(self):
        self.colors = ['черв', 'пик', 'бубен', 'треф']
        self.cards_list = ['6', '7', '8', '9', '10', "J", "Q", "K", "T"]
        self.suits = {
            "пик": "♠",
            "треф": "♣",
            "черв": "♥",
            "бубен": "♦"
        }
        self.deck = []

    def create(self):
        for suit in self.colors:
            for value in self.cards_list:
                self.deck.append((value, self.suits[suit], suit))
        random.shuffle(self.deck)

        return self.deck

    def deal_hand(self, deck):  #one time use
        hand = []
        for i in range(6):
            hand.append(random.choice(deck))
        return hand

    def get_card(self, hand, deck):
        while len(hand) < 6:
            hand.append(random.choice(deck))
        else:
            pass

    def deck_update(self, deck, turn_cards):
        for elem in turn_cards:
            deck.remove(elem)





