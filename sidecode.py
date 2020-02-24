from tkinter import *
from PIL import *
root=Tk()
im=PhotoImage(file='b_dotted_removed.png')
label=Label(image=im)
label.image=im
canvas=Canvas(root,height=500,width=500)
canvas.pack(expand=YES,fill=BOTH)
canvas.place(x=0,y=0)
canvas.create_image(0,0,image=im,anchor=NW)
root.update()
