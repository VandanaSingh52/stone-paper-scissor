import random

def gameWin(computer, you):
    if computer == you:
        return None

    elif computer == 's':
        if you == 'p':
            return True
        elif you == 'c':
            return False 

    elif computer == 'p':
        if you == 'c':
            return True
        elif you == 's':
            return False   
             
    elif computer == 'c':
        if you == 's':
            return True
        elif you == 'p':
            return False        
        
you = input("your's turn: choose stone(s), paper(p) and scissor(c) ?  ")
computer = print("computer's turn: choose stone(s), paper(p) and scissor(c) ?  ")
random_no = random.randint(1,3)
if random_no == 1:
    computer = 's'
elif random_no == 2:
    computer = 'p'
elif random_no == 3:
    computer = 'c' 

print(f"computer chose {computer}")

a = gameWin(computer, you)
if a == None:
    print("Tie!")
elif a:
    print("you win!")
else:
    print("you loose!")


           

