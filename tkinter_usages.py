# #              Основные виджеты tkinter:
# # Label — текстовая метка.
# # Button — кнопка.
# # Entry — поле ввода.
# # Text — многострочное текстовое поле.
# # Frame — контейнер для группировки виджетов.
# # Canvas — для рисования графики.
# # Menu — создание меню.
# # Treeview — таблицы или списки (в модуле ttk).


# #           №1
# import tkinter as tk
#
# # Создание главного окна
# root = tk.Tk()
# root.title("Мое первое приложение")  # Заголовок окна
# root.geometry("400x300")  # Размер окна (ширина x высота)
#
# # Запуск приложения
# root.mainloop()

# #           №2
# import tkinter as tk
#
# root = tk.Tk()
# root.title("Виджеты в tkinter")
#
# # Метка (текст)
# label = tk.Label(root, text="Привет, tkinter!", font=("Arial", 14))
# label.pack(pady=10)  # Разместить метку с отступом
#
# # Кнопка
# def on_button_click():
#     label.config(text="Кнопка нажата!")
#
# button = tk.Button(root, text="Нажми меня", command=on_button_click)
# button.pack(pady=10)
#
# # Поле ввода текста
# entry = tk.Entry(root, width=20)
# entry.pack(pady=10)
#
# # Добавление текста в метку из поля ввода
# def update_label():
#     text = entry.get()
#     label.config(text=f"Вы ввели: {text}")
#
# update_button = tk.Button(root, text="Обновить текст", command=update_label)
# update_button.pack(pady=10)
#
# root.mainloop()

# #           №3.1
# import tkinter as tk
#
# root = tk.Tk()
#
# label1 = tk.Label(root, text="Верхний элемент")
# label1.pack(side="top")
#
# label2 = tk.Label(root, text="Нижний элемент")
# label2.pack(side="bottom")
#
# label3 = tk.Label(root, text="Слева")
# label3.pack(side="left")
#
# label4 = tk.Label(root, text="Справа")
# label4.pack(side="right")
#
# root.mainloop()

# #           №3.2
# import tkinter as tk
#
# root = tk.Tk()
#
# tk.Label(root, text="Имя:").grid(row=0, column=0, padx=5, pady=5)
# tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)
#
# tk.Label(root, text="Пароль:").grid(row=1, column=0, padx=5, pady=5)
# tk.Entry(root, show="*").grid(row=1, column=1, padx=5, pady=5)
#
# tk.Button(root, text="Войти").grid(row=2, column=0, columnspan=2, pady=10)
#
# root.mainloop()

# #           №3.3
# import tkinter as tk
#
# root = tk.Tk()
#
# label = tk.Label(root, text="Пример place")
# label.place(x=50, y=50)  # Точное расположение в пикселях
#
# root.mainloop()

# #           №4
# import tkinter as tk
#
# def say_hello():
#     print("Привет!")
#
# root = tk.Tk()
#
# # Создание меню
# menu_bar = tk.Menu(root)
#
# # Добавление пункта "Файл"
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Открыть", command=say_hello)
# file_menu.add_command(label="Сохранить", command=say_hello)
# file_menu.add_separator()
# file_menu.add_command(label="Выход", command=root.quit)
# menu_bar.add_cascade(label="Файл", menu=file_menu)
#
# # Установка меню в окно
# root.config(menu=menu_bar)
#
# root.mainloop()

# #           №5
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# text = tk.Text(root, wrap="word", width=40, height=10)
# text.pack(side="left", fill="both", expand=True)
#
# # Прокрутка
# scrollbar = ttk.Scrollbar(root, command=text.yview)
# scrollbar.pack(side="right", fill="y")
# text.config(yscrollcommand=scrollbar.set)
#
# root.mainloop()

# #           №6
# import tkinter as tk
#
# root = tk.Tk()
#
# # Верхний фрейм
# top_frame = tk.Frame(root)
# top_frame.pack(side="top", fill="x")
#
# tk.Label(top_frame, text="Верхний текст").pack()
#
# # Нижний фрейм
# bottom_frame = tk.Frame(root)
# bottom_frame.pack(side="bottom", fill="x")
#
#
# tk.Button(bottom_frame, text="Кнопка 1").pack(side="left")
# tk.Button(bottom_frame, text="Кнопка 2").pack(side="right")
#
# root.mainloop()

# #           №7
# import tkinter as tk
# from PIL import Image, ImageTk  # Для работы с изображениями
#
# # Создаем главное окно
# root = tk.Tk()
# root.title("Кнопка с картинкой и надписью")
# root.geometry("400x300")  # Размер окна
#
# # Загружаем изображение
# image_path = "ОБНОВИТЬ БАЗУ (значок).png"  # Укажите путь к вашему изображению
# image = Image.open(image_path).resize((50, 50))  # Масштабируем изображение
# photo = ImageTk.PhotoImage(image)
#
# # Создаем кнопку
# button = tk.Button(root, text="Надпись", image=photo, compound="top")  # compound указывает положение текста
# button.place(x=300, y=10)  # Координаты для размещения в верхнем правом углу
#
# # Запуск главного цикла
# root.mainloop()

# #           №8.1
# import tkinter as tk
# from tkinter import ttk
#
#
# def show_repo1():
#     repo1_frame.pack(fill="both", expand=True)
#     repo2_frame.pack_forget()  # Скрываем второй репозиторий
#
#
# def show_repo2():
#     repo2_frame.pack(fill="both", expand=True)
#     repo1_frame.pack_forget()  # Скрываем первый репозиторий
#
#
# # Создаем главное окно
# root = tk.Tk()
# root.title("Переход между репозиториями")
# root.geometry("600x400")
#
# # Создаем панель для репозиториев
# main_frame = tk.Frame(root)
# main_frame.pack(fill="both", expand=True)
#
# # Фрейм для первого репозитория
# repo1_frame = tk.Frame(main_frame)
# repo1_label = tk.Label(repo1_frame, text="Это первый репозиторий", font=("Arial", 16))
# repo1_label.pack(pady=20)
#
# # Фрейм для второго репозитория
# repo2_frame = tk.Frame(main_frame)
# repo2_label = tk.Label(repo2_frame, text="Это второй репозиторий", font=("Arial", 16))
# repo2_label.pack(pady=20)
#
# # Кнопки для перехода между репозиториями
# button_frame = tk.Frame(root)
# button_frame.pack(side="bottom", fill="x")
#
# repo1_button = tk.Button(button_frame, text="Перейти в репозиторий 1", command=show_repo1)
# repo1_button.pack(side="left", padx=10, pady=10)
#
# repo2_button = tk.Button(button_frame, text="Перейти в репозиторий 2", command=show_repo2)
# repo2_button.pack(side="left", padx=10, pady=10)
#
# # Изначально показываем первый репозиторий
# show_repo1()
#
# # Запускаем главный цикл
# root.mainloop()

# #           №8.2
# import tkinter as tk
#
#
# def open_repo1_window():
#     repo1_window = tk.Toplevel(root)
#     repo1_window.title("Репозиторий 1")
#     repo1_label = tk.Label(repo1_window, text="Это репозиторий 1", font=("Arial", 16))
#     repo1_label.pack(padx=20, pady=20)
#
#
# def open_repo2_window():
#     repo2_window = tk.Toplevel(root)
#     repo2_window.title("Репозиторий 2")
#     repo2_label = tk.Label(repo2_window, text="Это репозиторий 2", font=("Arial", 16))
#     repo2_label.pack(padx=20, pady=20)
#
#
# # Создаем главное окно
# root = tk.Tk()
# root.title("Переход между репозиториями")
# root.geometry("400x300")
#
# # Кнопки для открытия окон
# repo1_button = tk.Button(root, text="Открыть репозиторий 1", command=open_repo1_window)
# repo1_button.pack(pady=20)
#
# repo2_button = tk.Button(root, text="Открыть репозиторий 2", command=open_repo2_window)
# repo2_button.pack(pady=20)
#
# # Запускаем главный цикл
# root.mainloop()

# #           №8.3
# import tkinter as tk
#
# def show_main():
#     """Показывает главный фрейм."""
#     main_frame.pack(fill="both", expand=True)
#     repo1_frame.pack_forget()
#     repo2_frame.pack_forget()
#
# def show_repo1():
#     """Показывает первый репозиторий."""
#     main_frame.pack_forget()
#     repo2_frame.pack_forget()
#     repo1_frame.pack(fill="both", expand=True)
#
# def show_repo2():
#     """Показывает второй репозиторий."""
#     main_frame.pack_forget()
#     repo1_frame.pack_forget()
#     repo2_frame.pack(fill="both", expand=True)
#
# # Создаем главное окно
# root = tk.Tk()
# root.title("Переход между репозиториями")
# root.geometry("600x400")
#
# # Главный фрейм
# main_frame = tk.Frame(root)
# main_label = tk.Label(main_frame, text="Главный экран", font=("Arial", 16))
# main_label.pack(pady=20)
#
# button_to_repo1 = tk.Button(main_frame, text="Перейти в репозиторий 1", command=show_repo1)
# button_to_repo1.pack(pady=10)
#
# button_to_repo2 = tk.Button(main_frame, text="Перейти в репозиторий 2", command=show_repo2)
# button_to_repo2.pack(pady=10)
#
# # Фрейм для первого репозитория
# repo1_frame = tk.Frame(root)
# repo1_label = tk.Label(repo1_frame, text="Это первый репозиторий", font=("Arial", 16))
# repo1_label.pack(pady=20)
#
# button_back_to_main1 = tk.Button(repo1_frame, text="Вернуться на главный экран", command=show_main)
# button_back_to_main1.pack(pady=10)
#
# # Фрейм для второго репозитория
# repo2_frame = tk.Frame(root)
# repo2_label = tk.Label(repo2_frame, text="Это второй репозиторий", font=("Arial", 16))
# repo2_label.pack(pady=20)
#
# button_back_to_main2 = tk.Button(repo2_frame, text="Вернуться на главный экран", command=show_main)
# button_back_to_main2.pack(pady=10)
#
# # Изначально показываем главный экран
# show_main()
#
# # Запускаем главный цикл
# root.mainloop()
