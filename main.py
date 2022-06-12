import random

comp_win = 0
player_win = 0

def choose_option():
    player_choice = input("Choose Rock, Paper or Scissors: ")
    if player_choice in ["Rock", "rock", "R", "r"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "P", "p"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "S", "s"]:
        player_choice = "s"
    else:
        print("Wrong Input, try again. ")
        choose_option()
    return player_choice

def computer_option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    player_choice = choose_option()
    comp_choice = computer_option()
    print("")

    if player_choice == "r":
        if comp_choice == "r":
            print("You and the computer chose rock, it is a tie")
        elif comp_choice == "p":
            print("You chose rock, the computer chose paper, you lose")
            comp_win +=1
        elif comp_choice == "s":
            print("You chose rock, the computer chose scissors, you win")
            player_win +=1

    elif player_choice == "p":
        if comp_choice == "r":
            print("You chose paper and the computer chose rock, you win")
            player_win +=1
        elif comp_choice == "p":
            print("You and the computer chose paper, it is a tie")
        elif comp_choice == "s":
            print("You chose paper, the computer chose scissors, you lose")
            comp_win +=1
    elif player_choice == "s":
        if comp_choice == "r":
            print("You chose scissors and the computer chose rock, you lose")
            comp_win +=1
        elif comp_choice == "p":
            print("You chose scissors and the computer chose paper, you win")
            player_win +=1
        elif comp_choice == "s":
            print("You and the computer chose scissors it is a tie")

        print("")
        print("Player wins: ", str(player_win))
        print("Computer wins: ", str(comp_win))
        print("")

        player_choice = input("Do you want to play again? (y/n)")
        if player_choice in ["Y", "y", "Yes", "yes"]:
            pass
        elif player_choice in ["N", "n", "No", "no"]:
            break
        else:
            break

            