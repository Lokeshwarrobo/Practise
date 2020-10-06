'''
Tyler had a list of elements with him and he needs a C developer to extract the
even numbers from that list and know the sum of all those even numbers. Write
an application program according to Tyler’s requirements.
INPUT FORMAT:
1. 1st line of input takes the size of list of elements(n)
2. 2nd line of input takes the elements for the list.
OUTPUT FORMAT:
Application should extract the even numbers from the list and put the total sum
as output to Tyler.
SAMPLE INPUT 0:
6
1 2 4 6 8 9
SAMPLE OUTPUT 0:
20
EXPLANATION:
Even numbers in the list are 2,4,6,8
Sum of them = 2+4+6+8=20
SAMPLE INPUT 1:
10
12 2 3 21 24 25 27 23 5 7
SAMPLE OUTPUT 1:
38
EXPLANATION:
Even numbers in the list are 12,2,24
Sum of them = 12+2+24=38
'''
size = int(input())
array = list(map(int,input().split()[:size]))
sum = 0
for i in array:
    if i % 2 == 0:
        sum += i

print(sum)
