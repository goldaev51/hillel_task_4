# hillel_task_4

1. Возвращать содержимое файла с python пакетами (requirements.txt):

PATH: /requirements/ - открыть файл requirements.txt и вернуть его содержимое



2. Вывести 100 случайно сгенерированных юзеров (почта + имя)

Например - 'Dmytro aasdasda@mail.com'

( можете использовать - https://pypi.org/project/Faker/ )

PATH: /generate-users/ + GET параметр который регулирует количество юзеров (/generate-users/?count=100)



3. Вывести средний рост, средний вес (см, кг) (из приикрепленного файла hw.csv)

PATH: /mean/

ОБРАТИТЕ ВНИМАНИЕ НА ЕДЕНИЦЫ ИЗМЕРЕНИЯ



4. Вывести количество космонавтов в настоящий момент

(API источник http://api.open-notify.org/astros.json )

(используйте библиотеку https://pypi.org/project/requests/ )

PATH: /space/





Пример запроса на сторонний API

import requests

r = requests.get('https://api.github.com/repos/psf/requests')

r.json()["description"]