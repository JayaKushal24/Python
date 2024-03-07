#HANGMAN GAME

import random
list_of_names=['suzuki','maruti','volkswagen']
list_of_names.append('bmw')
chosenword= list_of_names[random.randint(0,len(list_of_names)-1)]

print("hint:\t"+chosenword)
list1=[]
for i in range(len(chosenword)):
    list1+="_"
print(list1)

lives=3
while lives>0:
    guess=str(input("enter a letter\n").lower())
    if guess in list1:
       print("U have already guessed the letter")
    for position in range(len(chosenword)):
        letter=chosenword[position]
        if letter==guess:
         list1[position]=letter
    if guess not in chosenword:
       lives-=1
       print(f'The letter "{guess}" is not in the word.\nso,you have {lives} lives left')
    print(list1)
    
    if "_" not in list1:
        print("U WIN")
print("U LOST")
