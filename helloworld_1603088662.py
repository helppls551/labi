# -*- coding: utf-8 -*-
""" Программа использует flask и запускает веб-сервер. 
При запросе к этому серверу он возвращает текст "Привет, Мир!" """
from flask import Flask
import sqlite3 as sq
def index():
    """ Функция возвращает текст документа """
    cunn = sq.connect('Artistc.db')
    cursor = cunn.cursor()
    cursor.execute('SELECT Name FROM artists WHERE "Birth Year" == (?)',[year])
    data = cursor.fetchall()
    result ='<ol>'
    for i in data:
        result += '<li>'+ i[0] + '</li>'
    result += '</ol>'
    return result    


# Создаём объект веб-приложения:
year = int(input('Введите год художника'))
app = Flask(__name__)   # параметр - имя модуля для веб-приложения
                        # значение __name__ содержит корректное имя модуля для текущего файла 
                        # в нём будет значение "__main__", если модуль запускается непосредственно
                        # и другое имя, если модуль подключается

app.add_url_rule('/', 'index', index)   # создаёт правило для URL: 
                                        # при получении GET-запроса на адрес '/' на этом сайте
                                        # будет запускаться функция index (указана третьим параметром)
                                        # и её значение будет ответом на запрос.
                                        # Второй параметр - endpoint, "конечная точка", -
                                        # это строка, которая содержит имя данного правила. 
                                        # Обычно endpoint рекомендуют делать идентичным имени функции, 
                                        # но в сложных приложениях может быть несколько функций с одним именем в разных модулях, 
                                        # и для различения их в пределах всего сайта можно указывать разные endpoint.
if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run() 
