from tkinter import *
import base64
from tkinter import messagebox

root=Tk()
root.geometry("500x300")
root.configure(bg="#ECF0F1")
root.title("Message Encode and Decode")

def e():
    root.destroy()
    
def r(message,mode):
    if mode=='e':
        message=str(entry1.get()).strip()
        m_in_bytes=message.encode("ascii")
        base64_bytes=base64.b64encode(m_in_bytes)
        encoded=base64_bytes.decode("ascii")
        entry3.insert(END,encoded)
    elif mode=='d':
        message=str(entry1.get()).strip()
        m_in_bytes=message.encode("ascii")
        base64_bytes=base64.b64decode(m_in_bytes)
        decoded=base64_bytes.decode("ascii")
        entry3.insert(END,decoded)
    else:
        messagebox.showerror("error","Error occured!!!, Try Excecuting Again")

def r1():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    
main_heading=Label(root,text="ENCODE DECODE",font=("Book Antiqua",25),padx=109,pady=10).grid(row=0,column=0,columnspan=3)
heading1=Label(root,text="Message",font=("Book Antiqua",20)).grid(row=1,column=0)
entry1=Entry(root,width=25)
entry1.grid(row=1,column=1)
heading2=Label(root,text="Mode\n(e-encode,d-decode)",font=("Book Antiqua",20)).grid(row=2,column=0)
entry2=Entry(root,width=25)
entry2.grid(row=2,column=1)
entry3=Entry(root,width=60)
Label(root,text="",bg="#ECF0F1").grid(row=3,column=0)
entry3.grid(row=4,column=0,columnspan=3)
buttons_together=Frame(root,width=200,height=50,bg="white")
buttons_together.place(x=160,y=230)
button_exit=Button(buttons_together,text="Exit",bg="#E74C36",command=lambda:e(),font=("Book Antiqua",15)).grid(row=0,column=0)
button_result=Button(buttons_together,text="Result",bg="#FFFB71",command=lambda:r(entry1.get().lower(),entry2.get().lower()),font=("Book Antiqua",15)).grid(row=0,column=1)
button_reset=Button(buttons_together,text="Reset",bg="#97EA76",command=lambda:r1(),font=("Book Antiqua",15)).grid(row=0,column=2)

root.mainloop()

