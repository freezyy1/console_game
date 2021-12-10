import time
from atk_of_hero import *
from edu_of_hero import *
from hp_of_hero import *
from mana_of_hero import *
from reputation_of_hero import *
from punches import *
from find_time import current_time, find_time_of_day

# начальные значения
print('приветствую вас в этой простой консольной игре.')
print('управление: вводите валидные данные, на вопросы y/n вводите либо y либо n')
print('приятной игры')
find_time_of_day(current_time)
name_hero = input('введите имя')
hp = 20
mana = 30
backpack = []
edu = 1
atk = 1
time_of_dialog = int(input('введите количество секунд задержки для комфортного чтения'))
reputation = 1


# старт
def quest_1(hp, mana, backpack, edu, time_of_dialog, atk):
    bonus_item = 'какой-то странный кубок'
    item1 = 'посох отца из его юности'
    q1, q2, q3, q4, q5 = '1', '2', '3', '4', '5'
    right = 0
    time.sleep(time_of_dialog)
    print('день первый')
    time.sleep(time_of_dialog)
    print('вы просыпаетесь в своей комнате\nвокруг все выглядит таким знакомым..')
    time.sleep(time_of_dialog)
    print('вы растете в семье волшебников, скоро выпуск в вашей школе, вы чувствуете волнение')
    time.sleep(time_of_dialog)
    print('вы идете на кухню чтобы позавтракать ')
    time.sleep(time_of_dialog)
    print('ваш отец вдруг начал говорить о своем опыте в алхимии')
    time.sleep(time_of_dialog)
    edu = up_edu(edu)
    print('вы позавтракали, ваш уровень хп повысился')
    time.sleep(time_of_dialog)
    hp = weak_up_hp(hp)
    time.sleep(time_of_dialog)
    print('вы взяли ссобой аптечку')
    hp = middle_up_hp(hp)
    time.sleep(time_of_dialog)
    print(
        'вы приходите в школу, перед вами экзамен по основам магии, '
        'ответьте на вопросы правильно чтобы получить хорошую оценку')
    time.sleep(time_of_dialog)
    answ1 = str(input('ответ1'))
    answ2 = str(input('ответ2'))
    answ3 = str(input('ответ3'))
    answ4 = str(input('ответ4'))
    answ5 = str(input('ответ5'))
    # блок проверок
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
    time.sleep(time_of_dialog)
    if right == 1:
        print('ваш отец разозлен, ваша оценка', right)
    elif right == 2:
        print('ваш отец разозлен, ваша оценка', right)
    elif right == 3:
        print('ваш отец не проявляет эмоция, ваша оценка', right)
    elif right == 4:
        print('он отдает вам  подарок')
        print('ваш отец рад, ваша оценка', right)
        backpack.append(item1)
        middle_up_atk(atk)
    elif right == 5:
        print('ваш отец гордиться вами, ваша оценка', right)
        print('он отдает вам значимый подарок')
        backpack.append(bonus_item)
        backpack.append(item1)
        middle_up_atk(atk)

    time.sleep(time_of_dialog)
    print('уровень завершен, ваши вещи в рюкзаке:')
    print(', '.join(backpack))
    temp_list = [backpack, hp, edu, atk]
    return temp_list


# вызов 1 квеста
w1 = quest_1(hp, mana, backpack, edu, time_of_dialog, atk)
# получаем значения из 1 квеста
backpack = w1[0]
hp = w1[1]
edu = w1[2]
atk = w1[3]


def quest_2(hp, mana, backpack, edu, time_of_dialog, reputation):
    time.sleep(time_of_dialog)
    print('день второй')
    print('за ночь вы накапливаете уровень маны')
    time.sleep(time_of_dialog)
    mana = high_up_mana(mana)
    print('сегодня вам предстоит помочь своим одноклассникам')
    print('вас просят помочь перенести коробки яблок с помощью вашей магии')
    time.sleep(time_of_dialog)
    if len(backpack) == 0:
        print('хаха, у тебя что нет никакого магического оружия?')
        reputation = high_rep_down(reputation)
    else:
        while True:
            print('формат y/n')
            answ = str(input('помочь?'))
            if answ == 'n':
                print('как же так, мы же друзья:(')
                reputation = weak_rep_down(reputation)
                break
            if answ == 'y':
                print('вы помогаете друзьям...')
                time.sleep(5)
                print('вы помогаете друзьям, но у вас тратится уровень маны')
                mana = middle_down_mana(mana)
                break
            else:
                print('невалидные данные')
            # мана спокойно выходит из области видимости
    print('вы успешно помогаете друзьям')
    print('вдруг вы видите учителей')
    while True:
        print('формат y/n')
        answ2 = str(input('подслушать их разговор?'))
        if answ2 == 'n':
            time.sleep(time_of_dialog)
            print('вы просто проходите мимо')
            break
        elif answ2 == 'y':
            time.sleep(5)
            print('вы понимаете, что там идет обычная беседа о чем-то умном.. интегралы и еще прочие странные штуки')
            edu = up_edu(edu)
            print('учителя замечают вас и дают чаполаха')
            hp = weak_punch(hp)
            break

    print('уровень завершен.')
    temp_list = [edu, reputation, mana, hp]
    return temp_list


w2 = quest_2(hp, mana, backpack, edu, time_of_dialog, reputation)
edu = w2[0]
reputation = w2[1]
mana = w2[2]
hp = w2[3]


def quest_3(hp, atk, time_of_dialog):
    enemy_name = 'стриженый'
    enemy_hp = 2
    time.sleep(time_of_dialog)
    print('день третий')
    print(
        'вы вствете с кровати, идете в душ, вскоре выходите на улицу, но вам не дает покоя один задира.'
        '\nон подходит к вам и начинает бой')
    time.sleep(time_of_dialog)
    print(f'а ну-ка, {name_hero}, иди сюда')
    while True:
        if enemy_hp <= 0:
            print('победа')
            break
        print(f'получай! {name_hero}')
        hp = weak_punch(hp)
        enemy_hp -= atk

    time.sleep(time_of_dialog)
    print(f'это было легко, ох уж этот {enemy_name}')
    print('квест завершен')
    temp_list = [hp]
    return temp_list


w3 = quest_3(hp, atk, time_of_dialog)
hp = w3[0]
