from tkinter import *
root=Tk()
root.title("FLAMES")
root.geometry("400x450")
root.configure(bg="#FDC6C0")
flames_list=["Friends","Love","Affection","Marriage","Enemy","Siblings"]
display=Label(root,bg="#FDC6C0")
display.grid(row=5,column=0,columnspan=3)

def check(you,them):
    global display
    global flames_list
    display.grid_forget()
    you=str(entry1.get()).lower().replace(" ","")
    them=str(entry2.get()).lower().replace(" ","")
    list1=[]
    list2=[]
    for i in range(len(you)):
        list1.append(you[i])
    for j in range(len(them)):
        list2.append(them[j])
    k=(len(you)+len(them))/2
    while k>0:
        for n in list1:
            if n in list2:
                list1.remove(n)
                list2.remove(n)
                k=k-1
            else:
                k=k-1
    count=len(list1)+len(list2)
    if (count==0)or(count==10):
        display=Label(root,text="LOVE :)",bg="#FDC6C0",fg="#8B0000",borderwidth=10)
        display.config(font=("Forte",23))
        display.grid(row=5,column=0,columnspan=3)
        
    elif (count==8)or(count==12)or(count==13)or(count==28)or(count==30):
        display=Label(root,text=flames_list[2]+" :)",bg="#FDC6C0",fg="#8B0000",borderwidth=10)
        display.config(font=("Forte",23))
        display.grid(row=5,column=0,columnspan=3)
        
    elif (count==5)or(count==3)or(count==14)or(count==16)or(count==18)or(count==21)or(count==23):
        display=Label(root,text=flames_list[0]+" :D",bg="#FDC6C0",fg="#8B0000",borderwidth=10)
        display.config(font=("Forte",23))
        display.grid(row=5,column=0,columnspan=3)
        
    elif (count==2)or(count==4)or(count==7)or(count==9)or(count==20)or(count==22)or(count==24)or(count==25):
        display=Label(root,text=flames_list[4]+" :(",bg="#FDC6C0",fg="#8B0000",borderwidth=10)
        display.config(font=("Forte",23))
        display.grid(row=5,column=0,columnspan=3)
        
    elif (count==1)or(count==17)or(count==19)or(count==27)or(count==29):
        display=Label(root,text=flames_list[5],bg="#FDC6C0",fg="#8B0000",borderwidth=10)
        display.config(font=("Forte",23))
        display.grid(row=5,column=0,columnspan=3)
        
    elif (count==6)or(count==11)or(count==15)or(count==26):
        display=Label(root,text=flames_list[3],bg="#FDC6C0",fg="#8B0000",borderwidth=10)
        display.config(font=("Forte",23))
        display.grid(row=5,column=0,columnspan=3)
        
    else :
        display=Label(root,text=random.choice(flames_list),bg="#FDC6C0",fg="#8B0000",borderwidth=10)
        display.config(font=("Consolas",23))
        display.grid(row=5,column=0,columnspan=3)     
        
        
title=Label(root,text="F . L . A . M . E . S",bg="#FDC6C0",fg="#CD0000")
title.config(font=("Forte",38))
title.grid(row=0,column=0,columnspan=3)

heading1=Label(root,text="Please  enter  the  names",borderwidth=10,bg="#FDC6C0",fg="#8B0000")
heading1.config(font=("Forte",23))
heading1.grid(row=1,column=0,columnspan=3)
heading2=Label(root,text="you  are  intrested  in  !!!",bg="#FDC6C0",fg="#8B0000")
heading2.config(font=("Forte",23))
heading2.grid(row=2,column=0,columnspan=3)

name_1=Label(root,text="Name 1 :",borderwidth=20,bg="#FDC6C0",fg="#CD0000")
name_1.config(font=("Forte",20))
name_1.grid(row=3,column=0)
name_2=Label(root,text="Name 2 :",bg="#FDC6C0",borderwidth=20,fg="#CD0000")
name_2.config(font=("Forte",20))
name_2.grid(row=4,column=0)

entry1=Entry(root,borderwidth=3,width=28)
entry1.grid(row=3,column=1)
entry2=Entry(root,borderwidth=3,width=28)
entry2.grid(row=4,column=1)

you=entry1.get()
them=entry2.get()

button=Button(root,text="Check  Flames",bg="#8B0000",fg="white",borderwidth=5,command=lambda:check(you,them))
button.config(font=("Forte",17))
button.grid(row=6,column=0,columnspan=3)
root.mainloop()
