from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from datetime import date
import ttkbootstrap as tb
import delivery
from ttkbootstrap.scrolled import ScrolledText
import dbcon



def cus_detail(cide,cnamee,cmobilee,caddresse):
    
    cname=cnamee.get()
    cmobile=cmobilee.get()
    caddress=caddresse.get()
    dbcon.customercon(cname,cmobile,caddress)
    t=dbcon.selcid(cname)
    cide.insert(1,t[0][0])

def pack_detail(cnamee,pide,weighte,dlocatione,descriptione,sentdatee):
    cname=cnamee.get()
    cid=dbcon.selcid(cname)
    weight=weighte.get()
    dlocation=dlocatione.get()
    description=descriptione.get()
    sdate=sentdatee.get()
    dbcon.packcon(cid[0][0],weight,dlocation,description,sdate)
    k=dbcon.selpid(cid[0][0])
    pide.insert(1,k[0][0])

    
    

"""def receiver_detail(rname,raddress,rmobile):
    rname=rnamee.get()
    raddress=raddresse.getvar()
    rmobile=rmobilee.get()
    query = "INSERT INTO packet (receiver_name,delivery_location,receiver_mobile) values('{0}','{1}','{2}')".format(rname,raddress,rmobile)
    cursor.execute(query)
    cursor.fetchall()
    messagebox.showinfo("Sucessful", "you are added !")
    conn.commit()"""

def sdatey() :
    sentdatee.delete(0,'end')
    sentdatee.insert('end',sentdate.entry.get())

customer_window=Tk()
customer_window.title('Customer Info Page')
customer_window.geometry("1200x660")
bgImage=ImageTk.PhotoImage(file='tableframe.jpg')

bgLabel=Label(customer_window,image=bgImage)
bgLabel.grid()
frame1=Frame(customer_window,bg='white')
frame1.place(x=273,y=40)
frame2=Frame(customer_window,bg='white')
frame2.place(x=623,y=182)

cnamel=Label(frame1,text='Customer Name',font=('Arial',11,'bold'),bg='white')
cnamel.grid(row=0,column=0,sticky='w',padx=10)
cnamee=Entry(frame1,width=35,font=('Arial',11),bg='white')
cnamee.grid(row=1,column=0,sticky='w',padx=10)

caddressl=Label(frame1,text='Customer Address',font=('Arial',11,'bold'),bg='white')
caddressl.grid(row=2,column=0,sticky='w',padx=10)
caddresse=Entry(frame1,width=35,font=('Arial',11),bg='white')
caddresse.grid(row=3,column=0,sticky='w',padx=10)

cmobilel=Label(frame1,text='Customer Mobile No',font=('Arial',11,'bold'),bg='white')
cmobilel.grid(row=4,column=0,sticky='w',padx=10)
cmobilee=Entry(frame1,width=35,font=('Arial',11),bg='white')
cmobilee.grid(row=5,column=0,sticky='w',padx=10)

cidl=Label(frame1,text='Customer Id',font=('Arial',11,'bold'),bg='white')
cidl.grid(row=6,column=0,sticky='w',padx=10)
cide=Listbox(frame1,width=35,height=1,font=('Arial',11),bg='white')
cide.grid(row=7,column=0,sticky='w',padx=10)
cidbutton=Button(frame1,text='Generate Customer Id',font=('Arial',11),cursor='hand2',
                    bg='green',fg='black',bd=0,command=lambda:cus_detail(cide,cnamee,cmobilee,caddresse))
cidbutton.grid(row=8,column=0,pady=15)

pidlabel=Label(frame1,text='Packet Id',font=('Arial',11,'bold'),bg='white')
pidlabel.grid(row=9,column=0,sticky='w',padx=10)
pide=Entry(frame1,width=35,font=('Arial',11),bg='white')
pide.grid(row=10,column=0,sticky='w',padx=10)
pidbutton=Button(frame1,text='Generate Packet Id',font=('Arial',11),cursor='hand2',
                    bg='green',fg='black',bd=0,command=lambda:pack_detail(cnamee,pide,weighte,dlocatione,descriptione,sentdatee))
pidbutton.grid(row=11,column=0,pady=15)

sentdatelabel=tb.Label(frame2,text='Sent Date',font=('Arial',11,'bold'))
sentdatelabel.grid(row=0,column=0,sticky='w',padx=10)

dt2=date(2023, 12, 30)
sentdate=tb.DateEntry(frame2,dateformat="%y-%m-%d",startdate=dt2)
sentdate.grid(row=1,column=0,padx=10,sticky='e')
sentdatee=Entry(frame2,width=14,font=('Arial',11),bg='white')
sentdatee.grid(row=1,column=0,sticky='w',padx=10)
sentdatebutton=tb.Button(frame2,text='click to confirm date',cursor='hand2',command=lambda: sdatey())
sentdatebutton.grid(row=2,column=0,pady=15)

descriptionlabel=Label(frame2,text='Description',font=('Arial',11,'bold'),bg='white')
descriptionlabel.grid(row=3,column=0,sticky='w',padx=10)
descriptione=Entry(frame2,width=35,font=('Arial',11),bg='white')
descriptione.grid(row=4,column=0,sticky='w',padx=10)

dlocationl=Label(frame2,text='Delivery Address',font=('Arial',11,'bold'),bg='white')
dlocationl.grid(row=5,column=0,sticky='w',padx=10)
dlocatione=Entry(frame2,width=35,font=('Arial',11),bg='white')
dlocatione.grid(row=6,column=0,sticky='w',padx=10)

weightlabel=Label(frame2,text='Weight',font=('Arial',11,'bold'),bg='white')
weightlabel.grid(row=7,column=0,sticky='w',padx=10)
weighte=Entry(frame2,width=35,font=('Arial',11),bg='white')
weighte.grid(row=8,column=0,sticky='w',padx=10)

def gotodeliverypg() :
    #messagebox.showinfo("Success","Details were updated")
    cname=cnamee.get()
    customer_window.destroy()
    delivery.dpage(cname)

NextButton=Button(frame2,text='Next',cursor='hand2',
                    font=('Open Sans',16,'bold'),bg='white',fg='black',bd=0,width=10,command=gotodeliverypg)
NextButton.grid(row=9,column=0,padx=85,pady=30)

customer_window.mainloop()