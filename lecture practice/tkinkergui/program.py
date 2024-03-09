from tkinter import *
import mysql.connector
import tkinter.messagebox as MessageBox


def create_conection():
    return mysql.connector.connect(host="localhost",user="root",password="",database="studentdb")

def insert_data(f,l,e,m):
    conn=create_conection()
    cursor=conn.cursor()
  
    query="insert into student(id,fname,lname,email,mobile) values(%s,%s,%s,%s,%s)"
    args=(0,f,l,e,m)
    cursor.execute(query,args)
    conn.commit()
    print("Data Inserted Successfully")
    conn.close()
    
def update_data(f,l,e,m,id):
   conn=create_conection()
   cursor=conn.cursor()
   if(f == "" or l == ""):
            MessageBox.showinfo("ALERT", "Please enter fiels you want to update!")
   else:
        sql="update student set fname=%s, lname=%s,email=%s,mobile=%s where id=%s"
        val=(f,l,e,m,id)
        #    aa=cursor.execute("update Person set fname = '"+ f +"',lname = '"+ l +"',email = '"+ e +"', mobile='"+ m +"' where id ='"+ id +"'")
        cursor.execute(sql,val);
        conn.commit()
        MessageBox.showinfo("Status", "Successfully Updated")
        conn.close();

master=Tk()
master.geometry('500x500')

Label(master, text="First Name").place(x=50,y=50)
Label(master, text="Last Name").place(x=50,y=80)
Label(master, text="Email").place(x=50,y=110)
Label(master, text="Mobile").place(x=50,y=140)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)


e1.place(x=140,y=50)
e2.place(x=140,y=80)
e3.place(x=140,y=110)
e4.place(x=140,y=140)


def userinput():
    id=int(input("Enter Id : "))  
    return id


b1=Button(master, text='Insert Data',
          command=lambda:insert_data(e1.get(),e2.get(),e3.get(),e4.get())).place(x=140,y=170)


# btnDelete = Button(root, text="Delete", command=Del, font=("verdana 15")).place(x=200, y=190)

# ids=int(input("Enter  id : "))
btnUpdate = Button(master, text="Update", command=lambda:update_data(e1.get(),e2.get(),e3.get(),e4.get(),userinput())).place(x=220, y=170)
# btnSelect= Button(root, text="Select", command=Select, font=("verdana 15")).place(x=200, y=240)
master.mainloop()