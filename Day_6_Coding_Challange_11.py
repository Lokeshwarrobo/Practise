'''

A user is asked to enter a list of numbers in an array with size of his own choice .
Then he wants the programmer to give out the elements from the list which are
factors of a number X, given as input from the user. Develop an application
program meeting the required needs.
INPUT FORMAT:
1. First the user gives an integer input for specifying the size of his/her list (array
n)
2. Second line of input takes n elements from the user.
3. Third line of input takes an integer(x) from the user for which the programmer
needs to take out the factors.
OUTPUT FORMAT:
An array of integers which are factors of x.
CONSTRAINTS:
n, x should be a non-negative integers.
SAMPLE INPUT 0:
5
2 14 8 16 36
24
SAMPLE OUTPUT 0:
2 8
EXPLANATION:
2,8 from the given list are factors of 24.

SAMPLE INPUT 1:
10
1 2 3 4 5 6 7 8 9 10
15
SAMPLE OUTPUT:
1 3 5

'''
size = int(input())
array = list(map(int,input().split()[:size]))
target = int(input())
for i in array:
    if target % i == 0:
        print(i, end = ' ')
