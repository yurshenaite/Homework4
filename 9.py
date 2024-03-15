breed = input('Собака короткошерстной породы? ')
if breed == 'да':
    height = input('Рост собаки менее 50 см? ')
    if height == 'да':
        tail = input('У собаки короткий хвост? ')
        if tail == 'да':
            print('английский бульдог')
        else:
            ears = input('У собаки длинные уши? ')
            if ears == 'да':
                print('гончая')
            else:
                body = input('У собаки короткое тело? ')
                if body == 'да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        weight = input('Собака весит более 50 кг? ')
        if weight == 'да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    height = input('Рост собаки менее 50 см? ')
    if height == 'да':
        character = input('У собаки доброжелательный характер? ')
        if character == 'да':
            print('кокер- спаниель')
        else:
            print('ирландский сеттер')
    else:
        high = input('У собаки рост менее 70 см? ')
        if high == 'да':
            ears_1 = input('У собаки длинные уши? ')
            if ears_1 == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            white = input('Окрас рыжий с белыми отметинами? ')
            if white == 'да':
                print('сенбернар')
            else:
                color = input('Белоснежный окрас? ')
                if color == 'да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')