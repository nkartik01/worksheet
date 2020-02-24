from tkinter import *
from PIL import *
from PIL import Image
from docx import*
from tkinter import filedialog
from docx.shared import *
import subprocess
import io
import os
import pyscreenshot as ImageGrab
def initiate():
    global page_type
    page_type=StringVar(root)
    page_type.set('A4')
    OptionMenu(root,page_type,'A4','A3','Legal').place(x=50,y=50)
    Button(root,text='Submit',command=page_selected).place(x=50,y=100)
def page_selected():
    
    p_type=str(page_type.get())
    destroy1()
    canvas1=Canvas(root,height=990,width=500)
    canvas1.pack(expand=YES,fill=BOTH)
    canvas1.place(x=0,y=0)
    
    global canvas
    if p_type=='A4':
        canvas=Canvas(root,height=990,width=700,bg='white')
        canvas.pack(expand=YES,fill=BOTH)
        canvas.place(x=1000,y=50)
    elif p_type=='A3':
        canvas=Canvas(root,height=990,width=700,bg='white')
        canvas.pack(expand=YES,fill=BOTH)
        canvas.place(x=1000,y=50)
    print('h1')
    Label(root,text='Enter height').place(y=50,x=100)
    global e1
    e1=Entry(root)
    e1.place(y=70,x=100)
    Label(root,text='Enter number of chaaracters in a row').place(y=90,x=100)
    global e2
    e2=Entry(root)
    e2.place(y=110,x=100)
    Button(root,text='Set',command=set2).place(x=130,y=130)
    root.update()
    global e3
    e3=Entry(root)
    e3.place(x=100,y=200)
    Button(root,text='Save Output',command=save).place(x=100,y=220)
    Button(root,text='Add Image',command=set1).place(x=130,y=160)
    
def save():
    global canvas
    name=e3.get()
    print(canvas.winfo_rootx()+canvas.winfo_x(),canvas.winfo_rooty()+canvas.winfo_y(),canvas.winfo_rootx()+canvas.winfo_x()+canvas.winfo_width(),canvas.winfo_rooty()+canvas.winfo_y()+canvas.winfo_height())
    saved=ImageGrab.grab(bbox=(1000,50,1700,1040)).save(name+'.pdf')
    
def set2():
    global x1
    x1=0
    j=150
    global x
    x=int(e1.get())/2
    canvas.create_text(50,50,text='Apple Pie Convent School',font='times 40',anchor=NW)
    while(j+(4*x)<970):
        canvas.create_line(0,j,700,j,fill='red')
        canvas.create_line(0,j+x,700,x+j,fill='blue')
        canvas.create_line(0,j+x+x,700,x+j+x,fill='blue')
        canvas.create_line(0,j+(3*x),700,j+(3*x),fill='red')
        j+=(5*x)
        print(j)
    canvas.create_text(450,940,text="Teacher's Sign",anchor=NW,font='times 12')
    global k
    k=130
    global l
    l=0
    set1()
def set1():
    global label,im,x1,y1
    global canvas
    global img
    img=(filedialog.askopenfilename())
    im=(PhotoImage(file=(img)))
    global label
    label=Label(image=im)
    label.image=im
    h=im.height()
    im=im.zoom(int(e1.get()))
    #print(im[len(im)-1].height(),im[len(im)-1].width(),e1.get(),e2.get(),h,w)
    im=im.subsample(h)
    #print(im[len(im)-1].height(),im[len(im)-1].width())
    label.configure(image=im)
    label.image=im
    canvas.delete('cam')
    #logo=PhotoImage(file='logo.png')
    #h=logo.width()
    #logo=logo.zoom(700)
    #logo=logo.subsample(h)
    #logo_label=Label(image=logo)
    #logo_label.image=logo
    #canvas.create_image(0,0,image=logo,anchor=NW)
    global e4
    e4=Entry(root)
    e4.place(x=400,y=70+x1)
    Label(root,text='Number of times This Image is needed').place(x=400,y=50+x1)
    Button(root,text='Place',command=place1).place(x=400,y=90+x1)
    x1+=100
    img_dot=(filedialog.askopenfilename())
    global ix
    ix=PhotoImage(file=img_dot)
    h=ix.height()
    ix=ix.zoom(int(e1.get()))
    ix=ix.subsample(h)
    label2=Label(image=ix)
    label2.image=ix

def place1():
    global x,x1
    
    q1=int(e4.get())
    global k
    q=0
    global l
    print(q,l,k,q1)
    while(20+l<770 and q<q1):
        q+=1
        while(k+(5*x)<970):
            if k==130:
                canvas.create_image(20+l,150,image=im,anchor=NW)
            else:
                canvas.create_image(20+l,20+k,image=ix,anchor=NW)
            k+=(5*x)
            root.update()
            print(k,l,q)
        k=130
        l+=(770//int(e2.get()))
        
    
    
    root.update()
def destroy1():
    for i in root.grid_slaves():
        i.destroy()
root=Tk()
root.attributes('-fullscreen',True)
c=Canvas(root,height=1000,width=1500)
c.pack(expand=YES,fill=BOTH)
c.place(x=0,y=0)

img=[]
im=[]
initiate()
