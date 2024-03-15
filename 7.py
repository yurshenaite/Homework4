res_1, res_2, res_3 = map(int, input('Введите рекорды каждого игрока: ').split())
if res_1 > res_2 and res_1 > res_3:
    print(res_1)
elif res_2 > res_1 and res_2 > res_3:
    print(res_2)
else:
    print(res_3)