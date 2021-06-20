import requests
import json
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x200")
root.title("Weather Report")
root.configure(bg="#F7E7A8")

def get_weather():
    API_KEY="e24f7cd595a39b532bc10eb6e837d5da"
    try:
        city=e.get()
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res=requests.get(url)
        json_data=json.loads(res.text)
        des=json_data["weather"][0]["description"]
    except Exception:
        messagebox.showerror("Error","Please enter proper city name !")
    else:
        root1=Tk()
        root1.geometry("500x200")
        root1.title("Weather Data")
        root1.configure(bg="#F7E7A8")
        des=json_data["weather"][0]["description"]
        temp=json_data["main"]["temp"]
        hum=json_data["main"]["humidity"]
        speed=json_data["wind"]["speed"]
        pres=json_data["main"]["pressure"]
        Label(root1,text=des,font=("Franklin Gothic Medium",30),fg="#91C8AE",bg="#F7E7A8").pack(padx=5)
        m=Message(root1,text="Temparature(C)  "+str(temp)+"\n"+"Humidity(%)  "+str(hum)+"\n"+"Wind Speed(m/s)  "+str(speed)+"\n"+"Pressure(hpa)  "+str(pres),font=("Franklin Gothic Medium",15),justify=CENTER,fg="#F76C66",bg="#F7E7A8")
        m.pack(padx=5,pady=5)
    
    
Label(root,text="Weather Report",font=("Franklin Gothic Medium",30),fg="#91C8AE",bg="#F7E7A8").place(x=110,y=10)
Label(root,text="Enter City Name",font=("Franklin Gothic Medium",20),fg="#F76C66",bg="#F7E7A8").place(x=30,y=70)
city_name=StringVar()
e=Entry(root,width=27,bd=3,textvariable=city_name)
e.place(x=280,y=77)
b=Button(root,text="Get Data",font=("Franklin Gothic Medium",15),bg="#91C8AE",fg="#F7E7A8",command=get_weather)
b.place(x=200,y=130)
root.mainloop()





