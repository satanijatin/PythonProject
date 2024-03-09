import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="schooldb"
    
)

cursor=mydb.cursor()

# cursor.execute("create database schooldb")
# cursor.execute("create table student (id int primary key ,name varchar(255), address varchar(255),phone varchar(50))")


def insertdata(name,address,phone):
    
    sql="insert into student(name,address ,phone) VALUES (%s,%s,%s)"
    
    val=(name,address,phone)
    
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount, "record inserted" )
  
  
# name=input("Enter name : ")  
# address=input("Enter address : ")  
# phone=input("Enter phone : ")  

# insertdata(name,address,phone)


def updatedata(id,name,address,phone):
    sql="update student set name=%s, address=%s,phone=%s where id=%s"
    val=(name,address,phone,id)
    cursor.execute(sql,val)
    
    mydb.commit()
    print("update success")
    
    
# id=input("Enter id : ")   
# name=input("Enter name : ")  
# address=input("Enter address : ")  
# phone=input("Enter phone : ")  

# updatedata(id,name,address,phone)



def deletedata(id):
    sql="delete from student where id=%s"
    db=(id,)
    cursor.execute(sql,db)
    mydb.commit()
    print("delete success")
    
id=int(input("Enter id : "))
 
deletedata(id)


def viewdata():
    cursor.execute("select * from student")
    result=cursor.fetchall()
    for i in result:
        print(i)
        
        
# viewdata()






