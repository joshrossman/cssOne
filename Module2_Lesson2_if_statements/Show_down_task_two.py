#Task 2: Identify the Smallest Improve upon your code from 
# Task 1 to also determine the smallest number among the three and 
# print it out.
# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print 
# out that "The smallest number is 3. The largest number is 4. "


print("Please input three numbers:")
number_one,number_two,number_three='','',''

#check the user is inputting numbers
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

#collect three numbers
number_one=check_for_error(number_one)
number_two=check_for_error(number_two)
number_three=check_for_error(number_three)

highest = ""
lowest = ""
equal=False

#check if all numbers are equal
if number_one==number_two==number_three:
    equal=True

#find and print the highest and lowest number
if number_one<=number_two<=number_three:
    highest=number_three
    lowest=number_one
elif number_one<=number_three<=number_two:
    highest=number_two
    lowest=number_one
elif number_two<=number_three<=number_one:
    highest=number_one
    lowest=number_two
elif number_two<=number_one<=number_three:
    highest=number_three
    lowest=number_two
elif number_three<=number_one<=number_two:
   highest=number_two
   lowest=number_three  
elif number_three<=number_two<=number_one:
   highest=number_one
   lowest=number_three  
highest=str(highest)+'.'
lowest=str(lowest)+'.'

#print results
if equal:
    print("All numbers are equal!")
else:
    print("The smallest number is:", lowest,"The largest number is ", highest)