x = int(input('enter number: '))
sum = 0
temp = x

while temp > 0:
    m = temp % 10
    sum += m**3
    temp = temp // 10

if x == sum:
    print('is armstrong number')
else:
    print('not armstrong number')