import tkinter as tk
import numpy as np
from tkinter import ttk
import pytable
from tkinter import * 
import sys
root = tk.Tk()
root.title("Tabulka") 
my_menu = Menu(root)
root.config(menu=my_menu)
config_menu = Menu(my_menu)
my_menu.add_cascade(label="Option", menu=config_menu)
config_menu.add_command(label="help", command=help_program)
config_menu.add_command(label="actual data", command=actual_data)
config_menu.add_command(label="save", command=new_record)
config_menu.add_command(label="exit", command=sys.exit)

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

def new_record():
    pass
button = Button(root, text="New record", command=new_record)




# Přiřazení funkce k tlačítku
table = create_table(data, root)
table.pack(expand=True, fill="both")

# Spuštění hlavní smyčky Tkinter
root.mainloop()
