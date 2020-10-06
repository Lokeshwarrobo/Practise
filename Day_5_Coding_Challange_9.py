num = int(input())
while sum != 1 and sum != 4:
    sum = 0
    c = 1
    while num > 0:
        rem = num%10
        sum += (rem*rem)
        num = num//10
        c += 1
    num = sum

if sum == 1 and c <= 3:
    print('Happy Number')
else:
    print('Unhappy Number')


