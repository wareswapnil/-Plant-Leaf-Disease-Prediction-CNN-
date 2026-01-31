import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk



##############################################+=============================================================
#setting root file

root = tk.Tk()
root.configure(background="white")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login")




username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#For background Image

image2 = Image.open('background1.png')
image2 = image2.resize((w,h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)


#top lable 

label_l1 = tk.Label(root, text="LOGIN FORM",font=("Times New Roman", 30, 'bold'),
                    background="#B0E0E6", fg="black", width=69, height=1)
label_l1.place(x=-50, y=0)



#subprocess module imports the file register.py

def registration():
    root.destroy()
    from subprocess import call
    call(["python","register.py"])
   

def login():
        # make connection with database

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()
         id=list(result[0])
         print(str(id))
         with open(r"id.txt", 'w') as f:
                  id1=f.write(str(id[0]))
                  print(id1)

         if result:
            msg = ""
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            
            root.destroy()
            from subprocess import call
            call(['python','GUI_Master_old.py'])
            # window.destroy()
            # ===========================================
            #if successful login, fetch gui_main1

         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')



bg_icon=ImageTk.PhotoImage(file="hyy.png")
user_icon=ImageTk.PhotoImage(file="password_icon.png")
pass_icon=ImageTk.PhotoImage(file="username_icon.png")
        

# Load the image
image_path = "vector1.png"  # Replace with the path to your image
image = Image.open(image_path)
resized_image = image.resize((450, 373), Image.LANCZOS)  # Adjust size as needed
photo = ImageTk.PhotoImage(resized_image)

# Create a Label to display the image with no border
image_label = tk.Label(root, image=photo, bd=0)
image_label.place(x=230, y=170)  # Adjust position as needed


Login_frame=tk.Frame(root,bg="black")
Login_frame.place(x=610,y=170)
        
logolbl=tk.Label(Login_frame,image=bg_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username",image=user_icon,compound=LEFT,font=("Times new roman", 20),fg="white", bg="black").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=30)
        
lblpass=tk.Label(Login_frame,text="Password",image=pass_icon,compound=LEFT,font=("Times new roman", 20),fg="white", bg="black").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=30)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="#B0E0E6",fg="black")
btn_log.grid(row=3,column=1,pady=40)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="#B0E0E6",fg="black")
btn_reg.grid(row=3,column=0,pady=40)
        
        
    
       
        # Login Function



def log():
    root.destroy()
    from subprocess import call
    call(["python","GUI_main1.py"])
    
    
def window():
  root.destroy()
  
  
def con():
    root.destroy()
    from subprocess import call
    call(["python","register.py"])
    root.destroy()





root.mainloop()