#Task 1: Leap Year Checker Write a Python program that 
# prompts the user to input a year. The program should 
# determine if the given year is a leap year or not and then display 
# an appropriate message. Please note that this is the 
# definition of a leap year: 
# Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, but these centurial years 
# are leap years if they are exactly divisible by 400.

#Expected Outcome: If you test the year 1900, is should be False. 
# The year 2000 should be True. The year 2024 should be True

year=''
def check_for_error():
    error_checker=False
    while error_checker == False:
        try:
            my_number = input("Enter a year:")
            my_number = int(my_number) 
            if 0<=my_number:
                error_checker=True;
                return my_number;
            else:   
                print("Error:Not a valid year!")
        except: 
            print("Error:Not a valid year!")
year=check_for_error()
if year%4==0 and not year/100==year//100 or year%400==0:
    print(True)
else:
    print(False)