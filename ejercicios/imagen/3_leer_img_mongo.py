#https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from pymongo import MongoClient
from pprint import pprint#make the output look more pretty
from PIL import Image, ImageTk
import base64

def getdb():
    client=MongoClient(port=27017)#<<MONGODB URL>>)
    db=client.walmart
    return db

def item_selected(event):
    for selected_item in tabla.selection():
        item = tabla.item(selected_item)
        record = item['values']
        i=record[2]
        imagen=decodeBinaryData(almacen[i]['imagen'])
        showimagen(imagen)
        
def showimagen(arch):
    for widget in frameimage.winfo_children():
        widget.destroy()
    img=ImageTk.PhotoImage(data=arch)
    e1 =Label(frameimage)
    e1.grid(row=5,column=0)
    e1.image = img
    e1['image']=img
    
def decodeBinaryData(info):
    img=base64.b64decode(info)
    return img

def showtabla(datos):
    columns = ('nombre', 'id', 'imagen')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading('nombre', text='Nombre')
    tree.heading('id', text='id')
    tree.heading('imagen', text='Imagen')
    cont=0
    for p in datos:
        tree.insert('', END, values=(p['nombre'],p['id'],cont))
        cont=cont+1
    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.grid(row=0, column=0, sticky='nsew')
    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    return tree

root =Tk()
root.title('Interfaz grafica')
root.geometry('620x680')
db=getdb()
almacen=list(db.productos.find())
tabla=showtabla(almacen)
frameimage=Frame(root)
frameimage.grid(row=3,column=0)
root.mainloop()
