#importing tkinter module
from tkinter import *

#creating a window
root=Tk()
root.configure(bg="#F9F0A4")

root.title("Currency-Converter")

#setting up the options of the drop down menu
list_2=["AMERICAL DOLLAR",
        "YEN",
        "EURO",
        "BITCOIN",
        "SAUDI RIYAL"]
list_1=["INDIAN RUPEE"]

#defining a function to perform convert button operation
def convert(num):
    y=float(amount1.get())
    x=clicked2.get()
    
    if x == list_2[0]:
        amount2.delete(0,END)
        current2=0.014*y
        amount2.insert(0,round(float(current2),4))
        
    elif x == list_2[1]:
        amount2.delete(0,END)
        current2=1.43*y
        amount2.insert(0,round(float(current2),4))
        
    elif x == list_2[2]:
        amount2.delete(0,END)
        current2=0.012*y
        amount2.insert(0,round(float(current2),4))
        
    elif x == list_2[3]:
        amount2.delete(0,END)
        current2=0.0000013*y
        amount2.insert(0,round(float(current2),4))
        
    else:
        x == list_2[4]
        amount2.delete(0,END)
        current2=0.051*y
        amount2.insert(0,round(float(current2),4))


#first label for the title of the project    
mylabel=Label(root,text="WELCOME TO CURRENCY CONVERTER",anchor=CENTER,borderwidth=20,fg="black",bg="#36F5E9")
#mylabel.config(width=40)
mylabel.config(font=("Cooper Black", 25))
mylabel.grid(row=0,column=0,columnspan=3)

#creating a label
label_left=Label(root,text="CURRENCY 1",borderwidth=25,fg="black",bg="#FF9DC7")
label_left.config(font=("Arial Black",15))
label_left.config(width=19)
label_left.grid(row=2,column=0)
#creating a label
label_right=Label(root,text="CURRENCY 2",borderwidth=25,fg="black",bg="#FF9DC7")
label_right.config(font=("Arial Black",15))
label_right.config(width=19)

label_right.grid(row=2,column=2)

#creating drop down menu
clicked1=StringVar()
dropdown_left=OptionMenu(root,clicked1,*list_1)
dropdown_left.grid(row=4,column=0)
clicked1.set("INDIAN RUPEE")
clicked2=StringVar()
dropdown_right=OptionMenu(root,clicked2,*list_2)
dropdown_right.grid(row=4,column=2)
clicked2.set("AMERICAN DOLLAR")
nil=Label(root,text="",borderwidth=10,bg="#F9F0A4")
nil.grid(row=5,column=0,columnspan=3)

#creating an entry widget to get values from the user
amount1=Entry(root,width=20,borderwidth=3)
amount1.grid(row=6,column=0)

amount2=Entry(root,width=20,borderwidth=3)
amount2.grid(row=6,column=2)

num=amount1.get()

nil2=Label(root,text="",borderwidth=10,bg="#F9F0A4")
nil2.grid(row=7,column=0,columnspan=3)

#creating a button for converting the currencies
convert_button=Button(root,text="CONVERT",command=lambda:convert(num),width=10,height=2,fg="black",bg="#9BF794")

convert_button.grid(row=8,column=1)

root.mainloop()
              
