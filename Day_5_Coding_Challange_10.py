'''
Akash wants to check the whether he can count the number of vowels,
consonants, digits, white spaces in a sentence that he is going to enter?
Sample Input 0:
Placement Key
Sample Output 0:
Vowels : 4
Consonants : 8
Digits : 0
White Spaces : 1


Sample Input 1: Code Challenge3
Sample Output 1:
Vowels : 5
Consonants : 8
Digits : 1
White Spaces : 1
'''
string = 'Code Challenge3'

v = c = d = ws = 0
for i in string.lower():
    if i in 'aeiou':
        v += 1
    if i.isnumeric():
        d += 1
    elif i == ' ':
        ws += 1
    elif i in 'bcdfghjklmnpqrstvwxyz':
        c += 1
print('Vowels : ', v)
print('Consonants : ', c)
print('Digits : ', d)
print('White Spaces : ', ws)

