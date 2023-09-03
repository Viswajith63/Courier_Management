import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="courier_management"
)
cursor = conn.cursor()

def customercon(cname,cmobile,caddress) :
    query2 = "INSERT INTO customer (Name,mobile,address) values('{0}','{1}','{2}')".format(cname,cmobile,caddress)
    cursor.execute(query2)
    conn.commit()

def selcid():
    cname=int(input("Enter the name : "))
    query1 = "select customer_id from customer where Name=%s"
    vl=(cname,)
    cursor.execute(query1,vl)
    t=cursor.fetchall()
    for i in t:
        print(i)

selcid()

def packcon(cid,weight,dlocation,description,sdate) :
    query3 = "INSERT INTO packet (customer_id,weight,delivery_location,description,sent_date) values('{0}','{1}','{2}','{3}','{4}')".format(cid,weight,dlocation,description,sdate)
    cursor.execute(query3)
    conn.commit()

def selpid(cid) :
    query4 = "select id from packet where customer_id='{0}'".format(cid)
    cursor.execute(query4)
    return cursor.fetchall()

def deliverycon(pid,rname,rmobile,rdate,dstatus,dname) :
    query5 = "INSERT INTO delivery (id,receiver_name,receiver_mobile,recived_date,delivery_status,deliveryman_idandname) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(pid,rname,rmobile,rdate,dstatus,dname)
    cursor.execute(query5)
    conn.commit()
    
#messagebox.showinfo("Sucessful", "you are added !")
    