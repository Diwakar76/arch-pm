import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
faces = ['J', 'Q', 'K', 'A']
numbered= [2, 3, 4, 5, 6, 7, 8, 9, 10]
# def draw():
#     return random.choice(numbered + faces), 'of', random.choice(suits)
# for _ in range(5):
#     print(draw())
#       # Draw and print 5 random cards
deck = set()
def draw():
    for suit in suits:
        for card in numbered + faces:
            deck.add((card, 'of', suit))
    return random.choice(list(deck))

for _ in range(5):
     print(draw())

def draw():
    card = random.choice(list(deck))
    deck.remove(card)
    return card
     

for _ in range(5):
     print(draw())
print (len(deck))          

print(type(suits))