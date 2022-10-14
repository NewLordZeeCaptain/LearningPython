def sum(*numbers):
    res = 0
    for n in numbers:
        res = res + n
    print(f'sum = {res}')


sum(1, 2, 3, 4, 5)
print(1, 2)
