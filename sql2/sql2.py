﻿#import os
#from socket import create_connection
#import sqlite3
#import ntpath


#filename = path.abspath(__file__)
#dbdir = filenasme.rstrip('Database_Python.py')
#dbpath = path.join(dbdir, "data.db")
#conn = create_connection(dbpath)


# подключаем модуль случайных чисел
import random

# подключаем модуль для графиков
import plotly
import plotly.graph_objs as go

# сколько денег будет на старте для каждой стратегии
startmoney = 1000000

# коэффициент ставки
c1 = 0.001

# количество побед и проигрышей
win = 0
loose = 0

# количество игр, сыгранный по первой стратегии
games = 0

# статистика для первой стратегии
balance1 = []
games1 = []

# статистика для второй стратегии
balance2 = []
games2 = []

# статистика для третьей стратегии
balance3 = []
games3 = []

# начинаем играть с полной суммой
# первая стратегия — отрицательное матожидание, как в казино
money = startmoney
# пока у нас ещё есть деньги
while money > 0:
    # ставка —  постоянная часть от первоначальной суммы
    bet = startmoney * c1
    # если ставка получилась больше, чем у нас осталось денег — ставим всё, что осталось, чтобы не уйти в минус
    if bet > money:
        bet = money
    # после ставки количество денег уменьшилось
    money -= bet
    
    # записываем очередную игру в статистику — деньги и номер игры 
    balance1.append(money)
    games1.append(len(games1)+1)

    # крутим рулетку, на которой 18 чёрных чисел, 18 красных и одно зеро. Мы ставим на чёрное
    ball = random.randint(1,37)
    # пусть первые 18 будут чёрными — для простоты алгоритма
    # если наша ставка сыграла — мы попали в нужный диапазон
    if ball in range (1,19):
        # получаем назад нашу ставку в двойном размере
        money += bet * 2
        # увеличиваем количество побед
        win += 1
    else:
        # иначе — увеличиваем количество проигрышей
        loose += 1
games = win + loose
# выводим результат игры по первой стратегии
print("Выиграно ставок: " + str(win) + " (" + str(win/games * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/games * 100) + "%). ")

# началась вторая стратегия, тоже стартуем с полной суммой
# вторая стратегия — с нулевым матожиданием
money = startmoney
# обнуляем статистику
win = 0
loose = 0

# начинаем играть с полной суммой
money = startmoney
# играем, пока есть деньги или пока мы не сыграем столько же игр, как и в первый раз
while (money > 0) and (win + loose < games):
    # ставка —  постоянная часть от первоначальной суммы
    bet = startmoney * c1
    # если ставка получилась больше, чем у нас осталось денег — ставим всё, что осталось, чтобы не уйти в минус
    if bet > money:
        bet = money
    # после ставки количество денег уменьшилось
    money -= bet
    
    # записываем очередную игру в статистику — деньги и номер игры 
    balance2.append(money)
    games2.append(len(games2)+1)

    # крутим рулетку, на которой 18 чёрных чисел, 18 красных. Так как всего поровну, матожидание будет равно нулю.
    # Ставим, как и в прошлом случае, на чёрное
    ball = random.randint(1,36)
    # пусть первые 18 будут чёрными — для простоты алгоритма
    # если наша ставка сыграла — мы попали в нужный диапазон
    if ball in range (1,19):
        # получаем назад нашу ставку в двойном размере
        money += bet * 2
        # увеличиваем количество побед
        win += 1
    else:
        # иначе — увеличиваем количество проигрышей
        loose += 1

# выводим результат игры по второй  стратегии
print("Выиграно ставок: " + str(win) + " (" + str(win/games * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/games * 100) + "%). ")



# началась третья стратегия, тоже стартуем с полной суммой
# третья стратегия — с положительным матожиданием
money = startmoney
# обнуляем статистику
win = 0
loose = 0

# начинаем играть с полной суммой
money = startmoney
# играем, пока есть деньги или пока мы не сыграем столько же игр, как и в первый раз
while (money > 0) and (win + loose < games):
    # ставка —  постоянная часть от первоначальной суммы
    bet = startmoney * c1
    # если ставка получилась больше, чем у нас осталось денег — ставим всё, что осталось, чтобы не уйти в минус
    if bet > money:
        bet = money
    # после ставки количество денег уменьшилось
    money -= bet
    
    # записываем очередную игру в статистику — деньги и номер игры 
    balance3.append(money)
    games3.append(len(games3)+1)

    # крутим рулетку, на которой 18 чёрных чисел, 17 красных. Так как чёрных больше, а мы ставим на чёрное, то матожидание будет положительным
    # Ставим, как и в прошлом случае, на чёрное
    ball = random.randint(1,35)
    # пусть первые 18 будут чёрными — для простоты алгоритма
    # если наша ставка сыграла — мы попали в нужный диапазон
    if ball in range (1,19):
        # получаем назад нашу ставку в двойном размере
        money += bet * 2
        # увеличиваем количество побед
        win += 1
    else:
        # иначе — увеличиваем количество проигрышей
        loose += 1

# выводим результат игры по третьей  стратегии
print("Выиграно ставок: " + str(win) + " (" + str(win/games * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/games * 100) + "%). ")

# строим графики
fig = go.Figure()
# для первой стратегии
fig.add_trace(go.Scatter(x=games1, y=balance1, name = "Отрицательное матожидание"))
# для второй
fig.add_trace(go.Scatter(x=games2, y=balance2, name = "Нулевое матожидание"))
# и для третьей
fig.add_trace(go.Scatter(x=games3, y=balance3, name = "Положительное матожидание"))
# выводим графики в браузер
fig.show()
