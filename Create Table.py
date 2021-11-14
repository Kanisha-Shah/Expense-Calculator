import mysql.connector

myb = mysql.connector.connect(host="localhost", user="root", passwd="KANISHA*23", database="ExpenseTracker")

mycursor = myb.cursor()

#Creating table from query
mycursor.execute("CREATE TABLE Expense (DATE_OF_EXPENSE date,TITLE varchar(20),MONEY int)")

myb.commit()
