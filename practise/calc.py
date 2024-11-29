import tkinter as tk

window = tk.Tk()

window.title('Калькулятор')
window.geometry("350x250")
window.resizable(False, False)


button_sum = tk.Button(window, text="+", width= 3, height= 2)
button_sum.place(x = 10, y = 150)
button_sub = tk.Button(window, text="-", width= 3, height= 2)
button_sub.place(x = 80, y = 150)
button_div = tk.Button(window, text=":", width= 3, height= 2)
button_div.place(x = 10, y = 200)
button_mul = tk.Button(window, text="*", width= 3, height= 2)
button_mul.place(x = 80, y = 200)

number1_entry = tk.Entry()
number1_entry.place(x = 70, y = 40)
number2_entry = tk.Entry()
number2_entry.place(x = 70, y = 100)
answer_entry = tk.Entry()
answer_entry.place(x = 150, y = 180)


number1 = tk.Label(window, text= "Number_1")
number1.place(x = 70, y = 10)
number2 = tk.Label(window, text= "Number_2")
number2.place(x = 70, y = 70)


window.mainloop()