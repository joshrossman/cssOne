#Task 3: Ensure your code can handle division by zero 
# and other potential errors. So if you divide by 0, 
# there is error handling set up to prevent an error from
#  showing in the console.

#Task 2: Use inputs to ask the user what operation 
# they want to perform, and what numbers they want to use.


#bugs
#If you give bad input, it will not work on the first problems 
# afterwards 
# also need to fix for zero

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x*y

stay=0
while stay==0:
    my_operator=input("What operation would you like to perform? [A]ddition, [S]ubtraction, [M]ultiplication, or [D]ivision?").lower()
    if my_operator=="a" or my_operator=="addition":
        my_operator="a"
    elif my_operator=="s" or my_operator=="subtraction":
        my_operator="s"
    elif my_operator=="m" or my_operator=="multiplication":
        my_operator="m"
    elif my_operator=="d" or my_operator=="division":
        my_operator="d"
    else:
        input("Please make another selection. Not a valid choice!\n")

    num_one = input("Please input your first number:\n")
    num_two = input("Please input your second number:\n")

    if my_operator=="a":
        print(f"{num_one} + {num_two} = {float(num_one)+float(num_two)}")
    elif my_operator=="m":
        print(f"{num_one} * {num_two} = {float(num_one)*float(num_two)}")
    elif my_operator=="s":
        print(f"{num_one} - {num_two} = {float(num_one)-float(num_two)}")
    elif my_operator=="d":
        print(f"{num_one} / {num_two} = {float(num_one)/float(num_two)}")
    
    go_again = ''
    while go_again != "yes" and go_again!="y":
        go_again = input("Would you like to perform another operation? Y/N\n").lower()
        
        if go_again=="n" or go_again=="no":
            stay=1
            break
        else:
            print("Not a valid input")
   
