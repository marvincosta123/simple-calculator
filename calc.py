#It's a basic calculator that we'll be improving the the knowledge we get from it

import os
import math

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def addition(a,b):
    addition = a + b
    print(addition)
    return addition

def subtration(a,b):
    sub = a - b
    print(sub)
    return sub

def multiplication(a,b):
    multiplication = a * b
    print(multiplication)
    return multiplication

def exponation(a,b):
    exponation = a ** b
    print(exponation)
    return exponation

def division(a,b):
    division = a / b
    print(division)
    return division

def SquareRootA(a):
    SquareRootA = a ** 0.5
    print(SquareRootA)
    return SquareRootA

def SquareRootB(b):
    SquareRootB = b ** 0.5
    print(SquareRootB)
    return SquareRootB

def logA(a):
    logA = math.log(a)
    print(f"Log de A = {logA}")
    return logA

def logB(b):
    logB = math.log(b)
    print(f"Log de B = {logB}")
    return logB

def show_funtionalities():
    print('''
          1 - Addition
          2 - Subtration
          3 - Multiplication
          4 - Division
          5 - Exponation
          6 - Square Root A
          7 - Square Root B
          8 - Log A
          9 - Log B
          10 - Exit''')

def value_AB():
    global a,b
    print('Type a value for A')
    try:
        a = float(input())
    except ValueError:
        print('Type a correct value for A')
    print('Type a value for B')
    try:
        b = float(input())
    except ValueError:
        print('Type a correct value for B')

def ask():
    global answer
    print("Do you want to execute any more operation?")
    answer = input('S/N\n')
    return answer
    

while True:
    clear_screen()
    print('Which one of these operations do you wanna execute?')
    show_funtionalities()
    try:
        choice = int(input())
    except ValueError:
        print('Type a correct option please')
    
    match choice:
        case 1:
            value_AB()
            addition(a,b)
        case 2:
            value_AB()
            subtration(a,b)
        case 3:
            value_AB()
            multiplication(a,b)
        case 4:
            value_AB()
            division(a,b)
        case 5:
            value_AB()
            exponation(a,b)
        case 6:
            value_AB()
            SquareRootA(a)
        case 7:
            value_AB()
            SquareRootB(b)
        case 8:
            value_AB()
            logA(a)
        case 9:
            value_AB()
            logB(b)
        case 10:
            print("Thank you for using our app")
            break
        case _:
            print("Choose a correct value please")
    ask()
    if answer == 'n':
        print("Thank your for using our app")
        break
#clear_screen()