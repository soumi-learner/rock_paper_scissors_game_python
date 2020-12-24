import random
lst = ['r','p','s']

chance = 5
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Rock,Paper,Sizer\n \n")
print("r for Rock \np for Paper \ns for Sizer \n")

while no_of_chance<chance:
    _input = input('Rock,Paper,Sizer:')
    _random = random.choice(lst)

    if _input ==_random:
        print("game is tie because both choose the same thing\n")
     #humen take Rock
    elif (_input=="r" and _random=="p"):
        human_point=human_point+1
        print("human wins 1 point\n")
        print(f"you guess {_input} and computer guess {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    elif (_input == "r" and _random == "s"):
        human_point = human_point + 1
        print("human wins 1 point\n")
        print(f"you guess {_input} and computer guess {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    #humen take paper
    elif (_input == "p" and _random == "r"):
        computer_point = computer_point + 1
        print("computer wins 1 point\n")
        print(f"you guess {_input} and computer guess {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    elif (_input == "p" and _random == "s"):
        computer_point = computer_point + 1
        print("computer wins 1 point\n")
        print(f"you guess {_input} and computer guess {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    #humen take sezer
    elif (_input == "s" and _random == "r"):
        computer_point = computer_point + 1
        print("computer wins 1 point\n")
        print(f"you guess {_input} and computer guess {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    elif (_input == "s" and _random == "p"):
        human_point = human_point + 1
        print("human wins 1 point\n")
        print(f"you guess {_input} and computer guess {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    else:
        print("you have input wrong \n")


    no_of_chance = no_of_chance + 1
    chance_left=chance-no_of_chance
    print(f"your chances left {chance_left}")
    #print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point == human_point:
    print("Tie")
elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")