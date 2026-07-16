import tkinter as tk
from tkinter import ttk
import pandas as pd


def load_csv_to_treeview(tree, csv_file):
    # Очищаем предыдущие данные
    for row in tree.get_children():
        tree.delete(row)

    try:
        # Чтение CSV файла
        df = pd.read_csv(csv_file)

        # Установка заголовков столбцов
        tree["columns"] = list(df.columns)
        tree["show"] = "headings"  # Скрываем автоматический столбец "ID"

        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)  # Устанавливаем ширину столбцов

        # Добавление данных
        for _, row in df.iterrows():
            tree.insert("", tk.END, values=list(row))
    except Exception as e:
        print(f"Ошибка при загрузке CSV: {e}")


# Основное окно
root = tk.Tk()
root.title("Отображение CSV")
root.state('zoomed')

# Верхний текст
label = tk.Label(root, text="CSV Viewer", font=("Arial", 20))
label.pack(pady=10)

# Кнопка для обновления данных
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


def update_csv():
    load_csv_to_treeview(tree, "akyol.csv")  # Укажите путь к вашему CSV файлу


update_button = tk.Button(button_frame, text="Обновить CSV", command=update_csv)
update_button.pack()

# Создание виджета Treeview для таблицы
tree_frame = tk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True)

tree = ttk.Treeview(tree_frame)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Добавление полосы прокрутки
y_scrollbar = ttk.Scrollbar(tree, orient=tk.VERTICAL, command=tree.yview)
y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=y_scrollbar.set)

# Добавляем горизонтальную прокрутку
x_scrollbar = ttk.Scrollbar(tree, orient=tk.HORIZONTAL, command=tree.xview)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
tree.configure(xscrollcommand=x_scrollbar.set)

# Загрузка CSV при запуске
update_csv()

# Запуск основного цикла
root.mainloop()
