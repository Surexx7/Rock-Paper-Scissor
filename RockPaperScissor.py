#Rock wins against Scissors
#Scissors wins against Papper
#Papper wins against Rock

import random
rock="🪨"
paper="📃"
scissors="✂️"
gamesymbol=[rock,paper,scissors]

user_choice=int(input("Press\n- 0 for ROCK '🪨'\n- 1 for PAPER '📃'\n- 2 for SCISSORS '✂️'\nEnter your Choice: "))
#print("You choose:",gamesymbol[user_choice])
if user_choice<0 or user_choice>2:
    print("Invalid Input, You Loose..😢😢😢")
else:
     print("You choose:", gamesymbol[user_choice])
     list=[0,1,2]
     computer_choice=random.choice(list)
     print("Computer choose:",gamesymbol[computer_choice])

     if user_choice==0 and computer_choice==2:
         print("YOU WON...🫡✊👏")
     elif user_choice==2 and computer_choice==0:
         print("YOU LOOSE...😢😢😢")
     elif user_choice>computer_choice:
         print("YOU WON...🫡✊👏")
     elif user_choice<computer_choice:
         print("YOU WON...😢😢😢")

     elif user_choice==computer_choice:
         print("ITS DRAW...🫢😁")


