import sqlite3

## connect to sqllite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Ravikant','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Shubh','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Aman','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Neha','Data Science','B',77)''')
cursor.execute('''Insert Into STUDENT values('Anjali','Cybersecurity','A',92)''')
cursor.execute('''Insert Into STUDENT values('Vikram','DEVOPS','B',65)''')
cursor.execute('''Insert Into STUDENT values('Rahul','Data Science','C',58)''')
cursor.execute('''Insert Into STUDENT values('Priya','Cybersecurity','A',88)''')
cursor.execute('''Insert Into STUDENT values('Sonia','DEVOPS','C',45)''')
cursor.execute('''Insert Into STUDENT values('Karan','Data Science','B',81)''')
cursor.execute('''Insert Into STUDENT values('Isha','Cybersecurity','B',73)''')
cursor.execute('''Insert Into STUDENT values('Tarun','DEVOPS','A',69)''')
cursor.execute('''Insert Into STUDENT values('Meena','Data Science','A',95)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
