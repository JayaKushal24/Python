import random
#for user choices
userinput=int(input("Enter 0 for Rock (or) 1 for Paaper (or) 2 for Scissors\n"))
choices=['Rock','Paper','Scissors']
userchoice=choices[userinput]
print(f"user choice is:     {userchoice}")

#for computer choices
systemresponse=random.randint(0,2)
choices=['Rock','Paper','Scissors']
Systemchoice=choices[systemresponse]
print(f"system choice is :      {Systemchoice}")

#DECSION MAKING
if userinput>2 or userinput<0:
    print("invalid input ")
elif userinput==Systemchoice:
    print("DRAW")
elif userinput==0 and systemresponse==1:
    print("YOU LOSE")
elif userinput==2 and systemresponse==0:
    print("YOU LOSE")
else:
    print("YOU WIN")