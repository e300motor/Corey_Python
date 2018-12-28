import random

# here
print(random.random())          # 0 ~ 0.99999...
print(random.uniform(1, 10))    # [1 ~ 10] , float
print(random.randint(0, 10))     # [0 ~ 10] , int

greetings = ['Hello', 'Hi', 'Hey']

print(random.choice(greetings))

colors = ['Red', 'Black', 'Green']

print(random.choices(colors, weights=[10, 10, 2], k=10))

deck = list(range(1, 53))

random.shuffle(deck)

print(deck)

hand = random.sample(deck, k=5)     # random to grab one only
print(hand)

print(random.choice(deck))
