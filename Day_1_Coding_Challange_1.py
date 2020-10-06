'''
Ranjan wants to develop an application which prints the following pattern based on the required
size. Ranjan got struck while building the logic and somewhere he missed the code. So, help him
in order to print the required pattern as shown below.
Input format:
The first line contains the two integers “m” and “n”.
Output format:
Pattern of required size.
Sample input 0:
3 4
Sample output 0:
*
*3*
*44*
*555*
*6666*
*555*
*44*
*3*
*
Sample input 1:
10 10
Sample output 2:
*
*10*
*1111*
*121212*
*13131313*
*1414141414*
*151515151515*
*16161616161616*
*1717171717171717*
*181818181818181818*
*19191919191919191919*
*181818181818181818*
*1717171717171717*
*16161616161616*
*151515151515*
*1414141414*
*13131313*
*121212*
*1111*
*10*
*
'''
m, n = map(int,input().split())
print(m, n)
print('*')
for i in range(m):
    print('*')
    for j in range(n):
        print(j,end='')

    print('*')
