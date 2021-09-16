from tkinter import *
import tkinter as tk
import os
import time
from pydub import AudioSegment
from pydub.playback import play
import pygame


top = Tk()
top.geometry("500x500")

top.title("PINGPONG (CGA project by Rajeev)")
#top.configure(bg='white')
bg = PhotoImage(file = "pingpong.gif")
label1 = Label( top, image = bg)
label1.place(x = 0, y = 0)
  



pygame.mixer.init()
crash_sound = pygame.mixer.Sound("island-ncs-best-of.wav")
crash_sound.play()

T = Text(top, height = 5, width = 52) 
  
# Create label 
l = Label(top, text = "Ping Pong") 
l.config(font =("Azonix", 25)) 



p = Label(top, text = "Live Long and Play Ping Pong") 
p.config(font =("Abadi", 9))
 

'''

e1 = tk.Entry(top)
e2 = tk.Entry(top)
tk.Label(top, text="Player 1").place(relx=0.3, rely=0.3, anchor=CENTER)
e1.place(relx=0.5, rely=0.3, anchor=CENTER)
tk.Label(top, text="Player 2").place(relx=0.3, rely=0.4, anchor=CENTER)
e2.place(relx=0.5, rely=0.4, anchor=CENTER)
'''




def hello():
   

   os.system('python main.py')
  

   






photo = PhotoImage(file = r"invader.gif")
  
# Resizing image to fit on button
photoimage = photo.subsample(3, 3)
  
B1 = Button(top, text = "Start game", command = hello,image = photoimage,compound = LEFT,fg="red", height=100, width=100)
#B1.place(x = 210,y = 150)
B1.place(relx=0.5, rely=0.6, anchor=CENTER)

l.pack(pady=20)
p.pack()

top.mainloop()