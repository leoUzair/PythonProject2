print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Davy Jones' Locker island")
print("Your mission is to find the heart of Davy jones")
choice1 = input('You are at the shore of island and you see a cave and a mountain! where do you want to go? "cave" or "mountain".')
if choice1 == "cave" or choice1 == "Cave":
    print("nice decision! ")
    choice2 = input('you entered into cave you see two thing a small lake and a hole in cave\'s wall. where did you go "lake" or "hole".').lower()
    if choice2 == "hole":
        print("yep! Great choice ")
        choice3 = input(
            'You entered into hole and you see three boxes black yellow Red '
            'only one of them has Davy jones heart rest of them has poison gases. '
            'which box you choose "black" or "yellow" or "red".').lower()
        if choice3 == "red":
            print("Congratulation! you have find the Davy jones heart!!")
        elif choice3 == "yellow":
            print("Game over! you smell poison")
        elif choice3 == "black":
            print("Game over! you smell poison")
        else:
            print("you choose the box that does not exist! ")
    else:
        print("Game over! you have been eaten by crocodiles: ")


elif choice1 == "mountain" or choice1 == "Mountain":
    print("Game over! there is nothing on mountain 😂")
else:
    print("choose only two places")


