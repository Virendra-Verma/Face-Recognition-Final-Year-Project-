# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector as sq
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
from datetime import date
from datetime import datetime
import pandas as pd

#Global variable for importCsv Function 
mydata=[]

class Attendance:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1566x768+0+0")
                self.root.title("Attendance Pannel")

                #-----------Variables-------------------
                self.var_roll=StringVar()
                self.var_name=StringVar()
                self.var_status=StringVar()
                self.var_date=StringVar()
                self.var_subject=StringVar()


                # This part is image labels setting start 
                # first header image  
                img=Image.open(r"college_images\unnamed.jpg")
                img=img.resize((1566,130),Image.Resampling.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                # set image as lable
                f_lb1 = Label(self.root,image=self.photoimg)
                f_lb1.place(x=0,y=0,width=1566,height=130)

                # backgorund image 
                bg1=Image.open(r"college_images\employee_img2.jpg")
                bg1=bg1.resize((1566,768),Image.Resampling.LANCZOS)
                self.photobg1=ImageTk.PhotoImage(bg1)

                # set image as lable
                bg_img = Label(self.root,image=self.photobg1)
                bg_img.place(x=0,y=130,width=1566,height=768)


                #title section
                title_lb1 = Label(bg_img,text="Welcome to Attendance Management Panel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
                title_lb1.place(x=0,y=0,width=1566,height=45)

                #========================Section Creating==================================

                # Creating Frame 
                main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
                main_frame.place(x=20,y=60,width=1480,height=600)

                # Left Label Frame 
                left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
                left_frame.place(x=10,y=10,width=730,height=480)
                
                img_left=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\face-recognition.png")
                img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)
                f_lb1 = Label(left_frame,image=self.photoimg_left)
                f_lb1.place(x=10,y=0,width=705,height=130)
                
                left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white") #bd mean border 
                left_inside_frame.place(x=10,y=135,width=710,height=300)
                
                #  Lebeland Entry
                #Student id
                attendanceId_label = Label(left_inside_frame,text="AttendanceId:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

                attendanceID_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",12,"bold"))
                attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
                
                # roll
                rollLabel = Label(left_inside_frame,text="Roll_No",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                rollLabel.grid(row=0,column=2)

                atten_roll = ttk.Entry(left_inside_frame,width=15,font=("verdana",12,"bold"))
                atten_roll.grid(row=0,column=3,padx=8)
                
                # name
                nameLabel = Label(left_inside_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                nameLabel.grid(row=1,column=0)

                atten_name = ttk.Entry(left_inside_frame,width=15,font=("verdana",12,"bold"))
                atten_name.grid(row=1,column=1,pady=8)
                
                # Department
                depLabel = Label(left_inside_frame,text="Department",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                depLabel.grid(row=1,column=2)

                atten_dep = ttk.Entry(left_inside_frame,width=15,font=("verdana",12,"bold"))
                atten_dep.grid(row=1,column=3,pady=8)
                
                #time
                timeLabel = Label(left_inside_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                timeLabel.grid(row=2,column=0)
                
                atten_time = ttk.Entry(left_inside_frame,width=15,font=("verdana",12,"bold"))
                atten_time.grid(row=2,column=1,pady=8)
                
                # Date 
                dateLabel = Label(left_inside_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                dateLabel.grid(row=2,column=2)
                
                atten_date = ttk.Entry(left_inside_frame,width=15,font=("verdana",12,"bold"))
                atten_date.grid(row=2,column=3,pady=8)
                
                #  Attendance 
                attendanceLabel = Label(left_inside_frame,text="Attendance Status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                attendanceLabel.grid(row=3,column=0)
                
                self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_status,width=15,font=("verdana",12,"bold"),state="readonly")
                self.atten_status["values"]=("Status","Present","Absent")
                self.atten_status.current(0)
                self.atten_status.grid(row=3,column=1,pady=8)
                
                # button frame
                btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=200,width=700,height=40)
                
                # Save Button
                save_btn = Button(btn_frame,text="Import csv",command=self.save_data,font=("verdana",12,"bold"),bg="navyblue",fg="white",width=15)
                save_btn.grid(row=0,column=0)
                
                # Update Button
                update_btn = Button(btn_frame,text="Export csv",font=("verdana",12,"bold"),bg="navyblue",fg="white",width=15)
                update_btn.grid(row=0,column=1)
                
                # Delete Button
                delete_btn = Button(btn_frame,text="Update",font=("verdana",12,"bold"),bg="navyblue",fg="white",width=15)
                delete_btn.grid(row=0,column=2)
                
                # Reset Button
                reset_btn = Button(btn_frame,text="Reset",font=("verdana",12,"bold"),bg="navyblue",fg="white",width=15)
                reset_btn.grid(row=0,column=3)
                

                # right frame
                Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
                Right_frame.place(x=750,y=10,width=720,height=480)
                
                # Right label frame
                Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
                Right_frame.place(x=750,y=10,width=720,height=480)
                
                table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
                table_frame.place(x=10,y=10,width=695,height=410)
                
                
                # scroll bar
                scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
                
                self.attendanceReport = ttk.Treeview(table_frame,column=("AttendanceId","Roll_No","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.attendanceReport.xview)
                scroll_y.config(command=self.attendanceReport.yview)
                
                self.attendanceReport.heading("AttendanceId",text="AttendanceId")
                self.attendanceReport.heading("Roll_No",text="Roll_No")
                self.attendanceReport.heading("Name",text="Name")
                self.attendanceReport.heading("Department",text="Department")
                self.attendanceReport.heading("Time",text="Time")
                self.attendanceReport.heading("Date",text="Date")
                self.attendanceReport.heading("Attendance",text="Attendance")
                
                self.attendanceReport["show"]="headings"
                
                self.attendanceReport.column("AttendanceId",width=100)
                self.attendanceReport.column("Roll_No",width=100)
                self.attendanceReport.column("Name",width=100)
                self.attendanceReport.column("Department",width=100)
                self.attendanceReport.column("Time",width=100)
                self.attendanceReport.column("Date",width=100)
                self.attendanceReport.column("Attendance",width=100)
                
                
                
                self.attendanceReport.pack(fill=BOTH,expand=1)
                
                
                
                

                # ==================================Text boxes and Combo Boxes====================

                #Student Roll

                #Studnet Name

                # sub_combo=ttk.Combobox(left_frame,textvariable=self.var_subject,width=15,font=("verdana",12,"bold"),state="readonly")
                # sub_combo["values"]=("Select Subject","SE Economics","Arabic","NLP","Topics in SE")
                # sub_combo.current(0)
                # sub_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

                #Department
                # dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                # dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

                # dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
                # dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

                #Date 
                # ===============================Table Sql Data View==========================
                # table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
                # table_frame.place(x=10,y=100,width=780,height=310)
                # #scroll bar 
                # scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                # scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
                # #create table 
                # self.attendanceReport_left = ttk.Treeview(table_frame,column=("Name","Status","Date","Subject"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                # scroll_x.pack(side=BOTTOM,fill=X)
                # scroll_y.pack(side=RIGHT,fill=Y)
                # scroll_x.config(command=self.attendanceReport_left.xview)
                # scroll_y.config(command=self.attendanceReport_left.yview)
                # #self.attendanceReport_left.heading("Roll_No",text="Roll.No")
                # self.attendanceReport_left.heading("Name",text="Std-Name")
                # self.attendanceReport_left.heading("Status",text="status")
                # self.attendanceReport_left.heading("Date",text="date")
                # self.attendanceReport_left.heading("Subject",text="subject")

                # self.attendanceReport_left["show"]="headings"


                # Set Width of Colums 
                
                #self.attendanceReport_left.column("Roll_No",width=100)
                # self.attendanceReport_left.column("Name",width=100)
                # self.attendanceReport_left.column("Status",width=100)
                # self.attendanceReport_left.column("Date",width=100)
                # self.attendanceReport_left.column("Subject",width=100)
                # self.attendanceReport_left.pack(fill=BOTH,expand=1)
                # self.attendanceReport_left.bind("<ButtonRelease>")
        

                # =========================button section========================

   




        # Right section=======================================================

        # Right Label Frame 
        # right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        # right_frame.place(x=680,y=10,width=660,height=480)

        def get_cursor_left(self,event=""):
                cursor_focus = self.attendanceReport_left.focus()
                content = self.attendanceReport_left.item(cursor_focus)
                data = content["values"]

                self.var_roll.set(data[0]),
                self.var_name.set(data[1]),
                self.var_status.set(data[2]),
                self.var_date.set(data[3]),
                self.var_subject.set(data[4]),


        #----------------------------Fetch Data from Database----------------------
        def fetch_Data(self):
                conn = sq.connect(host="localhost",username="root",password="123456",database="face_recognition")
                mycursor = conn.cursor()
                if self.var_subject.get()=="Arabic":
                        mycursor = conn.cursor()

                        mycursor.execute("select * from arabic")
                        data=mycursor.fetchall()

                        if len(data)!= 0:
                                
                                self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
                        for i in data:
                                self.attendanceReport_left.insert("",END,values=i)
                        conn.commit()
                        conn.close()
                elif self.var_subject.get()=="NLP":

                        mycursor = conn.cursor()

                        mycursor.execute("select * from nlp")
                        data=mycursor.fetchall()

                        if len(data)!= 0:
                                self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
                        for i in data:
                                self.attendanceReport_left.insert("",END,values=i)
                        conn.commit()
                        conn.close()

                elif self.var_subject.get()=="SE Economics":

                        mycursor = conn.cursor()

                        mycursor.execute("select * from se_economics")
                        data=mycursor.fetchall()

                        if len(data)!= 0:
                                self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
                        for i in data:
                                self.attendanceReport_left.insert("",END,values=i)
                        conn.commit()
                        conn.close()

                elif self.var_subject.get()=="Topics in SE":
                        mycursor = conn.cursor()

                        mycursor.execute("select * from topics_in_se")
                        data=mycursor.fetchall()

                        if len(data)!= 0:
                                self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
                        for i in data:
                                self.attendanceReport_left.insert("",END,values=i)
                        conn.commit()
                        conn.close()
                else:
                        messagebox.showerror("error","Error")

        def save_data(self):
                aniData=pd.read_csv("text.txt",sep=' ',index_col=False,delimiter=',')
                aniData.head()
                today = str(date.today())
                aniData=pd.read_csv("text.txt",index_col=False,delimiter=',')
                aniData["Date"] = today
                aniData["Status"]="p"
                aniData["Subject"]=self.var_subject.get()
                finalFile="text.csv"
                aniData.to_csv(finalFile, index=False)
                        # finalFile="live.csv"
                if self.var_subject.get()=="Arabic":
                        try:
                                conn=sq.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                cursor=conn.cursor()
                                for i,row in aniData.iterrows():
                                        sql="Insert into arabic VALUES(%s,%s,%s,%s)"
                                        cursor.execute(sql,tuple(row))
                                        print("Saved")
                                        
                                        conn.commit()
                                messagebox.showinfo("Saved","Inserted successfully")
                        except Exception as ex:
                                print("Error while connecting to MYSQL",ex)
                elif self.var_subject.get()=="SE Economics":
                        try:
                                conn=sq.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                cursor=conn.cursor()
                                for i,row in aniData.iterrows():
                                        sql="Insert into se_economics VALUES(%s,%s,%s,%s)"
                                        cursor.execute(sql,tuple(row))
                                        print("Saved")
                                        
                                        conn.commit()
                                messagebox.showinfo("Saved","Inserted successfully")
                        except Exception as ex:
                                print("Error while connecting to MYSQL",ex)

                elif self.var_subject.get()=="NLP":
                        try:
                                conn=sq.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                cursor=conn.cursor()
                                for i,row in aniData.iterrows():
                                        sql="Insert into nlp VALUES(%s,%s,%s,%s)"
                                        cursor.execute(sql,tuple(row))
                                        print("Saved")
                                        
                                        conn.commit()
                                messagebox.showinfo("Saved","Inserted successfully")
                        except Exception as ex:
                                        print("Error while connecting to MYSQL",ex)
                elif self.var_subject.get()=="Topics in SE":
                        try:
                                conn=sq.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                cursor=conn.cursor()
                                for i,row in aniData.iterrows():
                                        sql="Insert into topics_in_se VALUES(%s,%s,%s,%s)"
                                        cursor.execute(sql,tuple(row))
                                        print("Saved")
                                
                                        conn.commit()
                                messagebox.showinfo("Saved","Inserted successfully")
                        except Exception as ex:
                                print("Error while connecting to MYSQL",ex)
                else:
                        messagebox.showinfo("Not saved","Something wrong")












if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()