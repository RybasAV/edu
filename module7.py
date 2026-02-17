import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

start_data = input("Введите начальную дату в формате дд.мм.гггг (01.09.2025)")
end_data = input("Введите конечную дату в формате дд.мм.гггг (16.09.2025)")

url = f"https://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01235&UniDbQuery.From={start_data}&UniDbQuery.To={end_data}"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

rate_list = soup.find_all("td")
list = []
for element in rate_list:
    list.append(str(element))
for i in range(len(list)):  # обрезаем лишнее
    list[i] = list[i][4:]
    list[i] = list[i][:-5]
list = list[1:]  # обрезаем лишнее
date_list = []
for i in range(0, len(list), 3):  # создаем список с датами
    date_list.append(list[i])
price_list = []
for i in range(2, len(list), 3):  # создаем список со значением курса,
    index = list[i].find(",")  # запятую меняем на точку и сразу переводим в float
    price_list.append(float(list[i][:index] + "." + list[i][index + 1 :]))


plt.plot(date_list[::-1], price_list)
plt.title(f"С {start_data} по {end_data} Динамика курса валюты Доллар США")
plt.xticks(rotation=90)
plt.xlabel("Дата")
plt.ylabel("Стоимость рублей")
plt.tight_layout()
plt.show()
