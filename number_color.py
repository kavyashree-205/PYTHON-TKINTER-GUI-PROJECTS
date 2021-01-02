from tkinter import *
import random
from tkinter import messagebox
  
root=Tk()
root.geometry("500x540")
root.title("Number Guessing Using Color ")
random_number=random.randint(1,10)
warm_colors=["#EC4F26","#ED8844","#EEAC31","#EDE61B","#F7F5AA"]
cold_colors=["#ABD140","#73C271","#567CBD","#514DFF"]
heading=Label(root,text="Guess Number\nBetween 1-10",font=("Arial Rounded MT Bold",45),padx=20).grid(row=0,column=0)
space=Label(root,text="",font=("Arial Rounded MT Bold",15)).grid(row=1,column=0)

def background_color():
    global num,diff,result,colour
    num=int(entry.get())
    diff=abs(random_number-num)
    if num/10<=1:
        if diff==0:
            root.configure(bg=warm_colors[0])
            result=Label(root,text="Correct!!!",font=("Arial Rounded MT Bold",30),bg="#EC4F26").place(x=140,y=460)
            heading=Label(root,text="Guess Number\nBetween 1-10",font=("Arial Rounded MT Bold",45),padx=20,bg="#EC4F26").grid(row=0,column=0)
            space=Label(root,text="",font=("Arial Rounded MT Bold",15),bg="#EC4F26").grid(row=1,column=0)
        elif diff==5:
            entry.delete(0,END)
            root.configure(bg="white")
            heading=Label(root,text="Guess Number\nBetween 1-10",font=("Arial Rounded MT Bold",45),padx=20,bg="white").grid(row=0,column=0)
            space=Label(root,text="",font=("Arial Rounded MT Bold",15),bg="white").grid(row=1,column=0)
        elif diff<5:
            entry.delete(0,END)
            root.configure(bg=warm_colors[diff])
            heading=Label(root,text="Guess Number\nBetween 1-10",font=("Arial Rounded MT Bold",45),padx=20,bg=warm_colors[diff]).grid(row=0,column=0)
            space=Label(root,text="",font=("Arial Rounded MT Bold",15),bg=warm_colors[diff]).grid(row=1,column=0)
        elif diff>5:
            entry.delete(0,END)
            root.configure(bg=cold_colors[diff-6])
            heading=Label(root,text="Guess Number\nBetween 1-10",font=("Arial Rounded MT Bold",45),padx=20,bg=cold_colors[diff-6]).grid(row=0,column=0)
            space=Label(root,text="",font=("Arial Rounded MT Bold",15),bg=cold_colors[diff-6]).grid(row=1,column=0)
        else:
            pass
    else:
        messagebox.showerror("error","Please enter digits from 1-10")

entry=Entry(root,borderwidth=1,width=2,font=("Arial Rounded MT Bold",80))
entry.grid(row=2,column=0)
frame=LabelFrame(root,text="",width=100,height=50,bd=5,relief=GROOVE,bg="gray")
frame.place(x=165,y=360)
check_button=Button(frame,text="Check",width=10,font=("Arial Rounded MT Bold",15),command=lambda:background_color(),pady=10,bg="white",activebackground="gray")
check_button.grid(row=0,column=0)
root.mainloop()
