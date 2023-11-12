import sqlite3
cunn = sqlite3.connect('artistc.db')
cursor = cunn.cursor()
cursor.execute('SELECT Name FROM artists')
l = cursor.fetchall()
cursor.execute('SELECT gender FROM artists WHERE gender == "Female"')
fem = cursor.fetchall()
cursor.execute('SELECT Name FROM artists WHERE ')
age = cursor.fetchall()
print(len(l))
print(len(fem))
print(age)

# cursor.fetchall()
# Вопрос 1. Информация о скольких художниках представлена в базе данных? 


# Вопрос 2. Сколько женщин (Female) в базе?


# Вопрос 3. Сколько человек в базе данных родились до 1900 года?


# Вопрос 4*. Как зовут самого пожилого художника?