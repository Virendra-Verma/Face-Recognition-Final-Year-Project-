from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 # pip install opencv-python
import os
import numpy as np # pip install numpy


class Face_Recognition:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1366x768+0+0")
                self.root.title("Face_Recogonition_System")
                
                #title section
                title_lb1 = Label(self.root,text="Face Recogonition",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
                title_lb1.place(x=0,y=0,width=1530,height=45)
                
                img_top=Image.open(r"college_images\face_detector1.jpg")
                img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)
                # set image as lable
                f_lb1 = Label(self.root,image=self.photoimg_top,cursor="hand2")
                f_lb1.place(x=0,y=55,width=650,height=750)
                
                img_bottom=Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
                img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
                self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
                # set image as lable
                f_lb1 = Label(self.root,image=self.photoimg_bottom,cursor="hand2")
                f_lb1.place(x=650,y=55,width=950,height=750)
                
                b1 = Button(f_lb1,text="Face Recognition", command=self.face_recog, cursor="hand2",bg="blue",fg="white",font=("times new roman",20,"bold"))
                b1.place(x=359,y=650,width=250,height=40)
                
                # =====attendance section=====
        def mark_attendance(self,i,n,d,r):
                with open("Attendance.csv","r+",newline="\n") as file:
                        myDataList = file.readlines()
                        nameList = []
                        for line in myDataList:
                                entry = line.split((","))
                                nameList.append(entry[0])
                        if ((i not in nameList) and (n not in nameList) and (d not in nameList) and (r not in nameList)):
                                now = datetime.now()
                                d1 = now.strftime("%d/%m/%Y")
                                dtString = now.strftime("%H:%M:%S")
                                file.writelines(f"\n{i},{n},{r},{d1},{dtString},Present")

                                
                
                # ========Face Recognition Details=======
        def face_recog(self):
                print("Attendance Taken Successfully")
                def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                        gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
                        coords = []
                        for (x,y,w,h) in features:
                                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                                conf_level = int(100*(1-predict/300))
                                                
                                conn = mysql.connector.connect(host="localhost",user="root",password="123456",database="face_recognition")
                                my_cursor = conn.cursor()
                                                
                                my_cursor.execute("select Name  from student where Student_id="+str(id))
                                n = my_cursor.fetchone()
                                n = "+".join(str(n))
                                                
                                my_cursor.execute("select Roll_No from student where Student_id="+str(id))
                                r = my_cursor.fetchone()
                                r = "+".join(str(r))
                                                
                                my_cursor.execute("select Dep from student where Student_id="+str(id))
                                d = my_cursor.fetchone()
                                d = "+".join(str(d))
                                                
                                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                                i = my_cursor.fetchone()
                                i = "+".join(str(i))
                                                
                                if conf_level>77:
                                        cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                                        cv2.putText(img,f"Roll_No:{r}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                                        self.mark_attendance(i,n,d,r)
                                else:
                                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                                coords = [x,y,w,h]
                        return coords
                                        
                def recognize(img,clf,faceCascade):
                        coords = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                        return img
                                        
                faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                clf = cv2.face.LBPHFaceRecognizer_create()
                clf.read("classifier.xml")
                                
                video_cap=cv2.VideoCapture(0)
                while True:
                        ret,img = video_cap.read()
                        img = recognize(img,clf,faceCascade)
                        cv2.imshow("Welcome to Face Recognition",img)
                        if cv2.waitKey(1)==13:
                                break
                video_cap.release()
                cv2.destroyAllWindows()
                        
                
if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition(root)
        root.mainloop()