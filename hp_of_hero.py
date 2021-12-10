def weak_up_hp (hp):
    if hp <= 100:
        hp += 5
        print(f'ваш уровень hp повысился\nтекущий уровень hp:{hp}')
    else:
        print('у вас итак максимальный уровень хп')
    return hp


def middle_up_hp (hp):
    if hp <= 100:
        hp += 10
        print(f'ваш уровень hp повысился\nтекущий уровень hp:{hp}')
    else:
        print('у вас итак максимальный уровень хп')
    return hp


def strong_up_hp (hp):
    if hp <= 100:
        hp += 15
        print(f'ваш уровень hp повысился\nтекущий уровень hp:{hp}')
    else:
        print('у вас итак максимальный уровень хп')
    return hp
