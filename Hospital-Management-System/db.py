import mysql.connector as my

#establishing a connection
mydb=my.connect(host='localhost',username='root',password='12345678',database='mydatabase')

#A cursor in MySQL (when using Python) is an object used to execute 
# SQL queries and fetch results from the database. 
# It acts as a pointer to manage the result set.
#creating cursor
cursor=mydb.cursor()

#to drop table
# cursor.execute('drop table if exists hospital')

#create db
# cursor.execute('create database mydatabase')

#show available db
# cursor.execute('show databases')
# for x in cursor:
#     print(x)

# create table with columns
query='''
create table hospital
               (Name_of_tablets Varchar(45),
               Reference_no varchar(10),
               Dose varchar(45),
               No_of_tablets varchar(45),
               Lot_No varchar(45),
               Issue_Date varchar(45),
               Expiry_Date varchar(10),
               Daily_Dose varchar(45),
               Side_Effect varchar(45),
               Further_Info varchar(45),
               Blood_Pressure varchar(45),
               Storage varchar(45),
               Medication varchar(45),
               Patient_ID varchar(20),
               Patient_Name varchar(45),
               Date_of_Birth varchar(45),
               Patient_Address varchar(45),
               Doctor_Name varchar(45)
               );'''
# print(query)
cursor=mydb.cursor()
cursor.execute(query)
print('table created')

# #show tables
# cursor.execute('show tables')
# for x in cursor:
#     print(x)

#showing table contents
# cursor.execute('select * from hospital')
# res=cursor.fetchall()
# for x in res:
#     print(x)

# cursor.execute('select * from hospital')
# res=cursor.fetchall()
# for x in res:
#     print(x)