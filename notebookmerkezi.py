import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_and_save(output_file='notebookmerkezi.csv'):
    """
    Функция для сбора данных из списка категорий и сохранения их в CSV файл.

    :param output_file: имя выходного файла CSV (по умолчанию 'notebookmerkezi.csv').
    """

    categories = ["https://notebookmerkezi.com.tm/category/53", "https://notebookmerkezi.com.tm/category/55", "https://notebookmerkezi.com.tm/category/54"]

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
                    data.append({"Название": title, "Обычная цена": "-", "Цена со скидкой": "-", "Наличие": "Нет в наличии"})
                else:
                    data.append(
                        {"Название": title, "Обычная цена": price, "Цена со скидкой": discount_price, "Наличие": "В наличии"})

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
