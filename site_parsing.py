import requests
from bs4 import BeautifulSoup
import pandas as pd
import Data_format

# Заголовки для имитации браузера
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}


def scrape_akyol_n():
    base_url = "https://akyol.com.tm/category/persnonalnye-kompyutery/category_2/?page="
    product_data = []
    page = 1

    while True:
        # Формирование URL для текущей страницы
        url = f"{base_url}{page}"
        print(f"Обработка страницы: {url}")

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Проверка успешного выполнения запроса
        except requests.RequestException as e:
            print(f"Ошибка при запросе страницы {url}: {e}")
            break

        # Парсинг HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Поиск товаров на странице
        products = soup.find_all('div', class_='js-product-item')
        if not products:
            print(f"Товары не найдены на странице {page}. Завершение.")
            break

        for product in products:
            # Название товара
            name_element = product.find('div', class_='product-tile__name')
            name = name_element.text.strip() if name_element else "Название не указано"

            # Исходная цена
            original_price_element = product.find('div', class_='product-price')
            original_price = (
                f"{original_price_element.find('span', class_='price').text.strip()} {original_price_element.find('span', class_='currency').text.strip()}"
                if original_price_element else "-"
            )

            # Цена со скидкой
            discounted_price_element = product.find('div', class_='product-price-compare')
            discounted_price = (
                f"{discounted_price_element.find('span', class_='price').text.strip()} {discounted_price_element.find('span', class_='currency').text.strip()}"
                if discounted_price_element else "-"
            )

            # Наличие товара
            stock_available = product.find('div', class_='product-stock product-tile__stock')
            stock_unavailable = product.find('div', class_='product-stock product-stock--none product-tile__stock')
            availability = ''
            if stock_unavailable:
                availability = "Нет в наличии"
                discounted_price = "-"
                original_price = "-"
            elif stock_available:
                availability = "В наличии"

            # Сохранение данных с правильным порядком столбцов
            product_data.append({
                "Название": name,
                "Обычная цена": original_price,  # Сначала реальная цена
                "Цена со скидкой": discounted_price,  # Потом цена со скидкой
                "Наличие": availability
            })

        print(f"Собрано {len(products)} товаров с {page}-й страницы.")
        page += 1

    # Сохранение данных в CSV
    if product_data:
        df = pd.DataFrame(product_data)
        df.to_csv('akyol.csv', index=False, encoding='utf-8')
        print("Данные успешно сохранены в akyol.csv")
    else:
        print("Товары не найдены на сайте Akyol.")


def scrape_and_save_notebook_merkezi_n(output_file='notebookmerkezi.csv'):
    """
    Функция для сбора данных из списка категорий и сохранения их в CSV файл.

    :param output_file: имя выходного файла CSV (по умолчанию 'notebookmerkezi.csv').
    """

    categories = ["https://notebookmerkezi.com.tm/category/53", "https://notebookmerkezi.com.tm/category/55",
                  "https://notebookmerkezi.com.tm/category/54"]

    def scrape_category(base_url):
        """
        Извлекает данные из одной категории.

        :param base_url: URL категории.
        :return: список товаров из категории.
        """
        page = 1
        seen_products = set()  # Храним уникальные товары для проверки повторов
        data = []  # Список для хранения данных

        while True:
            url = f"{base_url}?page={page}"
            print(f"Обрабатываем страницу: {url}")
            response = requests.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')

            # Находим товары на странице
            products = soup.find_all('div', class_='product-item')
            if not products:
                print(f"Нет товаров на странице {page}. Завершаем обработку категории {base_url}.")
                break

            new_products_found = False  # Проверка, найдены ли новые товары

            for product in products:
                title = product.find('div', class_='product-item__name').text.strip() if product.find('div',
                                                                                                      class_='product-item__name') else 'Нет названия'

                # Извлекаем основную цену
                price_span = product.find('div', class_='product-item__price').find('span') if product.find('div',
                                                                                                            class_='product-item__price') else None
                price = price_span.text.strip() if price_span else 'Нет в наличии'

                # Извлекаем цену со скидкой
                discount_price_span = product.find('div', class_='product-item__discount-price').find(
                    'span') if product.find('div', class_='product-item__discount-price') else None
                discount_price = discount_price_span.text.strip() if discount_price_span else '-'

                # Проверка уникальности товара
                if title in seen_products:
                    continue
                seen_products.add(title)
                new_products_found = True

                # Если цена не "Нет в наличии", считаем товар в наличии, иначе ставим "-" в цену и "Нет в наличии" в наличии
                if price == 'Нет в наличии':
                    data.append(
                        {"Название": title, "Обычная цена": "-", "Цена со скидкой": "-", "Наличие": "Нет в наличии"})
                else:
                    data.append(
                        {"Название": title, "Обычная цена": price, "Цена со скидкой": discount_price,
                         "Наличие": "В наличии"})

            if not new_products_found:
                print(f"На странице {page} нет новых товаров. Завершаем обработку категории {base_url}.")
                break

            page += 1

        return data

    # Основной процесс сбора данных
    all_data = []  # Общий список для хранения данных всех категорий
    for category in categories:
        print(f"Обрабатываем категорию: {category}")
        category_data = scrape_category(category)
        all_data.extend(category_data)

    # Создаем DataFrame и сохраняем в CSV
    df = pd.DataFrame(all_data)
    df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"Данные успешно сохранены в '{output_file}'")


def scrape_nts_computers_n():
    """
    Собирает информацию о товарах из всех каталогов сайта NTS Computers
    и сохраняет результат в файл 'nts_computers.csv'.
    """
    base_urls = [
        'https://www.nts-computers.com/notebooks/acer_notebooks/',
        'https://www.nts-computers.com/notebooks/dell_notebooks/',
        'https://www.nts-computers.com/notebooks/hp_notebooks/',
        'https://www.nts-computers.com/notebooks/lenovo_notebook/'
    ]

    all_products = []

    for base_url in base_urls:
        print(f"Сканируем каталог: {base_url}")
        page = 1

        while True:
            url = f"{base_url}?page={page}"
            print(f"Сканируем страницу: {url}")

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Проверка успешности запроса
            except requests.RequestException as e:
                print(f"Ошибка при доступе к {url}: {e}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')

            # Находим товары на странице
            products = soup.find_all('div', class_='product-thumb')
            if not products:
                print(f"Товары не найдены на странице {page}. Завершение.")
                break

            for product in products:
                # Название товара
                name_tag = product.find('h4').find('span', itemprop='name')
                name = name_tag.text.strip() if name_tag else "Название не указано"

                # Парсинг цен
                price_container = product.find('div', class_='price', itemprop='offers')
                original_price = "-"
                discounted_price = "-"

                if price_container:
                    # Проверяем наличие тега с оригинальной ценой (для товаров со скидкой)
                    original_price_tag = price_container.find('span', class_=lambda x: x and 'price-old' in x)
                    if original_price_tag:
                        # Если тег с "price-old" есть, это товар со скидкой
                        original_price = original_price_tag.text.strip()

                        # Ищем цену со скидкой
                        discount_tag = price_container.find('span', class_=lambda x: x and 'price_no_format' in x)
                        if discount_tag:
                            discounted_price = discount_tag.text.strip()
                    else:
                        # Если скидки нет, ищем просто текущую цену
                        price_tag = price_container.find('span', class_=lambda x: x and 'price_no_format' in x)
                        if price_tag:
                            original_price = price_tag.text.strip()

                # Наличие товара (по умолчанию "Нет информации о наличии")
                availability = "Нет информации о наличии"

                # Добавление данных в список
                all_products.append({
                    "Название": name,
                    "Обычная цена": original_price,
                    "Цена со скидкой": discounted_price,
                    "Наличие": availability
                })

            page += 1  # Переход на следующую страницу

    # Преобразование в DataFrame
    df = pd.DataFrame(all_products)

    # Заполнение дефисом вместо пустых значений
    df.fillna("-", inplace=True)

    # Сохранение в CSV
    df.to_csv('nts_computers.csv', index=False, encoding='utf-8')
    print("Данные сохранены в 'nts_computers.csv'")


def u_n():
    scrape_akyol_n()
    scrape_and_save_notebook_merkezi_n()
    scrape_nts_computers_n()
    Data_format.unify_and_compare_data()
