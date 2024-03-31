from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import mysql.connector

root = Tk()
root.geometry("800x800+0+0")
root.title("Exam Registration System")
root.configure(background='powder blue')

F1=Frame(root,bd=20,relief=RIDGE)
F1.pack(side=TOP)

label=Label(F1,font=('arial',20,'bold'),text='EXAM   REGISTRATION   SYSTEM',bd=20,bg='powder blue',justify=CENTER,width=30, height=1)
label.grid(row=0)

F2=Frame(root,bd=15,relief=RIDGE)
F2.pack(side=TOP)

title = Label(F2, text="PERSONAL  DETAILS", font=('Calibri', 16, 'bold'),bd=20,bg='powder blue',width=35, height=1)
title.grid(row=0)

F3=Frame(root,bd=15,relief=RIDGE)
F3.pack(side=TOP)

mydb= mysql.connector.connect(host='localhost',database='test',user='root',password='tiger')
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS exam_registration_system(CANDIDATE_NAME CHAR(50),FATHER_NAME CHAR(50),MOTHER_NAME CHAR(50),AADHAR_NUMBER VARCHAR(100),NATIONALITY CHAR(20),GENDER_TYPE CHAR(20),CATEGORY_TYPE CHAR(20),EXAM_TYPE CHAR(20),CURRENT_ADDRESS VARCHAR(100),RESIDENCE_PLACE VARCHAR(100),CITY_NAME CHAR(40),DISTRICT_NAME CHAR(40),STATE_NAME CHAR(40),PIN_CODE VARCHAR(50),EMAIL_ADDRESS VARCHAR(50),PHONE_NUMBER VARCHAR(50),PASS_STATUS_10 CHAR(20),NAME_EXAM_10 CHAR(20),SCHOOL_BOARD_10 CHAR(20),PASS_YEAR_10 VARCHAR(50),PASS_STATUS_12 CHAR(20),NAME_EXAM_12 CHAR(20),SCHOOL_BOARD_12 CHAR(20),PASS_YEAR_12 VARCHAR(50));")


candidatename_var=StringVar()
fathername_var=StringVar()  
mothername_var=StringVar()
aadharnumber_var=StringVar()
nationalitytype_var=StringVar()
gendertype_var=StringVar()
categorytype_var=StringVar()
examtype_var=StringVar()
checkvar = IntVar()


candidate_name = Label(F3, text='Name of Candidate:', font=("Calibri",20))
candidate_name.grid(row=0,column=0)
candidatename = Entry(F3,textvariable = candidatename_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
candidatename.grid(row=0,column=1,padx=10,pady=(10,5))

father_name = Label(F3, text='Name of Father:', font=("Calibri", 20))
father_name.grid(row=1,column=0)
fathername = Entry(F3,textvariable = fathername_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
fathername.grid(row=1,column=1,padx=10,pady=5)

mother_name = Label(F3, text='Name of Mother:', font=("Calibri", 20))
mother_name.grid(row=2,column=0)
mothername = Entry(F3,textvariable = mothername_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
mothername.grid(row=2,column=1,padx=10,pady=5)


aadhar_number = Label(F3, text='Aadhar Card Number:', font=("Calibri", 20))
aadhar_number.grid(row=3,column=0)
aadharnumber = Entry(F3,textvariable = aadharnumber_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
aadharnumber.grid(row=3,column=1,padx=10,pady=5)


nationality_type = Label(F3, text='Nationality:', font=("Calibri", 20))
nationality_type.grid(row=4,column=0)
nationalitytype = Entry(F3,textvariable = nationalitytype_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
nationalitytype.grid(row=4,column=1,padx=10,pady=5)


gender_type = Label(F3, text='Gender:', font=("Calibri", 20))
gender_type.grid(row=5,column=0)
gendertype = ttk.Combobox(F3, width = 20, textvariable = gendertype_var, font=('calibre',15,'normal'),state="readonly",values = ['MALE','FEMALE'])
gendertype.grid(row=5,column=1,padx=10,pady=5)
gendertype.bind("<<ComboboxSelected>>",lambda e: F3.focus())

category_type = Label(F3, text='Category:', font=("Calibri", 20))
category_type.grid(row=6,column=0)
categorytype = ttk.Combobox(F3, width = 20, textvariable = categorytype_var, font=('calibre',15,'normal'),state="readonly",values = ["GENERAL","OBC","SC/ST"])
categorytype.grid(row=6,column=1,padx=10,pady=5)
categorytype.bind("<<ComboboxSelected>>",lambda e: F3.focus())

examname_type = Label(F3, text='Exam Name:', font=("Calibri", 20))
examname_type.grid(row=7,column=0)
examnametype = ttk.Combobox(F3, width = 20, textvariable = examtype_var, font=('calibre',15,'normal'),state="readonly",values = ["JEE","NEET","SAT","CET","BITSAT"])
examnametype.grid(row=7,column=1,padx=10,pady=5)
examnametype.bind("<<ComboboxSelected>>",lambda e: F3.focus())

def validation():
    a=candidatename_var.get()
    b=fathername_var.get()
    c=mothername_var.get()
    d=aadharnumber_var.get()
    e=nationalitytype_var.get()
    f=gendertype_var.get()
    g=categorytype_var.get()
    h=examtype_var.get()

    if len(a)==0:
        messagebox.showwarning("Error", "Some Entry is left unfilled")
        B1['state'] = DISABLED
        checkvar.set(0)
    elif len(b)==0:
        messagebox.showwarning("Error", "Some Entry is left unfilled")
        B1['state'] = DISABLED
        checkvar.set(0)
    elif len(c)==0:
        messagebox.showwarning("Error", "Some Entry is left unfilled")
        B1['state'] = DISABLED
        checkvar.set(0)
    elif len(d)==0:
        messagebox.showwarning("Error", "Some Entry is left unfilled")
        B1['state'] = DISABLED
        checkvar.set(0)
    elif len(e)==0:
        messagebox.showwarning("Error", "Some Entry is left unfilled")
        B1['state'] = DISABLED
        checkvar.set(0)
    elif len(f)==0:
        messagebox.showwarning("Error", "Some Entry is left unfilled")
        B1['state'] = DISABLED
        checkvar.set(0)
    elif len(g)==0:
        messagebox.showwarning("Error", "Some Entry is left unfilled")
        B1['state'] = DISABLED
        checkvar.set(0)
    elif len(h)==0:
        messagebox.showwarning("Error", "Some Entry is left unfilled")
        B1['state'] = DISABLED
        checkvar.set(0)
    elif len(d)<12 or len(d)>12:
        messagebox.showwarning("Error", "Please Enter Aadhar Number Correctly")
        B1['state'] = DISABLED
        checkvar.set(0)
    else:
        candidatename.configure(state='readonly')
        fathername.configure(state='readonly')
        mothername.configure(state='readonly')
        aadharnumber.configure(state='readonly')
        nationalitytype.configure(state='readonly')
        gendertype.configure(state='readonly')
        categorytype.configure(state='readonly')
        examnametype.configure(state='readonly')
        B1['state'] = NORMAL

def check():
    if checkvar.get()==0:
        messagebox.showwarning("Error", "PLEASE TICK THE CHECKBOX")
    else:
        filedata()
        next1()
        mysqlconnectivity()

B1=Button(root,font=('arial',16,'bold'),width=20,text='NEXT PAGE',bg='white',command=check,relief=RIDGE,bd=10,state=DISABLED)
B1.pack(side=BOTTOM, pady=30)
 
C1=Checkbutton(F3,text="By clicking this checkbox, you assure that your \n personal details given by you are totally correct.",variable=checkvar,onvalue=1,offvalue=0,height=5,width=40,command= validation)
C1.grid(row=8,column=0)  

################################################################################################

def next1():
    root1=Toplevel()
    root1.geometry("800x800+0+0")
    root1.title("Exam Registration System")
    root1.configure(background='powder blue')

    F4=Frame(root1,bd=20,relief=RIDGE)
    F4.pack(side=TOP)

    label1=Label(F4,font=('arial',20,'bold'),text='EXAM   REGISTRATION   SYSTEM',bd=20,bg='powder blue',justify=CENTER,width=30, height=1)
    label1.grid(row=0)

    F5=Frame(root1,bd=15,relief=RIDGE)
    F5.pack(side=TOP)

    title1 = Label(F5, text="CONTACT  DETAILS", font=('Calibri', 16, 'bold'),bd=20,bg='powder blue',width=35, height=1)
    title1.grid(row=0)

    F6=Frame(root1,bd=15,relief=RIDGE)
    F6.pack(side=TOP)
    
    currentaddress_var=StringVar()
    placeofresidence_var=StringVar()
    cityname_var=StringVar()
    districtname_var=StringVar()
    statename_var=StringVar()
    pincode_var=StringVar()
    emailaddress_var=StringVar()
    phonenumber_var=StringVar()
    checkvar1=IntVar()

    
    current_address = Label(F6, text='Current Address:', font=("Calibri",20))
    current_address.grid(row=0,column=0)
    currentaddress= Entry(F6,textvariable = currentaddress_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    currentaddress.grid(row=0,column=1,padx=10,pady=(10,5))

    placeof_residence = Label(F6, text='Place Of Residence:', font=("Calibri", 20))
    placeof_residence.grid(row=1,column=0)
    placeofresidence = Entry(F6,textvariable = placeofresidence_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    placeofresidence.grid(row=1,column=1,padx=10,pady=5)

    city_name = Label(F6, text='City Name:', font=("Calibri", 20))
    city_name.grid(row=2,column=0)
    cityname = Entry(F6,textvariable = cityname_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    cityname.grid(row=2,column=1,padx=10,pady=5)

    district_name = Label(F6, text='District Name:', font=("Calibri", 20))
    district_name.grid(row=3,column=0)
    districtname = Entry(F6,textvariable = districtname_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    districtname.grid(row=3,column=1,padx=10,pady=5)

    state_name = Label(F6, text='State Name:', font=("Calibri", 20))
    state_name.grid(row=4,column=0)
    statename = Entry(F6,textvariable = statename_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    statename.grid(row=4,column=1,padx=10,pady=5)

    pin_code = Label(F6, text='Pincode:', font=("Calibri", 20))
    pin_code.grid(row=5,column=0)
    pincode = Entry(F6,textvariable = pincode_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    pincode.grid(row=5,column=1,padx=10,pady=5)

    email_address = Label(F6, text='Email Address:', font=("Calibri", 20))
    email_address.grid(row=6,column=0)
    emailaddress = Entry(F6,textvariable = emailaddress_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    emailaddress.grid(row=6,column=1,padx=10,pady=5)

    phone_number = Label(F6, text='Phone Number:', font=("Calibri", 20))
    phone_number.grid(row=7,column=0)
    phonenumber = Entry(F6,textvariable = phonenumber_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    phonenumber.grid(row=7,column=1,padx=10,pady=5)

    def validation1():
        i=currentaddress_var.get()
        j=placeofresidence_var.get()
        k=cityname_var.get()
        l=districtname_var.get()
        m=statename_var.get()
        n=pincode_var.get()
        o=emailaddress_var.get()
        p=phonenumber_var.get()
        
        if len(i)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B2['state'] = DISABLED
            checkvar1.set(0)
        elif len(j)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B2['state'] = DISABLED
            checkvar1.set(0)
        elif len(k)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B2['state'] = DISABLED
            checkvar1.set(0)
        elif len(l)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B2['state'] = DISABLED
            checkvar1.set(0)
        elif len(m)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B2['state'] = DISABLED
            checkvar1.set(0)
        elif len(n)<6 or len(n)>6:
            messagebox.showwarning("Error", "Please Enter Correct Pincode Number")
            B2['state'] = DISABLED
            checkvar1.set(0)
        elif len(o)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B2['state'] = DISABLED
            checkvar1.set(0)
        elif len(p)<10 or len(p)>10:
            messagebox.showwarning("Error", "Please Enter Phone Number Correctly")
            B2['state'] = DISABLED
            checkvar1.set(0)
        else:
            currentaddress.configure(state='readonly')
            placeofresidence.configure(state='readonly')
            cityname.configure(state='readonly')
            districtname.configure(state='readonly')
            statename.configure(state='readonly')
            pincode.configure(state='readonly')
            emailaddress.configure(state='readonly')
            phonenumber.configure(state='readonly')
            B2['state'] = NORMAL

    def mysqlconnectivity1():
            mydb= mysql.connector.connect(host='localhost',database='test',user='root',password='tiger')
            cursor=mydb.cursor()

            address_cur_table=currentaddress_var.get()
            residence_place_table=placeofresidence_var.get()
            city_name_table=cityname_var.get()
            district_name_table=districtname_var.get()
            state_name_table=statename_var.get()
            pin_code_table=pincode_var.get()
            email_add_table=emailaddress_var.get()
            phone_num_table=phonenumber_var.get()
            
            sql = "UPDATE exam_registration_system SET CURRENT_ADDRESS= %s,RESIDENCE_PLACE= %s,CITY_NAME= %s,DISTRICT_NAME= %s,STATE_NAME= %s,PIN_CODE= %s,EMAIL_ADDRESS= %s,PHONE_NUMBER = %s "
            val = (address_cur_table,residence_place_table,city_name_table,district_name_table,state_name_table,pin_code_table,email_add_table,phone_num_table)
            cursor.execute(sql,val)
            mydb.commit()

    
    def filedata1():
        
            f = open('Exam_Registration_Details.txt','a+')
            f.write('\nCurrent Address: '+str(currentaddress_var.get()))
            f.write('\nPlace of Residence: '+str(placeofresidence_var.get()))
            f.write('\nCity: '+str(cityname_var.get()))
            f.write('\nDistrict: '+str(districtname_var.get()))
            f.write('\nState: '+str(statename_var.get()))
            f.write('\nPin Code: '+str(pincode_var.get()))
            f.write('\nEmail Address: '+str(emailaddress_var.get()))
            f.write('\nPhone Number: '+str(phonenumber_var.get()))

            f.close()
    
        
    def check1():
        if checkvar1.get()==0:
            messagebox.showwarning("Error", "PLEASE TICK THE CHECKBOX")
        else:
            filedata1()
            next2()
            mysqlconnectivity1()

    C2=Checkbutton(F6,text="By clicking this checkbox, you assure that your \n contact details given by you are totally correct.",variable=checkvar1,onvalue=1,offvalue=0,height=5,width=40,command= validation1)
    C2.grid(row=8,column=0)

    B2=Button(root1,font=('arial',16,'bold'),width=20,text='NEXT PAGE',bg='white',command=check1,relief=RIDGE,bd=10,state=DISABLED)
    B2.pack(side=BOTTOM, pady=30)
    
########################################################################################
def next2():
    root2=Toplevel()
    root2.geometry("800x800+0+0")
    root2.title("Exam Registration System")
    root2.configure(background='powder blue')

    F7=Frame(root2,bd=20,relief=RIDGE)
    F7.pack(side=TOP)

    label2=Label(F7,font=('arial',20,'bold'),text='EXAM   REGISTRATION   SYSTEM',bd=20,bg='powder blue',justify=CENTER,width=30, height=1)
    label2.grid(row=0)

    F8=Frame(root2,bd=15,relief=RIDGE)
    F8.pack(side=TOP)

    title2 = Label(F8, text="ACADEMIC  DETAILS", font=('Calibri', 16, 'bold'),bd=20,bg='powder blue',width=35, height=1)
    title2.grid(row=0)

    F9=Frame(root2,bd=15,relief=RIDGE)
    F9.pack(side=TOP)

    passstatusofclass10_var=StringVar()
    nameofclass10exam_var=StringVar()
    class10schoolboard_var=StringVar()
    passingyearofclass10_var=StringVar()
    passing1appearingstatusofclass12_var=StringVar()
    nameofclass12exam_var=StringVar()
    class12schoolboard_var=StringVar()
    passingappearingyearofclass12_var=StringVar()
    checkvar2=IntVar()

    pass_status_of_class_10 = Label(F9, text='Pass Status of Class 10:', font=("Calibri",20))
    pass_status_of_class_10.grid(row=0,column=0)
    passstatusofclass10= Entry(F9,textvariable = passstatusofclass10_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    passstatusofclass10.grid(row=0,column=1,padx=10,pady=(10,5))

    name_of_class_10_exam= Label(F9, text='Name of Class 10 Exam:', font=("Calibri", 20))
    name_of_class_10_exam.grid(row=1,column=0)
    nameofclass10exam = Entry(F9,textvariable = nameofclass10exam_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    nameofclass10exam.grid(row=1,column=1,padx=10,pady=5)

    class_10_school_board = Label(F9, text='Class 10 School Board:', font=("Calibri", 20))
    class_10_school_board.grid(row=2,column=0)
    class10schoolboard = Entry(F9,textvariable = class10schoolboard_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    class10schoolboard.grid(row=2,column=1,padx=10,pady=5)

    passing_year_of_class_10 = Label(F9, text='Passing Year of Class 10:', font=("Calibri", 20))
    passing_year_of_class_10.grid(row=3,column=0)
    passingyearofclass10 = Entry(F9,textvariable =passingyearofclass10_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    passingyearofclass10.grid(row=3,column=1,padx=10,pady=5)

    passing1appearing_status_of_class_12 = Label(F9, text='Passing/Appearing Status of Class 12:', font=("Calibri", 20))
    passing1appearing_status_of_class_12.grid(row=4,column=0)
    passing1appearingstatusofclass12= Entry(F9,textvariable = passing1appearingstatusofclass12_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    passing1appearingstatusofclass12.grid(row=4,column=1,padx=10,pady=5)

    name_of_class_12_exam = Label(F9, text='Name of Class 12 Exam:', font=("Calibri", 20))
    name_of_class_12_exam.grid(row=5,column=0)
    nameofclass12exam = Entry(F9,textvariable = nameofclass12exam_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    nameofclass12exam.grid(row=5,column=1,padx=10,pady=5)

    class_12_school_board = Label(F9, text='Class 12 School Board:', font=("Calibri", 20))
    class_12_school_board.grid(row=6,column=0)
    class12schoolboard = Entry(F9,textvariable = class12schoolboard_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    class12schoolboard.grid(row=6,column=1,padx=10,pady=5)

    passingappearing_year_of_class_12 = Label(F9, text='Passing/Appearing Year of Class 12:', font=("Calibri", 20))
    passingappearing_year_of_class_12.grid(row=7,column=0)
    passingappearingyearofclass12 = Entry(F9,textvariable = passingappearingyearofclass12_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
    passingappearingyearofclass12.grid(row=7,column=1,padx=10,pady=5)

    def validation2():
        q=passstatusofclass10_var.get()
        r=nameofclass10exam_var.get()
        s=class10schoolboard_var.get()
        t=passingyearofclass10_var.get()
        u=passing1appearingstatusofclass12_var.get()
        v=nameofclass12exam_var.get()
        w=class12schoolboard_var.get()
        x=passingappearingyearofclass12_var.get()
        
        if len(q)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B3['state'] = DISABLED
            checkvar2.set(0)
        elif len(r)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B3['state'] = DISABLED
            checkvar2.set(0)
        elif len(s)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B3['state'] = DISABLED
            checkvar2.set(0)
        elif len(t)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B3['state'] = DISABLED
            checkvar2.set(0)
        elif len(u)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B3['state'] = DISABLED
            checkvar2.set(0)
        elif len(v)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B3['state'] = DISABLED
            checkvar2.set(0)
        elif len(w)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B3['state'] = DISABLED
            checkvar2.set(0)
        elif len(x)==0:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            B3['state'] = DISABLED
            checkvar2.set(0)
            
        else:
            passstatusofclass10.configure(state='readonly')
            nameofclass10exam.configure(state='readonly')
            class10schoolboard.configure(state='readonly')
            passingyearofclass10.configure(state='readonly')
            passing1appearingstatusofclass12.configure(state='readonly')
            nameofclass12exam.configure(state='readonly')
            class12schoolboard.configure(state='readonly')
            passingappearingyearofclass12.configure(state='readonly')
            B3['state'] = NORMAL

    def mysqlconnectivity2():
        
            mydb= mysql.connector.connect(host='localhost',database='test',user='root',password='tiger')
            cursor=mydb.cursor()

            pass_status_10_table=passstatusofclass10_var.get()
            name_exam_10_table=nameofclass10exam_var.get()
            school_board_10_table=class10schoolboard_var.get()
            pass_year_10_table=passingyearofclass10_var.get()
            pass_status_12_table=passing1appearingstatusofclass12_var.get()
            name_exam_12_table=nameofclass12exam_var.get()
            school_board_12_table=class12schoolboard_var.get()
            pass_year_12_table=passingappearingyearofclass12_var.get()
        
            sql = "UPDATE exam_registration_system SET PASS_STATUS_10 = %s,NAME_EXAM_10 = %s,SCHOOL_BOARD_10 = %s,PASS_YEAR_10 = %s,PASS_STATUS_12 = %s,NAME_EXAM_12 = %s,SCHOOL_BOARD_12 = %s,PASS_YEAR_12 = %s "
            val = (pass_status_10_table,name_exam_10_table,school_board_10_table,pass_year_10_table,pass_status_12_table,name_exam_12_table,school_board_12_table,pass_year_12_table)
            cursor.execute(sql,val)
            mydb.commit()

    def filedata2():

        
        f = open('Exam_Registration_Details.txt','a+')
        f.write('\nPass Status of Class 10: '+str(passstatusofclass10_var.get()))
        f.write('\nName of Class 10 Exam: '+str(nameofclass10exam_var.get()))
        f.write('\nClass 10 School Board: '+str(class10schoolboard_var.get()))
        f.write('\nPassing Year of Class 10: '+str(passingyearofclass10_var.get()))
        f.write('\nPass Status of Class 12: '+str(passing1appearingstatusofclass12_var.get()))
        f.write('\nName of Class 12 Exam: '+str(nameofclass12exam_var.get()))
        f.write('\nClass 12 School Board: '+str(class12schoolboard_var.get()))
        f.write('\nPassing Year of Class 12: '+str(passingappearingyearofclass12_var.get()))

        f.close()
    
            
    def check2():
        if checkvar2.get()==0:
            messagebox.showwarning("Error", "PLEASE TICK THE CHECKBOX")
        else:
            filedata2()
            next3()
            mysqlconnectivity2()

    C3=Checkbutton(F9,text="By clicking this checkbox, you assure that your \n academic details given by you are totally correct.",variable=checkvar2,onvalue=1,offvalue=0,height=5,width=40,command=validation2)
    C3.grid(row=8,column=0)

    B3=Button(root2,font=('arial',16,'bold'),width=20,text='NEXT PAGE',bg='white',command=check2,relief=RIDGE,bd=10,state=DISABLED)
    B3.pack(side=BOTTOM, pady=30)

    

######################################################################################################
def next3():
    root3=Toplevel()
    root3.geometry("800x800+0+0")
    root3.title("Exam Registration System")
    root3.configure(background='powder blue')

    F10=Frame(root3,bd=20,relief=RIDGE)
    F10.pack(side=TOP)

    label3=Label(F10,font=('arial',20,'bold'),text='EXAM   REGISTRATION   SYSTEM',bd=20,bg='powder blue',justify=CENTER,width=30, height=1)
    label3.grid(row=0)

    F11=Frame(root3,bd=15,relief=RIDGE)
    F11.pack(side=TOP)

    title3 = Label(F11, text="PAYMENT  DETAILS", font=('Calibri', 16, 'bold'),bd=20,bg='powder blue',width=35, height=1)
    title3.grid(row=0)

    F12=Frame(root3,bd=15,relief=RIDGE)
    F12.pack(side=TOP)

    modeofpayment_var=StringVar()
    checkvar3=IntVar()

    modeof_payment = Label(F12, text='MODE OF PAYMENT:', font=("Calibri", 20))
    modeof_payment.grid(row=0,column=0)
    modeofpayment = ttk.Combobox(F12, width = 20, textvariable = modeofpayment_var , font=('calibre',15,'normal'),state="readonly",values = ['DEBIT/CREDIT CARD','UPI','NET BANKING'])
    modeofpayment.grid(row=0,column=1,pady=50)
    modeofpayment.bind("<<ComboboxSelected>>",lambda e: F12.focus())

    def validation3():
        if modeofpayment_var.get()=='DEBIT/CREDIT CARD' or modeofpayment_var.get()=='UPI' or modeofpayment_var.get()=='NET BANKING' :
            B4['state'] = NORMAL
        else:
            messagebox.showwarning("Error", "Some Entry is left unfilled")
            checkvar3.set(0)
    

    def payment():
        if modeofpayment_var.get()=='DEBIT/CREDIT CARD':
            debitcreditcard()
        elif modeofpayment_var.get()=='UPI':
            upi()
        else:
            netbanking() 

    def debitcreditcard():
        root4=Toplevel()
        root4.geometry("800x800+0+0")
        root4.title("Exam Registration System")
        root4.configure(background='powder blue')

        F13=Frame(root4,bd=20,relief=RIDGE)
        F13.pack(side=TOP)

        label4=Label(F13,font=('arial',20,'bold'),text='EXAM   REGISTRATION   SYSTEM',bd=20,bg='powder blue',justify=CENTER,width=30, height=1)
        label4.grid(row=0)

        F14=Frame(root4,bd=15,relief=RIDGE)
        F14.pack(side=TOP)

        title4 = Label(F14, text="PAYMENT  DETAILS", font=('Calibri', 16, 'bold'),bd=20,bg='powder blue',width=35, height=1)
        title4.grid(row=0)

        F15=Frame(root4,bd=15,relief=RIDGE)
        F15.pack(side=TOP)

        cardnumber_var=StringVar()
        expirydate_var=StringVar()

        cardnumber = Label(F15, text='Card Number:', font=("Calibri",20))
        cardnumber.grid(row=0,column=0)
        card_number= Entry(F15,textvariable = cardnumber_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
        card_number.grid(row=0,column=1,padx=10,pady=(10,5))

        expirydate= Label(F15, text='Expiry Date:', font=("Calibri", 20))
        expirydate.grid(row=1,column=0)
        expiry_date = Entry(F15,textvariable = expirydate_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
        expiry_date.grid(row=1,column=1,padx=10,pady=(10,5))

        T1=Text(F15, height =1, width = 12,font=('calibre',15,'normal'))
        T1.grid(row=2,column=1, padx=(0,30),pady=10)

        def fees():
            if examtype_var.get() =='JEE' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"650")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"650")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"325")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"325")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"325")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"325")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"1600")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"1500")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"900")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"1600")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"1500")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"900")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"8500")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"8500")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"8500")
                T1.configure(state=DISABLED)
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"8500")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"8500")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"8500")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"800")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"600")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"600")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"800")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"600")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"600")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"3400")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"3400")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"3400")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T1.insert( 1.0,"2900")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T1.insert( 1.0,"2900")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T1.insert( 1.0,"2900")
                T1.configure(state=DISABLED)
                B5['state'] = NORMAL
            else:
                print("")

        C5=Checkbutton(F15,text="Get Fees.",onvalue=1,offvalue=0,height=5,width=40,command=fees)
        C5.grid(row=3,column=0,pady=20)
        
        B5=Button(root4,font=('arial',16,'bold'),width=20,text='PAY',bg='white',command=successfull,state=DISABLED,relief=RIDGE,bd=10)
        B5.pack(side=BOTTOM)
        
    def upi():
        successfull()

    def netbanking():
        root5=Toplevel()
        root5.geometry("800x800+0+0")
        root5.title("Exam Registration System")
        root5.configure(background='powder blue')

        F16=Frame(root5,bd=20,relief=RIDGE)
        F16.pack(side=TOP)

        label5=Label(F16,font=('arial',20,'bold'),text='EXAM   REGISTRATION   SYSTEM',bd=20,bg='powder blue',justify=CENTER,width=30, height=1)
        label5.grid(row=0)

        F17=Frame(root5,bd=15,relief=RIDGE)
        F17.pack(side=TOP)

        title5 = Label(F17, text="PAYMENT  DETAILS", font=('Calibri', 16, 'bold'),bd=20,bg='powder blue',width=35, height=1)
        title5.grid(row=0)

        F18=Frame(root5,bd=15,relief=RIDGE)
        F18.pack(side=TOP)

        username_var=StringVar()
        password_var=StringVar()

        username = Label(F18, text='User Name:', font=("Calibri",20))
        username.grid(row=0,column=0)
        user_name= Entry(F18,textvariable = username_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
        user_name.grid(row=0,column=1,padx=10,pady=(10,5))

        password= Label(F18, text='Password:', font=("Calibri", 20))
        password.grid(row=1,column=0)
        pass_word = Entry(F18,textvariable = password_var, font=('calibre',15,'normal'),bd=5,relief=SUNKEN)
        pass_word.grid(row=1,column=1,padx=10,pady=(10,5))

        T2=Text(F18, height =1, width = 12,font=('calibre',15,'normal'))
        T2.grid(row=2,column=1, padx=(0,30),pady=10)

        def fees2():
            if examtype_var.get() =='JEE' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"650")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"650")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"325")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"325")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"325")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='JEE' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"325")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"1600")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"1500")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"900")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"1600")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"1500")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='NEET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"900")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"8500")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"8500")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"8500")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"8500")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"8500")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='SAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"8500")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"800")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"600")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"600")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"800")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"600")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='CET' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"600")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"3400")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"3400")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='MALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"3400")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'GENERAL':
                T2.insert( 1.0,"2900")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'OBC':
                T2.insert( 1.0,"2900")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            elif examtype_var.get() =='BITSAT' and gendertype_var.get() =='FEMALE' and categorytype_var.get() == 'SC/ST':
                T2.insert( 1.0,"2900")
                T2.configure(state=DISABLED)
                B6['state'] = NORMAL
            else:
                print("")

    
        C6=Checkbutton(F18,text="Get Fees.",onvalue=1,offvalue=0,height=5,width=40,command=fees2)
        C6.grid(row=3,column=0,pady=20)
        
        B6=Button(root5,font=('arial',16,'bold'),width=20,text='PAY',bg='white',command= successfull,relief=RIDGE,bd=10,state=DISABLED)
        B6.pack(side=BOTTOM)

    def successfull():
        messagebox.showwarning("successfull", "PAYMENT SUCCESSFULL")
        root.destroy()
      
    C4=Checkbutton(F12,text="By clicking this checkbox, you assure that your \n payment details given by you are totally correct.",variable=checkvar3,onvalue=1,offvalue=0,height=5,width=40,command=validation3)
    C4.grid(row=2,column=0, pady=50)

    B4=Button(root3,font=('arial',16,'bold'),width=20,text='NEXT PAGE',bg='white',relief=RIDGE,bd=10,state=DISABLED,command=payment)
    B4.pack(side=BOTTOM, pady=30)
###############################    MY    SQL  ###############################################################

def mysqlconnectivity():
    mydb= mysql.connector.connect(host='localhost',database='test',user='root',password='tiger')
    cursor=mydb.cursor()

    cand_name_table=candidatename_var.get()
    father_name_table=fathername_var.get()
    mother_name_table=mothername_var.get()
    aadhar_card_num=aadharnumber_var.get()
    natio_table=nationalitytype_var.get()
    ge_type=gendertype_var.get()
    ca_type=categorytype_var.get()
    ex_type=examtype_var.get()
    
    sql = "INSERT INTO exam_registration_system(CANDIDATE_NAME,FATHER_NAME,MOTHER_NAME,AADHAR_NUMBER,NATIONALITY,GENDER_TYPE,CATEGORY_TYPE,EXAM_TYPE)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    vals = (cand_name_table, father_name_table, mother_name_table, aadhar_card_num, natio_table, ge_type, ca_type, ex_type)
    cursor.execute(sql,vals)
    mydb.commit()


mydb.commit()
mydb.close()

def filedata():

    f = open('Exam_Registration_Details.txt','a+')
    f.write('\n*****REGISTRATION DETAILS*****')
    f.write('\nCandidate Name: '+str(candidatename_var.get()))
    f.write('\nFather Name: '+str(fathername_var.get()))
    f.write('\nMother Name: '+str(mothername_var.get()))
    f.write('\nAadhar Number: '+str(aadharnumber_var.get()))
    f.write('\nNationality: '+str(nationalitytype_var.get()))
    f.write('\nGender: '+str(gendertype_var.get()))
    f.write('\nCategory: '+str(categorytype_var.get()))
    f.write('\nExam Name: '+str(examtype_var.get()))

    f.close()

    
root.mainloop()



