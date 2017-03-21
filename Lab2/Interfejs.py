import Calculator
import sys
calc = Calculator.Calculator()
print("Hi, you want calculate something?[Y/N]")
while True:
    decision = input()
    if decision=='N' or decision=='n':
        print("Godbay")
        sys.exit()
    elif decision=='Y' or decision=='y':
       break
    else:
      print("You click wrong button")
while True:
    Choice = int(input("Addition: 1  Divide: 2   Derivative: 3 Logarithm: 4\n"))
    if Choice==1:
        firstNumber = float(input("First number\n"))
        secondNumber = float(input("Second number\n"))
        print("Result {0}+{1}={2}".format(firstNumber,secondNumber,calc.Addition(firstNumber,secondNumber)))

    elif Choice==2:
        firstNumber = float(input("First number\n"))
        secondNumber = float(input("Second number\n"))
        print("Result {0}/{1}={2}".format(firstNumber,secondNumber,calc.Divide(firstNumber,secondNumber)))

    elif Choice == 3:
        firstNumber = str(input("Function\n"))
        secondNumber = str(input("Level\n"))
        print("Result  pochodna z {0} o stopniu {1}={2}".format(firstNumber, secondNumber, calc.Derivative(firstNumber, secondNumber)))

    elif Choice == 4:
        firstNumber = float(input("First number\n"))
        secondNumber = float(input("Second number\n"))
        print("Result logarytm o podstawie {1} z {0}={2}".format(firstNumber, secondNumber, calc.Logarithm(firstNumber, secondNumber)))

    else:
        print("Wrong button? Choose again")
        continue

    Choice = input("Press 'q' to quit\n")
    if Choice =='q' or Choice == 'Q':
        break
print("GoodBay!!")