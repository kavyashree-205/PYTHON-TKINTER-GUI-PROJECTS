from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("TIC-TAC-TOE GAME")
root.configure(bg="#FFEE98")
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()
w=600
h=700
x=screen_w/3
y=screen_h/3
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
clicked=True
count=0
winner=False
entry1=Entry(root,width=30,borderwidth=3)
entry1.grid(row=1,column=1)
entry2=Entry(root,width=30,borderwidth=3)
entry2.grid(row=2,column=1)
i=str(entry1.get())
j=str(entry2.get())
def b_disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    
def check_win():
    global winner
    global i,j
    i=str(entry1.get())
    j=str(entry2.get())
    if (b1["text"]==i[0] and b2["text"]==i[0] and b3["text"]==i[0] or b4["text"]==i[0] and b5["text"]==i[0] and b6["text"]==i[0] or
        b7["text"]==i[0] and b8["text"]==i[0] and b9["text"]==i[0] or b1["text"]==i[0] and b4["text"]==i[0] and b7["text"]==i[0] or
        b2["text"]==i[0] and b5["text"]==i[0] and b8["text"]==i[0] or b3["text"]==i[0] and b6["text"]==i[0] and b9["text"]==i[0] or
        b1["text"]==i[0] and b5["text"]==i[0] and b9["text"]==i[0] or b3["text"]==i[0] and b5["text"]==i[0] and b7["text"]==i[0]):
        win="Congradulations "+str(entry1.get().lower())+" you won the game !!"
        messagebox.showinfo("tic-tac-toe",win)
        b_disable()
        winner=True
    elif (b1["text"]==j[0] and b2["text"]==j[0] and b3["text"]==j[0] or b4["text"]==j[0] and b5["text"]==j[0] and b6["text"]==j[0] or
        b7["text"]==j[0] and b8["text"]==j[0] and b9["text"]==j[0] or b1["text"]==j[0] and b4["text"]==j[0] and b7["text"]==j[0] or
        b2["text"]==j[0] and b5["text"]==j[0] and b8["text"]==j[0] or b3["text"]==j[0] and b6["text"]==j[0] and b9["text"]==j[0] or
        b1["text"]==j[0] and b5["text"]==j[0] and b9["text"]==j[0] or b3["text"]==j[0] and b5["text"]==j[0] and b7["text"]==j[0]):
        win1="Congradulations "+str(entry2.get().lower())+" you won the game !!"
        messagebox.showinfo("tic-tac-toe",win1)
        b_disable()
        winner=True
    else:
        if(count==9 and winner==False):
            messagebox.showinfo("tic-tac-toe","IT'S A DRAW MATCH !!")
            b_disable()
    
def b_click(b):
    global clicked
    global count
    global i,j
    i=str(entry1.get())
    j=str(entry2.get())
    if (str(entry1.get())=="" or str(entry2.get()) == ""):
        messagebox.showerror("Error","Please enter the player names")
    if b["text"]==" " and clicked==True :
        i=str(entry1.get())
        b["text"]=i[0]
        b.config(bg="#FF7D66")
        clicked=False
        count=count+1
        check_win()
        
    elif b["text"]==" " and clicked==False :
         j=str(entry2.get())
         b["text"]=j[0]
         b.config(bg="#6AF576")
         clicked=True
         count=count+1
         check_win()
    else:
        messagebox.showerror("ERROR","The button is already clicked")
title=Label(root,text="Tic-Tac-Toe Game",font=("Arial Black",30),fg="black",padx=100,pady=10,bg="#FFEE98").grid(row=0,column=0,columnspan=2)
name1=Label(root,text="Name of Player 1 : ",font=("Arial Black",20),bg="#FFEE98").grid(row=1,column=0)
name2=Label(root,text="Name of Player 2 : ",font=("Arial Black",20),bg="#FFEE98").grid(row=2,column=0)
button_frame=Frame(root,bd=5,relief=GROOVE,bg="black")
button_frame.place(x=109,y=185,width=388,height=445)

b1=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b1))
b2=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b2))
b3=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b3))
b4=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b4))
b5=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b5))
b6=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b6))
b7=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b7))
b8=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b8))
b9=Button(button_frame,text=" ",font=("ArialBlack",25),height=3,width=6,bd=3,bg="SystemButtonFace",command=lambda:b_click(b9))

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
root.mainloop()
