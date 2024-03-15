n, k = map(int, input('Введите через пробел улов каждого рыбака: ').split())
if n > k:
    print(k)
elif n < k:
    print(n)
else:
    print('Обоим повезло одинаково')