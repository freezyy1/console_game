def weak_up_atk (atk):
    if atk <= 100:
        atk += 5
        print(f'ваш уровень atk повысился\nтекущий уровень hp:{atk}')
    else:
        print('у вас итак максимальный уровень atk')
    return atk


def middle_up_atk (atk):
    if atk <= 100:
        atk += 10
        print(f'ваш уровень atk повысился\nтекущий уровень atk:{atk}')
    else:
        print('у вас итак максимальный уровень atk')
    return atk


def strong_up_atk (atk):
    if atk <= 100:
        atk += 15
        print(f'ваш уровень atk повысился\nтекущий уровень atk:{atk}')
    else:
        print('у вас итак максимальный уровень atk')
    return atk