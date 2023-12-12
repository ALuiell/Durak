
class PlayerHand:

    def show_hand(self, player):
        cards = [f"{elem[0]}{elem[1]}" for elem in player]
        hand_string = " ".join(cards)
        print(hand_string)
