# Chapter 18: Inheritance

# Ex. 18.1
 
class Time(object):
    def __init__(self, hour=0, minute=0, second=0.0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        amass_seconds = (60**2)*self.hour + 60*self.minute + self.second
        return amass_seconds

    # make it so that if first parameter is greater than second, 
    # the __cmp__ method returns 1. If equal, 0. and if the second
    # object is greater, -1. Python uses this to process <,>,>=,<=,==
    def __cmp__(self, other):
        t1 = (self.hour, self.minute, self.second)
        t2 = (other.hour, other.minute, other.second)
        return cmp(t1,t2)

    # an alternate way:
    #def __cmp__(self,other):
    #    return self.time_to_int - other.time_to_int

t1 = Time(15,30,15)
t2 = Time(15,20,32)
print t1 > t2
print t1 < t2


# Ex. 18.2
 
# See the second-to-last method defined in the class Deck for
# what the exercise was asking.

class Card(object):
    """Represents a playing card"""
    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = ['None','Ace','1','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self,other):
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        return cmp(t1,t2)


class Deck(object):
    """Represents a deck of playing cards"""
    def __init__(self):
        self.cards = []
        for suit in range(0,4):
            for rank in range(1,15):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card)) # string function uses __str__ method
    # just like print does
        return '\n'.join(res)

    def add_card(self, card):
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def shuffle(self):
        import random
        random.shuffle(self.cards) # in-place, no return statement needed
        # This is a modifier, not a pure function

    def sort(self):
        self.cards.sort() # internally uses the __cmp__ method in the
        # Card class. This is also a modifier

    def deal_hands(self, hnum, cnum):
        res = []
        for i in range(hnum):
            newhand = Hand()
            for j in range(cnum):
                newhand.cards.append(self.pop_card())
            res.append(newhand)
        return res


deck1 = Deck()
print deck1

print '\n'

deck1.shuffle()
print deck1

print '\n'

deck1.sort()
print deck1


# Ex. 18.3 

# See the last method defined in the deck class
# in my exercise 18.2 answer for the deal_hands method.

# See below for the hand class definition.

class Hand(Deck):
    """Represents a hand of playing cards"""
    def __init__(self, label = ''): # overrides the Deck class __init__
        self.label = label
        self.cards = []

deck2 = Deck()
deck2.shuffle()
[Bob, Joe, Jane, Kate] = deck2.deal_hands(4,13)

print '\n'
print "Bob's hand:\n",Bob,'\n'
print "Joe's hand:\n",Joe,'\n'
print "Jane's hand:\n",Jane,'\n'
print "Kate's hand:\n",Kate,'\n'

