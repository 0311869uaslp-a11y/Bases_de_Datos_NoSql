#https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from pymongo import MongoClient
from PIL import Image, ImageTk
import base64

def getdb():
    client=MongoClient(port=27017)#<<MONGODB URL>>)
    db=client.walmart
    return db

def showinputint(frame,nrow,valmin,valmax):
    idato=IntVar()
    cint=Spinbox(frame,from_=valmin,to=valmax,increment=1,textvariable=idato)
    cint.grid(padx=8,pady=6,row=nrow,column=1)
    return idato

def showinputstr(frame,nrow):
    sdato=StringVar()
    ctex=Entry(frame,textvariable=sdato)
    ctex.grid(padx=8,pady=6,row=nrow,column=1)
    return sdato

def showinputfile(frame,nrow):
    b1 = Button(frame, text='Seleccionar imagen', width=20,command = upload_file)
    b1.grid(padx=8,pady=6,row=nrow,column=1)

def upload_file():
    global filename
    f_types = [('Jpg Files', '*.jpg'),
                ('PNG Files','*.png')]   # type of files to select 
    filename =filedialog.askopenfilename(multiple=False,filetypes=f_types)
    muestraimagen(filename)
    
def muestraimagen(arch):
    img=Image.open(arch) # read the image file
    img=img.resize((100,100)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =Label(FCaptura)
    e1.grid(row=5,column=1)
    e1.image = img
    e1['image']=img # garbage collection

def captura(win,campos,tipocampos,handler):
    FCaptura=Frame(win)
    SDatos=dict()
    etiqueta=Label(FCaptura,text="Registrar Producto",font=("Helvetica", 13))
    etiqueta.grid(padx=6,pady=8,row=0,column=0)
    nrow=1
    i=0
    for i in range(len(campos)):
        campo=campos[i]
        tipo=tipocampos[i]
        etiqueta=Label(FCaptura,text=campo+":",font=("Arial", 12))
        etiqueta.grid(padx=8,pady=6,row=nrow,column=0)
        if tipo=="str":
            SDatos[campo]=showinputstr(FCaptura,nrow)
        elif tipo=="int":
            SDatos[campo]=showinputint(FCaptura,nrow,1,5000)
        elif tipo=="img":
            showinputfile(FCaptura,nrow)
        nrow=nrow+1
    BRegistro=Button(FCaptura, text="Registrar producto", command=handler)
    BRegistro.grid(padx=8,pady=10,row=7,column=1)
    FCaptura.grid(row=0,column=0)
    return SDatos,FCaptura
    
def HRegistrar():
    global filename
    documento=dict()
    i=0
    for i in range(len(campos)):
        campo=campos[i]
        tipo=tipocampos[i]
        if tipo=="int":
            documento[campo]=int(SDatos[campo].get())
        elif tipo=="str" or tipo=="date":
            documento[campo]=str(SDatos[campo].get())
        elif tipo=="img":
            documento[campo]=convertToBinaryData(filename)
    print(documento)
    DBH.productos.insert_one(documento)
    messagebox.showinfo(title="Registro",message="Producto registrado correctamente")
    
def convertToBinaryData(arch):
    # Convert digital data to binary format
    with open(arch, 'rb') as file:
        binaryData = file.read()
    bin64=base64.b64encode(binaryData)
    return bin64
    
window=Tk()
campos=["nombre","id","imagen"]
tipocampos=["str","int","img"]
SDatos,FCaptura=captura(window,campos,tipocampos,HRegistrar)
DBH=getdb()
window.mainloop()

