from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognizer import FaceRecognizer
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"college_images\Stanford.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
    
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((550,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        img2=Image.open(r"college_images\u.jpg")
        img2=img2.resize((550,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        #student button
        img4=Image.open(r"college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        #Detect face button
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognizer)
        b2.place(x=500,y=100,width=220,height=220)
        b2_2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recognizer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=500,y=300,width=220,height=40)
        #Attendace face button
        img6=Image.open(r"college_images\report.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_details)
        b3.place(x=800,y=100,width=220,height=220)
        b3_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=800,y=300,width=220,height=40)
        #help desk button
        img7=Image.open(r"college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_page)
        b4.place(x=1100,y=100,width=220,height=220)
        b4_4=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_page,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1100,y=300,width=220,height=40)
        #Train face button
        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)
        b5_5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=200,y=580,width=220,height=40)
        #Photos face button
        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b6=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b6.place(x=500,y=380,width=220,height=220)
        b6_6=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=500,y=580,width=220,height=40)
        #Developer button
        img10=Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.dev_page)
        b7.place(x=800,y=380,width=220,height=220)
        b7_7=Button(bg_img,text="Developer",cursor="hand2",command=self.dev_page,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=800,y=580,width=220,height=40)
        #exit button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=380,width=220,height=220)
        b8_8=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=1100,y=580,width=220,height=40)
    def open_img(self):
        os.startfile("data")
    def iExit(self):
        self.xit=messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.xit>0:
            self.root.destroy()

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_recognizer(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognizer(self.new_window)
    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    def dev_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
