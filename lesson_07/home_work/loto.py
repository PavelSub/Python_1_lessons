#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import re


class LotoGame:
    def __init__(self):
        self.player = Player()
        self.comp_p = ComPl()

    def game_start(self):
        meshok = [j for j in range(1, 91)]
        self.player.gen_card()
        self.comp_p.gen_card()
        while len(meshok) > 0:
            n = random.choice(meshok)
            print(f'На этот раз на боченке: {n}, осталось ходов: {len(meshok) - 1} \n')
            meshok.remove(n)
            self.loto_card_info()
            self.player.pl_turn(n)
            self.comp_p.com_turn(n)

    def loto_card_info(self):
        p = self.player.card.copy()
        c = self.comp_p.card.copy()

        print('{:-^40}'.format('Ваша карточка'))
        [print(f'{j: ^40}') for j in [re.sub(r"[][',]|[^1-9]0|\b0", ' ', str(j)) for j in p]]
        print('{:-^40}'.format(''))
        print('{:-^40}'.format('Карточка компьютера'))
        [print(f'{j: ^40}') for j in [re.sub(r"[][',]|[^1-9]0|\b0", ' ', str(j)) for j in c]]
        print('{:-^40}'.format(' '))


class LotoCard:
    def __init__(self):
        self.card = self.gen_card()
        self.numb = 15

    @staticmethod
    def gen_card():
        b, m = [j for j in range(1, 91)], [0, 0, 0, 0]
        random.shuffle(b)
        s1, s2, s3 = b[:5], b[5:10], b[10:15]
        s1.extend(m)
        s1.sort()
        s2.sort()
        s2.extend(m)
        s3.extend(m)
        s3.sort()
        return [s1, s2, s3]

    def f_b(self, n, t):
        f = False
        for e in self.card:
            for el in e:
                if el == n:
                    self.card[list(self.card).index(e)][e.index(el)] = '-'
                    f = True
                    self.numb -= 1
                    if self.numb == 0:
                        print('\nПобедил игрок!!!') if t == 'p' else print('\nПобедил компьютер!!!')
                        quit()
                    return f
        return f


class Player(LotoCard):
    def __init__(self):
        LotoCard.__init__(self)

    def pl_turn(self, n):
        ans, f = input('\nЗачеркнуть цифру? (y/n)'), self.f_b(n, 'p')
        if ans == 'y' or ans == 'Y':
            if f == True:
                print('\nИгра продолжается')
            else:
                print('\nВы проиграли!')
                quit()
        else:
            if f == True:
                print('\nВы проиграли!')
                quit()
            else:
                print('\nИгра продолжается')


class ComPl(LotoCard):
    def __init__(self):
        LotoCard.__init__(self)

    def com_turn(self, n):
        self.f_b(n, 'c')


loto = LotoGame()
loto.game_start()
