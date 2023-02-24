import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

members= ["Jogo", "Jnne", "Max", "Cindy"]
print(random.choice(members))

#### Roll a dice


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())

