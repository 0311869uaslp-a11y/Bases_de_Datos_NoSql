from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from pprint import pprint

class Registro:
    def __init__(self,window):
        self.__win=window
        self.__getdb()
    
    def setcampos(self,campos,intcampos):
        self.__campos=campos
        self.__intcampos=intcampos

    def sethandlerHRegistrar(self):
        self.__handler=self.__HRegistrar
    
    def __getdb(self):
        client=MongoClient(port=27017)#<<MONGODB URL>>)
        self.__DBH=client.hospital

    def captura(self):
        self.__FCaptura=ttk.Frame(self.__win)
        self.__SDatos=dict()
        EDatos=dict()
        etiqueta=ttk.Label(self.__FCaptura,text="Registrar Doctor",font=("Helvetica", 13))
        etiqueta.grid(padx=6,pady=8,row=0,column=0)
        nrow=1
        for campo in self.__campos:
            etiqueta=ttk.Label(self.__FCaptura,text=campo+":",font=("Arial", 12))
            etiqueta.grid(padx=8,pady=6,row=nrow,column=0)
            self.__SDatos[campo]=StringVar()
            EDatos[campo]=ttk.Entry(self.__FCaptura,textvariable=self.__SDatos[campo])
            EDatos[campo].grid(padx=8,pady=6,row=nrow,column=1)
            nrow=nrow+1
        BRegistro=Button(self.__FCaptura, text="Registrar doctor", command=self.__handler)
        BRegistro.grid(padx=8,pady=15,row=8,column=1)
        self.__FCaptura.grid(row=0,column=0)
        
    def __HRegistrar(self):
        documento=dict()
        for campo in self.__campos:
            if campo in self.__intcampos:
                documento[campo]=int(self.__SDatos[campo].get())
            else:
                documento[campo]=str(self.__SDatos[campo].get())
        print(documento)
        self.__DBH.doctores.insert_one(documento)
        messagebox.showinfo(title="Error",message="Doctor registrado correctamente")
    
window=Tk()
campos=["nombre","apellido","edad","especialidad","origen"]
intcampos=["edad"]
program=Registro(window)
program.setcampos(campos,intcampos)
program.sethandlerHRegistrar()
program.captura()
window.mainloop()