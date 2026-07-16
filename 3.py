import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def fetch_akyol_products():
    base_url = "https://akyol.com.tm/category/persnonalnye-kompyutery/category_2/?page="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    product_data = []
    page = 1

    while True:
        url = f"{base_url}{page}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='js-product-item')

        if not products:
            break

        for product in products:
            name_element = product.find('div', class_='product-tile__name')
            name = name_element.text.strip() if name_element else "Название не указано"

            discounted_price_element = product.find('div', class_='product-price')
            discounted_price = (
                discounted_price_element.find('span', class_='price').text.strip() +
                " " +
                discounted_price_element.find('span', class_='currency').text.strip()
                if discounted_price_element else None
            )

            original_price_element = product.find('div', class_='product-price-compare')
            original_price = (
                original_price_element.find('span', class_='price').text.strip() +
                " " +
                original_price_element.find('span', class_='currency').text.strip()
                if original_price_element else None
            )

            if original_price and discounted_price and original_price != discounted_price:
                price = f"Реальная цена: {original_price}, Цена со скидкой: {discounted_price}"
            else:
                price = f"Цена: {discounted_price}" if discounted_price else f"Реальная цена: {original_price}"

            stock_available = product.find('div', class_='product-stock product-tile__stock')
            stock_unavailable = product.find('div', class_='product-stock product-stock--none product-tile__stock')

            if stock_available:
                availability = stock_available.text.strip()
            elif stock_unavailable:
                availability = stock_unavailable.text.strip()
            else:
                availability = "Нет информации о наличии"

            product_data.append((name, price, availability))

        page += 1

    return pd.DataFrame(product_data, columns=['Название', 'Цена', 'Наличие'])


def fetch_gold_computers_products():
    base_urls = [
        "https://gold-computers.com/noutbuklar?page=",
        "https://gold-computers.com/ultrabuklar?page="
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    product_data = []

    for base_url in base_urls:
        page = 1
        while True:
            url = f"{base_url}{page}"
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('div', class_='ProductCardVertical')

            if not products:
                break

            for product in products:
                name_element = product.find('div', class_='ProductCardVertical__name')
                name = name_element.text.strip() if name_element else "Без названия"

                price_element = product.find('div', class_='ProductCardVertical__price-current')
                price = price_element.text.strip() if price_element else "Цена не указана"

                availability = "Нет информации о наличии"
                product_data.append((name, price, availability))

            page += 1

    return pd.DataFrame(product_data, columns=['Название', 'Цена', 'Наличие'])


def unify_data_format(df):
    """
    Приведение данных к единому формату:
    - Приводит названия столбцов к стандартным.
    - Убирает лишние пробелы и символы в названиях товаров.
    - Очищает цены от текста и лишних символов.
    - Удаляет дубликаты.
    """
    # Переименование столбцов, если их названия отличаются
    standard_columns = ['Название', 'Цена', 'Наличие']
    df.columns = standard_columns

    # Очистка названий моделей
    def clean_name(name):
        if isinstance(name, str):
            return re.sub(r'\s+', ' ', name.replace('\n', ' ').strip())  # Убираем лишние пробелы и символы
        return name

    df['Название'] = df['Название'].apply(clean_name)

    # Очистка цен от текста и лишних символов
    def clean_price(price):
        if isinstance(price, str):
            match = re.search(r'\d+', price.replace(',', '').replace('TMT', ''))
            return int(match.group()) if match else float('inf')
        return price

    df['Цена'] = df['Цена'].apply(clean_price)

    # Удаление дубликатов
    df.drop_duplicates(subset=['Название', 'Цена'], inplace=True)

    return df


def filter_by_manufacturer_from_web(manufacturer):
    # Получение данных с сайтов
    akyol_data = fetch_akyol_products()
    gold_computers_data = fetch_gold_computers_products()

    # Приведение данных к единому формату
    akyol_data = unify_data_format(akyol_data)
    gold_computers_data = unify_data_format(gold_computers_data)

    # Объединение данных
    combined_data = pd.concat([akyol_data, gold_computers_data], ignore_index=True)

    # Фильтрация по производителю
    filtered_data = combined_data[combined_data['Название'].str.contains(manufacturer, case=False, na=False)]

    # Сортировка по цене
    filtered_data.sort_values(by='Цена', inplace=True)

    return filtered_data


# Запуск функции
manufacturer_name = "Dell"
result = filter_by_manufacturer_from_web(manufacturer_name)

# Вывод результата
print(result)

# Сохранение результата в файл
result.to_csv(f"filtered_{manufacturer_name}_products.csv", index=False, encoding="utf-8")
print(f"Данные сохранены в файл 'filtered_{manufacturer_name}_products.csv'")
