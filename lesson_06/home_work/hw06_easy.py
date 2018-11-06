import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Figure:
    def __init__(self):
        pass
    def len_line(self, p1, p2):
        return math.sqrt((p1['x'] - p2['x']) ** 2 + (p1['y'] - p2['y']) ** 2)

    def per(self):
        return sum(self.sides.values())

    def len_s(self):
        return self.sides


class Triangle(Figure):
    def __init__(self, a, b, c):
        Figure.__init__(self)
        self.a = {'x': a[0], 'y': a[1]}
        self.b = {'x': b[0], 'y': b[1]}
        self.c = {'x': c[0], 'y': c[1]}
        self.sides = {'ab': self.len_line(self.b, self.a),
                'ac': self.len_line(self.c, self.a),
                'bc': self.len_line(self.c, self.b)}

    def square(self):
        p = self.per() / 2
        return math.sqrt(p * (p - self.sides['ab']) * (p - self.sides['ac']) * (p - self.sides['bc']))

    def hei(self):
        return (2 * self.square()) / self.sides['ab']


triangle_1 = Triangle([2, 2], [3, 5], [5, 3])

print(f'Площадь треугольника: {triangle_1.square()}')
print(f'Высота треугольника: {triangle_1.hei()}')
print(f'Периметр треугольника: {triangle_1.per()}')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class ETrapeze(Figure):
    def __init__(self, a, b, c, d):
        Figure.__init__(self)
        self.a = {'x': a[0], 'y': a[1]}
        self.b = {'x': b[0], 'y': b[1]}
        self.c = {'x': c[0], 'y': c[1]}
        self.d = {'x': d[0], 'y': d[1]}
        self.sides = {'ab': self.len_line(self.b, self.a),
                'bc': self.len_line(self.c, self.b),
                'cd': self.len_line(self.d, self.c),
                'ad': self.len_line(self.d, self.a)}

    def equ(self):
        return True if self.len_line(self.c, self.a) == self.len_line(self.b, self.d) else False

    def square(self):
        s = self
        return ((s.sides['ab'] + s.sides['cd']) / 2) * math.sqrt(s.sides['ad']**2 - (((s.sides['cd'] - s.sides['ab'])**2 + s.sides['ad']**2 - s.sides['bc']**2) / ((s.sides['cd'] - s.sides['ab']) * 2)))
        # part1 = (self.sides['ab'] + self.sides['cd']) / 2
        # part2 = ((self.sides['cd'] - self.sides['ab'])**2 + self.sides['ad']**2 - self.sides['bc']**2) / ((self.sides['cd'] - self.sides['ab']) * 2)
        # return part1 * math.sqrt(self.sides['ad']**2 - part2)


e_trapeze_1 = ETrapeze([2, 4], [4, 4], [5, 2], [1, 2])

print(f'Это равнобочная трапеция: {e_trapeze_1.equ()}')
print(f'Длины сторон трапеции: {e_trapeze_1.len_s()}')
print(f'Длины сторон трапеции: {e_trapeze_1.sides}')
print(f'Площадь трапеции: {e_trapeze_1.square()}')
print(f'Периметр трапеции: {e_trapeze_1.per()}')
