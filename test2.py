# Створити репозиторій та запушити вашу домашку на GitHub!
# Отримати текст головного заголовка (h1):
#   Очікуваний результат: "Welcome to Our Website"
# Отримати перелік послуг (li) з розділу "Our Services":
#   Очікуваний результат(list): ["Web Development", "Mobile App Development", "SEO", "Graphic Design"]
# Отримати текст з футера, а саме з його параграфу(тег <p>): "© 2023 Our Website. All rights reserved."

from bs4 import BeautifulSoup

path_to_my_file = "C:\\Users\\HP\\Python_0\\testg\\example1.html"

with open(path_to_my_file, encoding='utf-8') as file:
    soup = BeautifulSoup(file, "html.parser")

for data in soup.find(id="main-title"):
    print(data.text)

for data in soup.find(id="services-section"):
    print(data.text)

for data in soup.select("footer > p"):
    print(data.text)



