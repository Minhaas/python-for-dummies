from random import randint

possibilities = ["Rock", "Paper", "Scissors"]

computer = possibilites[randint(0,2)]

player = False

while player == False:
    player = input("Rock ,Paper or Scissors?")
    if computer == player:
        print("Tie!")
    elif computer == "Rock":
        if player == "Paper":
            print("You lose! Rock crushes paper")
        else :
            print("You win! ")
    elif computer == ""