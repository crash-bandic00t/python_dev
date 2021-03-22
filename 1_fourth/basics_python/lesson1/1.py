# Человеко-ориентированное представление интервала времени
sec = int(input('Введите число секунд\n')) 
min = sec // 60
if min >= 1:
    sec = sec - min * 60
    hour = min // 60
    if hour >= 1:
        min = min - hour * 60
        day = hour // 24
        if day >= 1:
            hour = hour - day * 24
            month = day // 30
            if month >= 1:
                day = day - month * 30
                year = month // 12
                if year >= 1:
                    print('Больше года')
                else:
                    print(f'{month} мес {day} дн {hour} ч {min} мин {sec} сек')
            else:
                print(f'{day} дн {hour} ч {min} мин {sec} сек')
        else:
            print(f'{hour} ч {min} мин {sec} сек')
    else:
        print(f'{min} мин {sec} сек')
else:
    print(f'{sec} сек')
