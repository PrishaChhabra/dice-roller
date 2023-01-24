import random
response='y'
#input("Do you want to roll the dice or not. Press y for yes and n for no")
print("Dice Roller (Random number generator)")
while response=='y':
    rand=random.randint(1,6)
    if rand==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if rand==2:
        print("[-----]")
        print("[  0  ]")
        print("[  0  ]")
        print("[-----]")

    if rand==3:
        print("[-----]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[-----]")

    if rand==4:
        print("[-----]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[-----]")

    if rand==5:
        print("[-----]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[  0  ]")
        print("[-----]")

    if rand==6:
        print("[-----]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[-----]")

    response=input("Do you want to roll the dice or not. Press y for yes and n for no.")
    print("\n")

