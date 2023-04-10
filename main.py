import tkinter as tk
import numpy as np
from tkinter import ttk
import pytable

def create_table(data, parent):
    # Vytvoření Treeview widgetu
    columns = [""] + [f"Col {i+1}" for i in range(data.shape[1])]
    table = ttk.Treeview(parent, columns=columns, show="headings")

    # Vytvoření nadpisů sloupců
    for i, column in enumerate(columns):
        table.heading(column, text=column)
    
    # Vypsání hodnot do tabulky
    for i in range(data.shape[0]):
        values = [f"Row {i+1}"] + list(data[i])
        table.insert("", "end", values=values)
    
    # Nastavení minimální velikosti sloupce
    table.column("#0", width=10, minwidth=10)

    # Vrácení widgetu
    return table

# Testovací data
data = pytable.load("numpy")

# Vytvoření okna s tabulkou
window = tk.Tk()
window.title("Tabulka")

table = create_table(data, window)
table.pack(expand=True, fill="both")

# Spuštění hlavní smyčky Tkinter
window.mainloop()
