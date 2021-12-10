import os


def weak_punch(hp):
    hp -= 10
    print('вас ударили\nваш уровень хп', hp)
    if hp < 0:
        print('игра окончена, рестарт? y/n')
        a = input('')
        if a == 'y' or 'Y':
            os.system('python main.py')
        else:
            exit()
    return hp


def middle_punch(hp):
    hp -= 10
    print('вас ощутимо ударили\nваш уровень хп', hp)
    if hp < 0:
        print('игра окончена, рестарт? y/n')
        a = input('')
        if a == 'y' or 'Y':
            os.system('python main.py')
        else:
            exit()
    return hp


def strong_punch(hp):
    hp -= 20
    print('вас сильно покалечили\nваш уровень хп', hp)
    if hp < 0:
        print('игра окончена, рестарт? y/n')
        a = input('')
        if a == 'y' or 'Y':
            os.system('python main.py')
        else:
            exit()
    return hp