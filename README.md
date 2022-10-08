1. Вью функция должна выводить количество уникальных исполнителей (artist) из таблицы tracks.
PATH: /names/

2. Вью функция должна выводить количество записей из таблицы tracks.
PATH: /tracks/

3. Вью функция должна принимать название жанра трека и выводить количество записей этого жанра (genre) из таблицы
   tracks.
PATH: /tracks/<genre>

4. Вью функция должна выводить все названия треков (title) и соответствующую продолжительность трека в секундах (length)
   из таблицы tracks.
PATH: /tracks-sec/

5. Вью функция должна выводить среднюю продолжительность трека и общую продолжительность всех треков в секундах из
   таблицы tracks.
PATH: /tracks-sec/statistics/


To start program open terminal in folder where current process exists
Than run this commands:
1. flask --app flaskr init-db (Initialize database)
2. flask --app flaskr fill-db (Fill db)
3. flask --app flaskr --debug run (Start server)

