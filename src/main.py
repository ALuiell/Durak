import Deck
import hand

"""
Ход игры
"""
class Gameplay:

    def __init__(self):
        self.control_hand = hand.PlayerHand()
        self.my_deck = Deck.CreateDeck()
        self.deck = self.my_deck.create()

    def player_init(self):
        p = ("human", self.my_deck.deal_hand(self.deck))
        p_ai = ("ai", self.my_deck.deal_hand(self.deck))
        return p, p_ai

    def show_hand(self, player):
        self.control_hand.show_hand(player)


gp = Gameplay()

player, player1 = gp.player_init()

player_lst = []

player_lst.append(player)
player_lst.append(player1)


for elem in player_lst:
    print(f"player: {elem[0]}")
    gp.show_hand(elem[1])






