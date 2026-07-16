import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


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


# Вызов основной функции
scrape_nts_computers_n()
