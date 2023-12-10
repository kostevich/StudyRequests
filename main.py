#!/usr/bin/env python

#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import CheckPythonMinimalVersion


import requests

#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#

# Проверка поддержки используемой версии Python.
CheckPythonMinimalVersion(3, 11)

#==========================================================================================#
# >>>>> ЗНАКОМСТВО С МЕТОДАМИ REQUESTS <<<<< #
#==========================================================================================#

# Изменим headers get-запросa.
headers = {"User-Agent": "Difficult"}

# Получение ответа на get-запрос и изменение заголовка и параметров.
response = requests.get('https://www.httpbin.org/get', headers=headers, params={'1':'2432'})

# Получение ответа на post-запрос, изменение параметров и информации в json-формате.
response = requests.post('https://www.httpbin.org/post', params={'1':'2432'}, json={'username':'krolik'})

# Проверка правильности выполнения запроса.
response.raise_for_status()

# Вывод тела запроса в формате JSON.
print(response.json())

website = "https://jsonplaceholder.typicode.com/posts/1"
print(requests.get(website).json())

response = requests.put(website, data={"id": 1,"userId": 12, "title": "Мой новый пост", "body": "Хочу и могу"})
print(response.json())


website = "https://jsonplaceholder.typicode.com/posts/1"
print(requests.get(website).json())

response = requests.delete(website, data={"id": 1,"userId": 12, "title": "Мой новый пост"})
print(response.json)