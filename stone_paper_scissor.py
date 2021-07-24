import random

def gameWin(computer, you):
    if computer == you:
        return None

    elif computer == 'stone':
        if you == 'paper':
            return True
        elif you == 'scissor':
            return False 

    elif computer == 'paper':
        if you == 'scissor':
            return True
        elif you == 'stone':
            return False   
             
    elif computer == 'scissor':
        if you == 'stone':
            return True
        elif you == 'paper':
            return False        
        
you = input("your's turn: choose stone(stone), paper(paper) and scissor(scissor) ?  ")
computer = print("computer's turn: choose stone(stone), paper(paper) and scissor(scissor) ?  ")
random_no = random.randint(1,3)
if random_no == 1:
    computer = 'stone'
elif random_no == 2:
    computer = 'paper'
elif random_no == 3:
    computer = 'scissor' 

print(f"computer chose {computer}")

a = gameWin(computer, you)
if a == None:
    print("Tie!")
elif a:
    print("you win!")
else:
    print("you loose!")


           

