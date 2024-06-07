from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter.messagebox
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")
        
        # This part is image labels setting start 
        # first image  
        img=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\Stanford.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)
        
        # Second image  
        img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)
        
        # thrid image  
        img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\u.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1000,y=0,width=500,height=130)
        # bg image  
        img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        # set image as lable
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title section
        title_lb1 = Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=55)
        
        # time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lb1,font=('times new roman',14,'bold'),background='white',foreground='navyblue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        # Student Button  
        img4=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        # set image as lable
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=120,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="navyblue",fg="white")   
        b1_1.place(x=200,y=320,width=220,height=40)
    
        # Detect Face Button  
        img5=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        # set image as lable
        b1 = Button(self.root,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=250,width=220,height=220)
        
        b1_1 = Button(self.root,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="navyblue",fg="white")   
        b1_1.place(x=500,y=450,width=220,height=40)
    
        # Attendance Button  
        img6=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\report.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        # set image as lable
        b1 = Button(self.root,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=250,width=220,height=220)
        
        b1_1 = Button(self.root,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="navyblue",fg="white")   
        b1_1.place(x=800,y=450,width=220,height=40)
    
        # Help Button  
        img7=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        # set image as lable
        b1 = Button(self.root,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=250,width=220,height=220)
        
        b1_1 = Button(self.root,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="navyblue",fg="white")   
        b1_1.place(x=1100,y=450,width=220,height=40)
        
        # Train Button  
        img8=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        # set image as lable
        b1 = Button(self.root,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=510,width=220,height=220)
        
        b1_1 = Button(self.root,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="navyblue",fg="white")   
        b1_1.place(x=200,y=710,width=220,height=40)
    
        # Photo Face Button  
        img9=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        # set image as lable
        b1 = Button(self.root,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=510,width=220,height=220)
        
        b1_1 = Button(self.root,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="navyblue",fg="white")   
        b1_1.place(x=500,y=710,width=220,height=40)
    
        # Developer Button  
        img10=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        # set image as lable
        b1 = Button(self.root,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=510,width=220,height=220)
        
        b1_1 = Button(self.root,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="navyblue",fg="white")   
        b1_1.place(x=800,y=710,width=220,height=40)
    
        # Exit Button  
        img11=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        # set image as lable
        b1 = Button(self.root,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=510,width=220,height=220)
        
        b1_1 = Button(self.root,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="navyblue",fg="white")   
        b1_1.place(x=1100,y=710,width=220,height=40)
        
        # ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return  
    
        # function declaration
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)   
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 
          
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 
          
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)   
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)   
    
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()