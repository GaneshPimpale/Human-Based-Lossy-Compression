import os

import mysql.connector
from mysql.connector import errorcode

#Connection to database:
try:
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        passwd = "",
    )
#Errors from MySQL:
except mysql.connector.Error as err:
    print(err)

cur = mydb.cursor()

cur.execute("USE waicDb")
#Using mainTable

Change = False

#Functions to edit the database:
def addRow(objectDir, transDir, tagsDir):
    global Change
    Change = True
    #SQL code:
    sql = "INSERT INTO customers (ID, Object, Trans, Tags) VALUES (%s, %s, %s, %s)"
    #insert values:
    val = (0, objectDir, transDir, tagsDir)
    cur.execute(sql, val)

def deleteRow(ID):
    #Change Variable
    global Change
    Change = True
    #SQL command
    sql = "DELETE FROM mainTable WHERE ID = %s"
    #Values to change
    val = ID
    cur.execute(sql, val)

def query(Tag):
    #SQL command
    sql = "SELECT * FROMWHERE Tags = %s"
    #Value to find
    val = Tag
    cur.execute(sql, val)
    for x in cur:
        print(x)

#Calling functions:


#Commit changes and close:
if (Change  == True):
    mydb.commit()
    cur.close()




