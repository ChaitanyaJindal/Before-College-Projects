import mysql.connector

def studentData():
    con=mysql.connector.connect(host="localhost", username="root", passwd="12345")
    cur= con.cursor()
    cur.execute("create database if not exists student")
    cur.execute("use student")
    cur.execute("CREATE TABLE IF NOT EXISTS student (StdID INT(10) PRIMARY KEY, Firstname VARCHAR(100), Lastname VARCHAR(100),Dob VARCHAR(100), Age VARCHAR(100),Gender VARCHAR(100), Addresst VARCHAR(100),Mobile BIGINT)")
    cur.execute("commit")
    con.close()

def addstdrecord(StdID , Firstname ,Lastname ,Dob, Age ,Gender , Addresst,Mobile ):
    con=mysql.connector.connect(host="localhost", username="root", passwd="12345")
    cur = con.cursor()
    cur.execute("create database if not exists student")
    cur.execute("use student")
    x = (StdID , Firstname ,Lastname ,Dob, Age ,Gender , Addresst, Mobile)
    y = ("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
    cur.execute(y,x)
    cur.execute("commit")
    con.close()

def viewData():
    con=mysql.connector.connect(host="localhost", username="root", passwd="12345", database="student")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleterec(StdID):
    con=mysql.connector.connect(host="localhost", username="root", passwd="12345", database="student")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE StdID=%s",(StdID,))
    cur.execute("commit")
    con.close()

def searchData(StdID="" , Firstname="" ,Lastname="" ,Dob="", Age="" ,Gender="", Addresst="",Mobile="" ):
    con=mysql.connector.connect(host="localhost", username="root", passwd="12345", database="student")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=%s OR Firstname=%s OR Lastname=%s OR Dob=%s OR Age=%s OR Gender=%s OR Addresst=%s OR Mobile=%s",(StdID , Firstname ,Lastname ,Dob, Age ,Gender , Addresst,Mobile))
    rows=cur.fetchall()
    con.close()
    return rows

def updateData(StdID="" , Firstname="" ,Lastname="" ,Dob="", Age="" ,Gender="", Addresst="",Mobile="" ):
    con=mysql.connector.connect(host="localhost", username="root", passwd="12345", database="student")
    cur = con.cursor()
    cur.execute("UPDATE student SET  StdID=%s , Firstname=%s , Lastname=%s , Dob=%s , Age=%s , Gender=%s , Addresst=%s , Mobile=%s, WHERE StdId=%s",(StdID , Firstname ,Lastname ,Dob, Age ,Gender , Addresst,Mobile))
    cur.execute("commit")
    con.close()

studentData()
