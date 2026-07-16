# # # import requests
# # # from bs4 import BeautifulSoup
# # # import pandas as pd
# # # import re
# # #
# # # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
# # #
# # #
# # # def scrape_akyol_n():
# # #     """
# # #     Парсинг товаров с сайта Akyol с обновлённой логикой.
# # #     """
# # #     base_url = "https://akyol.com.tm/category/persnonalnye-kompyutery/category_2/?page="
# # #     product_data = []
# # #     page = 1
# # #
# # #     while True:
# # #         # Формирование URL для текущей страницы
# # #         url = f"{base_url}{page}"
# # #         print(f"Обработка страницы: {url}")
# # #
# # #         try:
# # #             response = requests.get(url, headers=headers)
# # #             response.raise_for_status()  # Проверка успешного выполнения запроса
# # #         except requests.RequestException as e:
# # #             print(f"Ошибка при запросе страницы {url}: {e}")
# # #             break
# # #
# # #         # Парсинг HTML
# # #         soup = BeautifulSoup(response.text, 'html.parser')
# # #
# # #         # Поиск товаров на странице
# # #         products = soup.find_all('div', class_='js-product-item')
# # #         if not products:
# # #             print(f"Товары не найдены на странице {page}. Завершение.")
# # #             break
# # #
# # #         for product in products:
# # #             # Название товара
# # #             name_element = product.find('div', class_='product-tile__name')
# # #             name = name_element.text.strip() if name_element else "Название не указано"
# # #
# # #             # Исходная цена
# # #             original_price_element = product.find('div', class_='product-price')
# # #             original_price = (
# # #                 f"{original_price_element.find('span', class_='price').text.strip()} {original_price_element.find('span', class_='currency').text.strip()}"
# # #                 if original_price_element else "-"
# # #             )
# # #
# # #             # Цена со скидкой
# # #             discounted_price_element = product.find('div', class_='product-price-compare')
# # #             discounted_price = (
# # #                 f"{discounted_price_element.find('span', class_='price').text.strip()} {discounted_price_element.find('span', class_='currency').text.strip()}"
# # #                 if discounted_price_element else "-"
# # #             )
# # #
# # #             # Наличие товара
# # #             stock_available = product.find('div', class_='product-stock product-tile__stock')
# # #             stock_unavailable = product.find('div', class_='product-stock product-stock--none product-tile__stock')
# # #             availability = ''
# # #             if stock_unavailable:
# # #                 availability = "Нет в наличии"
# # #                 discounted_price = "-"
# # #                 original_price = "-"
# # #             elif stock_available:
# # #                 availability = "В наличии"
# # #
# # #             # Сохранение данных с правильным порядком столбцов
# # #             product_data.append({
# # #                 "Название": name,
# # #                 "Реальная цена": original_price,  # Сначала реальная цена
# # #                 "Цена со скидкой": discounted_price,  # Потом цена со скидкой
# # #                 "Наличие": availability
# # #             })
# # #
# # #         print(f"Собрано {len(products)} товаров с {page}-й страницы.")
# # #         page += 1
# # #
# # #     return pd.DataFrame(product_data)
# # #
# # #
# # # def unify_data_format(df):
# # #     """
# # #     Приведение данных к единому формату:
# # #     - Приводит названия столбцов к стандартным.
# # #     - Убирает лишние пробелы и символы в названиях товаров.
# # #     - Преобразует цены в числовой формат (где возможно).
# # #     - Удаляет дубликаты.
# # #     """
# # #     # Очистка названий моделей
# # #     def clean_name(name):
# # #         if isinstance(name, str):
# # #             return re.sub(r'\s+', ' ', name.replace('\n', ' ').strip())
# # #         return name
# # #
# # #     df['Название'] = df['Название'].apply(clean_name)
# # #
# # #     # Очистка цен и преобразование в числовой формат
# # #     def extract_price(price):
# # #         if isinstance(price, str):
# # #             match = re.search(r'\d+', price.replace(',', ''))
# # #             return int(match.group()) if match else float('inf')
# # #         return price
# # #
# # #     df['Реальная цена'] = df['Реальная цена'].apply(extract_price)
# # #     df['Цена со скидкой'] = df['Цена со скидкой'].apply(extract_price)
# # #
# # #     # Удаление дубликатов
# # #     df.drop_duplicates(subset=['Название', 'Реальная цена', 'Цена со скидкой'], inplace=True)
# # #
# # #     return df
# # #
# # #
# # # def filter_by_manufacturer_from_web(manufacturer):
# # #     """
# # #     Основная функция для:
# # #     1. Парсинга данных с сайта Akyol.
# # #     2. Приведения данных к единому стандарту.
# # #     3. Фильтрации по производителю.
# # #     4. Сортировки по цене.
# # #     """
# # #     # Получение данных с сайта Akyol
# # #     akyol_data = scrape_akyol_n()
# # #
# # #     # Приведение данных к единому формату
# # #     akyol_data = unify_data_format(akyol_data)
# # #
# # #     # Фильтрация по производителю
# # #     filtered_data = akyol_data[akyol_data['Название'].str.contains(manufacturer, case=False, na=False)]
# # #
# # #     # Сортировка по реальной цене (если указана) или цене со скидкой
# # #     filtered_data['Цена для сортировки'] = filtered_data[['Цена со скидкой', 'Реальная цена']].min(axis=1)
# # #     filtered_data.sort_values(by='Цена для сортировки', inplace=True)
# # #     filtered_data.drop(columns=['Цена для сортировки'], inplace=True)
# # #
# # #     return filtered_data
# # #
# # #
# # # # Пример использования:
# # # manufacturer_name = "Dell"
# # # result = filter_by_manufacturer_from_web(manufacturer_name)
# # #
# # # # Вывод результата
# # # print(result)
# # #
# # # # Сохранение результата в файл
# # # result.to_csv(f"filtered_{manufacturer_name}_akyol.csv", index=False, encoding="utf-8")
# # # print(f"Данные сохранены в файл 'filtered_{manufacturer_name}_akyol.csv'")
# #
# #
# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd
# #
# # # Заголовки для имитации браузера
# # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
# #
# # def scrape_notebookmerkezi_by_manufacturer(manufacturer):
# #     """
# #     Функция для парсинга товаров с сайта NotebookMerkezi, фильтрации по производителю и сохранения результата в CSV.
# #     """
# #     # URL категорий NotebookMerkezi
# #     categories = [
# #         "https://notebookmerkezi.com.tm/category/53",
# #         "https://notebookmerkezi.com.tm/category/55",
# #         "https://notebookmerkezi.com.tm/category/54"
# #     ]
# #     all_data = []  # Для хранения данных
# #
# #     def scrape_category(base_url):
# #         """Функция для обработки одной категории товаров."""
# #         page = 1
# #         seen_products = set()  # Для проверки уникальности товаров
# #         data = []  # Список для хранения данных одной категории
# #
# #         while True:
# #             url = f"{base_url}?page={page}"
# #             print(f"Обрабатываем страницу: {url}")
# #             try:
# #                 response = requests.get(url, headers=headers)
# #                 response.raise_for_status()  # Проверка успешного запроса
# #             except requests.RequestException as e:
# #                 print(f"Ошибка при запросе страницы {url}: {e}")
# #                 break
# #
# #             soup = BeautifulSoup(response.text, 'html.parser')
# #             products = soup.find_all('div', class_='product-item')
# #             if not products:
# #                 print(f"Товары не найдены на странице {page}. Завершение категории.")
# #                 break
# #
# #             for product in products:
# #                 # Извлечение названия товара
# #                 title = product.find('div', class_='product-item__name').text.strip() if product.find('div', class_='product-item__name') else "Нет названия"
# #
# #                 # Извлечение основной цены
# #                 price_span = product.find('div', class_='product-item__price').find('span') if product.find('div', class_='product-item__price') else None
# #                 price = price_span.text.strip() if price_span else "Нет в наличии"
# #
# #                 # Извлечение цены со скидкой
# #                 discount_price_span = product.find('div', class_='product-item__discount-price').find('span') if product.find('div', class_='product-item__discount-price') else None
# #                 discount_price = discount_price_span.text.strip() if discount_price_span else "-"
# #
# #                 # Проверка уникальности
# #                 if title in seen_products:
# #                     continue
# #                 seen_products.add(title)
# #
# #                 # Определение наличия
# #                 if price == "Нет в наличии":
# #                     availability = "Нет в наличии"
# #                     price = "-"
# #                     discount_price = "-"
# #                 else:
# #                     availability = "В наличии"
# #
# #                 # Сохранение данных
# #                 data.append({"Название": title, "Цена": price, "Цена со скидкой": discount_price, "Наличие": availability})
# #             page += 1
# #
# #         return data
# #
# #     # Обработка всех категорий
# #     for category in categories:
# #         print(f"Обрабатываем категорию: {category}")
# #         category_data = scrape_category(category)
# #         all_data.extend(category_data)
# #
# #     # Приведение данных к общему формату и фильтрация по производителю
# #     df = pd.DataFrame(all_data)
# #     df['Название'] = df['Название'].str.lower().str.strip()  # Приведение названий к нижнему регистру
# #     manufacturer = manufacturer.lower().strip()  # Приведение фильтра к нижнему регистру
# #     filtered_df = df[df['Название'].str.contains(manufacturer, na=False)]  # Фильтрация по производителю
# #
# #     # Сохранение результата
# #     output_file = f"notebookmerkezi_filtered_{manufacturer}.csv"
# #     filtered_df.to_csv(output_file, index=False, encoding='utf-8')
# #     print(f"Данные сохранены в файл: {output_file}")
# #     return filtered_df
# #
# #
# # # Пример вызова функции
# # manufacturer = "HP"  # Производитель для фильтрации
# # result_df = scrape_notebookmerkezi_by_manufacturer(manufacturer)
#
#
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# # Заголовки для имитации браузера
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
# }
#
#
# def scrape_nts_computers_by_manufacturer(manufacturer):
#     """
#     Парсит данные с сайта NTS Computers, фильтрует товары по производителю и сохраняет результат в CSV.
#     """
#     # URL каталога товаров NTS Computers
#     base_urls = [
#         'https://www.nts-computers.com/notebooks/acer_notebooks/',
#         'https://www.nts-computers.com/notebooks/dell_notebooks/',
#         'https://www.nts-computers.com/notebooks/hp_notebooks/',
#         'https://www.nts-computers.com/notebooks/lenovo_notebook/'
#     ]
#
#     all_products = []
#
#     # Обход всех категорий
#     for base_url in base_urls:
#         print(f"Сканируем каталог: {base_url}")
#         page = 1
#
#         while True:
#             url = f"{base_url}?page={page}"
#             print(f"Сканируем страницу: {url}")
#
#             try:
#                 response = requests.get(url, headers=headers)
#                 response.raise_for_status()  # Проверка успешности запроса
#             except requests.RequestException as e:
#                 print(f"Ошибка при доступе к {url}: {e}")
#                 break
#
#             soup = BeautifulSoup(response.text, 'html.parser')
#
#             # Находим товары на странице
#             products = soup.find_all('div', class_='product-thumb')
#             if not products:
#                 print(f"Товары не найдены на странице {page}. Завершение.")
#                 break
#
#             for product in products:
#                 # Название товара
#                 name_tag = product.find('h4').find('span', itemprop='name')
#                 name = name_tag.text.strip() if name_tag else "Название не указано"
#
#                 # Парсинг цен
#                 price_container = product.find('div', class_='price', itemprop='offers')
#                 original_price = "-"
#                 discounted_price = "-"
#
#                 if price_container:
#                     # Проверяем наличие тега с оригинальной ценой (для товаров со скидкой)
#                     original_price_tag = price_container.find('span', class_=lambda x: x and 'price-old' in x)
#                     if original_price_tag:
#                         # Если тег с "price-old" есть, это товар со скидкой
#                         original_price = original_price_tag.text.strip()
#
#                         # Ищем цену со скидкой
#                         discount_tag = price_container.find('span', class_=lambda x: x and 'price_no_format' in x)
#                         if discount_tag:
#                             discounted_price = discount_tag.text.strip()
#                     else:
#                         # Если скидки нет, ищем просто текущую цену
#                         price_tag = price_container.find('span', class_=lambda x: x and 'price_no_format' in x)
#                         if price_tag:
#                             original_price = price_tag.text.strip()
#
#                 # Наличие товара (по умолчанию "Нет информации о наличии")
#                 availability = "Нет информации о наличии"
#
#                 # Сохранение данных
#                 all_products.append({
#                     "Название товара": name,
#                     "Реальная цена": original_price,
#                     "Цена со скидкой": discounted_price,
#                     "Наличие": availability
#                 })
#
#             page += 1  # Переход на следующую страницу
#
#     # Преобразование в DataFrame
#     df = pd.DataFrame(all_products)
#
#     # Приведение названий к единому регистру
#     df['Название товара'] = df['Название товара'].str.lower().str.strip()
#
#     # Фильтрация по производителю
#     manufacturer = manufacturer.lower().strip()
#     filtered_df = df[df['Название товара'].str.contains(manufacturer, na=False)]
#
#     # Сохранение результата
#     output_file = f"nts_computers_filtered_{manufacturer}.csv"
#     filtered_df.to_csv(output_file, index=False, encoding='utf-8')
#     print(f"Данные сохранены в файл: {output_file}")
#
#     return filtered_df
#
#
# # Пример вызова функции
# manufacturer = "HP"  # Укажите производителя
# result_df = scrape_nts_computers_by_manufacturer(manufacturer)