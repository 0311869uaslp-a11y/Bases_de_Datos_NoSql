from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from pprint import pprint

def getdb():
    client=MongoClient(port=27017)#<<MONGODB URL>>)
    db=client.hospital
    return db

def captura(win,campos,handler):
    FCaptura=ttk.Frame(win)
    SDatos=dict()
    EDatos=dict()
    etiqueta=ttk.Label(FCaptura,text="Registrar Doctor",font=("Helvetica", 13))
    etiqueta.grid(padx=6,pady=8,row=0,column=0)
    nrow=1
    for campo in campos:
        etiqueta=ttk.Label(FCaptura,text=campo+":",font=("Arial", 12))
        etiqueta.grid(padx=8,pady=6,row=nrow,column=0)
        SDatos[campo]=StringVar()
        EDatos[campo]=ttk.Entry(FCaptura,textvariable=SDatos[campo])
        EDatos[campo].grid(padx=8,pady=6,row=nrow,column=1)
        nrow=nrow+1
    BRegistro=Button(FCaptura, text="Registrar doctor", command=handler)
    BRegistro.grid(padx=8,pady=15,row=8,column=1)
    FCaptura.grid(row=0,column=0)
    return SDatos
    
def HRegistrar():
    documento=dict()
    for campo in campos:
        if campo in intcampos:
            documento[campo]=int(SDatos[campo].get())
        else:
            documento[campo]=str(SDatos[campo].get())
    print(documento)
    DBH.doctores.insert_one(documento)
    messagebox.showinfo(title="Error",message="Doctor registrado correctamente")
    
window=Tk()
campos=["nombre","apellido","edad","especialidad","origen"]
intcampos=["edad"]
SDatos=captura(window,campos,HRegistrar)
DBH=getdb()
window.mainloop()