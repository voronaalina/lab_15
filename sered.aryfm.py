import tkinter as tk

def calculate_average():
    numbers = entry_field.get()
    
    try:
        numbers_list = [float(num) for num in numbers.split()]
        if numbers_list:
            average = sum(numbers_list) / len(numbers_list)
            #pytannya
            result_field.delete("1.0", tk.END)
            result_field.insert("1.0", "Середнє арифметичне: "+ str(average))
        else:
            result_field.delete("1.0", tk.END)
            result_field.insert("1.0", "Введіть числа ще раз")
    except ValueError:
        result_field.delete("1.0", tk.END)
        result_field.insert("1.0", "Error")

window = tk.Tk()
window.title("обчислення середнього арифметичного")
window.geometry("400x300")
window.configure(bg="pink")

frame = tk.Frame(window, bg="white")
frame.pack(pady=20)

entry_label = tk.Label(frame, text="введіть числа через пробіл: ")
entry_label.pack()
entry_field = tk.Entry(frame, width = 40, bg="light blue")
entry_field.pack(pady=5)

calculate_button = tk.Button(frame, text = "обчислити", command = calculate_average, bg="pink")
calculate_button.pack(pady=10)
result_field = tk.Text(frame, width = 40, height = 5, bg="light blue")
result_field.pack()
window.mainloop()
