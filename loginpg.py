from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def hide():
   closeye.config(file='closeye.png')
   passworde.config(show='*')
   eyeButton.config(command=show)

def show():
   closeye.config(file='openeye.png')
   passworde.config(show='')
   eyeButton.config(command=hide)

def user_enter(event):
    if usernamee.get()=='Username':
        usernamee.delete(0,END)    

def password_enter(event):
    if passworde.get()=='Password':
        passworde.delete(0,END) 

def forgetpwd() :
    messagebox.showinfo("Please Remember","Your password is admin") 

def gotoadminpg() :
    if((usernamee.get()=='admin') and (passworde.get()=='admin')) :
        login_window.destroy()
        import adminpg
    else :
        messagebox.showerror("Login Error","Invalid Username or Password")
    


login_window=Tk()
login_window.title('Login Page')
login_window.geometry("990x660")
login_window.resizable(0,0)
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='ADMIN LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=600,y=120)

usernamee=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernamee.place(x=580,y=200)
username = StringVar()
usernamee.insert(0,'Username')
usernamee.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passworde=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passworde.place(x=580,y=260)
password = StringVar()
passworde.insert(0,'Password')
passworde.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)
closeye=PhotoImage(file="closeye.png")
eyeButton=Button(login_window,image=closeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
hide()
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',
                    font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',activeforeground='dodgerblue2',command=forgetpwd)
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='Login',cursor='hand2',
                    font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='green',bd=0,width=19,command=gotoadminpg)
loginButton.place(x=578,y=350)

orlabel=Label(login_window,text='........................................',font=('Open Sans',16),fg='firebrick1')
orlabel.place(x=583,y=400)
facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo)
fbLabel.place(x=635,y=440)
twitter_logo=PhotoImage(file='twitter.png')
tweetLabel=Label(login_window,image=twitter_logo)
tweetLabel.place(x=690,y=440)
google_logo=PhotoImage(file='google.png')
glLabel=Label(login_window,image=google_logo)
glLabel.place(x=740,y=440)
login_window.mainloop()