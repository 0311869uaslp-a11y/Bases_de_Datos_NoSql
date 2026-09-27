import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from pymongo import MongoClient
from pprint import pprint#make the output look more pretty

client = MongoClient(port=27017)#<<MONGODB URL>>)
db=client.hospital
doctores=list(db.doctores.find())

root = tk.Tk()
root.title('Interfaz grafica')
root.geometry('620x200')

# define columns
columns = ('nombre', 'apellido', 'especialidad','origen')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('nombre', text='Nombre')
tree.heading('apellido', text='Apellido')
tree.heading('especialidad', text='Especialidad')
tree.heading('origen', text='Origen')

# add data to the treeview
for dr in doctores:
    tree.insert('', tk.END, values=(dr['nombre'],dr['apellido'],dr['especialidad'],dr['edad'],dr["_id"]))

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        print(record)

tree.bind('<<TreeviewSelect>>', item_selected)
tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()
