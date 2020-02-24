import PIL.Image
from PIL import ImageTk
import numpy as np
from tkinter import *
from tkinter import filedialog
root=Tk()
img=filedialog.askopenfilename()
img=img.split('/')
img=img[len(img)-1]
fp=open(img,'rb')
im=PIL.Image.open(fp)
im=im.convert('RGBA')
data=np.array(im)
rgb=data[:,:,:3]
colour=[255,255,255]
mask=np.all(rgb==colour,axis=-1)
data[mask]=[0,0,0,0]
new_im=PIL.Image.fromarray(data)
img='removed_'+img
im=ImageTk.PhotoImage(new_im)
new_im.save(img)
#label=Label(image=new_im)
#label.image=new_im
#Label(root,image=new_im).pack()
