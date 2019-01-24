##Benji Saltz
##07/02/18
##8. Card Game
##Description: Card game: Divides cards into four hands and finds highest worth hand and longest suit in a team 
import random

class Hand(object): ##Class for cards 
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0
        
    def append(self, val):
        self.hand.append(val)
        
    def calc_points(self):##allocates points
        for c in self.hand:
            if c[1] == 'A':
                self.points += 4
            elif c[1] == 'K':
                self.points += 3
            elif c[1] == 'Q':
                self.points += 2
            elif c[1] == 'J':
                self.points += 1
        return self.points
    
    def __str__(self):##Prints each players points and hand
        return self.name + ' with ' + str(self.points) + ' points and the hand '+ str(self.hand)

def find_top(hands):##Finds who has the best hand with the highest amount of points
    top = Hand('tmp')
    for h in hands:
        if h.points > top.points:
            top = h
    return top

def find_max(suit_count): ##finds suit count
    longest = 'C'
    for i in suit_count:
        if suit_count[i] > suit_count[longest]:
            longest = i
    return longest
    
def find_longest(hands, top):##compares teams suit count
        pairs = (['North', 'South'], ['East', 'West'])
        pair = []
        for p in pairs:
            if top.name in p:
                pair = p
        
        for i in range(0, len(pair)):
            for h in hands:
                if h.name == pair[i]:
                    pair[i] = h
                    
        com_hand = pair[0].hand + pair[1].hand
        suit_count = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
        for i in com_hand:
            suit_count[i[0]] += 1
        print(str(hands[0]),'\n',str(hands[1]),'\n',str(hands[2]),'\n',str(hands[3]))##Prints hands 
        
        
        longest = find_max(suit_count)
        print ('The pair ' + pair[0].name + ' and ' + pair[1].name + ' had the highest suit of ' + longest + ' with ' + str(suit_count[longest]) + ' cards.')
        return longest

def main(args):## creates and shuffles cards
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['S', 'D', 'H', 'C']
    
    deck = []
    for s in suits:
        for c in cards:
            deck.append(s + c)
    
    random.shuffle(deck)
    
    hands = [Hand('North'), Hand('West'), Hand('South'), Hand('East')]
    for c in range(0, len(deck)):
        i = c % 4
        hands[i].append(deck[c])
    
    for h in hands:
        h.calc_points()
    
    top = find_top(hands)
    print ('The winner is ' + str(top)) #Prints top hands 
    find_longest(hands, top)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
print ('The pair ' + pair[0].name + ' and ' + pair[1].name + ' had the highest suit of ' + longest + ' with ' + str(suit_count[longest]) + ' cards.') #Prints longest team and their longest hand 
