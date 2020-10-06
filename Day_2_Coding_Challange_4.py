'''
Jaswanth wants to find the second largest number in the array store. Based on this
he is developing the application. So, help him to build the logic which helps him to
develop the application.
Input:
The first line contains an integer T, total number of elements. Then follow T integers.
Output:
Display the second largest among the given T integers.
Constraints
1 ≤ T ≤ 1000
1 ≤ integers ≤ 1000000
Sample Input 0:
7
23 45 7 34 25 25 89
Sample Output 0:
45
Sample input 1:
10
10 5 10 19 100 15 16 24 22 24
Sample output 1:
24
'''
size = int(input())  # Takes the size of array
array = list(map(int,input().split()[:size])) # Takes the elements into an array
array.sort()
print(array[-2])

#First sort the array
#Second print the second element from last
