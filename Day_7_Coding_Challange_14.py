'''User wants to list out all the Armstrong numbers in the interval given. Develop an
application program to print the Armstrong numbers between the given interval.
ARMSTRONG NUMBER: If the sum of cubes of each digit is equal to the number
itself, then it is said to be an Armstrong number.
E,g 153 is an Armstrong number as 13+53+33=153, the number itself.
INPUT FORMAT:
User must give the intervals for finding the Armstrong numbers in between.
OUTPUT FORMAT:
Print all the Armstrong numbers between x and y
SAMPLE INPUT 0:
100 200
SAMPLE OUTPUT 0:
153
SAMPLE INPUT 1:
10 500
SAMPLE OUTPUT:
153 370 371 407
'''
lower , upper = map(int, input().split())
for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))

   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

