# install with: $ pip install beautifulsoup4
HTML_DOC = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(HTML_DOC, 'html.parser')

# класс BeautifulSoup() - принимает следующие основные параметры:
# 1 markup="", - Строка или файловый объект, представляющий разметку для анализа.
# 2 features=None,features: желаемые особенности парсера, которые должны быть Это может быть имя конкретного парсера.





# Here are some simple ways to navigate that data structure:
# (Вот несколько простых способов навигации по этой структуре данных:)

a = soup.find_all()  # - список содержащий1 строку( строка:весь переданный в класс html обьэкт (HTML_DOC) )

# def find_all(self, name=None, attrs={}, recursive=True, text=None,
#              limit=None, **kwargs):
#     """Look in the children of this PageElement and find all
#     PageElements that match the given criteria.
#
#     All find_* methods take a common set of arguments. See the online
#     documentation for detailed explanations.
#
#     :param name: A filter on tag name.
#     :param attrs: A dictionary of filters on attribute values.
#     :param recursive: If this is True, find_all() will perform a
#         recursive search of this PageElement's children. Otherwise,
#         only the direct children will be considered.
#     :param limit: Stop looking after finding this many results.
#     :kwargs: A dictionary of filters on attribute values.
#     :return: A ResultSet of PageElements.
#     :rtype: bs4.element.ResultSet
#     """
b = soup.title  # - <title>The Dormouse's story</title> теги + их содержимое в виде строки
c = soup.title.name # title - Название тега. Таким образом через
                              # точку, можно указать название тега и вывести его содержимое
d = soup.title.string  # -The Dormouse's story /достаем строку находящуюся внутри тега
e = soup.title.parent.name # - head - название родительского тега
f = soup.p # - <p class="title"><b>The Dormouse's story</b></p> достаем p тег
g = soup.p['class'] # - ['title'] - список со строки содержимого пареметра class
h = soup.a["href"] # - http://example.com/elsie / достаем а тег, из него содержимое атрибута href

i = soup.find_all('a')
list_of_links = []  #['http://example.com/elsie', 'http://example.com/lacie', 'http://example.com/tillie']
for a in i:
    list_of_links.append(a["href"]) # - Достаем все ссылка с тегов а

j = soup.find(id="link3") # - <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

k = soup.get_text() # - Достаем весь текст из html документа
print(k)

# Пример использования парсинга(НБУ достаем курсы валют)

# from bs4 import BeautifulSoup
# import requests
# web_sheets = "https://bank.gov.ua/ua/markets/exchangerates?date=30.11.2021&period=daily"
# responce = requests.get(web_sheets)
# list_value_name = []
# list_of_exchange= []
# if responce.status_code == 200:
#     html_doc = BeautifulSoup(responce.text,features="html.parser")
#     list_table = html_doc.tbody.find_all("td",{"class":"value-name"})
#     list_value_int = html_doc.find_all("td",{"data-label":"Офіційний курс"})
#     for i in list_table:
#         list_value_name.append(i.a.string.strip())
#     for i in list_value_int:
#         list_of_exchange.append(i.string)
#
#
# for name , values  in zip(list_value_name,list_of_exchange):
#     print(f"{values} гривен  стоит 1 -  {name}")


