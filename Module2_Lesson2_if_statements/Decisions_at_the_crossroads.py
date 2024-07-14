#Task 1: Code Correction You are provided with a Python script 
# that uses conditional statements to tell if a number is positive, 
# negative, or zero, but it has some errors. Identify and fix them.
#Buggy Code:
#number = input("Enter a number: ")
#if number > 0:
#    print("The number is positive.")
#elif number = 0:
#    print("The number is zero.")
#else number < 0:
#    print("The number is negative.")

number=''
error_checker=False

while error_checker == False:
    try:
       number = input("Enter a number: ") 
       number = float(number) 
       error_checker=True
    except: 
        print("Please input a number!")

number = float(number)
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")
