point_1, point_2 = map(int, input('Введите итоговый счёт: ').split(':'))
if point_1 > point_2:
    print(1)
elif point_1 < point_2:
    print(2)
else:
    print(0)