print(question_1 := 'Здравствуйте! Как Вас зовут?')
answer_1 = input()
print(f'Очень приятно, {answer_1}! Меня зовут Марк')

print(question_2 := 'Сколько Вам лет?')
answer_2 = int(input())
mark_age = 79
difference = mark_age - answer_2
print(f'Да, {answer_1} , я старше Вас на {difference} лет')

print(question_3 := 'Вам нравится программировать?')
answer_3 = input()
if answer_3 == 'да' or answer_3 == 'Да':
    print(f'Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ')
elif answer_3 == 'нет' or answer_3 == 'Нет':
    print(f'Жаль. Я думал, Вы сможете написать интересную программу для меня')