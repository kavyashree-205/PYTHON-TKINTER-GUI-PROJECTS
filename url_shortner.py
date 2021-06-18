import bitly_api
from tkinter import *

root=Tk()
root.geometry("500x300")
root.configure(bg="#DCB9ED")
root.title("Url-Shortener")


def excecute():
    Access_Token="abad8da9a97363b79c4d5068e9d62e3503cbfb5b"
    connect=bitly_api.Connection(access_token=Access_Token)
    url=entry1.get()
    shorten_url=connect.shorten(url)
    entry2.insert(0,shorten_url.get('url'))
   

def clear_all():
    entry1.delete(0,END)
    entry2.delete(0,END)

    
main_heading=Label(root,text="---Url Shortener---",font=("Book Antiqua",25),padx=109,pady=10,fg="#FF00AA",bg="#DCB9ED").pack()
heading1=Label(root,text="Original Url",font=("Book Antiqua",20),fg="#FF00AA",bg="#DCB9ED").pack()
value=StringVar()
entry1=Entry(root,width=25,textvariable=value)
entry1.pack()
heading2=Label(root,text="Shortened Url",font=("Book Antiqua",20),fg="#FF00AA",bg="#DCB9ED").pack()
entry2=Entry(root,width=25)
entry2.pack()

Label(root,text="",bg="#DCB9ED").pack()
btn_frame=Frame(root,bg="#DCB9ED")
btn_frame.pack()
get_url=Button(btn_frame,text="Get Url",bg="#FF00AA",command=lambda:excecute(),font=("Book Antiqua",15),fg="#DCB9ED")
get_url.grid(row=0,column=0,padx=20)
clear=Button(btn_frame,text="Reset",bg="#FF00AA",command=lambda:clear_all(),font=("Book Antiqua",15),fg="#DCB9ED")
clear.grid(row=0,column=1,padx=20)

root.mainloop()
