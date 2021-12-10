def f():
    answ1 = str(input('ответ1'))
    answ2 = str(input('ответ2'))
    answ3 = str(input('ответ3'))
    answ4 = str(input('ответ4'))
    answ5 = str(input('ответ5'))
    q1,q2,q3,q4,q5 = '1', '2', '3', '4', '5'
    right = 0
    if q1 == answ1.lower():
        right = right + 1
    if q2 == answ2.lower():
        right += 1
    if q3 == answ3.lower():
        right += 1
    if q4 == answ4.lower():
        right += 1
    if q5 == answ5.lower():
        right += 1

    if right == 1:
        print('ваш отец разозлен, ваша оценка', right)
    elif right == 2:
        print('ваш отец разозлен, ваша оценка', right)
    elif right == 3:
        print('ваш отец разозлен, ваша оценка', right)
    elif right == 4:
        print('ваш отец разозлен, ваша оценка', right)
    elif right == 5:
        print('ваш отец разозлен, ваша оценка', right)


f()