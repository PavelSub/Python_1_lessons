# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

import collections

class Person():
    def __init__(self, fio):
        self.name = str(fio).split()[1]
        self.surname = str(fio).split()[0]
        self.o = str(fio).split()[2]

    @property
    def fio(self):
        return f'{self.surname} {self.name[0]}. {self.o[0]}.'


class Parents:
    def __init__(self, par_s):
        self.mom = Person(par_s[0])
        self.dad = Person(par_s[1])


class Student(Person):
    def __init__(self, fio, par_s):
        Person.__init__(self, fio)
        self.par_s = par_s


class ClassRoom():
    def __init__(self, class_room, stud_s):
        self.letter = str(class_room).split()[1]
        self.level = str(class_room).split()[0]
        self.stud_s = list(stud_s)

    @property
    def class_room(self):
        return f'{self.level} {self.letter}'


class Teacher(Person):
    def __init__(self, fio, class_rooms):
        Person.__init__(self, fio)
        self.class_rooms = class_rooms


class Discipline:
    def __init__(self, d_name, teach):
        self.d_name = d_name
        self.teach = teach


st_parents = [['Olegova A. I.', 'Olegov B. B.'],
              ['Pupkina O. A.', 'Pupkin V. B.'],
              ['Ivanova I. O.', 'Ivanov A. P.']]
st_parents = [Parents(i) for i in st_parents]

students = [{'n': 'Olegova B. B.', 'p': st_parents[0]},
            {'n': 'Pupkin I. V.', 'p': st_parents[1]},
            {'n': 'Olegova О. B.', 'p': st_parents[0]},
            {'n': 'Ivanov I. A.', 'p': st_parents[2]}]
students = [Student(i['n'], i['p']) for i in students]

class_r = [{'c-n': '8 A', 's_t': students[:2]}, {'c-n': '8 B', 's_t': students[2:]},
           {'c-n': '5 B', 's_t': students[:2]}, {'c-n': '7 A', 's_t': students[2:]}]
class_r = [ClassRoom(i['c-n'], i['s_t']) for i in class_r]

teachers = [Teacher('Vladov V. I.', class_r[:3]),
            Teacher('Nicov N. C.', class_r[3:])]

disciplines = [Discipline('Math', teachers[0]),
               Discipline('Literature', teachers[1])]


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School():
    def __init__(self, s_classes, teach_s, disc_s):
        self.s_classes = s_classes
        self.teach_s = teach_s
        self.disc_s = disc_s

    def s_cl(self):
        return [i.class_room for i in self.s_classes]

    def get_cl_st(self, cl):
        return [[e.fio for e in i.stud_s] for i in self.s_classes if i.class_room == cl][0]

    def get_d_st(self, st):
        cl, d_l = self.get_st_cl(st), []
        for a in self.disc_s:
            [d_l.append(a.d_name) for b in a.teach.class_rooms if b.class_room == cl]
        return d_l

    def get_st_cl(self, st):
        for i in self.s_classes:
            for j in i.stud_s:
                if j.fio == st:
                    return i.class_room

    def get_p_st(self, st):
        p = []
        for i in self.s_classes:
            [p.append(j) for j in i.stud_s if j.fio == st]
        return f'{p[0].par_s.mom.fio} {p[0].par_s.dad.fio}'

    def get_cl_t(self, t):
        l_c = []
        for i in self.teach_s:
            [l_c.append(i.fio) for j in i.class_rooms if j.class_room == t]
        return l_c


school_1 = School(class_r, teachers, disciplines)
print(school_1.s_cl())
print(school_1.get_cl_st('8 A'))
print(school_1.get_d_st('Olegova B. B.'))
print(school_1.get_p_st('Pupkin I. V.'))
print(school_1.get_cl_t('8 A'))

