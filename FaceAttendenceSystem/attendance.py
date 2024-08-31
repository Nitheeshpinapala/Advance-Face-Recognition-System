from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.id=StringVar()
        self.roll=StringVar()
        self.name=StringVar()
        self.dep=StringVar()
        self.time=StringVar()
        self.date=StringVar()
        self.attstatus=StringVar()
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        img1=Image.open(r"college_images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)
        img_left=Image.open(r"college_images\face-recognition.png")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        left_inside_frame=Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=0,y=135,width=725,height=360)
        attendanceid_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        attendanceid_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.id,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        dept_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        dept_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.dep,font=("times new roman",12,"bold"))
        dept_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        Time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        Time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.time,font=("times new roman",12,"bold"))
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        attendancestatus_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendancestatus_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        self.att_combo=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),textvariable=self.attstatus,width=18,state="read only")
        self.att_combo["values"]=("Status","Present","Absent")
        self.att_combo.current(0)
        self.att_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)
        import_btn=Button(btn_frame,text="Import csv",command=self.importcsv,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        import_btn.grid(row=0,column=0)
        export_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        export_btn.grid(row=0,column=1)
        update_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        update_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        reset_btn.grid(row=0,column=3)


        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=5,width=715,height=480)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.Attendance_report_table=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.Attendance_report_table.xview)
        scroll_y.config(command=self.Attendance_report_table.yview)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.Attendance_report_table.heading("id",text="ID")
        self.Attendance_report_table.heading("roll",text="Roll No")
        self.Attendance_report_table.heading("name",text="Name")
        self.Attendance_report_table.heading("department",text="Department")
        self.Attendance_report_table.heading("time",text="Time")
        self.Attendance_report_table.heading("date",text="Date")
        self.Attendance_report_table.heading("attendance",text="Attendance Status")
        self.Attendance_report_table["show"]="headings"
        self.Attendance_report_table.column("id",width=100)
        self.Attendance_report_table.column("roll",width=100)
        self.Attendance_report_table.column("name",width=100)
        self.Attendance_report_table.column("department",width=100)
        self.Attendance_report_table.column("time",width=100)
        self.Attendance_report_table.column("date",width=100)
        self.Attendance_report_table.column("attendance",width=100)
        self.Attendance_report_table.pack(fill=BOTH,expand=1)
        self.Attendance_report_table.bind("<ButtonRelease>",self.get_cursor)
    def fetchdata(self,rows):
        self.Attendance_report_table.delete(*self.Attendance_report_table.get_children())
        for i in rows:
            self.Attendance_report_table.insert("",END,values=i)
    def importcsv(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fin)+"successfully")
        except Exception as e:
            messagebox.showerror("Error",f"due to:{str(e)}",parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.Attendance_report_table.focus()
        content=self.Attendance_report_table.item(cursor_row)
        rows=content['values']
        self.id.set(rows[0])
        self.roll.set(rows[1])
        self.name.set(rows[2])
        self.dep.set(rows[3])
        self.time.set(rows[4])
        self.date.set(rows[5])
        self.attstatus.set(rows[6])
    def reset_data(self):
        self.id.set("")
        self.roll.set("")
        self.name.set("")
        self.dep.set("")
        self.time.set("")
        self.date.set("")
        self.attstatus.set("")





if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()