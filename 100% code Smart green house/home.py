# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:51:56 2023

@author: admin
"""

import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()



#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))






Height = tk.IntVar()
Weight = tk.IntVar()

def main():
    h = Height.get()
    w = Weight.get()
    

image2 = Image.open('HOME.jpg')
image2 = image2.resize((1500, 700), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



lbl = tk.Label(root, text="Welcome To Plant Species Identification System", font=('Lucida Sans Unicode', 40,' bold ',), height=1, width=48,bg="#B0E0E6",fg="black")
lbl.place(x=0, y=3)


image2 = Image.open('gui.jpg')
image2 = image2.resize((90, 60), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=7, y=8)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=450, y=300)


# logolbl=tk.Label(LabelFrame,bd=0).grid(row=0,columnspan=2,pady=20)
        
# lbluser=tk.Label(LabelFrame,text="Username",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
# txtuser=tk.Entry(LabelFrame,bd=5,textvariable=username,font=("",15),bg="white")
# txtuser.grid(row=1,column=1,padx=20)



        
Login_frame=tk.Frame(root)
Login_frame.place(x=180,y=200)
        

        
lbluser=tk.Label(Login_frame,text="About Us \n At  plant leaf diseases for healthier and more productive crops. \n Always consult with local agricultural extension services or \n plant pathology experts for specific guidance based on the region and plant species..",compound=LEFT,font=("Times new roman", 20, "bold"),bg="darkseagreen2").grid(row=1,column=0,padx=20,pady=10)


Login_frame=tk.Frame(root)
Login_frame.place(x=280,y=400)
        

        
lbluser=tk.Label(Login_frame,text="Get in Touch \n Have questions or feedback? We'd love to hear from you.\n Reach out to our support team at [support@plantleafdisease.com] \n Follow Us \n Stay updated on the latest news and features by following us on \n [Social Media Icons - Twitter, Facebook, LinkedIn].",compound=LEFT,font=("Times new roman", 20, "bold"),bg="darkseagreen2").grid(row=1,column=0,padx=20,pady=10)




#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image



         


root.mainloop()