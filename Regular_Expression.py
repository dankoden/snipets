import re
import datetime
# .             О дин любой символ, кроме новой строки \n.
# ?             0 или 1 вхождение шаблона слева
# +             1 и более вхождений шаблона слева
# *             0 и более вхождений шаблона слева
# \w            Любая цифра или буква (\W — все, кроме буквы или цифры)
# \d            Любая цифра [0-9] (\D — все, кроме цифры)
# \s            Любой пробельный символ (\S — любой непробельный символ)
# \b            Граница слова
# [..]          Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# \             Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
# ^ и $         Начало и конец строки соответственно
# {n,m}         От n до m вхождений ({,m} — от 0 до m)
# a|b           Соответствует a или b
# ()            Группирует выражение и возвращает найденный текст
# \t, \n, \r    Символ табуляции, новой строки и возврата каретки соответственно


S = "Привет как дела как"
MAIL = "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com"
DATE = str(datetime.date.today())



a = re.findall(r"\w+",S) # ----> ['Привет', 'как', 'дела', 'как']

b = re.findall(r"\w*",S) # ----> ['Привет', '', 'как', '', 'дела', '', 'как', '']

c = re.findall(r"\w",S) # ----> ['П', 'р', 'и', 'в', 'е', 'т', 'к', 'а', 'к', 'д', 'е', 'л', 'а', 'к', 'а', 'к']

d = re.findall(r".",S) # ----> ['П', 'р', 'и', 'в', 'е', 'т', ' ', 'к', 'а', 'к', ' ', 'д', 'е', 'л', 'а', ' ', 'к', 'а', 'к']

e = re.findall(r'^\w+',S) # ----> ['Привет']

f = re.findall(r'\w+$',S) # ----> ['как']

g = re.findall(r'\w\w',S) # ----> ['Пр', 'ив', 'ет', 'ка', 'де', 'ла', 'ка']

h = re.findall(r'\b\w.',S) # ----> ['Пр', 'ка', 'де', 'ка']

i = re.findall(r'@\w+',MAIL) # ----> ['@gmail', '@test', '@analyticsvidhya']

j = re.findall(r'@\w+.\w+',MAIL) # ----> ['@gmail.com', '@test.in', '@analyticsvidhya.com']

k = re.findall(r'@\w+.(\w+)',MAIL) # ----> ['com', 'in', 'com']

l = re.findall(r'\d{4}-\d{2}-\d{2}',DATE) # ----> ['2021-11-19']

m = re.findall(r'(\d{4})-\d{2}-\d{2}',DATE) # ----> ['2021']

n = re.findall(r'[Пк]\w+',S) # ----> ['Привет', 'как', 'как']

o = re.findall(r'\b[Пк]\w+',S) # ----> ['Привет', 'как', 'как'] нету обрезынных слов (\b  срез слова)

p = re.findall(r'\b[^Пк ]\w+',S) # ----> ['дела']

r = re.match(r".[1-9]{1}[0-9]{11}","+380985657530") # ----> return None if nor right, else return +380985657530

print(r.group(0))