"""
2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.

"""
from collections import Counter
import pickle


my_log = []
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for i in f:
        my_log.append(i.split('-')[0].strip())

# my_log = my_log * 1000
print(sorted(Counter(my_log).items(), key=lambda x: x[1], reverse=True)[0])
