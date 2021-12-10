def weak_rep_down(reputation):
    reputation += 10
    print('вас ударили\nваш уровень репутации', reputation)
    if reputation < 30:
        pass
        # TODO добавить скрипт по слишком сильном уменьшении репутации
    return reputation


def middle_rep_down(reputation):
    reputation += 10
    print('вас ощутимо ударили\nваш уровень хп', reputation)
    if reputation < 30:
        pass
    return reputation


def high_rep_down(reputation):
    reputation += 20
    print('вас сильно покалечили\nваш уровень хп', reputation)
    if reputation < 30:
        pass
    return reputation

def weak_rep_up(reputation):
    reputation += 10
    print('вас ударили\nваш уровень репутации', reputation)
    if reputation > 30:
        pass
        # TODO добавить скрипт по слишком сильном увеличении репутации
    return reputation


def middle_rep_up(reputation):
    reputation += 10
    print('вас ощутимо ударили\nваш уровень хп', reputation)
    if reputation > 30:
        pass
    return reputation


def high_rep_up(reputation):
    reputation += 20
    print('вас сильно покалечили\nваш уровень хп', reputation)
    if reputation > 30:
        pass
    return reputation
