import mysql.connector as my

#establishing a connection
mydb=my.connect(host='localhost',username='root',password='12345678',database='mydatabase')

#A cursor in MySQL (when using Python) is an object used to execute 
# SQL queries and fetch results from the database. 
# It acts as a pointer to manage the result set.
#creating cursor
cursor=mydb.cursor()

# create table with columns

query='''
create table library
               (Member_Type Varchar(45),
               PRN_No varchar(10),
               Title varchar(45),
               First_Name varchar(45),
               Last_Name varchar(45),
               Address1 varchar(45),
               Address2 varchar(10),
               Post_ID varchar(45),
               Mobile_No varchar(45),
               Book_ID varchar(45),
               Book_Title varchar(45),
               Author varchar(45),
               Date_Borrowed varchar(45),
               Date_Due varchar(20),
               Days varchar(45),
               Late_Return_Fine varchar(45),
               Date_Overdue varchar(45),
               Final_Price varchar(45)
               );'''
# print(query)
cursor=mydb.cursor()
cursor.execute(query)
print('table created')