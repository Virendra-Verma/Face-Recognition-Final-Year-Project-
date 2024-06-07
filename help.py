from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 # pip install opencv-python


class Help:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1366x768+0+0")
                self.root.title("Face_Recogonition_System")
                
                #title section
                title_lb1 = Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
                title_lb1.place(x=0,y=0,width=1530,height=50)
                
                img_top=Image.open(r"college_images\helpp.jpeg")
                img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)
                # set image as lable
                f_lb1 = Label(self.root,image=self.photoimg_top,cursor="hand2")
                f_lb1.place(x=0,y=55,width=1550,height=720)
                
                #Developer info
                dev_lb1=Label(f_lb1,text="E-mail: vkverma515@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=550,y=150,width=450,height=50)
                
                dev_lb1=Label(f_lb1,text="E-mail: priyagupta515@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=550,y=200,width=450,height=50)
                
                dev_lb1=Label(f_lb1,text="E-mail: ssrha007@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=550,y=250,width=450,height=50)
                
                
                
if __name__ == "__main__":
        root=Tk()
        obj=Help(root)
        root.mainloop()