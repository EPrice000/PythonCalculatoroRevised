#This program is for Assignment Week 2: Elements of a programming language. Creating a simple calculator.

#About the Program
# Program name     : Wk8P1_Erica_Price.py
# Student Name     : Erica Price
# Course           : ENTD220
# Instructor       : Georgia Brown
# Date             :09-29-2019

#Stored variables and printing an introduction concatenating those variables in a string.
myprogram='My Calculator'
myname='Erica Price'
coursename='ENTD220 I001 Sum 19'
professorname='Professor Georgia Brown'
date='2019-09-29'
class wrfile:
    print("Hello! My name is: ", myname, " and today you will be using", myprogram, "in", coursename, professorname, date)
#Defining addition, subtraction, multiplication, and division
#Providing a user input
#My list/dictionary
# creating a class
class MyClass:
    myList ={"Add": "add","Sub": "sub", "Mul": "mul", "Div": "div"}
    #defining the addition function
    def add (n1,n2):
        return n1 + n2
    print("This first function uses addition")
    n1 = float(input("Enter in your first number: "))
    n2 = float(input("Enter in your second number: "))
    print("The Sum = ", add(n1,n2))
#defining the sub function
    def sub(n1,n2):
        return n1 - n2
    print("This first function uses subtraction")
    n1 = float(input("Enter in your first number: "))
    n2 = float(input("Enter in your second number: "))
    print("The Sub = ", sub(n1,n2))
    #defining the mul function
    def mul(n1,n2):
        return n1* n2
    print("This first function uses multiplication")
    n1 = float(input("Enter in your first number: "))
    n2 = float(input("Enter in your second number: "))
    print("The Mul = ", mul(n1,n2))
#defining the div fucntion
    def div(n1,n2):
        return n1 / n2
    print("This first function uses division")
    n1 = float(input("Enter in your first number: "))
    n2 = float(input("Enter in your second number: "))
    print("The Div = ", div(n1,n2))
#importing the scalc() function
    import Mylib
#defining a function for all operations
    def allInOne(n1,n2):
        return n1 + n2
        return n1 - n2
        return n1 * n2
        return n1 / n2
    print("YOU ARE ABOUT TO GET A LIST OF DICTIONARIES WITH THE RESULTS")
#user input value
    n1 = float(input("Enter in your first number: "))
    n2 = float(input("Enter in your second number: "))
#The results = the value of the key in dictionary based on the defined function
    myList["Add"] = n1 + n2
    myList["Sub"] = n1 - n2
    myList["Mul"] = n1 * n2
    myList["Div"] = n1 / n2
#This prints myList and adds the results value to the keys
    print ("Congrats you've printed the LIST and added the values to the dictionary: ",myList)
#end of class, this prints the class
thisIsMyClass = MyClass()
#Adding test to print along with the variables which stores the class and the list
print("This is from the Class by printing the solutions in mass: ",thisIsMyClass.myList)
#print ("What operations would you like to do? 1 = Add, 2 = Subtract, 3 = Multiplication, 4 = Division")
operator = input("Please Choose Another Type: 1 = Add, 2 = Subtract, 3 = Multiplication, 4 = Division: ")
#the if..elif statments based on the input from the user for operation
if operator == '1':
    #the "try" "except" to check for errors based on a given range to catch and handle exceptions
    #this is the try block from the try to except clause
    try:
        #user input for adding, multiplying, subtracting, and dividing a given number
        x = float(input("Enter in First number: "))
        y = float(input("Enter in Second number: "))

        #if this condition is not met to execute the except
        if (x < -100 or y < -100) and (x > 100 or y > 100):
            """Raise is used to throw an exception based on the condition in the if statement if
the numbers entered is lower than -100 range and/or higher than 100 the except clause is ran the raise
forces an exception"""
            raise ValueError;
        else:
            print(x + y)
            """if the numbers entered are out of range the except clause displays and comes to a halt
"""
    except ValueError:
                print("One or more values entered are not in range.")
                print("Thank You for using our calculator!")
                #the "try" "except" to check for errors based on a given range to catch and handle exceptions
    #this is the try block from the try to except clause
elif operator == '2':
    try:
        x = float(input("Enter in First number: "))
        y = float(input("Enter in Second number: "))
        if (x < -100 or y < -100) and (x > 100 or y > 100):
            """Raise is used to throw an exception based on the condition in the if statement if
the numbers entered is lower than -100 range and/or higher than 100 the except clause is ran the raise
forces an exception"""
            raise ValueError;
        else:
            print(x - y)
            """if the numbers entered are out of range the except clause displays and comes to a halt
"""
    except ValueError:
        print("One or more values entered are not in range.")
        print("Thank You for using our calculator!")

elif operator == '3':
    try:
        x = float(input("Enter in First number: "))
        y = float(input("Enter in Second number: "))
        if (x < -100 or y < -100) and (x > 100 or y > 100):
            """Raise is used to throw an exception based on the condition in the if statement if
the numbers entered is lower than -100 range and/or higher than 100 the except clause is ran the raise
forces an exception"""
            raise ValueError;
        else:
            print(x * y)
            """if the numbers entered are out of range the except clause displays and comes to a halt
"""
    except ValueError:
        print("One or more values entered are not in range.")
        print("Thank You for using our calculator!")
elif operator == '4':
    try:
        x = float(input("Enter your First number: "))
        y = float(input("Enter your Second number: "))
        if (x < -100 or y < -100) and (x > 100 or y > 100):
            """Raise is used to throw an exception based on the condition in the if statement if
the numbers entered is lower than -100 range and/or higher than 100 the except clause is ran the raise
forces an exception"""
            raise ValueError;
        else:
            print(x / y)
            """if the numbers entered are out of range the except clause displays and comes to a halt
"""
    except ValueError:
        print("One or more values entered are not in range.")
        output = x / y
#When the zero shows up in the denominator of a division operation a ZeroDevisionError is raised
    except ZeroDivisionError:
        #output = 0
        print("You cannot divide by Zero: ",)
        print("Thank You for using our calculator!")
#else:
    #print(x / y)
print("Do you want to try another number?")
#This function allows the user to repeat an operation the startOver jumps back to the top to start an operation based on input
def startOver():
    operator = input("Pick a new operation? Add, Sub, Mul, Div: ")
    Add = "Add"
    Sub = "Sub"
    Mul = "Mul"
    Div = "Div"
    x = float(input("Enter in the First Number: "))
    y = float(input("Enter in the Second Number: "))
    #if a certain condition is met
    if  operator == "Add" or operator == "add" or operator == "ADD":
        #sum
        print(x + y)
        startOver()
    elif operator == "Sub" or operator == "sub" or operator == "SUB":
        #diff
        print(x - y)
        startOver()
    elif operator == "Mul" or operator == "mul" or operator == "MUL":
        #multiplication
        print(x* y)
        startOver()
    elif operator == "Div" or operator == "div" or operator == "DIV":
        #division
        print(x/y)
        startOver()
        Add = "Add"
        Sub = "Sub"
        Mul = "Mul"
        Div = "Div"
#After the main calculation is complete, this input prompts for a new operation
operator = input("Which operation do you want to try? Add, Sub, Mul, Div: ")
x = float(input("Enter in the First Number: "))
y = float(input("Enter in the Second Number: "))
if  operator == "Add" or operator == "add" or operator == "ADD":
        print(x + y)

elif operator == "Sub" or operator == "sub" or operator == "SUB":
        print(x-y)
elif operator == "Mul" or operator == "mul" or operator == "MUL":
        print(x*y)
elif operator == "Div" or operator == "div" or operator == "DIV":
        print(x/y)
else:
    #If an input is outside the range of -100 to 100.
    print("Out Of Range, Please enter a number between -100 - 100")
    #This loops all operations based on the user input
add = x + y
while True:
    print("This is a loop adding x + y: ",add)
    add +=1
    break
sub = x - y
while True:
    print("This is a loop subtracting x - y: ", sub)
    sub+=1
    break
mul = x * y
while True:
    print("this is a loop multiplying x * y: ", mul)
    mul+=1
    break
div = x / y
while True:
    print("This is a loop dividing x / y: ", div)
    div+=1
    break
#menu options
menu = {}
Add= "Add"
Sub= "Sub"
Mul = "Mul"
Div = "Div"
#user input
x = float(input("Enter in the First Number: "))
y = float(input("Enter in the Second Number: "))
results = x + y
operation = input("Please select an input (1 2  3 4): ")
if operation == "1":
    print(x + y)
#directory : \Documents\ENTD220Python\
filename = open('myfile.txt', 'w')
#printing the file
print(filename.write("operation"))
print(filename)
file = open("myfile.txt", "r")
print(file)
print("x equals",x,"and y equals",y)
wrfile()
