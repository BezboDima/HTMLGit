import random
class P21:
    def __init__(self):
        V = random.randint(1,13) - 1
        S = random.randint(1,4) - 1
        self.__suits = ['clubs', 'peeks', 'hearts', 'dimonds' ]
        self.__value = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        self.__names = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.__cardV = self.__value[V]
        self.__cardS = self.__suits[S]
        self.__cardN = self.__names[V] 
    def get_value(self):
        return self.__cardV
    def get_suit(self):
        return self.__cardS
    def get_name(self):
        return self.__cardN
    def __str__(self):
        return (self.__cardN) + ' : ' + (self.__cardS)
    def compare_cards_war(self, card2):
        if self.__cardV > card2.get_value():
            return True
        else:
            return False
    def add_cards_poker (self, card):
        Q = self.__cardV + card.get_value()
        return Q
    def change_value_ACE(self):
        self.__cardV = 1

#  Assume that deck is infinite with standart  blackjack rules
#  Shows 2 of your cards and 1 dealer card, asking if you would like another
# If you are over 21 you are losing at EVERY scenario. 
# depends on your hand Ace can be 11 or 1 . (program doing it automatically, calculating the best way)
# dealer is drawing cards until total of 17 or more. 
def main():
    hand = give_card()
    dealer = give_card()
    print('dealer card ', dealer[0])
    show_cards(hand)
    Q = input('would you like a card Y/N')
    S = set('YyNn')
    while not Q in S:
            Q = input('Value is incorrect')
    while Q.upper() != 'N':
        hand = add(hand)
        show_cards(hand)
        Q = input('would you like a card Y/N')
        while not Q in S:
            Q = input('Value is incorrect')
    u = add_cards(hand)
    opponent = add_cards(dealer)
    while u > 21 and find_ace(hand):
        u = Ace_1_11(u, hand)
    while opponent < 17:
        deal_taumil = add(dealer)
        opponent += deal_taumil[-1].get_value()
        while opponent > 21 and find_ace(dealer):
            opponent = Ace_1_11(opponent, dealer)
    print('Dealers cards')
    show_cards(dealer)
    if u > opponent and u <= 21 and opponent <= 21 or u <= 21 and opponent > 21:
        print('You won!!!')
        print(u, opponent)
    elif u == opponent:
        print('TIE')
        print(u, opponent)
    else:
        print('you lost')
        print(u, opponent)
def add(hand):
    card_appolo = P21()
    hand.append(card_appolo)
    return hand
def show_cards(hand):
    for y in hand:
        print(y)
def add_cards(hand):
    total = 0
    oppolon = 0
    if len(hand) % 2 == 0:
        for i in range(1, (len(hand) // 2) + 1):
            z = hand[i - 1].add_cards_poker(hand[0 - i])
            total += z
    else:
        for i in range(1, (len(hand) - 1) // 2 + 1 ):
            z = hand[i - 1].add_cards_poker(hand[-1 - i])
            oppolon += z
            total = oppolon + hand[-1].get_value()
    return total
def give_card():
    card = P21()
    card2 = P21()
    dealer_hand = [card, card2]
    return dealer_hand
def find_ace(hand):
    for i in hand:
        if i.get_value() == 11:
            return True
    return False
def Return_ace(hand):
    for i in hand:
        if i.get_value() == 11:
            return i
def Ace_1_11(player, hand):
        Return_ace(hand).change_value_ACE()
        return add_cards(hand)
    
            
main()




