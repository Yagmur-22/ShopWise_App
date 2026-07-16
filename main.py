import tkinter as tk
from PIL import Image, ImageTk
import site_parsing
from tkinter import ttk
import pandas as pd

tree, df = None, None


def show_comparison_table():
    global tree, df
    """Загружает и отображает таблицу comparison_result.csv в notebooks_frame."""
    # Создаём новый контейнер для таблицы
    tree_frame = tk.Frame(notebooks_frame)
    tree_frame.grid(row=2, sticky='nsew', pady=5, padx=5)  # Убедитесь, что размещение происходит после создания

    # Попробуем загрузить данные из CSV
    try:
        df = pd.read_csv('comparison_result.csv')  # Замените на нужный путь к файлу
    except Exception as e:
        tk.Label(notebooks_frame, text=f"Ошибка загрузки данных: {e}", fg="red", font=("Arial", 10)).grid(row=1, column=0)
        return

    # Обработка NaN значений для всех столбцов, содержащих "Обычная цена" или "Цена со скидкой"
    for col in df.columns:
        if "Обычная цена" in col:
            df[col] = df[col].fillna(float("inf"))  # Заполнение NaN значений в "Обычных ценах"
        elif "Цена со скидкой" in col:
            df[col] = df[col].fillna(float("inf"))  # Заполнение NaN значений в "Ценах со скидкой"

    # Создаём Treeview для отображения данных
    columns = list(df.columns)  # Считываем названия колонок
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=27)

    # Устанавливаем заголовки колонок
    for col in columns:
        tree.heading(col, text=col)
        # Устанавливаем ширину для каждого столбца
        if col == "Название":
            tree.column(col, width=333, anchor="w")  # Название товара - выравнивание по левому краю
        else:
            tree.column(col, width=222, anchor="center")  # Все остальные столбцы - выравнивание по центру

    # Заполняем строки таблицы
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    # Добавляем вертикальную прокрутку
    y_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=y_scrollbar.set)

    # Добавляем горизонтальную прокрутку
    x_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(xscrollcommand=x_scrollbar.set)

    # Размещение таблицы и прокруток
    tree.grid(sticky="nsew")
    y_scrollbar.grid(row=0, column=1, sticky="ns")
    x_scrollbar.grid(row=1, column=0, sticky="ew")

    # Настройка `tree_frame` для растяжения
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)


def apply_filter():
    """Применяет выбранный фильтр."""
    selected_filter = filter_var.get()
    sort_table(selected_filter)  # Передаём критерий сортировки в функцию
    print(f"Применён фильтр: {selected_filter}")


# Функция для работы с копией данных
def sort_table(criteria):
    """Сортирует таблицу на основе выбранного критерия."""
    global df, tree

    if df is None or tree is None:
        print("Таблица или данные не загружены.")
        return

    # Создаем копию DataFrame, чтобы избежать изменений в оригинале
    df_copy = df.copy()

    # Преобразуем все столбцы, связанные с ценами, в числовой формат в копии
    price_columns = [col for col in df_copy.columns if "Обычная цена" in col or "Цена со скидкой" in col]

    # Преобразуем каждый столбец с ценой в числовой формат в копии
    for col in price_columns:
        df_copy[col] = pd.to_numeric(df_copy[col], errors="coerce")

    # Заполнение NaN значений в копии (не в оригинале)
    for col in price_columns:
        df_copy[col] = df_copy[col].fillna(float("inf"))  # Не меняем оригинальные данные

    # Преобразуем столбцы с наличием в булевый тип для сортировки
    availability_columns = [col for col in df_copy.columns if "Наличие" in col]
    for col in availability_columns:
        df_copy[col] = df_copy[col].apply(lambda x: 1 if "в наличии" in str(x).lower() else 0)

    # Проверка, что критерий сортировки правильный
    valid_criteria = [
        "Обычная цена ↑", "Обычная цена ↓",
        "Цена со скидкой ↑", "Цена со скидкой ↓",
        "От А до Я", "От Я до А",
        "Наличие ↑", "Наличие ↓"
    ]

    if criteria not in valid_criteria:
        print(f"Неизвестный критерий сортировки: {criteria}")
        return

    # Определяем порядок сортировки
    if criteria == "Обычная цена ↑":
        df_sorted = df_copy.sort_values(price_columns[0], ascending=True)  # Используем первый столбец "Обычной цены"
    elif criteria == "Обычная цена ↓":
        df_sorted = df_copy.sort_values(price_columns[0], ascending=False)
    elif criteria == "Цена со скидкой ↑":
        df_sorted = df_copy.sort_values(price_columns[1], ascending=True)  # Используем второй столбец "Цены со скидкой"
    elif criteria == "Цена со скидкой ↓":
        df_sorted = df_copy.sort_values(price_columns[1], ascending=False)
    elif criteria == "От А до Я":
        df_sorted = df_copy.sort_values(by=["Название"], ascending=True)  # Сортировка по алфавиту
    elif criteria == "От Я до А":
        df_sorted = df_copy.sort_values(by=["Название"], ascending=False)  # Сортировка по убыванию
    elif criteria == "Наличие ↑":
        # Сортировка по наличию: сначала в наличии
        df_sorted = df_copy.sort_values(by=availability_columns, ascending=False)  # 1 в наличии
    elif criteria == "Наличие ↓":
        # Сортировка по наличию: сначала отсутствующие
        df_sorted = df_copy.sort_values(by=availability_columns, ascending=True)  # 0 отсутствуют

    # Сохраняем порядок названий из отсортированной копии
    sorted_names = df_sorted["Название"].tolist()

    # Теперь сортируем оригинальный DataFrame на основе этого порядка
    df_display = df.set_index("Название").reindex(sorted_names).reset_index()

    # Очистка текущего содержимого Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Добавляем отсортированные данные в Treeview
    for _, row in df_display.iterrows():
        tree.insert("", "end", values=list(row))

    # Отображаем в таблице только данные из копии (изменения не затрагивают оригинальные данные)
    # Не изменяем глобальный df
    df_display = df_copy.copy()  # Сохраняем копию для отображения


def toggle_sidebar(sidebar, button, expanded_text="<<", collapsed_text=">>"):
    """Переключает видимость бокового меню."""
    if sidebar.winfo_viewable():
        sidebar.grid_remove()
        button.config(text=collapsed_text)
    else:
        sidebar.grid()
        button.config(text=expanded_text)


def search_and_select(search_entry, no_match_label):
    """Ищет и выделяет первый найденный элемент в Treeview."""
    search_text = search_entry.get().strip().lower()  # Получаем текст поиска и приводим его к нижнему регистру

    # Фильтруем DataFrame по совпадению текста в столбце "Название"
    matches = df[df["Название"].str.lower().str.contains(search_text, na=False)]

    if not matches.empty:  # Если есть совпадения
        # Скрываем сообщение о том, что ничего не найдено, если оно есть
        no_match_label.grid_forget()

        # Получаем индекс первой найденной строки
        first_match_index = matches.index[0]

        # Очищаем текущее выделение
        tree.selection_remove(tree.selection())

        # Выделяем и прокручиваем к первой найденной строке
        item_id = tree.get_children()[first_match_index]  # Получаем ID элемента в Treeview
        tree.selection_set(item_id)  # Устанавливаем выделение
        tree.see(item_id)  # Прокручиваем к элементу
    else:
        # Если совпадений нет, выводим сообщение "Ничего не найдено"
        if not no_match_label.winfo_ismapped():  # Проверка, чтобы не создавать новый label каждый раз
            no_match_label.grid(row=1, column=1)  # Размещение сообщения на экране


def show_main():
    """Отображает главный экран."""
    main_frame.grid(row=0, column=1, sticky="nsew")
    notebooks_frame.grid_forget()
    printers_frame.grid_forget()
    sidebar.grid_remove()
    toggle_button.grid_remove()


def update_notebooks():
    """Обновляет базу ноутбуков."""
    update_label = tk.Label(notebooks_frame, text="Обновление базы ноутбуков...", font=("Arial", 10), fg="dark blue")
    update_label.grid(row=1, column=0, sticky="nw", padx=10, pady=10)
    site_parsing.u_n()
    show_comparison_table()
    update_label.destroy()


def show_notebooks():
    """Отображает экран ноутбуков."""
    main_frame.grid_forget()
    printers_frame.grid_forget()
    notebooks_frame.grid(row=0, column=1, sticky="nsew")
    sidebar.grid(row=0, column=0, sticky="ns")
    toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
    toggle_sidebar(sidebar, toggle_button)
    search_entry_n.delete(0, tk.END)  # Очищаем поле ввода


def update_printers():
    """Обновляет базу принтеров."""
    update_label = tk.Label(printers_frame, text="Обновление базы принтеров...", font=("Arial", 10), fg="dark blue")
    update_label.grid(row=1, column=0, sticky="nw", padx=10, pady=10)

    def remove_update_label():
        update_label.destroy()

    printers_frame.after(2000, remove_update_label)


def show_printers():
    """Отображает экран принтеров."""
    main_frame.grid_forget()
    notebooks_frame.grid_forget()
    printers_frame.grid(row=0, column=1, sticky="nsew")
    sidebar.grid(row=0, column=0, sticky="ns")
    toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
    toggle_sidebar(sidebar, toggle_button)
    search_entry_p.delete(0, tk.END)  # Очищаем поле ввода


# Настройка окна
root = tk.Tk()
root.title('ShopWise v1.0.1')
root.state("zoomed")

# Позволяем root растягивать содержимое
root.grid_rowconfigure(0, weight=1)  # Позволяет первой строке растягиваться
root.grid_columnconfigure(1, weight=1)  # Позволяет второй колонке растягиваться

# Боковое меню
sidebar = tk.Frame(root, bg="lightgray", padx=5, pady=5, width=200)
sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_remove()

# Кнопка для бокового меню
toggle_button = tk.Button(root, text="<<", font=("Arial", 7), command=lambda: toggle_sidebar(sidebar, toggle_button))
toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
toggle_button.grid_remove()

# Элементы бокового меню
tk.Label(sidebar, text="СОРТИРОВКА", font=("Arial", 13, "bold"), bg="lightgray").pack(anchor="w", pady=20)
filter_var = tk.StringVar(value="none")
filters = ("От А до Я", "От Я до А", "Обычная цена ↑", "Обычная цена ↓", "Цена со скидкой ↑", "Цена со скидкой ↓", "Наличие ↑", "Наличие ↓")
for text in filters:
    tk.Radiobutton(sidebar, text=text, variable=filter_var, value=text, bg="lightgray").pack(anchor="w", pady=2)
apply_button = tk.Button(sidebar, text="Применить", command=apply_filter, bg="darkgray", font=("Arial", 10))
apply_button.pack(anchor="w", pady=10)

# Главный фрейм
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=1, sticky="nsew")
main_frame.grid_rowconfigure(0, weight=1)  # Позволяет содержимому внутри main_frame растягиваться
main_frame.grid_columnconfigure(0, weight=1)

mid_frame = tk.Frame(main_frame)
mid_frame.pack(anchor="n", pady=10, padx=10)
tk.Label(mid_frame, text="ShopWise", font=("Arial", 23)).pack(side="top")
tk.Button(mid_frame, text="Ноутбуки", command=show_notebooks, height=2, width=22, font=("Arial", 17)).pack(side="left", padx=10, pady=35)
tk.Button(mid_frame, text="Принтеры", command=show_printers, height=2, width=22, font=("Arial", 17)).pack(side="right", padx=10, pady=35)

# Фрейм для ноутбуков
notebooks_frame = tk.Frame(root)
notebooks_frame.grid_rowconfigure(0, weight=0)  # Строка с заголовком не растягивается
notebooks_frame.grid_rowconfigure(1, weight=1)  # Строка с таблицей будет растягиваться
notebooks_frame.grid_columnconfigure(0, weight=1)  # Колонка, в которой содержится таблица, растягивается
tk.Label(notebooks_frame, text="Ноутбуки", font=("Arial", 27)).grid(row=0, column=0, pady=5, sticky="n")
tk.Button(notebooks_frame, text="НАЗАД", font=("Arial", 12), command=show_main).grid(row=3, column=0, pady=10)
search_frame_n = tk.Frame(notebooks_frame)
search_frame_n.grid(row=1, column=0, pady=5, sticky="n")
tk.Label(search_frame_n, text="Поиск:").grid(row=0, column=0, padx=5)
search_entry_n = tk.Entry(search_frame_n, width=50)
search_entry_n.grid(row=0, column=1)
no_match_label_n = tk.Label(search_frame_n, text="Ничего не найдено", fg="red", font=("Arial", 10))

# Фрейм для принтеров
printers_frame = tk.Frame(root)
printers_frame.grid_rowconfigure(1, weight=1)
printers_frame.grid_columnconfigure(0, weight=1)
tk.Label(printers_frame, text="Принтеры", font=("Arial", 27)).grid(row=0, column=0, pady=5, sticky="n")
tk.Button(printers_frame, text="НАЗАД", font=("Arial", 12), command=show_main).grid(row=3, column=0, pady=10)
search_frame_p = tk.Frame(printers_frame)
search_frame_p.grid(row=1, column=0, pady=5, sticky="n")
tk.Label(search_frame_p, text="Поиск:").grid(row=0, column=0, padx=5)
search_entry_p = tk.Entry(search_frame_p, width=50)
search_entry_p.grid(row=0, column=1)
no_match_label_p = tk.Label(search_frame_p, text="Ничего не найдено", fg="red", font=("Arial", 10))

try:
    photo_u_d = ImageTk.PhotoImage(Image.open('ОБНОВИТЬ БАЗУ (значок).png').resize((42, 42)))
    tk.Button(notebooks_frame, text="ОБНОВИТЬ\nБАЗУ", image=photo_u_d, compound="top", command=update_notebooks, font=("Arial", 6)).grid(row=0, column=1, pady=5, padx=10)
    tk.Button(printers_frame, text="ОБНОВИТЬ\nБАЗУ", image=photo_u_d, compound="top", command=update_printers, font=("Arial", 6)).grid(row=0, column=1, pady=5, padx=10)
except Exception as e:
    print("Ошибка загрузки изображений для кнопок:", e)
    tk.Button(notebooks_frame, text="ОБНОВИТЬ\nБАЗУ", command=update_notebooks, font=("Arial", 6)).grid(row=0, column=1, pady=5, padx=10)
    tk.Button(printers_frame, text="ОБНОВИТЬ\nБАЗУ", command=update_printers, font=("Arial", 6)).grid(row=0, column=1, pady=5, padx=10)

try:
    photo_s = ImageTk.PhotoImage(Image.open('ПОИСК (значок).png').resize((30, 30)))
    tk.Button(search_frame_n, text="ИСКАТЬ", image=photo_s, compound="top", command=lambda: search_and_select(search_entry_n, no_match_label_n), font=("Arial", 6)).grid(row=0, column=2, padx=5)
    tk.Button(search_frame_p, text="ИСКАТЬ", image=photo_s, compound="top", command=lambda: search_and_select(search_entry_p, no_match_label_p), font=("Arial", 6)).grid(row=0, column=2, padx=5)
except Exception as e:
    print("Ошибка загрузки изображений для кнопок:", e)
    tk.Button(search_frame_n, text="ИСКАТЬ", command=lambda: search_and_select(search_entry_n, no_match_label_n), font=("Arial", 5)).grid(row=0, column=2, padx=5)
    tk.Button(search_frame_p, text="ИСКАТЬ", command=lambda: search_and_select(search_entry_p, no_match_label_p), font=("Arial", 5)).grid(row=0, column=2, padx=5)

# Отображение главного фрейма
show_main()
tk.Label(main_frame, text='*** Кнопка "Принтеры" ещё не оснащена полным функционалом! Находится в разработке!').pack(side='bottom', pady=5)

# Запуск приложения
root.mainloop()
