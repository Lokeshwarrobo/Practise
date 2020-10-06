'''
Adia wants to develop a calculator which returns factorial of the given number.
If the number is less than 0 then it will return -1. If the number is equal to 0, it returns
1 and if the number is greater than 0 it returns the factorial of that number.
So, work along with her to crack the logic.
Input format:
The line contains an integer “num”.
Output format:
1. If the number is less than 0 it should -1.
2. If the number is greater than 0 it should return the factorial of the given number.
Sample input 0:
10
Sample output 0:
3628800
Sample input 1:
20
Sample output 1:
2432902008176640000
'''
num = int(input())
factorial = 1
if num < 0:
    print(-1)
else:
    for i in range(1, num+1):
        factorial = factorial * i

    print(factorial)

#Time Complexcity : O(N)
