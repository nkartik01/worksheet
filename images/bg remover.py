import PIL.Image
from PIL import ImageTk
import numpy as np
from tkinter import *
from tkinter import filedialog
import os,sys
root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack(expand=YES,fill=BOTH)
canvas.place(x=0,y=0)
onlyfiles = [f for f in os.listdir('C:/Users/aknar/Desktop/image_in_docs/images')]
for img1 in onlyfiles:
    img=str(img1)
    print(img[-4::])
    if str(img[-4::])=='.png' and str(img[:8:])!='removed_':
        print(img)
        print('hi')
        img=img.split('/')
        img=img[len(img)-1]
        
        fp=open(img,'rb')
        im=PIL.Image.open(fp)
        im=im.convert('RGBA')
        data=np.array(im)
        rgb=data[:,:,:]
        #if img=='l_dotted.png':
         #   for i in range(len(rgb)):
          #      for j in range(len(rgb[0])):
           #         print(rgb[i][j])
        print(len(rgb),len(rgb[0]))
        b=0
        for i in range(len(rgb)):
            ##print(i,rgb[i][0][0])
            for j in range(len(rgb[i])):
                if rgb[i][j][0]<100 and rgb[i][j][1]<100 and rgb[i][j][2]<100:
                    b=1
                if b==1:
                    rgb=rgb[i:,:,:]
                    break
            if b==1:
                break
        print(len(rgb),len(rgb[0]))
        b=0
        for i in range(len(rgb)-1,-1,-1):
            ##print(i,rgb[i][0][0])
            for j in range(len(rgb[i])):
                if rgb[i][j][0]<100 and rgb[i][j][1]<100 and rgb[i][j][2]<100:
                    b=1
                if b==1 and i<len(rgb)-3:
                    rgb=rgb[:i+2,:,:]
                    break
            if b==1:
                break
        print(len(rgb),len(rgb[0]))
        b=0
        mi=1000
        for i in range(len(rgb[0])):
            for j in range(len(rgb)):
                ##print(i,j,mi,rgb[j][i][0],rgb[j][i][1],rgb[j][i][2])
                if mi>i and rgb[j][i][0]<100 and rgb[j][i][1]<100 and rgb[j][i][2]<100:
                    #print('h1')
                    mi=i
                    break
        if mi!=0:
            rgb=rgb[:,mi:,:]
        print(len(rgb),len(rgb[0]))
        mi=0
        for i in range(len(rgb[0])-1,-1,-1):
            #print(i,mi)
            for j in range(len(rgb)):
                #print(j)
                #print(rgb[j][i])
                if mi<i and rgb[j][i][0]<100 and rgb[j][i][1]<100 and rgb[j][i][2]<100:
                    mi=i
                    break
        print(len(rgb),len(rgb[0]))
        #print(rgb)
        
        if(mi<len(rgb[0])-3):
            rgb=rgb[:,:mi+2,:]
        #print(rgb)
        
        colour=[255,255,255,255]
        mask=np.all(rgb==colour,axis=-1)
        #print(rgb[mask])
        rgb[mask]=[0,0,0,0]
        new_im=PIL.Image.fromarray(rgb)
        #label=Label(image=new_im)
        #label.image=new_im
        #canvas.create_image(100,100,image=new_im,anchor=NW)
        #root.update()
        #time.sleep(2)
        #new_im=ImageTk.PhotoImage(new_im)
        new_im.save('removed_'+img)
        print('k')
root.destroy()
#label=Label(image=new_im)
#label.image=new_im
#Label(root,image=new_im).pack()
