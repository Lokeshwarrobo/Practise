'''
Rajendar is supposed to ask the program developer to find out whether the year
given by him is leap year or not. So, come with an efficient logic to check whether
the input year is leap year or not.
INPUT FORMAT:
User has to enter a number (the year for which he needs to check whether it is
leap or not)
OUTPUT FORMAT:
1. Output a string saying the given number is leap year if it is and the given
number is not a leap year if it is not.
2. Output a message saying Invalid year if the user enters a negative integer.
CONSTRAINTS:
The input number must be a non-negative integer.
SAMPLE INPUT 0:
2000
SAMPLE OUTPUT 0:
The given year is a leap year.
SAMPLE INPUT 1:
200
SAMPLE OUTPUT 1:
The given year is not a leap year
'''
year = int(input())
if (year % 4) == 0 and (year % 100) == 0 and (year % 400) == 0 :
    print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
