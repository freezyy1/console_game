import datetime


def find_time_of_day(time):
    if time <= 0 and time < 7:
        print('доброе утро, чего это вы так рано зашли в игру?')
    elif 7 <= time <= 11:
        print('доброе утро')
    elif 12 <= time < 17:
        print('добрый день')
    elif 18 <= time < 22:
        print('добрый вечер')
    elif 22 <= time <= 23:
        print('добрый вечер, пора бы спать..')


# datetime realization
def find_time_in_hours():
    a = datetime.datetime.now()
    a = str(a)
    b = a.split()
    counter = 0
    temp_list = []
    for i in b:
        if counter == 1:
            temp_list.append(i)
        counter += 1

    temp_list = str(temp_list)
    temp_list = (temp_list[2:4])
    temp_list = int(temp_list)
    return temp_list


# передаем как параметр текущее время
current_time = find_time_in_hours()
# передаем как параметр введеную строку
