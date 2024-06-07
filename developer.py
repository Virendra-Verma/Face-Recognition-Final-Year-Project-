from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 # pip install opencv-python


class Developer:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1366x768+0+0")
                self.root.title("Face_Recogonition_System")
                
                #title section
                title_lb1 = Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
                title_lb1.place(x=0,y=0,width=1530,height=50)
                
                img_top=Image.open(r"college_images\dev.jpg")
                img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)
                # set image as lable
                f_lb1 = Label(self.root,image=self.photoimg_top,cursor="hand2")
                f_lb1.place(x=0,y=55,width=1530,height=720)
                
                #frame
                main_frame=Frame(f_lb1,bd=2,bg="white")
                main_frame.place(x=450,y=5,width=760,height=650)
                
                img_top1=Image.open(r"college_images\clg.jpg")
                img_top1=img_top1.resize((200,200),Image.Resampling.LANCZOS)
                self.photoimg_top1=ImageTk.PhotoImage(img_top1)
                # set image as lable
                f_lb1 = Label(main_frame,image=self.photoimg_top1,cursor="hand2")
                f_lb1.place(x=550,y=0,width=200,height=200)
                
                #Developer info
                dev_lb1=Label(main_frame,text="Hello,My name is Virendra",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=0,y=0,width=550,height=50)
                
                dev_lb1=Label(main_frame,text="I am Full Stack, AI & Java Developer..",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=0,y=40,width=550,height=50)
                
                img_top2=Image.open(r"college_images\clg1.jpg")
                img_top2=img_top2.resize((200,200),Image.Resampling.LANCZOS)
                self.photoimg_top2=ImageTk.PhotoImage(img_top2)
                # set image as lable
                f_lb1 = Label(main_frame,image=self.photoimg_top2,cursor="hand2")
                f_lb1.place(x=550,y=210,width=200,height=200)
                
                #Developer info
                dev_lb1=Label(main_frame,text="Hello,My name is Priya  ",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=0,y=210,width=550,height=50)
                
                dev_lb1=Label(main_frame,text="I am Full Stack & Java Developer..",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=0,y=250,width=550,height=50)
                
                img_top3=Image.open(r"college_images\clg3.jpg")
                img_top3=img_top3.resize((200,200),Image.Resampling.LANCZOS)
                self.photoimg_top3=ImageTk.PhotoImage(img_top3)
                # set image as lable
                f_lb1 = Label(main_frame,image=self.photoimg_top3,cursor="hand2")
                f_lb1.place(x=550,y=420,width=200,height=200)
                
                #Developer info
                dev_lb1=Label(main_frame,text="Hello,My name is Abhishek  ",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=0,y=420,width=550,height=50)
                
                dev_lb1=Label(main_frame,text="I am Android App & Full Stack Developer..",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
                dev_lb1.place(x=0,y=460,width=550,height=50)
                
                
                # img_top2=Image.open(r"college_images\clg1.jpg")
                # img_top2=img_top2.resize((500,300),Image.Resampling.LANCZOS)
                # self.photoimg_top2=ImageTk.PhotoImage(img_top2)
                # # set image as lable
                # f_lb1 = Label(main_frame,image=self.photoimg_top2,cursor="hand2")
                # f_lb1.place(x=0,y=210,width=600,height=300)





if __name__ == "__main__":
        root=Tk()
        obj=Developer(root)
        root.mainloop()