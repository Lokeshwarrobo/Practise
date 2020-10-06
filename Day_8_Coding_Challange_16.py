'''
User wants to check whether his number is a lucky number or not provided the
number is four-digited. Develop an application program which checks the user’s
four-digited number is either lucky number or not.
A four-digit number PQRS is called LUCKY NUMBER if P+Q =R+S
INPUT FORMAT:
A four digited number input given from the user.
OUTPUT FORMAT:
Print as The given number is a lucky number if it satisfies the conditions of a lucky
number otherwise not
CONSTRAINTS:
The given input must be a non-negative integer and consisting of 4 digits.
SAMPLE INPUT 0:
2341
SAMPLE OUTPUT 0:
The given number is a lucky number.
EXPLANATION:
2+3 = 4+1
SAMPLE INPUT 1:
1234
SAMPLE OUTPUT 1:
The given number is not a lucky number.
EXPLANATION:
1+2 is not equal to 3+4
'''
number = int(input())
numbe = list(map(int,(str(number))))
mid = len(numbe)//2
if sum(numbe[:mid]) == sum(numbe[mid:]):
    print("LUCKY NUMBER")
else:
    print("Not a LUCKY NUMBER")



