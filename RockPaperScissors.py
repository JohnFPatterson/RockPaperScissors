from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
playerScore = 0
computerScore = 0

while player == False:
    print('Player-Computer Score: ', int(playerScore), '-', int(computerScore))
    print(" ")
    player = input("Rock, Paper, or Scissors? ").lower().capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computerScore = computerScore + 1
        else:
            print("You win!", player, "smashes", computer)
            playerScore = playerScore + 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computerScore = computerScore + 1
        else:
            print("You win!", player, "covers", computer)
            playerScore = playerScore + 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computerScore = computerScore + 1
        else:
            print("You win!", player, "cut", computer)
            playerScore = playerScore + 1
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]
