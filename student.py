from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 # pip install opencv-python
import pkg_resources
from numpy import roll


class Student:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1366x768+0+0")
                self.root.title("Face_Recogonition_System")
                self.s_wind = Toplevel()
                
                #-----------Variables-------------------
                self.var_dep=StringVar()
                self.var_course=StringVar()
                self.var_year=StringVar()
                self.var_semester=StringVar()
                self.var_std_id=StringVar()
                self.var_std_name=StringVar()
                self.var_div=StringVar()
                self.var_roll=StringVar()
                self.var_gender=StringVar()
                self.var_dob=StringVar()
                self.var_email=StringVar()
                self.var_mob=StringVar()
                self.var_address=StringVar()
                self.var_teacher=StringVar()
                self.var_class=StringVar()
                self.var_radio=StringVar()
                
                
        
        
                # first image  
                img=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\smart-attendance.jpg")
                img=img.resize((500,130),Image.Resampling.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)
                # set image as lable
                f_lb1 = Label(self.root,image=self.photoimg)
                f_lb1.place(x=0,y=0,width=500,height=130)
        
                # Second image  
                img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\iStock-182059956_18390_t12.jpg")
                img1=img1.resize((500,130),Image.Resampling.LANCZOS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                # set image as lable
                f_lb1 = Label(self.root,image=self.photoimg1)
                f_lb1.place(x=500,y=0,width=500,height=130)
        
                # thrid image  
                img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\imgref3_orig.jpg")
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
                title_lb1 = Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
                title_lb1.place(x=0,y=0,width=1530,height=45)
                
                # Creating Frame 
                main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
                main_frame.place(x=20,y=50,width=1480,height=600)

                # Left Label Frame 
                left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
                left_frame.place(x=20,y=10,width=690,height=590)
                
                img_left=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\AdobeStock_303989091.jpeg")
                img_left=img_left.resize((500,130),Image.Resampling.LANCZOS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)
                # set image as lable
                f_lb1 = Label(left_frame,image=self.photoimg_left)
                f_lb1.place(x=10,y=0,width=670,height=110)
                
                # Current Course 
                current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="navyblue")
                current_course_frame.place(x=10,y=135,width=635,height=150)

                #label Department
                dep_label=Label(current_course_frame,text="Department",font=("verdana",12,"bold"),bg="white",fg="navyblue")
                dep_label.grid(row=0,column=0,padx=5,pady=15)

                #combo box 
                dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"),state="readonly")
                dep_combo["values"]=("Select Department","CSE","EE","EC","AIML","IT","civil","Mechanical","Chemical","Biotech","Agriculture","Architecture","Fashion Designing","Pharmacy","Hotel Management")
                dep_combo.current(0)
                dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)
                
                # -----------------------------------------------------

                #label Course
                cou_label=Label(current_course_frame,text="Course",font=("verdana",12,"bold"),bg="white",fg="navyblue")
                cou_label.grid(row=0,column=2,padx=5,pady=15)

                #combo box 
                cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("verdana",12,"bold"),state="readonly")
                cou_combo["values"]=("Select Course","B.tech","M.tech","BBA","BCA","Bsc","Msc","MBA","Bcom","Mcom","BA","MA","BFA","MFA","BHM","MHM","BTTM","MTTM","BMS","MMS","BBA","MBA")
                cou_combo.current(0)
                cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)

                #-------------------------------------------------------------

                #label Year
                year_label=Label(current_course_frame,text="Session",font=("verdana",12,"bold"),bg="white",fg="navyblue")
                year_label.grid(row=1,column=0,padx=5,sticky=W)

                #combo box 
                year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
                year_combo["values"]=("Select Year","2018-22","2019-23","2020-24","2021-25","2022-26","2023-27","2024-28","2025-29","2026-30")
                year_combo.current(0)
                year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

                #-----------------------------------------------------------------
                
                #label Semester 
                year_label=Label(current_course_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="navyblue")
                year_label.grid(row=1,column=2,padx=5,sticky=W)

                #combo box 
                year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("verdana",12,"bold"),state="readonly")
                year_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
                year_combo.current(0)
                year_combo.grid(row=1,column=3,padx=5,pady=15,sticky=W)

                #Class Student Information
                class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",12,"bold"),fg="navyblue")
                class_Student_frame.place(x=10,y=290,width=635,height=230)

                #Student id
                studentId_label = Label(class_Student_frame,text="Std-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

                studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
                studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

                #Student name
                student_name_label = Label(class_Student_frame,text="Student Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

                student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
                student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

                #Class Didvision
                student_div_label = Label(class_Student_frame,text="Class Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

                div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=13,font=("verdana",12,"bold"),state="readonly")
                div_combo["values"]=("Morning","Evening")
                div_combo.current(0)
                div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

                #Roll No
                student_roll_label = Label(class_Student_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

                student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
                student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

                #Gender
                student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

                #combo box 
                gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
                gender_combo["values"]=("Male","Female","Others")
                gender_combo.current(0)
                gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

                #Date of Birth
                student_dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

                student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
                student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

                #Email
                student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

                student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
                student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

                #Phone Number
                student_mob_label = Label(class_Student_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

                student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
                student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

                #Address
                student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

                student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
                student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)


                #Teacher Name
                student_tutor_label = Label(class_Student_frame,text="Teacher Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                student_tutor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

                student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("verdana",12,"bold"))
                student_tutor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

                #Radio Buttons
                self.var_radio1=StringVar()
                radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
                radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

                radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
                radiobtn1.grid(row=5,column=1,padx=5,pady=5,sticky=W)

                #Button Frame
                btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
                btn_frame.place(x=10,y=525,width=635,height=60)

                #save button
                save_btn=Button(btn_frame,text="Save",command=self.add_data,width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
                save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

                #update button
                update_btn=Button(btn_frame,text="Update",command=self.update_data,width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
                update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

                #delete button
                del_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
                del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

                #reset button
                reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
                reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

                #take photo button
                take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
                take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

                #update photo button
                update_photo_btn=Button(btn_frame,text="Update Pic",command=self.update_data,width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
                update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)


                
                # Right Label Frame 
                right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
                right_frame.place(x=740,y=10,width=690,height=477)
                
                img_right=Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognition\college_images\AdobeStock_303989091.jpeg")
                img_right=img_right.resize((690,130),Image.Resampling.LANCZOS)
                self.photoimg_right=ImageTk.PhotoImage(img_right)
                # set image as lable
                f_lb1 = Label(right_frame,image=self.photoimg_right)
                f_lb1.place(x=5,y=0,width=690,height=130)
                
                        #Searching System in Right Label Frame 
                search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
                search_frame.place(x=10,y=135,width=670,height=80)

                #Phone Number
                search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
                search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
                self.var_searchTX=StringVar()
                #combo box 
                search_combo=ttk.Combobox(search_frame,width=12,font=("verdana",12,"bold"),state="readonly")
                search_combo["values"]=("Select","Roll-No")
                search_combo.current(0)
                search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

                self.var_search=StringVar()
                search_entry = ttk.Entry(search_frame,width=12,font=("verdana",12,"bold"))
                search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

                search_btn=Button(search_frame,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
                search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

                showAll_btn=Button(search_frame,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
                showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

                # -----------------------------Table Frame-------------------------------------------------
                #Table Frame 
                #Searching System in Right Label Frame 
                table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
                table_frame.place(x=10,y=220,width=670,height=220)

                #scroll bar 
                scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
                
                        #create table 
                self.student_table = ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","ID","Name","Div","Roll-No","Gender","DOB","Email","Mob-No","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)
                
                
                self.student_table.heading("ID",text="Student_id")
                self.student_table.heading("Name",text="Name")
                self.student_table.heading("Dep",text="Department")
                self.student_table.heading("Course",text="Course")
                self.student_table.heading("Year",text="Year")
                self.student_table.heading("Sem",text="Semester")
                self.student_table.heading("Div",text="Division")
                self.student_table.heading("Gender",text="Gender")
                self.student_table.heading("DOB",text="DOB")
                self.student_table.heading("Mob-No",text="Mob_No")
                self.student_table.heading("Address",text="Address")
                self.student_table.heading("Roll-No",text="Roll_No")
                self.student_table.heading("Email",text="Email")
                self.student_table.heading("Teacher",text="Teacher")
                self.student_table.heading("Photo",text="PhotoSample")
                self.student_table["show"]="headings"
                
                # Set Width of Colums 
                self.student_table.column("ID",width=100)
                self.student_table.column("Name",width=100)
                self.student_table.column("Dep",width=100)
                self.student_table.column("Course",width=100)
                self.student_table.column("Year",width=100)
                self.student_table.column("Sem",width=100)
                self.student_table.column("Div",width=100)
                self.student_table.column("Gender",width=100)
                self.student_table.column("DOB",width=100)
                self.student_table.column("Mob-No",width=100)
                self.student_table.column("Address",width=100)
                self.student_table.column("Roll-No",width=100) 
                self.student_table.column("Email",width=100)
                self.student_table.column("Teacher",width=100)
                self.student_table.column("Photo",width=100)

                self.student_table.pack(fill=BOTH,expand=1)
                self.student_table.bind("<ButtonRelease>",self.get_cursor)      
                self.fetch_data()
                
        
        # ==================Function Decleration==============================
        def add_data(self):
                if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
                        messagebox.showerror("Error","All Fields are required",parent=self.root)        
                else:
                        
                        try:
                                conn = mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                mycursor = conn.cursor()
                                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_id.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_mob.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get()
                                ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","Student details has been added successfully.",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
                                
                                
        # ===========================Fetch data form database to table ================================

        def fetch_data(self):
                conn = mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                data=my_cursor.fetchall()

                if len(data)!= 0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("",END,values=i)
                        conn.commit()
                conn.close()
        
        
#================================get cursor function=======================

        def get_cursor(self,event=""):
                cursor_focus = self.student_table.focus()
                content = self.student_table.item(cursor_focus)
                data = content["values"]

                self.var_email.set(data[0]),
                self.var_dep.set(data[1]),
                self.var_std_id.set(data[2]),
                self.var_std_name.set(data[3]),
                self.var_course.set(data[4]),
                self.var_year.set(data[5]),
                self.var_semester.set(data[6]),
                self.var_div.set(data[7]),
                self.var_gender.set(data[8]),
                self.var_dob.set(data[9]),
                self.var_mob.set(data[10]),
                self.var_address.set(data[11]),
                self.var_roll.set(data[12]),
                self.var_teacher.set(data[13]),
                self.var_radio1.set(data[14])
        
        
# ========================================Update Function==========================
        def update_data(self):
                if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
                        messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
                else:
                        try:
                                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                                if Update > 0:
                                        conn = mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                        mycursor = conn.cursor()
                                        mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                                        self.var_std_name.get(),
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_div.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_mob.get(),
                                        self.var_address.get(),
                                        self.var_roll.get(),
                                        self.var_email.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()   
                                        ))
                                else:
                                        if not Update:
                                                return
                                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                                
#==============================Delete Function=========================================
        def delete_data(self):
                if self.var_std_id.get()=="":
                        messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
                else:
                        try:
                                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                                if delete>0:
                                        conn = mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                        mycursor = conn.cursor() 
                                        sql="delete from student where Student_ID=%s"
                                        val=(self.var_std_id.get(),)
                                        mycursor.execute(sql,val)
                                else:
                                        if not delete:
                                                return

                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    
                        # Reset Function 
        def reset_data(self):
                self.var_std_id.set(""),
                self.var_std_name.set(""),
                self.var_dep.set("Select Department"),
                self.var_course.set("Select Course"),
                self.var_year.set("Select Year"),
                self.var_semester.set("Select Semester"),
                self.var_div.set("Select Division"),
                self.var_gender.set("Gender"),
                self.var_dob.set(""),
                self.var_mob.set(""),
                self.var_address.set(""),
                self.var_roll.set(""),
                self.var_email.set(""),
                self.var_teacher.set(""),
                self.var_radio1.set("")
                
                
                
# ===========================Search Data===================
        def search_data(self):
                if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
                        messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
                else:
                        try:
                                conn = mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                my_cursor = conn.cursor()
                                sql = "SELECT Student_ID,Name,Department,Course,Year,Semester,Division,Gender,DOB,Mobile_No,Address,Roll_No,Email,Teacher_Name,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                                my_cursor.execute(sql)
                                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                                rows=my_cursor.fetchall()        
                                if len(rows)!=0:
                                        self.student_table.delete(*self.student_table.get_children())
                                        for i in rows:
                                                self.student_table.insert("",END,values=i)
                                        if rows==None:
                                                messagebox.showerror("Error","Data Not Found",parent=self.root)
                                                conn.commit()
                                        conn.close()
                        except Exception as es:
                                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

# ==================================Generate Data set take image=========================
        def generate_dataset(self):
                if self.var_dep.get()=="select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
                        messagebox.showerror("Error","All fields are required",parent=self.s_wind)
                else:
                        try:
                                conn = mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognition")
                                my_cursor=conn.cursor()
                                my_cursor.execute("select * from student")
                                myresult=my_cursor.fetchall()
                                id=0
                                # sroll=self.var_roll.get()
                                # sname=self.var_std_name.get()
                                for x in myresult:
                                        id+=1
                                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,class=%s,roll_no=%s,Gender=%s,Dob=%s,email=%s,phone=%s,address=%s,Teacher=%s,photoSample=%s where Student_Id=%s",(
                                        
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_name.get(),
                                        self.var_class.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_mob.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio.get(),
                                        self.var_std_id.get()==id+1
                                        ))
                                
                                conn.commit()
                                self.fetch_data()
                                self.reset_data()
                                conn.close()
                                
                                

                # messagebox.showinfo(sroll,parent=s_wind)

                #========== Load data on frontal face from opencv
                
                
                                face_classifier=cv2.CascadeClassifier('cv2',"haarcascade_frontalface_default.xml")
                                
                                def face_cropped(img):
                                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                                        #scalling factor =1.3
                                        #Minimum Neighbor =5
                                        for(x,y,w,h)in faces:
                                                face_cropped=img[y:y+h,x:x+w]
                                                return face_cropped
                                        cap=cv2.VideoCapture(0)
                                        img_id=0
                                        
                        
                                
                
                                        while True:
                                                ret,my_frame=cap.read()
                                                
                                                if face_cropped(my_frame) is not None:
                                                        img_id+=1
                                                        face=cv2.resize(face_cropped(my_frame),(500,500))
                                                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                                        cv2.imwrite(file_name_path)
                                                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,255,29),2)
                                                        cv2.imshow("Croped Face",face)
                                                        
                                        

                                                        if cv2.waitKey(1)==13 or int(img_id)==100:
                                                                break
                                                        
                                                        
                                                        cap.release()
                                                        cv2.destroyAllWindows()
                                                        
                                                        messagebox.showinfo("Info","DataSet Completed!")
                                                        
                        except Exception as es:
                                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                                
                        

if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()