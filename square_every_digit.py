def square_digits(num):
    s = ''
    for i in str(num):
        s += str((int(i)**2))
    return int(s)

if square_digits(9119) == 811181:
    print('yes')
