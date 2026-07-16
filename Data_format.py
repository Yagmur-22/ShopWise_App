import pandas as pd
import re


def unify_and_compare_data(akyol_file="akyol.csv", notebook_merkezi_file="notebookmerkezi.csv",
                           nts_file="nts_computers.csv", output_file="comparison_result.csv"):
    """
    Объединяет данные из трех CSV-файлов (Akyol, NotebookMerkezi, NTS),
    приводит их к единому формату, удаляет дубли на каждом сайте
    и сохраняет результат в CSV-файл.

    :param akyol_file: путь к файлу Akyol (например, "akyol.csv")
    :param notebook_merkezi_file: путь к файлу Notebook Merkezi (например, "notebookmerkezi.csv")
    :param nts_file: путь к файлу NTS Computers (например, "nts_computers.csv")
    :param output_file: имя выходного файла (по умолчанию "comparison_result.csv")
    """

    def clean_name(name):
        """
        Очищает название товара от русских слов и лишних символов.
        """
        # Удаление русских слов
        name = re.sub(r"\b[А-Яа-яЁё]+\b", "", name)

        # Удаление лишних символов и пробелов
        name = re.sub(r"[^\w\s\-\(\)\.]", "", name)
        name = re.sub(r"\s+", " ", name).strip()
        name = name.replace("-", "").strip()
        name = name.upper()
        return name

    def clean_price(price):
        """
        Очищает строку с ценой, оставляя только числовую часть.
        """
        # Оставляем только цифры и точку
        price = re.sub(r"[^\d.]", "", str(price))

        # Если после очистки цена пустая, вернем "-"
        if price == "":
            return "-"

        # Если цена имеет точку и больше одного знака после, оставляем два знака после запятой
        if '.' in price:
            price = "{:.2f}".format(float(price))  # Ограничиваем до двух знаков после запятой

        # Добавляем " ТМТ" к числовой цене
        return f"{price} ТМТ"

    def process_data(df, source_name=""):
        """
        Преобразует данные в единый формат, очищает названия товаров, удаляет дубли.
        Добавляет суффиксы для столбцов, чтобы отражать источник данных.
        """
        df["Название"] = df["Название"].apply(clean_name)
        df["Обычная цена"] = df["Обычная цена"].apply(clean_price)
        df["Цена со скидкой"] = df["Цена со скидкой"].apply(clean_price)
        df["Наличие"] = df["Наличие"].apply(lambda x: "В наличии" if "В наличии" in str(x) else "-")

        # Удаление дубликатов по названию
        df = df.drop_duplicates(subset="Название", keep="first")

        # Добавление суффиксов, если это необходимо
        if source_name:
            df.columns = [f"{col} на {source_name}" if col not in ["Название"] else col for col in df.columns]

        return df

    # Чтение данных из CSV-файлов
    akyol_df = pd.read_csv(akyol_file)
    notebook_merkezi_df = pd.read_csv(notebook_merkezi_file)
    nts_df = pd.read_csv(nts_file)

    # Приведение данных к единому формату и удаление дубликатов
    akyol_df = process_data(akyol_df, "Ak Ýol Computers")
    notebook_merkezi_df = process_data(notebook_merkezi_df, "Notebook Merkezi")
    nts_df = process_data(nts_df, "NTS Computers")

    # Объединение данных по столбцу "Название"
    result_df = pd.merge(
        akyol_df,
        nts_df,
        on="Название",
        how="outer"
    )
    result_df = pd.merge(
        result_df,
        notebook_merkezi_df,
        on="Название",
        how="outer"
    )

    # Замена NaN на "-"
    result_df.fillna("-", inplace=True)

    # Удаление строк, где все столбцы (кроме "Название") равны "-"
    columns_to_check = result_df.columns.difference(["Название"])
    result_df = result_df[~result_df[columns_to_check].eq("-").all(axis=1)]

    # Сохранение результата в файл
    result_df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Данные объединены и сохранены в файл '{output_file}'")
