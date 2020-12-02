from tkinter import *

root=Tk()
root.title("BMI CALCULATOR")
root.geometry("400x300")
root.configure(bg="#FFFF99")

title_label=Label(root,text="BMI-CALCULATOR",anchor=CENTER,borderwidth=10,fg="#FF8000",bg="#FFFF99")
title_label.config(font=("Lucida Console",30))
title_label.grid(row=0,column=0,columnspan=5)

weight=Label(root,text="WEIGHT",borderwidth=1,fg="#CC6600",bg="#FFFF99")
weight.config(font=("Lucida Console",20))
weight.grid(row=1,column=0)

nill1=Label(root,text="",borderwidth=4,bg="#FFFF99").grid(row=2,column=0,columnspan=5)

kg=Label(root,text="kgs",fg="#CC6600",bg="#FFFF99")
kg.config(font=("Lucida Console",13))
kg.grid(row=1,column=5)

height=Label(root,text="HEIGHT",borderwidth=15,fg="#CC6600",bg="#FFFF99")
height.config(font=("Lucida Console",20))
height.grid(row=3,column=0)

nill2=Label(root,text="",borderwidth=4,bg="#FFFF99").grid(row=4,column=0,columnspan=5)

slider=Scale(root,from_=20,to=120,orient=HORIZONTAL,bd=3,length=200,tickinterval=20,width=15,fg="#CC6600",bg="#FFFF99",troughcolor="#CC6600")
slider.config(highlightbackground="#FFFF99")
slider.set(60)
slider.grid(row=1,column=1,columnspan=4)

list_feet=[3,4,5,6,7,8]

clicked1=StringVar()
feet_menu=OptionMenu(root,clicked1,*list_feet)
clicked1.set(5)
feet_menu.config(bg="#CC6600",fg="#FFFF99")
feet_menu.config(highlightbackground="#FFFF99")
feet_menu.grid(row=3,column=1)
feet=Label(root,text="feet",borderwidth=5,fg="#CC6600",bg="#FFFF99")
feet.config(font=("Lucida Console",13))
feet.grid(row=3,column=2)

list_inch=[0,1,2,3,4,5,6,7,8,9,10,11,12]
clicked2=StringVar()
inch_menu=OptionMenu(root,clicked2,*list_inch)
clicked2.set(5)
inch_menu.config(bg="#CC6600",fg="#FFFF99")
inch_menu.config(highlightbackground="#FFFF99")
inch_menu.grid(row=3,column=3)
inch=Label(root,text="inches",borderwidth=5,fg="#CC6600",bg="#FFFF99")
inch.config(font=("Lucida Console",13))
inch.grid(row=3,column=4)

def sub(w,h1,h2):
    new=Tk()
    new.title("YOUR BMI RESULTS")
    new.geometry("445x80")
    new.configure(bg="#CC6600")
    w=int(slider.get())
    h1=int(clicked1.get())
    h2=int(clicked2.get())
    a=(h1*12+h2)*0.0254
    result=float(w/(a*a))
    result_label=Label(new,text="YOUR BMI : "+str(round(result,2)),bg="#CC6600",fg="#FFFF99")
    result_label.config(font=("Lucida Console",20))
    result_label.grid(row=0,column=0)
    if result<18.5:
        info_label=Label(new,text="YOU BELONG TO UNDERWEIGHT CATEGORY",bg="#CC6600",fg="#FFFF99")
        info_label.config(font=("Lucida Console",15))
        info_label.grid(row=1,column=0)
    elif 18.5<=result<25:
        info_label=Label(new,text="YOU BELONG TO NORMAL WEIGHT CATEGORY",bg="#CC6600",fg="#FFFF99")
        info_label.config(font=("Lucida Console",15))
        info_label.grid(row=1,column=0)
    elif 25<=result<30:
        info_label=Label(new,text="YOU BELONG TO OVER WEIGHT CATEGORY",bg="#CC6600",fg="#FFFF99")
        info_label.config(font=("Lucida Console",15))
        info_label.grid(row=1,column=0)
    else:
        info_label=Label(new,text="YOU ARE OBESE..NEED TO BURN OUT A LOT!",bg="#CC6600",fg="#FFFF99")
        info_label.config(font=("Lucida Console",15))
        info_label.grid(row=1,column=0)
     
w=slider.get()
h1=clicked1.get()
h2=clicked2.get()

submit=Button(root,text="SUBMIT",command=lambda:sub(w,h1,h2),width=10,borderwidth=5,anchor=CENTER)
submit.configure(bg="#CC6600",fg="#FFFF99")
submit.grid(row=5,column=0,columnspan=5)

root.mainloop()

