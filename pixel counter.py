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
k=1
p=0
print(rgb)
for i in range(len(rgb)):
    for j in range(len(rgb[i])):
        if(list(rgb[i][j])==[255,255,255]):
            if(k==0):
                
                try:
                    if(p>1):
                        data[i][j-1]=[255,0,0,100]
                        data[i][j-2]=[255,0,0,100]
                except:
                    pass
                k=1
                print(p)
        else:
            if(k==0):
                p+=1
            else:
                k=0
                p=1
new_im=PIL.Image.fromarray(data)
img='marked_'+img
im=ImageTk.PhotoImage(new_im)
new_im.save(img)

#label=Label(image=new_im)
#label.image=new_im
#Label(root,image=new_im).pack()
