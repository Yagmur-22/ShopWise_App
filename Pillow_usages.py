# #              №1
# import tkinter as tk
# from PIL import Image, ImageTk
#
# # Создаем основное окно
# root = tk.Tk()
# root.title("Кнопка с изображением")
#
# # Загружаем изображение
# image = Image.open("path_to_image.png")  # Укажите путь к вашему изображению
# image = image.resize((100, 100))  # Устанавливаем размер изображения (если нужно)
# photo = ImageTk.PhotoImage(image)
#
# # Создаем кнопку с изображением
# button = tk.Button(root, image=photo)
# button.pack()
#
# # Запускаем главный цикл
# root.mainloop()

# #              №2
# import tkinter as tk
#
# # Создаем основное окно
# root = tk.Tk()
#
# # Загружаем изображение (можно использовать .png, .gif и другие форматы)
# image = tk.PhotoImage(file="path_to_image.gif")  # Укажите путь к вашему изображению
#
# # Создаем кнопку с изображением
# button = tk.Button(root, image=image, command=lambda: print("Button clicked!"))
# button.pack()
#
# # Запускаем основной цикл приложения
# root.mainloop()

# #              №3
# import tkinter as tk
# from PIL import Image, ImageTk
#
# # Создаем основное окно
# root = tk.Tk()
#
# # Загружаем изображение с помощью Pillow
# img = Image.open("path_to_image.png")  # Укажите путь к изображению
# photo = ImageTk.PhotoImage(img)
#
# # Создаем кнопку с изображением
# button = tk.Button(root, image=photo, command=lambda: print("Button clicked!"))
# button.pack()
#
# # Запускаем основной цикл приложения
# root.mainloop()
