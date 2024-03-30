import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase1"


)

#  mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase1")

# mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# mycursor = mydb.cursor() 
# mycursor.execute("alter table customers change `phone` `telephone` int")


# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")



# def insertdata(name,address,phone):
    
#     mycursor = mydb.cursor()

#     sql = "INSERT INTO customers (name, address, telephone) VALUES (%s, %s,%s)"
#     val = (name, address,phone)
#     mycursor.execute(sql, val)

#     mydb.commit()

#     print(mycursor.rowcount, "record inserted.")
    
    
# name=input("Enter Name : ")
# address=input("Enter Address :")
# phone=input("Enter Phone :")

# insertdata(name,address,phone)



# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address,telephone) VALUES (%s, %s,%s)"
# val = [
#   ('Peter', 'Lowstreet 4',"4645768696969"),
#   ('Amy', 'Apple st 652',"4645768696969"),
#   ('Hannah', 'Mountain 21',"4645768696969"),
#   ('Michael', 'Valley 345',"4645768696969"),
#   ('Sandy', 'Ocean blvd 2',"4645768696969"),
#   ('Betty', 'Green Grass 1',"4645768696969"),
#   ('Richard', 'Sky st 331',"4645768696969"),
#   ('Susan', 'One way 98',"4645768696969"),
#   ('Vicky', 'Yellow Garden 2',"4645768696969"),
#   ('Ben', 'Park Lane 38',"4645768696969"),
#   ('William', 'Central st 954',"4645768696969"),
#   ('Chuck', 'Main Road 989',"4645768696969"),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

# mycursor = mydb.cursor() 
# mycursor.execute("alter table customers modify column telephone varchar(50)")

# mycursor = mydb.cursor()

# mycursor.execute("Alter table customers add phone int")




# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
    
    
    
# mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

