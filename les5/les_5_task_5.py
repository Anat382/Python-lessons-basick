
"""
5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()
result = [el for el in src if src.count(el) == 1]
print(result, perf_counter() - start)

start = perf_counter()
unique_brands = []
for el in src:
    if el not in unique_brands:
        unique_brands.append(el)
    else:
        unique_brands.remove(el)
print(unique_brands, perf_counter() - start)


# наиболее оптимальное решение
start = perf_counter()
unique_brands = set()
for el in src:
    if el not in unique_brands:
        unique_brands.add(el)
    else:
        unique_brands.discard(el)
print(unique_brands, perf_counter() - start)
