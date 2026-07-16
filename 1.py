# import tkinter as tk
# from tkinter import messagebox
#
# def apply_filter():
#     selected_filter = filter_var.get()
#     if selected_filter == "a_to_z":
#         messagebox.showinfo("Фильтр", "Сортировка от А до Я")
#     elif selected_filter == "z_to_a":
#         messagebox.showinfo("Фильтр", "Сортировка от Я до А")
#     elif selected_filter == "price_ascending":
#         messagebox.showinfo("Фильтр", "Сортировка по возрастанию цены")
#     elif selected_filter == "price_descending":
#         messagebox.showinfo("Фильтр", "Сортировка по убыванию цены")
#     elif selected_filter == "availability":
#         messagebox.showinfo("Фильтр", "Сортировка по наличию товара")
#     else:
#         messagebox.showwarning("Фильтр", "Фильтр не выбран!")
#
# # Настройка основного окна
# root = tk.Tk()
# root.title("Фильтр по левому краю")
# root.geometry("600x400")
#
# # Левый фрейм для фильтров
# filter_frame = tk.Frame(root, bg="lightgray", padx=5, pady=5)
# filter_frame.pack(side=tk.LEFT, fill=tk.Y)
#
# # Заголовок фильтра
# tk.Label(filter_frame, text="Фильтры", font=("Arial", 14), bg="lightgray").pack(pady=5)
#
# # Переменная для хранения выбранного фильтра
# filter_var = tk.StringVar(value="none")  # По умолчанию ничего не выбрано
#
# # Радиокнопки для выбора фильтра
# tk.Radiobutton(filter_frame, text="От А до Я", variable=filter_var, value="a_to_z", bg="lightgray").pack(anchor="w", pady=2)
# tk.Radiobutton(filter_frame, text="От Я до А", variable=filter_var, value="z_to_a", bg="lightgray").pack(anchor="w", pady=2)
# tk.Radiobutton(filter_frame, text="Цена ↑", variable=filter_var, value="price_ascending", bg="lightgray").pack(anchor="w", pady=2)
# tk.Radiobutton(filter_frame, text="Цена ↓", variable=filter_var, value="price_descending", bg="lightgray").pack(anchor="w", pady=2)
# tk.Radiobutton(filter_frame, text="Наличие", variable=filter_var, value="availability", bg="lightgray").pack(anchor="w", pady=2)
#
# # Кнопка "Применить фильтр"
# tk.Button(filter_frame, text="Применить", command=apply_filter, width=10).pack(pady=10)
#
# # Основной контент
# content_frame = tk.Frame(root, bg="white")
# content_frame.pack(fill=tk.BOTH, expand=True)
#
# tk.Label(content_frame, text="Содержимое окна", font=("Arial", 18), bg="white").pack(pady=50)
#
# root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
#
#
# def apply_filter():
#     """Применяет выбранный фильтр."""
#     selected_filter = filter_var.get()
#     print(f"Применён фильтр: {selected_filter}")
#
#
# def toggle_sidebar(sidebar, button, expanded_text="<<", collapsed_text=">>"):
#     """Переключает видимость бокового меню."""
#     if sidebar.winfo_viewable():
#         sidebar.grid_remove()
#         button.config(text=collapsed_text)
#     else:
#         sidebar.grid()
#         button.config(text=expanded_text)
#
#
# def show_main():
#     """Отображает главный экран."""
#     main_frame.grid(row=0, column=1, sticky="nsew")
#     notebooks_frame.grid_forget()
#     printers_frame.grid_forget()
#     sidebar.grid_remove()
#     toggle_button.grid_remove()
#
#
# def show_notebooks():
#     """Отображает экран ноутбуков."""
#     main_frame.grid_forget()
#     printers_frame.grid_forget()
#     notebooks_frame.grid(row=0, column=1, sticky="nsew")
#     sidebar.grid(row=0, column=0, sticky="ns")
#     toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
#
#
# def show_printers():
#     """Отображает экран принтеров."""
#     main_frame.grid_forget()
#     notebooks_frame.grid_forget()
#     printers_frame.grid(row=0, column=1, sticky="nsew")
#     sidebar.grid(row=0, column=0, sticky="ns")
#     toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
#
#
# def update_notebooks():
#     """Обновляет базу ноутбуков."""
#     print("Обновление базы ноутбуков...")  # Заглушка для реального обновления
#
#
# def update_printers():
#     """Обновляет базу принтеров."""
#     print("Обновление базы принтеров...")  # Заглушка для реального обновления
#
#
# def search_item(category):
#     """Имитирует поиск."""
#     search_query = search_entries[category].get()
#     print(f"Поиск {category}: {search_query}")
#
#
# # Настройка окна
# root = tk.Tk()
# root.title("ShopWise v1.0.1")
# root.state("zoomed")
#
# # Сетка окна
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
#
# # Боковое меню
# sidebar = tk.Frame(root, bg="lightgray", padx=5, pady=5, width=200)
# sidebar.grid(row=0, column=0, sticky="ns")
# sidebar.grid_remove()
#
# # Кнопка для бокового меню
# toggle_button = tk.Button(root, text="<<", command=lambda: toggle_sidebar(sidebar, toggle_button))
# toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
# toggle_button.grid_remove()
#
# # Элементы бокового меню
# tk.Label(sidebar, text="Фильтры", font=("Arial", 14), bg="lightgray").pack(anchor="w", pady=5)
# filter_var = tk.StringVar(value="none")
# filters = ("От А до Я", "От Я до А", "Цена ↑", "Цена ↓", "Наличие")
# for text in filters:
#     tk.Radiobutton(sidebar, text=text, variable=filter_var, value=text, bg="lightgray").pack(anchor="w", pady=2)
# apply_button = tk.Button(sidebar, text="Применить", command=apply_filter, bg="darkgray", font=("Arial", 12))
# apply_button.pack(anchor="w", pady=10)
#
# # Главный фрейм
# main_frame = tk.Frame(root)
# main_frame.grid(row=0, column=1, sticky="nsew")
#
# mid_frame = tk.Frame(main_frame)
# mid_frame.pack(anchor="n", pady=10, padx=10)
# tk.Label(mid_frame, text="ShopWise", font=("Arial", 22)).pack(side="top")
# tk.Button(mid_frame, text="Ноутбуки", command=show_notebooks, height=2, width=22, font=("Arial", 15)).pack(side="left", padx=10, pady=35)
# tk.Button(mid_frame, text="Принтеры", command=show_printers, height=2, width=22, font=("Arial", 15)).pack(side="right", padx=10, pady=35)
#
# # Фреймы "Ноутбуки" и "Принтеры"
# notebooks_frame = tk.Frame(root)
# notebooks_frame.grid_rowconfigure(1, weight=1)
# notebooks_frame.grid_columnconfigure(0, weight=1)
# tk.Label(notebooks_frame, text="Ноутбуки", font=("Arial", 25)).grid(row=0, column=0, pady=5, sticky="n")
# tk.Button(notebooks_frame, text="Назад", command=show_main).grid(row=2, column=0, pady=10)
#
# printers_frame = tk.Frame(root)
# printers_frame.grid_rowconfigure(1, weight=1)
# printers_frame.grid_columnconfigure(0, weight=1)
# tk.Label(printers_frame, text="Принтеры", font=("Arial", 25)).grid(row=0, column=0, pady=5, sticky="n")
# tk.Button(printers_frame, text="Назад", command=show_main).grid(row=2, column=0, pady=10)
#
# # Поля поиска
# search_entries = {}  # Словарь для хранения ссылок на Entry
#
# def create_search_section(parent, category):
#     """Создаёт секцию поиска."""
#     frame = tk.Frame(parent)
#     frame.grid(row=1, column=0, pady=5, sticky="n")
#     tk.Label(frame, text="Поиск:").grid(row=0, column=0, padx=5)
#     entry = tk.Entry(frame, width=30)
#     entry.grid(row=0, column=1)
#     search_entries[category] = entry
#     try:
#         search_icon = ImageTk.PhotoImage(Image.open("ПОИСК (значок).png").resize((30, 30)))
#         tk.Button(frame, image=search_icon, compound="top", command=lambda: search_item(category)).grid(row=0, column=2, padx=5)
#         frame.image = search_icon  # Сохранение ссылки на изображение
#     except Exception:
#         tk.Button(frame, text="ИСКАТЬ", command=lambda: search_item(category), font=("Arial", 10)).grid(row=0, column=2, padx=5)
#
# create_search_section(notebooks_frame, "ноутбуки")
# create_search_section(printers_frame, "принтеры")
#
# # Отображение главного экрана
# show_main()
#
# # Запуск приложения
# if __name__ == "__main__":
#     root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
#
#
# def apply_filter():
#     """Применяет выбранный фильтр."""
#     selected_filter = filter_var.get()
#     print(f"Применён фильтр: {selected_filter}")
#
#
# def toggle_sidebar(sidebar, button, expanded_text="<<", collapsed_text=">>"):
#     """Переключает видимость бокового меню."""
#     if sidebar.winfo_viewable():
#         sidebar.grid_remove()
#         button.config(text=collapsed_text)
#     else:
#         sidebar.grid()
#         button.config(text=expanded_text)
#
#
# def show_main():
#     """Отображает главный экран."""
#     main_frame.grid(row=0, column=1, sticky="nsew")
#     notebooks_frame.grid_forget()
#     printers_frame.grid_forget()
#     sidebar.grid_remove()
#     toggle_button.grid_remove()
#
#
# def show_notebooks():
#     """Отображает экран ноутбуков."""
#     main_frame.grid_forget()
#     printers_frame.grid_forget()
#     notebooks_frame.grid(row=0, column=1, sticky="nsew")
#     sidebar.grid(row=0, column=0, sticky="ns")
#     toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
#
#
# def show_printers():
#     """Отображает экран принтеров."""
#     main_frame.grid_forget()
#     notebooks_frame.grid_forget()
#     printers_frame.grid(row=0, column=1, sticky="nsew")
#     sidebar.grid(row=0, column=0, sticky="ns")
#     toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
#
#
# def update_notebooks():
#     """Обновляет базу ноутбуков."""
#     update_label = tk.Label(notebooks_frame, text="Обновление базы ноутбуков...", font=("Arial", 10), fg="dark blue")
#     update_label.grid(row=1, column=0, sticky="nw", padx=10, pady=10)
#
#     def remove_update_label():
#         update_label.destroy()
#
#     notebooks_frame.after(2000, remove_update_label)
#
#
# def update_printers():
#     """Обновляет базу принтеров."""
#     update_label = tk.Label(printers_frame, text="Обновление базы принтеров...", font=("Arial", 10), fg="dark blue")
#     update_label.grid(row=1, column=0, sticky="nw", padx=10, pady=10)
#
#     def remove_update_label():
#         update_label.destroy()
#
#     printers_frame.after(2000, remove_update_label)
#
#
# def search_item():
#     """Поиск элементов."""
#     print("Поиск выполняется...")  # Заглушка для функции поиска
#
#
# # Настройка окна
# root = tk.Tk()
# root.title("ShopWise v1.0.1")
# root.state("zoomed")
#
# # Сетка окна
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
#
# # Боковое меню
# sidebar = tk.Frame(root, bg="lightgray", padx=5, pady=5, width=200)
# sidebar.grid(row=0, column=0, sticky="ns")
# sidebar.grid_remove()
#
# # Кнопка для бокового меню
# toggle_button = tk.Button(root, text="<<", font=("Arial", 7), command=lambda: toggle_sidebar(sidebar, toggle_button))
# toggle_button.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
# toggle_button.grid_remove()
#
# # Элементы бокового меню
# tk.Label(sidebar, text="Фильтры", font=("Arial", 13), bg="lightgray").pack(anchor="w", pady=20)
# filter_var = tk.StringVar(value="none")
# filters = ("От А до Я", "От Я до А", "Цена ↑", "Цена ↓", "Наличие")
# for text in filters:
#     tk.Radiobutton(sidebar, text=text, variable=filter_var, value=text, bg="lightgray").pack(anchor="w", pady=2)
# apply_button = tk.Button(sidebar, text="Применить", command=apply_filter, bg="darkgray", font=("Arial", 10))
# apply_button.pack(anchor="w", pady=10)
#
# # Главный фрейм
# main_frame = tk.Frame(root)
# main_frame.grid(row=0, column=1, sticky="nsew")
#
# mid_frame = tk.Frame(main_frame)
# mid_frame.pack(anchor="n", pady=10, padx=10)
# tk.Label(mid_frame, text="ShopWise", font=("Arial", 23)).pack(side="top")
# tk.Button(mid_frame, text="Ноутбуки", command=show_notebooks, height=2, width=22, font=("Arial", 17)).pack(side="left", padx=10, pady=35)
# tk.Button(mid_frame, text="Принтеры", command=show_printers, height=2, width=22, font=("Arial", 17)).pack(side="right", padx=10, pady=35)
#
# # Фреймы "Ноутбуки" и "Принтеры"
# notebooks_frame = tk.Frame(root)
# notebooks_frame.grid_rowconfigure(1, weight=1)
# notebooks_frame.grid_columnconfigure(0, weight=1)
# tk.Label(notebooks_frame, text="Ноутбуки", font=("Arial", 27)).grid(row=0, column=0, pady=5, sticky="n")
# tk.Button(notebooks_frame, text="НАЗАД", command=show_main).grid(row=2, column=0, pady=10)
#
# printers_frame = tk.Frame(root)
# printers_frame.grid_rowconfigure(1, weight=1)
# printers_frame.grid_columnconfigure(0, weight=1)
# tk.Label(printers_frame, text="Принтеры", font=("Arial", 27)).grid(row=0, column=0, pady=5, sticky="n")
# tk.Button(printers_frame, text="НАЗАД", command=show_main).grid(row=2, column=0, pady=10)
#
# # Поиск изображений для кнопок
# try:
#     photo_u_d = ImageTk.PhotoImage(Image.open('ОБНОВИТЬ БАЗУ (значок).png').resize((42, 42)))
#     tk.Button(notebooks_frame, image=photo_u_d, compound="top", text="ОБНОВИТЬ\nБАЗУ", command=update_notebooks).grid(row=0, column=1, pady=5, padx=10)
#     tk.Button(printers_frame, image=photo_u_d, compound="top", text="ОБНОВИТЬ\nБАЗУ", command=update_printers).grid(row=0, column=1, pady=5, padx=10)
# except Exception as e:
#     print("Ошибка загрузки изображений для кнопок:", e)
#
# # Отображение главного экрана
# show_main()
#
# # Запуск приложения
# if __name__ == "__main__":
#     root.mainloop()
