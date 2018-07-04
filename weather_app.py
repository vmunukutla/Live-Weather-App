import tkinter
from tkinter import *
import weather

top = tkinter.Tk()

def showWeatherCallBack(city, country):
    x = weather.Weather(city.get(), country.get())
    city.delete(0, END)
    country.delete(0, END)
    fiveDay = x.getFiveDay()
    if fiveDay != None:
        newTop = tkinter.Tk()
        frame = Frame(newTop)
        frame.pack()

        for item in fiveDay:
            text = Label(frame, text="High: " + str(item[1])+"\nLow: "+str(item[0]))
            text.pack(side = LEFT)
        newTop.mainloop()

cityLabel = Label(top, text="City")
cityLabel.pack(side=LEFT)
city = Entry(top)
city.pack(side=LEFT)
countryLabel = Label(top, text="Country")
countryLabel.pack(side=LEFT)
country = Entry(top)
country.pack(side=LEFT)
b = tkinter.Button(top, text="Show!", command=lambda:showWeatherCallBack(city, country))
b.pack()

top.mainloop()
