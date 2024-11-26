import os
import tkinter as tk

# Подавление предупреждения о депрекации Tk
os.environ['TK_SILENCE_DEPRECATION'] = '1'

print("Начало выполнения скрипта")

# Создание главного окна
window = tk.Tk()
print("Окно создано")
window.geometry("300x200")  # Устанавливаем размер окна

# Создание метки
text = tk.Label(window, text='Файл:', background='blue', foreground='white')
print("Метка создана")
text.place(x=100, y=100)  # Измененные координаты для лучшей видимости

# Запуск главного цикла
window.mainloop()
print("Главный цикл завершен")
