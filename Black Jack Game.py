import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
			
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank + " of "+ self.suit
    
    
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_cards=Card(suit,rank)
                self.all_cards.append(created_cards)
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def del_one(self):
        return self.all_cards.pop()
		
obj2=Deck()
sdd=obj2.all_cards[2]


for card in obj2.all_cards:
    print(card)
obj2.shuffle()
print(obj2.all_cards[1])

    
mycard=obj2.del_one()
print(mycard)
    
   
   
 class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f" Player {self.name} has {len(self.all_cards)} cards"
		

obj3=Player("Rohit")
print(obj3)
obj3.add_cards(mycard)
print(obj3)
print(obj3.all_cards[0])

pcard=obj3.remove_one()
print(pcard)
print(obj3.all_cards)