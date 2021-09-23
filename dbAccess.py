import mysql.connector

#SQL connector is a connector to access to a DB 
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Valleysoft1!",
  database= "mydatabase"
)

#creating a database
mycursor = mydb.cursor()

#CREATE DATABASE
# mycursor.execute("CREATE DATABASE mydatabase")

#CREATE TABLE
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#IF TABLE EXSITS ALTER THE TABLE COLUMNS
#mycursor.execute("ALTER TABLE customers ADD COLUMN age VARCHAR(255)")

#INSERT MANY ROWS

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# myval = [
#     ("John", "Highway 21"),
#     ('Amy', 'Apple st 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, myval)
# mydb.commit()

# onResult = mycursor.fetchone()
# print(onResult)


userInput = input("User Input:")

sql = "SELECT * FROM customers WHERE name =" + userInput
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# y = input("Type another number")
# print(x)
# sum = int(x) + int(y)
# print("The sum is: ", sum)