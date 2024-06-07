from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 # pip install opencv-python
import os
import numpy as np # pip install numpy


class Train:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1366x768+0+0")
                self.root.title("Face_Recogonition_System")
                
                #title section
                title_lb1 = Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
                title_lb1.place(x=0,y=0,width=1530,height=45)
                
                img_top=Image.open(r"college_images\facialrecognition.png")
                img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)
                # set image as lable
                f_lb1 = Button(self.root,image=self.photoimg_top,cursor="hand2",command=self.train_classifier)
                f_lb1.place(x=0,y=55,width=1530,height=325)
                
                b1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2")
                b1.place(x=0,y=380,width=1530,height=60)
                
                img_bottom=Image.open(r"college_images\facial-recognition_0.jpg")
                img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
                self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
                # set image as lable
                f_lb1 = Label(self.root,image=self.photoimg_bottom)
                f_lb1.place(x=0,y=440,width=1530,height=325)
                
        def train_classifier(self):
                data_dir=("data")
                path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
                
                faces=[]
                ids=[]
                
                for image in path:
                        img=Image.open(image).convert('L') # gray scale image
                        imageNp=np.array(img,'uint8')
                        id=int(os.path.split(image)[1].split('.')[1])
                        
                        faces.append(imageNp)
                        ids.append(id)
                        cv2.imshow("Training",imageNp) 
                        cv2.waitKey(1)==13
                ids=np.array(ids)
                
        #=================Train Classifier=============
                clf=cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces,ids)
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Training dataset completed!!",parent=self.root)

if __name__ == "__main__":
        root=Tk()
        obj=Train(root)
        root.mainloop()