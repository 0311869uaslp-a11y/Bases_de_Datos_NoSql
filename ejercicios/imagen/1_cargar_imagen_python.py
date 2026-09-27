#https://www.plus2net.com/python/tkinter-filedialog-upload-display.php
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

def muestraimagen(arch,row,col):
    img=Image.open(arch) # read the image file
    img=img.resize((100,100)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =Label(my_w)
    e1.grid(row=row,column=col)
    e1.image = img
    e1['image']=img # garbage collection 

def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
                ('PNG Files','*.png')]   # type of files to select 
    filename = filedialog.askopenfilename(multiple=True,filetypes=f_types)
    col=1 # start from column 1
    row=3 # start from row 3 
    for f in filename:
        muestraimagen(f,row,col)
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column  

my_w = Tk()
my_w.geometry("410x300")  # Size of the window 
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')
l1 = Label(my_w,text='Subir imagenes',width=30,font=my_font1)  
l1.grid(row=1,column=1,columnspan=4)
b1 = Button(my_w, text='Seleccionar archivos', width=20,command = upload_file)
b1.grid(row=2,column=1,columnspan=4)               
my_w.mainloop()
