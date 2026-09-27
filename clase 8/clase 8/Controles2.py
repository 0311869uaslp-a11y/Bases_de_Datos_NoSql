#https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/
from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from tkcalendar import DateEntry

def getdb():
    client=MongoClient(port=27017)#<<MONGODB URL>>)
    db=client.hospital
    return db

def showinputint(frame,nrow,valmin,valmax):
    idato=IntVar()
    #variable enteo declarada
    cint=Spinbox(frame,from_=valmin,to=valmax,increment=1,textvariable=idato)
    cint.grid(padx=8,pady=6,row=nrow,column=1)
    return idato

def showinputstr(frame,nrow):
    sdato=StringVar()
    ctex=Entry(frame,textvariable=sdato)
    ctex.grid(padx=8,pady=6,row=nrow,column=1)
    return sdato

def showinputdate(frame,nrow):
    sdato=StringVar()
    cdate=DateEntry(frame,locale='en_US',date_pattern='y-mm-dd',textvariable=sdato,
                    selectmode='day',year=2022,month=11,day=28)
    cdate.grid(padx=8,pady=6,row=nrow,column=1)
    return sdato

def showinputcheck(frame,opciones,nrow):
    sdatos=dict()
    for j in range(len(opciones)):
        valor=opciones[j]
        sdatos[valor]=IntVar()
        check=Checkbutton(frame,text=valor,onvalue=1, offvalue=0,
                          variable=sdatos[valor],textvariable=sdatos)
        check.grid(padx=8,pady=6,row=nrow,column=1)
        nrow=nrow+1
    return sdatos,nrow

def showinputradio(frame,opciones,nrow):
    idato=IntVar()
    for j in range(len(opciones)):
        valor=opciones[j]
        cradio=Radiobutton(frame,text=valor,variable=idato,value=j)
        cradio.grid(padx=8,pady=6,row=nrow,column=1)
        nrow=nrow+1
    return idato,nrow

def captura(win,campos,tipocampos,listopc,handler):
    FCaptura=Frame(win)
    #me genera un espacio para agregar los datos
    SDatos=dict()
    etiqueta=Label(FCaptura,text="Registrar Doctor",font=("Helvetica", 13))
    etiqueta.grid(padx=6,pady=8,row=0,column=0)
    nrow=1
    i=0
    #todos los textos van en la primer columna
    for i in range(len(campos)):
        campo=campos[i]
        tipo=tipocampos[i]
        etiqueta=Label(FCaptura,text=campo+":",font=("Arial", 12))
        etiqueta.grid(padx=8,pady=6,row=nrow,column=0)
        if tipo=="str":
            SDatos[campo]=showinputstr(FCaptura,nrow)
        elif tipo=="int":
            SDatos[campo]=showinputint(FCaptura,nrow,18,90)
        elif tipo=="date":
            SDatos[campo]=showinputdate(FCaptura,nrow)
        elif tipo=="check":
            SDatos[campo],nrow=showinputcheck(FCaptura,listopc[campo],nrow)
        elif tipo=="radio":
            SDatos[campo],nrow=showinputradio(FCaptura,listopc[campo],nrow)
        nrow=nrow+1
    BRegistro=Button(FCaptura, text="Registrar doctor", command=handler)
    BRegistro.grid(padx=8,pady=15,row=nrow,column=1)
    FCaptura.grid(row=0,column=0)
    return SDatos
    
def HRegistrar():
    documento=dict()
    i=0
    for i in range(len(campos)):
        campo=campos[i]
        tipo=tipocampos[i]
        if tipo=="int":
            documento[campo]=int(SDatos[campo].get())
        elif tipo=="str" or tipo=="date":
            documento[campo]=str(SDatos[campo].get())
        elif tipo=="radio":
            documento[campo]=listopciones[campo][SDatos[campo].get()]
        elif tipo=="check":
            documento[campo]=[];
            for j in range(len(listopciones[campo])):
                valor=listopciones[campo][j]
                if SDatos[campo][valor].get()==1:
                    documento[campo].append(listopciones[campo][j])
    print(documento)
    DBH.doctores.insert_one(documento)
    messagebox.showinfo(title="Error",message="Doctor registrado correctamente")
    
window=Tk()
campos=["nombre","edad","sexo","especialidad","fcontratacion","idiomas"]
tipocampos=["str","int","radio","check","date","check"]
listopciones={"sexo":["femenino","masculino"],
              "especialidad":["cirujano","cirujano cardiotoracico","infectologo","general","patologo"],
              "idiomas":["español","ingles","francés","chino"]}
SDatos=captura(window,campos,tipocampos,listopciones,HRegistrar)
DBH=getdb()
window.mainloop()
