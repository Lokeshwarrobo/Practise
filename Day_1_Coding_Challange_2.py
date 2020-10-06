'''
Given an array, of size, reverse it.
Example: If array = [1,2,3,4,5], after reversing it, array = [5,4,3,2,1].

Input Format:
The first line contains an integer “size”, denoting the size of the array. The next line
contains n(=size) space-separated integers denoting the elements of the array.

Constraints:
1 ≤n ≤ 1000
I ≤ 𝒂𝒓𝒓𝒊𝒕𝒉 ≤1000, where is the 𝒂𝒓𝒓𝒊𝒕𝒉 element of the array.
Output Format:
The output should contain the reverse array of the given array.
Sample Input 0:
6
16 13 7 2 1 12
Sample Output 0:
12 1 2 7 13 16
'''
size = int(input())  # Takes the size of array
array = list(map(int,input().split()[:size])) # Takes the elements into an array
print(array[::-1])



