import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from datetime import date
from PIL import ImageTk
import random
from random import randint, randrange
import dbcon
def dpage(cname):
    def delivery_detail(rnamee,rmobilee,rdatee,dstatuse,dnamee):
        cid=dbcon.selcid(cname)
        pid=dbcon.selpid(cid[0][0])
        #print("############ "+str(pid[0][0])+" ##########")
        rname=rnamee.get()
        rmobile=rmobilee.get()
        rdate=rdatee.get()
        dstatus=dstatuse.get()
        dname=dnamee.get()
        dbcon.deliverycon(pid[0][0],rname,rmobile,rdate,dstatus,dname)
        

    def rdatey() :
        rdatee.delete(0,'end')
        rdatee.insert('end',rdate.entry.get())

    """def assigndno() :
        randno=random.randint(1000,1006)
        dnoEntry.delete(0,'end')
        dnoEntry.insert('end',randno)"""
    def assigndname() :
        randchoice=random.choice(lstofnames)
        dnamee.delete(0,'end')
        dnamee.insert('end',randchoice)
        
        
    lstofnames=['1000 - Ram','1001 - Raju','1002 - Sanjay','1003 - Takur','1004 - Tom','1005 - Mark','1006 - Ahmed']

    delivery_window=tk.Tk()
    delivery_window.title('Delivery Info Page')
    delivery_window.geometry("1200x660")
    bgImage=ImageTk.PhotoImage(file='tableframe.jpg')

    bgLabel=Label(delivery_window,image=bgImage)
    bgLabel.grid()
    frame1=Frame(delivery_window,bg='white')
    frame1.place(x=273,y=40)
    frame2=Frame(delivery_window,bg='white')
    frame2.place(x=623,y=182)



    rname=Label(frame1,text='Receiver Name',font=('Arial',11,'bold'),bg='white')
    rname.grid(row=0,column=0,sticky='w',padx=10)
    rnamee=Entry(frame1,width=35,font=('Arial',11),bg='white')
    rnamee.grid(row=1,column=0,sticky='w',padx=10)

    rmobilel=Label(frame1,text='Receiver Mobile No',font=('Arial',11,'bold'),bg='white')
    rmobilel.grid(row=2,column=0,sticky='w',padx=10)
    rmobilee=Entry(frame1,width=35,font=('Arial',11),bg='white')
    rmobilee.grid(row=3,column=0,sticky='w',padx=10)

    rdatelabel=tb.Label(frame1,text='Received Date',font=('Arial',11,'bold'))
    rdatelabel.grid(row=4,column=0,sticky='w',padx=10)
    dt3=date(2023, 6, 13)
    rdate=tb.DateEntry(frame1,dateformat="%y-%m-%d",startdate=dt3)
    rdate.grid(row=5,column=0,padx=10,sticky='e')
    rdatee=Entry(frame1,width=10,font=('Arial',11),bg='white')
    rdatee.grid(row=5,column=0,sticky='w',padx=10)
    rdatebutton=tb.Button(frame1,text='click to confirm date',cursor='hand2',command=lambda: rdatey())
    rdatebutton.grid(row=6,column=0,pady=15)

    dnamelabel=Label(frame1,text="Deliveryman's Id & Name",font=('Arial',11,'bold'),bg='white')
    dnamelabel.grid(row=7,column=0,sticky='w',padx=10)
    dnamee=Entry(frame1,width=35,font=('Arial',11),bg='white')
    dnamee.grid(row=8,column=0,sticky='w',padx=10)

    dnamebutton=Button(frame1,text='Assign Deliveryman\'s Id & Name',cursor='hand2',
                        bg='green',fg='black',bd=0,command=assigndname)
    dnamebutton.grid(row=9,column=0,pady=15)

    statuslabel=Label(frame2,text='Delivery Status',font=('Arial',11,'bold'))
    statuslabel.grid(row=7,column=0,sticky='w',padx=10)
    dstatuse=Entry(frame2,width=35,font=('Arial',11),bg='white')
    dstatuse.grid(row=8,column=0,sticky='e',padx=10)

    confirmbutton=Button(frame2,text='Confirm',font=('Arial',11,'bold'),cursor='hand2',bg='white',fg='green',command=lambda: delivery_detail(rnamee,rmobilee,rdatee,dstatuse,dnamee))
    confirmbutton.grid(row=9,column=0,padx=10,pady=10,sticky='ew')

    delivery_window.mainloop()