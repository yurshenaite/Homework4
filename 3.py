print(question := 'Как зовут главного героя романов Яна Флеминга о вымышленном шпионе?')
word = input('Имя персонажа: ')
def answer(word):
    match word:
        case 'Джеймс Бонд' | 'джеймс бонд' | 'Агент 007' | 'агент 007':
            answer = 'Верно'
        case _:
            answer = 'Неверно'
    return answer


result = answer(word)
print(result)