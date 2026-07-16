# import tkinter as tk
# from tkinter import ttk
#
# # Функция для обработки поиска
# def search_item():
#     query = search_entry.get().lower()  # Получаем текст из поля поиска
#     for row in tree.get_children():
#         # Проверяем каждую строку
#         if query in str(tree.item(row, "values")).lower():
#             tree.selection_set(row)  # Выделяем строку
#             tree.see(row)  # Прокручиваем к строке
#             return
#     result_label.config(text="Ничего не найдено.")  # Если ничего не найдено
#
# # Основное окно
# root = tk.Tk()
# root.title("Поиск в таблице")
#
# # Поле поиска
# search_frame = tk.Frame(root)
# search_frame.pack(pady=10)
#
# search_label = tk.Label(search_frame, text="Поиск: ")
# search_label.pack(side=tk.LEFT, padx=5)
#
# search_entry = tk.Entry(search_frame, width=30)
# search_entry.pack(side=tk.LEFT, padx=5)
#
# search_button = tk.Button(search_frame, text="Искать", command=search_item)
# search_button.pack(side=tk.LEFT, padx=5)
#
# result_label = tk.Label(root, text="", fg="red")
# result_label.pack(pady=5)
#
# # Таблица
# tree = ttk.Treeview(root, columns=("Column1", "Column2", "Column3"), show="headings", height=10)
# tree.pack(fill=tk.BOTH, expand=True)
#
# # Установка заголовков столбцов
# tree.heading("Column1", text="Столбец 1")
# tree.heading("Column2", text="Столбец 2")
# tree.heading("Column3", text="Столбец 3")
#
# # Пример данных
# data = [
#     ("Apple", "Fruit", "Red"),
#     ("Carrot", "Vegetable", "Orange"),
#     ("Banana", "Fruit", "Yellow"),
#     ("Potato", "Vegetable", "Brown"),
# ]
#
# # Добавление данных в таблицу
# for row in data:
#     tree.insert("", tk.END, values=row)
#
# # Запуск приложения
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# import csv
#
#
# def display_csv_in_treeview(root, csv_data):
#     """Отображение таблицы CSV в Treeview."""
#     frame = tk.Frame(root)
#     frame.pack(fill="both", expand=True, padx=10, pady=10)
#
#     # Создаём заголовок таблицы
#     columns = ("col1", "col2", "subcol1", "subcol2")
#     tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
#     tree.pack(fill="both", expand=True)
#
#     # Заголовки столбцов
#     tree.heading("col1", text="Столбец 1")
#     tree.heading("col2", text="Столбец 2")
#     tree.heading("subcol1", text="Подстолбец 1")
#     tree.heading("subcol2", text="Подстолбец 2")
#
#     # Задаём ширину столбцов
#     tree.column("col1", width=150, anchor="center")
#     tree.column("col2", width=150, anchor="center")
#     tree.column("subcol1", width=75, anchor="center")
#     tree.column("subcol2", width=75, anchor="center")
#
#     # Добавляем данные из CSV
#     for row in csv_data:
#         tree.insert("", "end", values=row)
#
#     # Создаём имитацию общей шапки
#     tree.tag_configure("group_heading", background="#D9EAF7")
#     tree.insert("", "end", values=("—", "—", "Группа 1", "Группа 1"), tags=("group_heading",))
#     tree.insert("", "end", values=("—", "—", "Группа 2", "Группа 2"), tags=("group_heading",))
#
#
# # Создаём окно
# root = tk.Tk()
# root.title("Таблица CSV с подстолбцами")
# root.geometry("600x400")
#
# # Пример данных CSV
# csv_data = [
#     ["A1", "B1", "C1", "D1"],
#     ["A2", "B2", "C2", "D2"],
#     ["A3", "B3", "C3", "D3"],
#     ["A4", "B4", "C4", "D4"],
#     ["A5", "B5", "C5", "D5"],
#     ["A6", "B6", "C6", "D6"],
#     ["A7", "B7", "C7", "D7"],
#     ["A8", "B8", "C8", "D8"],
#     ["A9", "B9", "C9", "D9"],
#     ["A10", "B10", "C10", "D10"],
# ]
#
# # Отображаем данные
# display_csv_in_treeview(root, csv_data)
#
# # Запускаем приложение
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
#
# def create_table_with_subcolumns(root):
#     # Основной фрейм
#     frame = ttk.Frame(root)
#     frame.pack(fill="both", expand=True, padx=10, pady=10)
#
#     # Canvas для реализации объединения заголовков
#     canvas = tk.Canvas(frame, height=40, bg="white")
#     canvas.grid(row=0, column=0, sticky="ew")
#
#     # Treeview для отображения данных
#     tree = ttk.Treeview(frame, show="headings", columns=("col1", "col2", "subcol1", "subcol2"), height=10)
#     tree.grid(row=1, column=0, sticky="nsew")
#
#     # Расширение колонок
#     frame.columnconfigure(0, weight=1)
#     frame.rowconfigure(1, weight=1)
#
#     # Заголовки подстолбцов
#     tree.heading("col1", text="Столбец 1")
#     tree.heading("col2", text="Столбец 2")
#     tree.heading("subcol1", text="Подстолбец 1")
#     tree.heading("subcol2", text="Подстолбец 2")
#
#     # Настройка ширины столбцов
#     tree.column("col1", width=150, anchor="center")
#     tree.column("col2", width=150, anchor="center")
#     tree.column("subcol1", width=100, anchor="center")
#     tree.column("subcol2", width=100, anchor="center")
#
#     # Добавление данных
#     data = [
#         ["A1", "B1", "C1", "D1"],
#         ["A2", "B2", "C2", "D2"],
#         ["A3", "B3", "C3", "D3"],
#         ["A4", "B4", "C4", "D4"]
#     ]
#     for row in data:
#         tree.insert("", "end", values=row)
#
#     # Объединение для группы подстолбцов
#     canvas.create_text(325, 15, text="Группа подстолбцов", font=("Arial", 12, "bold"))
#     canvas.create_line(250, 20, 400, 20)  # Горизонтальная линия
#
#     # Вертикальные линии
#     canvas.create_line(250, 20, 250, 40)
#     canvas.create_line(400, 20, 400, 40)
#
#     return tree
#
# # Окно Tkinter
# root = tk.Tk()
# root.title("Таблица с подстолбцами")
# root.geometry("600x400")
#
# create_table_with_subcolumns(root)
#
# root.mainloop()


# from tkinter import Tk, Frame
# from tkintertable import TableCanvas, TableModel
#
# def create_excel_table(data):
#     # Создаём модель данных
#     model = TableModel()
#     model.importDict(data)
#
#     # Создаём таблицу и прикрепляем её к родительскому фрейму
#     table = TableCanvas(frame, model=model)
#     table.show()
#
# # Данные для отображения
# excel_data = {
#     '1': {'Column 1': 'A1', 'Column 2': 'B1', 'SubColumn 1': 'C1', 'SubColumn 2': 'D1'},
#     '2': {'Column 1': 'A2', 'Column 2': 'B2', 'SubColumn 1': 'C2', 'SubColumn 2': 'D2'},
#     '3': {'Column 1': 'A3', 'Column 2': 'B3', 'SubColumn 1': 'C3', 'SubColumn 2': 'D3'}
# }
#
# # Интерфейс приложения
# root = Tk()
# root.geometry("600x400")
#
# # Фрейм для таблицы
# frame = Frame(root)
# frame.pack(fill="both", expand=True)
#
# create_excel_table(excel_data)
#
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# import pandas as pd
#
# def load_excel_to_treeview(filepath, treeview):
#     # Чтение данных из Excel
#     df = pd.read_excel(filepath)
#
#     # Настройка колонок Treeview
#     treeview["columns"] = list(df.columns)
#     for col in df.columns:
#         treeview.heading(col, text=col)
#         treeview.column(col, anchor="center")
#
#     # Добавление данных в Treeview
#     for _, row in df.iterrows():
#         treeview.insert("", "end", values=list(row))
#
# # Интерфейс приложения
# root = tk.Tk()
# root.geometry("600x400")
#
# # Treeview для отображения данных
# tree = ttk.Treeview(root, show="headings")
# tree.pack(fill="both", expand=True)
#
# # Загрузка Excel-данных
# file_path = r"C:\Users\Machri\Desktop\Ягмур\Результаты первого (отборочного) этапа DANO 2024-25.xlsx"  # Замените на путь к вашему Excel-файлу
# load_excel_to_treeview(file_path, tree)
#
# root.mainloop()



# import tkinter as tk
# from tkinter import ttk
# import pandas as pd
#
#
# def load_excel_to_treeview(filepath, treeview):
#     # Чтение данных из Excel
#     df = pd.read_excel(filepath)
#
#     # Объединяем столбцы "Класс" и "Образовательное учреждение" в один
#     if "Класс" in df.columns and "Образовательное учреждение" in df.columns:
#         df["Обучение"] = df["Класс"].astype(str) + " | " + df["Образовательное учреждение"].astype(str)
#         df.drop(columns=["Класс", "Образовательное учреждение"], inplace=True)
#
#     # Настройка колонок Treeview
#     treeview["columns"] = list(df.columns)
#     for col in df.columns:
#         treeview.heading(col, text=col)
#         treeview.column(col, anchor="center", width=150)
#
#     # Добавление данных в Treeview
#     for _, row in df.iterrows():
#         treeview.insert("", "end", values=list(row))
#
#
# # Интерфейс приложения
# root = tk.Tk()
# root.geometry("800x400")
#
# # Обёртка для Treeview с прокруткой
# frame = tk.Frame(root)
# frame.pack(fill="both", expand=True)
#
# # Treeview для отображения данных
# tree = ttk.Treeview(frame, show="headings")
#
# # Горизонтальная прокрутка
# x_scroll = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
# x_scroll.pack(side="bottom", fill="x")
#
# # Вертикальная прокрутка
# y_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
# y_scroll.pack(side="right", fill="y")
#
# tree.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
# tree.pack(fill="both", expand=True)
#
# # Загрузка Excel-данных
# file_path = r"C:\Users\Machri\Desktop\Ягмур\Результаты первого (отборочного) этапа DANO 2024-25.xlsx"  # Замените на путь к вашему Excel-файлу
# load_excel_to_treeview(file_path, tree)
#
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# import pandas as pd
#
#
# def load_excel_to_treeview(filepath, treeview):
#     # Чтение данных из Excel
#     df = pd.read_excel(filepath)
#
#     # Преобразуем столбцы "Класс" и "Образовательное учреждение" в столбец "Обучение"
#     df["Обучение"] = df["Класс"].astype(str) + " | " + df["Образовательное учреждение"].astype(str)
#     df.drop(columns=["Класс", "Образовательное учреждение"], inplace=True)
#
#     # Настройка колонок Treeview (с учетом объединенного столбца "Обучение")
#     treeview["columns"] = list(df.columns)
#     treeview["show"] = "headings"
#     treeview.heading("#1", text="Обучение", anchor="center")
#     treeview.column("#1", anchor="center", width=250)
#
#     # Добавление данных в Treeview
#     for _, row in df.iterrows():
#         treeview.insert("", "end", values=list(row))
#
#
# # Интерфейс приложения
# root = tk.Tk()
# root.geometry("800x400")
#
# # Обёртка для Treeview с прокруткой
# frame = tk.Frame(root)
# frame.pack(fill="both", expand=True)
#
# # Treeview для отображения данных
# tree = ttk.Treeview(frame, show="headings")
#
# # Горизонтальная прокрутка
# x_scroll = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
# x_scroll.pack(side="bottom", fill="x")
#
# # Вертикальная прокрутка
# y_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
# y_scroll.pack(side="right", fill="y")
#
# tree.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
# tree.pack(fill="both", expand=True)
#
# # Загрузка Excel-данных
# file_path = r"C:\Users\Machri\Desktop\Ягмур\Результаты первого (отборочного) этапа DANO 2024-25.xlsx"  # Замените на путь к вашему Excel-файлу
# load_excel_to_treeview(file_path, tree)
#
# root.mainloop()



# import tkinter as tk
# import xlwings as xw
#
# def open_excel(filepath):
#     app = xw.App(visible=True)
#     workbook = app.books.open(filepath)
#
# # Интерфейс приложения
# root = tk.Tk()
# root.geometry("200x100")
#
# btn = tk.Button(root, text="Открыть Excel", command=lambda: open_excel(r"C:\Users\Machri\Desktop\Ягмур\Результаты первого (отборочного) этапа DANO 2024-25.xlsx"))
# btn.pack(pady=20)
#
# root.mainloop()


