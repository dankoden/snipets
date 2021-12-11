import requests

proxy = {"https://":"localhost:8080","http://":"localhost:8080"}
response = requests.get('https://mail.ru/',proxies=proxy)



