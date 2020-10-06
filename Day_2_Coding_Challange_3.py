'''
Drishti is working in a Techno company. Drishti was developing an application, where
the application will sort the salaries of the workers in increasing order. So, help him
in building the application in required time.
Input format:
1. The first line of input contains integer “n” which resembles the size of the array.
2. The second line contains “n” number of array elements.
Output format:
The output contains sorted array in increasing manner.
Sample input 0:
5
900 500 100 200 800
Sample output 0:
100 200 500 800 900
Explanation:
Sort the given array in increasing order. Given array=[900, 500, 100, 200, 800].
The array in increasing manner i.e., array=[100, 200, 500, 800, 900]
Sample input 1:
10
1000 900 800 500 600 200 1100 100 200 1200
Sample output 1:
100 200 200 500 600 800 900 1000 1100 1200
'''
size = int(input())  # Takes the size of array
array = list(map(int,input().split()[:size])) # Takes the elements into an array
print(sorted(array))
