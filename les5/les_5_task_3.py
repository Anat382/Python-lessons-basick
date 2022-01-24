"""
3. Есть два списка:
tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей',
'Дмитрий', 'Борис', 'Елена'
]
klasses = [
'9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
кортежи в виде: (<tutor>, None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
"""

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'  # , '10Б', '9А'
]

count_klasses = len(klasses)
count_ftutors = len(tutors)
difcount_ftutors = abs(count_klasses-count_ftutors)

klasses = [klasses + [None] for _ in range(difcount_ftutors) if count_klasses < count_ftutors][0]

n_gen = ((i, n) for i, n in zip(tutors, klasses))
print(type(n_gen), dict(n_gen))
print(type(n_gen), dict(n_gen))
print(dict(zip(tutors, klasses)))
