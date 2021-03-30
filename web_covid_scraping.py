
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()
w=450
h=400
x=screen_w/3
y=screen_h/3
root.geometry("%dx%d+%d+%d" %(w,h,x,y))
root.configure(bg="#FFC300")
root.title("Covid-Informatica")
text_font="COMIC SANS MS"
tc=tk.Label(root,bg="#FFC300")
tc.grid(row=3,column=0)

def get_info():
    global tc
    data=[]
    tc.grid_forget()
    try:
        country=str(entry.get()).lower()
        url_c="https://www.worldometers.info/coronavirus/country/"+country+"/"
        contents_c=requests.get(url_c)
        page_source_c=contents_c.content
        soup_c=BeautifulSoup(page_source_c,'html.parser')
        div_tag=soup_c.find_all("div",class_="maincounter-number")
        for i in div_tag:
            g=i.find("span")
            data.append(g.string)
        lf=tk.LabelFrame(root,text="",bd=6,font=(text_font,18),bg="#FF5733")
        lf.place(x=16,y=180,width=420)
        tc=tk.Label(lf,text="Total Covid Cases : "+ data[0]+"\n"+"Total Deaths : "+ data[1]+"\n"+"Total Recovered : "+ data[2],font=(text_font,20),bg="#FF5733",padx=6)
        tc.grid(row=0,column=0)
    except IndexError:
        messagebox.showerror("Error","Country Unrecognised!!")
        lf=tk.LabelFrame(root,text="",bd=6,font=(text_font,18),bg="#FFC300")
        lf.place(x=16,y=180,width=420)

  
title=tk.Label(root,text="COVID-INFORMATICA",font=(text_font,24),padx=14,pady=6,bg="#FF5733",width=21).grid(row=0,column=0,columnspan=3)
name=tk.Label(root,text="Country Name :",font=(text_font,18),pady=5,bg="#FFC300").grid(row=1,column=0)
entry=tk.Entry(root,width=25,borderwidth=3)
entry.grid(row=1,column=1)
button=tk.Button(root,text="Search",command=lambda:get_info(),width=10,borderwidth=3,font=(text_font,10),pady=5,bg="#C70039",activebackground="#FF5733").grid(row=2,column=0,columnspan=3)
root.mainloop()