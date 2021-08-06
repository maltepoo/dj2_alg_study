str_time = input()
time = int(str_time)
b1, b2, b3 = 0, 0, 0

if 9 >= int(str_time[-1]) > 0:
    print('-1')
else:
    b1 += (time // 300)
    time %= 300
    b2 += (time // 60)
    time %= 60
    b3 += (time // 10)
    print(f'{b1} {b2} {b3}')