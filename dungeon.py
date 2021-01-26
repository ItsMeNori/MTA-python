#a dungeon simulator
import random
EnemyHealth = 300
YourHealth = 500
potions = 3
check = True
print("You are a warrior exploring a dungeon for loot.")
print("You suddenly run into a monster. The battle starts!")
while check == True:
    if YourHealth <= 0:
        check = False
        print("You died. Game over.")
        break
    elif EnemyHealth<=0:
        print("You won the battle!")
        break    
    elif int(YourHealth)>0:
        print("Your current health:" + str(YourHealth))
        print("1. Attack.")
        print("2. Run.")
        print("3. Use item.")
        choice = input("Choose your action:")
        if choice == ("1"):
            print("You choose to attack.")
            attack = random.randint(0,30)
            if attack == 0:
                print("You missed!")
                print("The enemy attacks you.")
                oppattack = random.randint(5,40)
                YourHealth = int(YourHealth) - oppattack
                print("You lost " + str(oppattack) + " hp.")
            else:
                EnemyHealth = EnemyHealth - attack
                print("You attacked the enemy for " + str(attack) + " damage.")
                print("The enemy is now at "+ str(EnemyHealth) + " hp.")
                print("The enemy attacks you.")
                oppattack = random.randint(5,40)
                YourHealth = int(YourHealth) - oppattack
                print("You lost " + str(oppattack) + " hp.")
        elif choice ==("2"):
            print("You choose to run.")
            run = random.randint(0,12)
            if run <= 10:
                print("You failed to escape.")
                print("The enemy attacks you.")
                oppattack = random.randint(0,40)
                YourHealth = int(YourHealth) - oppattack
                print("You lost " + str(oppattack) + " hp.")
            elif run>10:
                print("You successfully escaped.")
                break
        elif choice ==("3"):
            potions = potions - 1
            if potions < 0:
                print("You have no more potions.")
            else:
                print("You used a potion.")
                YourHealth = YourHealth + 80
                print("You healed 80 hp!")
            print("The enemy attacks you.")
            oppattack = random.randint(0,40)
            YourHealth = int(YourHealth) - oppattack
            print("You lost " + str(oppattack) + " hp.")
        else:
            print("Wrong input. Try again.")





    