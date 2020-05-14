from tkinter import *
import pymysql
import tkinter.messagebox as mb

def quit():
    root.destroy()


def clear():
        emp_name.delete(0,END)
        emp_address.delete(0,END)
        emp_age.delete(0,END)
        emp_gender.delete(0,END)
        emp_id.delete(0,END)
        emp_position.delete(0,END)
        emp_sal.delete(0,END)
        

def get():
    name=emp_name.get()
    address=emp_address.get()
    age=emp_age.get()
    gender=emp_gender.get()
    id1=emp_id.get()
    position=emp_position.get()
    sal=emp_sal.get()
    con=pymysql.connect(host="localhost",user="root",password="123",db="employee")
    cursor=con.cursor()
    cursor.execute("select * from employee_info where Emp_id='"+emp_id.get()+"'")
    row=cursor.fetchall()
    for row in row:
        emp_name.insert(0,row[0])
        emp_address.insert(0,row[1])
        emp_age.insert(0,row[2])
        emp_gender.insert(0,row[3])
        emp_position.insert(0,row[6])
        emp_sal.insert(0,row[5])


def update():
        name=emp_name.get()
        address=emp_address.get()
        age=emp_age.get()
        gender=emp_gender.get()
        id1=emp_id.get()
        position=emp_position.get()
        sal=emp_sal.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="employee")
        cursor=con.cursor()
        cursor.execute("Update employee_info set Name='"+ name +"',AdDress='"+ address +"',Age='"+ age +"',Gender='"+ gender +"',Emp_position='"+ position +"',Emp_sal='"+ sal + "'where emp_id='"+ id1 +"'")
        cursor.execute("commit");
        mb.showinfo("Updated","Data Sucessfully Updated")

def delete():
        name=emp_name.get()
        address=emp_address.get()
        age=emp_age.get()
        gender=emp_gender.get()
        id1=emp_id.get()
        position=emp_position.get()
        sal=emp_sal.get()
        
        con=pymysql.connect(host="localhost",user="root",password="123",db="employee")
        cursor=con.cursor()
        cursor.execute("delete from employee_info where Emp_id='"+emp_id.get()+"'")
        ques=mb.askquestion("Delete","Are You Sure You Want To Delete Data")
        if ques=="yes":
                cursor.execute("commit");
                mb.showinfo("Deleted","Data Sucessfully Deleted")

def insert():
    name=emp_name.get()
    address=emp_address.get()
    age=emp_age.get()
    gender=emp_gender.get()
    id1=emp_id.get()
    position=emp_position.get()
    sal=emp_sal.get()
    

    con=pymysql.connect(host="localhost",user="root",password="123",db="employee")
    cursor=con.cursor()
    cursor.execute("insert into employee_info values('"+name +"','"+ address+"','"+age+"','"+gender+"','"+id1 +"','"+sal+"','"+ position +"')")
    cursor.execute("commit");
    mb.showinfo("Inserted","Data Sucessfully Inserted")



root=Tk()

root.geometry("800x600")

#Top Frame
topframe=Frame(root,bg="#2f7cf7",height="80",width="800")
topframe.place(x=0,y=0)

label1=Label(topframe,text="Employee Management System",bg="#2f7cf7",font="arial 20 bold",fg="white")
label1.place(x=200,y=15)

#Main Frame
mainframe=Frame(root,bg="#d5d8de",height="400",width="800")
mainframe.place(x=0,y=80)

#Button Frame
buttonframe=Frame(root,height="100",width="800",bg="black")
buttonframe.place(x=0,y=500)

#Entry
emp_name=Entry(mainframe,bd="3")
emp_name.place(x=150,y=50)

emp_address=Entry(mainframe,bd="3")
emp_address.place(x=150,y=110)


emp_age=Entry(mainframe,bd="3")
emp_age.place(x=150,y=170)

emp_gender=Entry(mainframe,bd="3")
emp_gender.place(x=150,y=230)


emp_id=Entry(mainframe,bd="3")
emp_id.place(x=550,y=50)


emp_position=Entry(mainframe,bd="3")
emp_position.place(x=550,y=170)


emp_sal=Entry(mainframe,bd="3")
emp_sal.place(x=550,y=110)



#Label
emp_first_label=Label(mainframe,text="Employee Name",font="arial 11 bold",bg="#d5d8de")
emp_first_label.place(x=20,y=50)


emp_age_label=Label(mainframe,text="Age",font="arial 11 bold",bg="#d5d8de")
emp_age_label.place(x=20,y=170)

emp_gender_label=Label(mainframe,text="Gender",font="arial 11 bold",bg="#d5d8de")
emp_gender_label.place(x=20,y=230)

emp_address_label=Label(mainframe,text="Address",font="arial 11 bold",bg="#d5d8de")
emp_address_label.place(x=20,y=110)

emp_id_label=Label(mainframe,text="Employee ID",font="arial 11 bold",bg="#d5d8de")
emp_id_label.place(x=400,y=50)

emp_sal_label=Label(mainframe,text="Employee Salary",font="arial 11 bold",bg="#d5d8de")
emp_sal_label.place(x=400,y=110)

emp_position_label=Label(mainframe,text="Employee Position",font="arial 11 bold",bg="#d5d8de")
emp_position_label.place(x=400,y=170)


#Button
insert_btn=Button(buttonframe,text="Insert",font="arial 12 bold",bg="#6dbbf2",command=insert)
insert_btn.place(x=80,y=35)

update_btn=Button(buttonframe,text="Update",font="arial 12 bold",bg="#6dbbf2",command=update)
update_btn.place(x=200,y=35)

get_btn=Button(buttonframe,text="Get Info",font="arial 12 bold",bg="#6dbbf2",command=get)
get_btn.place(x=320,y=35)

delete_btn=Button(buttonframe,text="Delete",font="arial 12 bold",bg="#6dbbf2",command=delete)
delete_btn.place(x=440,y=35)

clear_btn=Button(buttonframe,text="Clear",font="arial 12 bold",bg="#6dbbf2",command=clear)
clear_btn.place(x=560,y=35)

quit_btn=Button(buttonframe,text="Quit",font="arial 12 bold",bg="#db3a35",command=quit)
quit_btn.place(x=680,y=35)







root.mainloop()
