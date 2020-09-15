import random

def attack_animal(animal, playerHealth):
    blood = 60
    if animal == 'Pig' or animal == 'Hen' or animal == 'Boar':
        blood = 20
    elif animal == 'Fox':
        blood = 40
    elif animal == 'Dog':
        blood = 100
        print ("You are not allowed to kill dogs. The police beat your butt off! LMAO")
    elif animal == 'Gigantic_Poop':
        blood = 60

    if playerHealth-blood < 0:
        playerHealth = 0
    else:
        playerHealth = playerHealth-blood

    print ("You killed a", animal + "!", "You lost " + str(blood) + " hp. Now your health status is:", playerHealth)

    return playerHealth

health = 100
fishTimes = 0
action = str(input("Do you want to hunt, fish, fight a miniboss, fight a boss, or quit:"))
mbList = ['Zombie', 'Witch', 'The Toygar Toilet']
coins = 0
lifeBoost = 0
strongLifeBoost = 0
healthLimit = 350
fishLimit = 4
while health != 0 and action != 'quit':
    if action == 'hunt':
        animal_List = ('Fox', 'Pig', 'Hen', 'Dog', 'Boar', 'Gigantic_Poop')
        animal = random.choice(animal_List)
        health = attack_animal(animal, health)
        fishTimes = 0
        coins += 15

    elif action == 'fish':
        if fishTimes < fishLimit:
            fishList = ['Normal Fish', 'Normal Fish', 'Normal Fish', 'Normal Fish', 'SUPER FISH']
            if random.choice(fishList) == 'Normal Fish':
                fish = random.randint(0,5)
                print ("You got", fish, "fish!!")
                health += fish*10
                coins += fish*10
            else:
                superFish = random.randint(1,3)
                health += superFish*50
                coins += superFish*50
                print ("You got", superFish, "SUPER fish!!!")
            if health > healthLimit:
                print ("You were too greedy! Your health cannot be higher than", healthLimit, "Your health is back to 100.")
                health = 100
            print ("Now you have", health, "health.")
            fishTimes += 1
            print ("You have fished", fishTimes, "time(s) in a row")
        else:
            print ("You already fished 4 times in a row!")

    elif action == 'miniboss':
        fishTimes = 0
        health -= 200
        if health >= 0:
            print ("You killed a", random.choice(mbList), "You lost 200 lives! Your current health status is", health)
            coins += 300

    elif action == 'boss':
        fishTimes = 0
        health -= 250
        if health >= 0:
            print ("You killed THE SUPREME KNOWLEDGE OF EVIL!!! You lost 250 lives! Your current health status is", health)
            healthLimit += 10
            coins += 500

    elif action == 'shop':
        fishTimes = 0
        print ("You currently have", coins, "coins.")
        item = int(input('''What do you want to buy:
        1. Life boost (200 coins)
        2. Strong life boost (500 coins)
        3. Never mind
        '''))
        if item == 1:
            if coins >= 200:
                lifeBoost += 1
                healthLimit += 50
                fishLimit += 1
                coins -= 200
            else:
                print ("Don't try to trick me!! You don't have enough money!!!")
        elif item == 2:
            if coins >= 500:
                strongLifeBoost += 1
                healthLimit += 150
                fishLimit += 2
                coins -= 500
            elif item == 2:
                print ("Don't try to trick me!! You don't have enough money!!!")
            else:
                print ("Goodbye! Good riddance!")

    elif health <= 0:
        print ("You Died! LOL")
        action = 0
    action = str(input("Do you want to hunt, fish, shop, fight a miniboss, or fight a boss:"))


if action != 'quit':
    print("Game Over")
else:
    print("You ended the game")
