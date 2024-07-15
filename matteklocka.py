import pygame
import random
import datetime
import tkinter as tk
from tkinter import *

#Ljud
pygame.init()
pygame.mixer.music.load("Alarm-ringtone/ringtone.wav")
ljud = pygame.mixer.music.play
ljudav = pygame.mixer.music.stop

#Frågor och svar
mattetal = [" 1 * 1 = "," 2 * 2 = "," 3 * 3 = "," 3 * 9 = "," (6^2) * 2) = "," (5 / 2) + 0.5 = "," (49/7) + (15/3) = "]
mattesvar = ["1","4","9","27","72","3","12"]
slumpa = random.choice(mattetal)
antalratt = 0


#Gui
window = tk.Tk()
window.title("<Matteklocka by Samuel")
window.configure(bg="black")
window.attributes("-fullscreen",True)


#Rutor i gui
klocka = tk.Label(
    text=window,
    font=("Arial",80),
    fg="red",
    bg="black")
fraga = tk.Label(
    text = slumpa,
    font=("Arial",42),
    bg="white",)
varde = tk.Entry(
    bg="white",
    font=("Arial",21))
output = tk.Label(
    font = ("Arial",15))
setlarm = tk.Entry(bg="white",font=("Arial",20))
larm1 = tk.Label(bg="red", text = "doiwajdaij")
larm2 = tk.Label(bg="orange", text = "awdaoiwdjO")
mellanrum = tk.Label(bg="black",height=7)


#Enter knapp och ruta
def get_data(event):
    global slumpa
    global antalratt
    pos = int(mattetal.index(slumpa))
    rattsvar = mattesvar[pos]
    output.config(text = varde.get())
    svar = varde.get()
    if svar == rattsvar:
        antalratt += 1
        slumpa = random.choice(mattetal)
        fraga["text"] = slumpa
        if antalratt == 3:
            output.config(text = "Rätt!")
            fraga["text"] = "Godmorgon!"
varde.bind("<space>",get_data)

            

#Shutdown
def close_win(e):
    window.destroy()
window.bind("<Tab>", lambda e: close_win(e))
 

#Tid
tidnu = datetime.datetime.now()
def digitalclock():
    nu = datetime.datetime.now()
    tid = [len(str(nu.hour)) % 2 * "0" + str(nu.hour),":",len(str(nu.minute)) % 2 * "0" + str(nu.minute), ":",len(str(nu.second)) % 2 * "0" + str(nu.second)]
    klocka.config(text = tid)
    klocka.after("200",digitalclock)
alarm = [0,0]
   
tidnu2 = datetime.datetime.now()
timimorn = 0
minimorn = tidnu.minute
tidimorn = tidnu + datetime.timedelta(days=1)
printtimme = str(alarm[0])
printminut = str(alarm[1])

#Set alarm
startprogram = 0
def set_time(event):
    global startprogram
    if startprogram == 1:
        alarm[1] = int(setlarm.get())
        larm2.config(text = alarm[1])
        startprogram = 2
        setlarm.delete(0,END)
        setlarm.destroy()
    if startprogram == 0:
        alarm[0] = int(setlarm.get())
        larm1.config(text = alarm[0])
        startprogram = 1
        setlarm.delete(0,END)
setlarm.bind("<space>",set_time)

#Saker i GUI
mellanrum.grid(row=0)
enter = tk.Button(window,text = "Enter", command = get_data, bg="yellow")
lämna = tk.Button(window,text = "Quit", command = window.destroy)
klocka.grid(column = 0, row=1, columnspan = 2,padx=20)
#lämna.grid(column = 2, row = 0, columnspan = 1)
digitalclock()
setlarm.grid(column=0,row=2,columnspan=2,pady=10)
#larm1.grid(column=0,row=2,columnspan=1)
#larm2.grid(column=1,row=2,columnspan=1)
setlarm.focus_force()

def aktiveralarm():
    global startprogram
    waitlarm = tk.Label(text = ("Väntar på larm vid " + len(str(alarm[0])) % 2 * "0" + str(alarm[0]) + ":" + len(str(alarm[1])) % 2 * "0" + str(alarm[1]) + "..."), font=("Arial",35), fg="darkGrey",bg="black")
    if startprogram != 3 or startprogram != 4:
        waitlarm.grid(column=0,row=3,columnspan=2)
    tidnu = datetime.datetime.now()
    print(tidnu.hour,":",tidnu.minute,":",tidnu.second)
    if alarm[0] >= tidnu.hour and alarm[1] >= tidnu.minute:
        varde.focus_force()
        if (alarm[0] <= tidnu.hour and alarm[1] <= tidnu.minute) or (alarm[0] < tidnu.hour):
            startprogram = 3
            setlarm.destroy()
            larm1.destroy()
            larm2.destroy()
            fraga.grid(column=0, row=2, columnspan=1, pady=10, padx=10)
            varde.grid(column=1, row =2, columnspan=1,pady=10, padx=10)
            
            if output["text"] != "Rätt!":
                ljud(10000000)
            else:
                ljudav()              
                
    elif tidimorn.day <= tidnu2.day:
            varde.focus_force()
            if (alarm[0] <= tidimorn.hour and alarm[1] <= tidimorn.minute) or (alarm[0] < tidimorn.hour):
                startprogram = 4
                fraga.grid(column=0, row=2, columnspan=1, pady=10, padx=10)
                varde.grid(column=1, row=2, columnspan=1,pady=10, padx=10)
                if output["text"] != "Rätt!":
                    ljud(1000000000)
                else:
                    ljudav()
    
    window.after(1000,aktiveralarm)
  
window.after(100,aktiveralarm)
window.lift()
window.mainloop()
ljudav()

