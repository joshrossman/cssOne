#Task 1: Identify the Greatest Write a Python program that 
# asks the user to enter three numbers. Your code should then 
# identify and print out the largest number among the three.


print("Please input three numbers:")
number_one,number_two,number_three='','',''

def check_for_error(my_number):
    error_checker=False
    while error_checker == False:
        try:
            my_number = input("Enter a number: ") 
            my_number = float(my_number) 
            error_checker=True
            return my_number
        except: 
            print("Please input a number!")

number_one=check_for_error(number_one)
number_two=check_for_error(number_two)
number_three=check_for_error(number_three)
print(number_one+number_two+number_three)

if number_one<number_two and number_one<number_three:
    print("The smallest number is", number_one)
elif number_two<number_one and number_two<number_three:
    print("The smallest number is", number_two)
elif number_three<number_one and number_three<number_two:
     print("The smallest number is", number_three)
