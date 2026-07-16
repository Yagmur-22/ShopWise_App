# #           №1
# import requests
# from bs4 import BeautifulSoup
#
# # URL сайта
# url = "https://akyol.com.tm"
#
# # Отправляем GET-запрос
# response = requests.get(url)
#
# # Проверяем статус ответа
# if response.status_code == 200:
#     # Создаем объект BeautifulSoup для анализа HTML
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     # Пример: получение всех ссылок на странице
#     links = soup.find_all("a")  # Найти все теги <a>
#     for link in links:
#         href = link.get("href")  # Получить значение атрибута href
#         print(href)
# else:
#     print(f"Ошибка: {response.status_code}")

# #           №2
# import requests
# from bs4 import BeautifulSoup
#
# # URL первой страницы каталога
# url = "https://akyol.com.tm/category/persnonalnye-kompyutery/category_2"
#
# # Отправляем GET-запрос
# response = requests.get(url)
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     # Пример: ищем ссылки в пагинации
#     pagination = soup.find("ul", class_="pagination")  # Класс пагинации может быть разным
#     if pagination:
#         pages = pagination.find_all("a")  # Все ссылки в пагинации
#         page_numbers = [int(page.text) for page in pages if page.text.isdigit()]  # Только числа
#         max_page = max(page_numbers)
#         print(f"Количество страниц: {max_page}")
#     else:
#         print("Пагинация не найдена.")
# else:
#     print(f"Ошибка загрузки страницы: {response.status_code}")

# #           №3
# import requests
#
# url_template = "https://akyol.com.tm/category/persnonalnye-kompyutery/category_2/?page={}"
# page = 1
# while True:
#     response = requests.get(url_template.format(page))
#     if response.status_code != 200 or "No items found" in response.text:  # Проверяем на конец
#         print(f"Обнаружено страниц: {page - 1}")
#         break
#     print(f"Страница {page} существует.")
#     page += 1

# #           №4
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://akyol.com.tm/category/persnonalnye-kompyutery/category_2"
# response = requests.get(url)
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     # Пример: ищем общее количество товаров
#     total_items_tag = soup.find("span", class_="total-items")  # Класс метки с общим числом
#     if total_items_tag:
#         total_items = int(total_items_tag.text.strip())
#         items_per_page = 20  # Например, если на странице 20 товаров
#         total_pages = (total_items + items_per_page - 1) // items_per_page
#         print(f"Количество страниц: {total_pages}")
#     else:
#         print("Метка общего количества товаров не найдена.")
# else:
#     print(f"Ошибка загрузки страницы: {response.status_code}")
