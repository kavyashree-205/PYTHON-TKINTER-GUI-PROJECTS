from tkinter import *

from tkinter import messagebox

import os

def register_user():
    username_info=username.get() 
    password_info=password.get()
    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    u_entry.delete(0, END)
    p_entry.delete(0, END)
    messagebox.showinfo("info","Registration Successful")
    
def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    u_entry1.delete(0, END)
    p_entry1.delete(0, END)
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            messagebox.showinfo("info","Login Successfull!!")
        else:
            messagebox.showinfo("info","Password has not been recognised")
    else:
        messagebox.showinfo("info","User not found")

def register():
    global username,password
    global u_entry,p_entry,root1
    root1=Toplevel(root)
    username=StringVar()
    password=StringVar()
    root1.title("Register")
    root1.configure(bg="#F1C40F")
    w1=350
    h1=310
    root1.geometry("%dx%d+%d+%d" %(w1,h1,x,y))
    Label(root1,text="Please enter the details below\nin the given empty fields",font=("Georgia",15),bg="#F9E79F").pack()
    Label(root1,text="",bg="#F1C40F").pack()
    Label(root1,text="Username *",font=("Georgia",15),bg="#F9E79F").pack()
    Label(root1,text="",bg="#F1C40F").pack()
    u_entry=Entry(root1,textvariable=username,width="15",borderwidth=3)
    u_entry.pack()
    Label(root1,text="",bg="#F1C40F").pack()
    Label(root1,text="Password *",font=("Georgia",15),bg="#F9E79F").pack()
    Label(root1,text="",bg="#F1C40F").pack()
    p_entry=Entry(root1,textvariable=password,width="15",borderwidth=3)
    p_entry.pack()
    Label(root1,text="",bg="#F1C40F").pack()
    button=Button(root1,text="Register",width=10,command=lambda:register_user(),bg="#F9E79F",font=("Georgia",12)).pack()
    root1.mainloop()

def login():
    global root2,u_entry1,p_entry1
    global username_verify,password_verify
    username_verify=StringVar()
    password_verify=StringVar()
    root2=Toplevel(root)
    w2=350
    h2=250
    root2.geometry("%dx%d+%d+%d" %(w2,h2,x,y))
    root2.configure(bg="#AF7AC5")
    root2.title("Login")
    Label(root2,text="Username",bg="#D7BDE2",font=("Georgia",17)).pack()
    Label(root2,text="",bg="#AF7AC5").pack()
    u_entry1=Entry(root2,textvariable=username_verify,width=15,borderwidth=3)
    u_entry1.pack()
    Label(root2,text="",bg="#AF7AC5").pack()
    Label(root2,text="Password",bg="#D7BDE2",font=("Georgia",17)).pack()
    Label(root2,text="",bg="#AF7AC5").pack()
    p_entry1=Entry(root2,textvariable=password_verify,width=15,borderwidth=3)
    p_entry1.pack()
    Label(root2,text="",bg="#AF7AC5").pack()
    button1=Button(root2,text="Login",width=10,command=lambda:login_verify(),bg="#D7BDE2",font=("Georgia",13)).pack()
    root2.mainloop()
    
def mainscreen():
    global root,screen_w,screen_h,x,y
    root=Tk()
    screen_w=root.winfo_screenwidth()
    screen_h=root.winfo_screenheight()
    w=350
    h=200
    x=screen_w/2.7
    y=screen_h/2.7
    root.geometry("%dx%d+%d+%d" %(w,h,x,y))
    root.title("Register-Login")
    root.configure(bg="#1ABC9C")
    heading=Label(root,text="Register/Login Form",font=("Georgia",18),bg="#A3E4D7").pack()
    Label(root,text="",bg="#1ABC9C").pack()
    login_button=Button(root,text="Login",width="300",font=("Georgia",15),bg="#A3E4D7",command=lambda:login()).pack()
    Label(root,text="",bg="#1ABC9C").pack()
    register_button=Button(root,text="Register",width="300",font=("Georgia",15),bg="#A3E4D7",command=lambda:register()).pack()
    Label(root,text="",bg="#1ABC9C").pack()
    root.mainloop()
mainscreen()
