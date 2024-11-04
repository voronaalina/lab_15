import tkinter as tk
import json

with open("c://lab15//elements.json", "r", encoding="utf-8")as file:
    elements_data = json.load(file)

window = tk.Tk()
window.title("Довідник хімічних елементів")
window.geometry("410x380")
window.configure(bg="olive")

def search_element():
    symbol = entry_symbol.get().strip()
    element = elements_data.get(symbol)
    if element:
        result_text = ("Назва: " + element['name'], "\nНомер: " + str(element['number']),  "\nАтомна маса: " + str(element['mass']))
    else:
        result_text = "елемент не знайдено"
    
    entry_result.delete(0, tk.END)
    entry_result.insert(0, result_text)

label_prompt = tk.Label(text="введіть елемент:", fg="black", bg="olive", width=30)
entry_symbol = tk.Entry(fg="black", bg="white", width=20)
button_search = tk.Button(text="Пошук", width=10, height=1, background="pink", foreground="light blue", command=search_element)
entry_result = tk.Entry(fg="black", bg="white", width=50)

label_prompt.pack(pady=10)
entry_symbol.pack(pady=5)
button_search.pack(pady=10)
entry_result.pack(pady=20)

entry_result.insert(0, "Результат з'явиться тут...")
button_search.config(command=search_element)
window.mainloop()
