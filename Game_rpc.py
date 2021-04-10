
import random
print("There will be 9 rounds")
print("Who will score more he will be the winner")
print("1)Rock\n2)Paper\n3)Scissor\n")

score_of_user=0
score_of_system=0

def opt_of_system():
    if (system == 1):
        print("Rock",end=" ")
    elif (system == 2):
        print("Paper",end=" ")
    elif (system == 3):
        print("Scissor",end=" ")

def opt_of_user():
    if (user == 1):
        print("Rock")
    elif (user == 2):
        print("Paper")
    elif (user == 3):
        print("Scissor")


round_number=1

while(round_number<=9):
    print("This is a"," round",round_number)

    user = int(input())
    while(user>=4):
        print("only Rock, Paper, Scissor  \nNo 4th opt")
        print("cotinue")
        user = int(input())

    system = random.randint(1, 3)
    if(system==user):
        opt_of_system()
        print( end=" ------ ")
        opt_of_user()
        print("Draw")
        print("this round is draw so no round is counted")
        print((10 - round_number), " Roundes left")


    elif((system==1 and user==2) or (system==2 and user==3) or (system==3 and user==1)):
        opt_of_system()
        print(end=" ------ ")
        opt_of_user()
        print("✨-winner of this round-✨")
        score_of_user=score_of_user+1
        print((9 - round_number), " Roundes left")
        print("U R score is",score_of_user)
        round_number = round_number + 1

    elif((user==1 and system==2) or (user==2 and system==3) or (user==3 and system==1)):
        opt_of_system()
        print(end=" ------ ")
        opt_of_user()
        print("👎--Loose this round")
        score_of_system=score_of_system+1
        print((9 - round_number), " Roundes left")
        print("U R score is", score_of_user)
        round_number = round_number + 1
    print(" ")



if(score_of_user>score_of_system):
    print("👑----✨YOU ARE THE WINNER✨--🌀")

elif(score_of_user<score_of_system):
    print("BETTER LUCK NEXT TIME")
