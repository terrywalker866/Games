from random import randint
options = ["ROCK", "PAPER", "SCISSORS"]
message = {
    "tie": "You tie, Congrats your the Browns!", "won": "You win, No days off!", "lost": "You lose!"
    }
def decide_winner(user_choice, computer_choice):
    print ("You selected: %s" % user_choice)
    print ("Computer selected: %s" % computer_choice)
    if user_choice == computer_choice:
        print (message["tie"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print (message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print (message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print (message["won"])
    else:
        print (message["lost"])
def play_RPS():
    user_choice = input("Enter ROCK, PAPER, or SCISSORS: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)

    play_RPS()
