
import random
game=["rock","paper","scissor"]
user_count=0
computer_count=0
for i in range(1,4):
    user1=input("enter your object")
    computer= random.choice(game)
    if user1==computer:
        print("tie🫡🫡🫡")
    elif (user1=="rock" and computer=="scissor") or (user1=="scissor" and computer=="paper") or (user1=="paper" and computer=="rock"):
        user_count+=1
        print("user1 got a point🤩🤩")
    else:
        computer_count+=1
        print("computer got a point😒😒")

if user_count>computer_count:
    print("user win the game😀😍")
else:
    print("computer won the game😏🙄")


    