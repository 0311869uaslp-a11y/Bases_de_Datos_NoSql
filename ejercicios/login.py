#https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/
#colores
#http://patriciaemiguel.com/python/2019/08/01/python-tkinter-colores.html
from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import hashlib

class CUsers():
    def __init__(self,win):
        self.win=win
        self.frame=Frame(self.win,bg="cornsilk2")
        client=MongoClient(port=27017)
        self.db=client.walmart
        
    def clearframe(self):
        vaciar(self.frame)
    
    def registro(self):
        self.campos=["nombre","contrasena"]
        self.tipocampos=["str","pwd"]
        self.captura("Registrar usuario","Registrar",self.HRegistrar)
        
    def login(self):
        self.campos=["nombre","contrasena"]
        self.tipocampos=["str","pwd"]
        self.captura("Iniciar sesión","Entrar",self.HLogin)
        self.win.mainloop()

    def showinputstr(self):
        sdato=StringVar()
        cpwd=Entry(self.frame,textvariable=sdato)
        cpwd.grid(padx=8,pady=6,row=self.nrow,column=1)
        return sdato
    
    def showinputpwd(self):
        sdato=StringVar()
        ctex=Entry(self.frame,textvariable=sdato, show="*")
        ctex.grid(padx=8,pady=6,row=self.nrow,column=1)
        return sdato

    def captura(self,titulo,bottext,handler):
        self.clearframe()
        self.Datos=dict()
        etiqueta=Label(self.frame,text=titulo,font=("Helvetica", 13),bg="cornsilk2")
        etiqueta.grid(padx=6,pady=8,row=2,column=0)
        self.nrow=3
        i=0
        for i in range(len(self.campos)):
            campo=self.campos[i]
            tipo=self.tipocampos[i]
            etiqueta=Label(self.frame,text=campo+":",font=("Arial", 12),bg="cornsilk2")
            etiqueta.grid(padx=8,pady=6,row=self.nrow,column=0)
            if tipo=="str":
                self.Datos[campo]=self.showinputstr()
            elif tipo=="int":
                self.Datos[campo]=self.showinputint(4,90)
            elif tipo=="pwd":
                self.Datos[campo]=self.showinputpwd()
            self.nrow=self.nrow+1
        BRegistro=Button(self.frame, text=bottext, command=handler)
        BRegistro.grid(padx=8,pady=15,row=6,column=0)
        BCancel=Button(self.frame, text="Cancelar")
        BCancel.grid(padx=8,pady=15,row=6,column=1)
        self.frame.grid(row=6,column=0,columnspan=2,padx=15)
        
    def getDatos(self):
        documento=dict()
        i=0
        for i in range(len(self.campos)):
            campo=self.campos[i]
            tipo=self.tipocampos[i]
            if tipo=="int":
                documento[campo]=int(self.Datos[campo].get())
            elif tipo=="str" or tipo=="date" or tipo=="pwd":
                documento[campo]=str(self.Datos[campo].get())
        documento['contrasena']=(documento['nombre']+documento['contrasena']).encode('UTF-8')
        cifrar=hashlib.sha512()
        cifrar.update(documento['contrasena'])
        documento['contrasena']=cifrar.hexdigest()
        print(documento)
        return documento
    
    def HRegistrar(self):
        document=self.getDatos()
        self.db.empleados.insert_one(document)
        messagebox.showinfo(title="Registro",message="Jugador registrado correctamente")
        self.win.destroy
        
    def HLogin(self):
        document=self.getDatos()
        empleado=self.db.empleados.find_one({"nombre":document['nombre'],"contrasena":document['contrasena']})
        print(empleado)
        if empleado !=None:
            homeusuario(self.win,empleado['nombre'])
        else:
            messagebox.showinfo(title="Error",message="Usuario o contraseña incorrectos")

def vaciar(element):
    for widget in element.winfo_children():
        widget.destroy()

def homeusuario(win,user):
    vaciar(win)
    etiqueta=Label(win,text="Bienvenido "+user,font=("Helvetica", 13),bg="cornsilk2")
    etiqueta.grid(padx=6,pady=8,row=2,column=0)

main=Tk()
main.configure(bg="Antiquewhite4")
main.geometry("360x280")
sesion=CUsers(main)
BRegistro=Button(main, text="Registrarse", command=sesion.registro)
BRegistro.grid(padx=8,pady=15,row=4,column=0)
BLogin=Button(main, text="Iniciar sesión", command=sesion.login)
BLogin.grid(padx=8,pady=15,row=4,column=1)
main.mainloop()
