import random


# Nature class contains combat method
class Nature:
    def combat(pred, prey): # both parameters should be of animal type

        # More positive => better chance of prey living
        attack_score = prey.defense - 1.5 * pred.attack

        # Prey is more likely to survive with camouflage, especially if predator's senses are poor
        if (pred.sight + pred.smell + pred.hearing) / 3 > prey.camo:
            attack_score /= 2

        eff_speed = prey.speed
        # Realistically, high defense and health would probably indicate a slower animal
        if (prey.defense + prey.health) > 2 * prey.speed:
            eff_speed /= 2

        eff_sense = (pred.sight + pred.smell + pred.hearing) + 2 * max(pred.sight, pred.smell, pred.hearing)

        score = prey.health - 1.5 * attack_score + eff_speed - 0.2 * eff_sense
        score = max(2, score)

        return random.randint(0, int(score)) < random.randint(0, 100)


class Animal:
    # Stats are auto-scaled (sum = 1000) at end of constructor
    def __init__(self, health = 100, attack = 100, defense = 100, speed = 100, sight = 100, smell = 100, hearing = 100, camo = 100, poison = 0, mutate_rate = 1.2):
        # Genes (carry over in offspring)
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.sight = sight
        self.smell = smell
        self.hearing = hearing
        self.camo = camo
        self.poison = poison
        self.mutate_rate = mutate_rate
        self.scale_stats()

        # Stats  from combating
        self.score = 0
        self.attack_success = 0
        self.attack_fail = 0
        self.defend_success = 0
        self.defend_fail = 0

    def scale_stats(self):
        scale = 800 / (self.health + self.attack + self.defense + self.speed + + self.sight + self.smell + self.hearing + self.camo + self.poison)
        self.health = int(scale * self.health)
        self.attack = int(scale * self.attack)
        self.defense = int(scale * self.defense)
        self.speed = int(scale * self.speed)
        self.sight = int(scale * self.sight)
        self.smell = int(scale * self.smell)
        self.hearing = int(scale * self.hearing)
        self.camo = int(scale * self.camo)
        self.poison = int(scale * self.poison)

    def __str__(self):
        return "heal:  " + str(self.health) + "\tatck:  " + str(self.attack) + "\tdefs:  " + str(self.defense) + "\tsped:  " + str(self.speed) + "\tsigt:  " + str(self.sight) + "\tsmel:  " + str(self.smell) + "\thear:  " + str(self.hearing) + "\tcamo:  " + str(self.camo) + "\tpois:  " + str(self.poison)

    def mutate(self):
        if random.randint(0, 100) < 30:
            self.health *= self.mutate_rate
        if random.randint(0, 100) < 30:
            self.attack *= self.mutate_rate
        if random.randint(0, 100) < 30:
            self.defense *= self.mutate_rate
        if random.randint(0, 100) < 30:
            self.speed *= self.mutate_rate
        if random.randint(0, 100) < 30:
            self.sight *= self.mutate_rate
        if random.randint(0, 100) < 30:
            self.smell *= self.mutate_rate
        if random.randint(0, 100) < 30:
            self.hearing *= self.mutate_rate
        if random.randint(0, 100) < 30:
            self.camo *= self.mutate_rate
        if random.randint(0, 100) < 30:
            self.poison *= self.mutate_rate
        self.scale_stats()

    def copy(self):
        return Animal(self.health, self.attack, self.defense, self.speed, self.sight, self.smell, self.hearing, self.camo, self.poison, self.mutate_rate)

parent_rabbit = Animal()
#predator = Animal(100, 200, 100, 100, 50, 200, 75, 150, 0)
predator = Animal(100, 150, 100, 125, 150, 150, 125, 125, 0) # Best guess for a coyote
#predator = Animal(300, 200, 200, 100, 50, 100, 50, 50, 0) # Best guess for a bear

for generation in range(100):
    print("\nGeneration: " + str(generation))

    # Offspring of ten rabbits
    rabbits = [parent_rabbit.copy() for i in range(10)]

    # Each with genes slightly mutated, as per Animal.mutate()
    for rabbit in rabbits:
        rabbit.mutate()

    # Each gets attacked 1000 times by a predator (coyote)
    for attack_number in range(1000):
        for rabbit in rabbits:
            if Nature.combat(predator, rabbit):
                rabbit.defend_fail += 1
                predator.attack_success += 1
            else:
                rabbit.defend_success += 1
                predator.attack_fail += 1

    # Print out how the rabbits did
    for rabbit in rabbits:
        print(str(rabbit) + "\tWins:  " + str(rabbit.defend_success) + "\tLosses:  " + str(rabbit.defend_fail))

    # Find most successful, replace parent_rabbit
    max_wins = 0
    best_rabbit = rabbits[0]
    for rabbit in rabbits:
        if rabbit.defend_success > max_wins:
            max_wins = rabbit.defend_success
            best_rabbit = rabbit
    parent_rabbit = best_rabbit