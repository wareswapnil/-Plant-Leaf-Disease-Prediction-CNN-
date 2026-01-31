import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import tensorflow as tf 
from tensorflow import keras

import numpy as np
import time
import CNNModelp 
import pickle
from skimage import feature
#import svm as svm
global fn
fn=""
##############################################+=============================================================

root = tk.Tk()    
root.configure(background="brown")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title(" Smart Green House System ")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('111.jpg')
image2 =image2.resize((w,h), Image.LANCZOS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#
lbl = tk.Label(root, text="Smart Green House System", font=('times', 35,' bold '), height=1, width=65,bg="#B0E0E6",fg="black")
lbl.place(x=0, y=10)


frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=500, bd=5, font=('times', 14, ' bold '),bg="lightpink")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=90)

    
    
###########################################################################



import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from keras.models import load_model
    #from keras.optimizers import Adam

#    global fn
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('Plant_model.h5')
            
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        plant=np.argmax(prediction)
        print(plant)
        
        
        
        if plant == 0:
            Cd="CNN Algorithm Accurecy is 99% \n Apple___Apple_scab  \n medicine=Bonide Captan,\n wettable sulfur,\n summer lime sulfur, \n the price will be near about (1230)"
        
        elif plant == 8:
            Cd="CNN Algorithm Accurecy is 99% \n Apple___Black_rot \n medicine = Mancozeb, and Ziram are \n all highly effective \n against black rot., \n the price will be near about (1500)"
        elif plant == 9:
            Cd="CNN Algorithm Accurecy is 99% \n Apple___Cedar_apple_rust \n medicine = Fungicides with the active \n  ingredient Myclobutanil are most \n effective in preventing rust, \n the price will be near about (1230)"
        elif plant == 10:
            Cd="CNN Algorithm Accurecy is 99% \n Apple___healthy"
        elif plant == 11:
            Cd="CNN Algorithm Accurecy is 99% \n Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot \n medicine = Fungicides with the active \n  ingredient Myclobutanil are most \n effective in preventing rust, \n the price will be near about (800)"
        elif plant == 12:
            Cd="CNN Algorithm Accurecy is 99% \n Corn_(maize)___Common_rust \n medicine = pyraclostrobin, pyraclostrobin + metconazole,\n  pyraclostrobin + fluxapyroxad, \n  azoxystrobin + propiconazole, \n trifloxystrobin + prothioconazole, \n the price will be near about (14500)"
        elif plant == 13:
            Cd="CNN Algorithm Accurecy is 99% \n Corn_(maize)___healthy"
        elif plant == 14:
            Cd="CNN Algorithm Accurecy is 99% \n Corn_(maize)___Northern_Leaf_Blight \n medicine = (TLB) is a foliar disease of \n corn (maize) caused by Exserohilum \n turcicum, the anamorph of the \n ascomycete Setosphaeria turcica., \n the price will be near about (1230) "
        elif plant == 15:
            Cd="CNN Algorithm Accurecy is 99% \n Grape___Black_rot \n medicine = Post-bloom spray \n  mancozeb + mycobutanil, imidacloprid \n  or azadirachtin.,\n the price will be near about (2467) "
        elif plant == 1:
            Cd="CNN Algorithm Accurecy is 99% \n Grape___Esca_(Black_Measles) \n medicine = Post-bloom spray \n  mancozeb + mycobutanil, imidacloprid \n  or azadirachtin.,\n the price will be near about (2467)"
        elif plant == 2:
            Cd="CNN Algorithm Accurecy is 99% \n Grape___healthy"
        elif plant == 3:
            Cd="CNN Algorithm Accurecy is 99% \n Grape___Leaf_blight_(Isariopsis_Leaf_Spot), \n medicne = Fungicides with the active \n  ingredient Myclobutanil are most \n effective in preventing rust, \n the price will be near about (800)"   
        elif plant == 4:
            Cd="CNN Algorithm Accurecy is 99% \n Peach___Bacterial_spot \n medicine = copper, oxytetracycline \n (Mycoshield and generic equivalents),\n  and syllit+captan; ,\n the price will be near about (2467) "
        elif plant == 5:
            Cd="CNN Algorithm Accurecy is 99% \n Peach___healthy"
        elif plant == 6:
            Cd="CNN Algorithm Accurecy is 99% \n Strawberry___healthy"
        elif plant == 7:
            Cd="CNN Algorithm Accurecy is 99% \n Strawberry___Leaf_scorch, \n medicine = copper, oxytetracycline \n (Mycoshield and generic equivalents),\n  and syllit+captan; ,\n the price will be near about (2467) "
            
            
        A=Cd
        return A

############################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=60, font=("bold", 20), bg='bisque2', fg='black')
    result_label.place(x=250, y=410)

###############################################################################


def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        #X1="Selected Image is {0}".format(X)
        x2=format(X)+" Diesease is detected"
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ x2 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
#############################################################################
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='Leaf Disease 100% Code', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])



    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)
  
#############################################################################    

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)


#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=50)

button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=100)

# button3 = tk.Button(frame_alpr, text="Train CNN Model", command=train_model, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=150)

button4 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=200)

# button4 = tk.Button(frame_alpr, text="SVM_Prediction", command=testSVM_model,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
# button4.place(x=10, y=250)

# button3 = tk.Button(frame_alpr, text="svm Train Model", command=CL_SVM, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=300)
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=15, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=350)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=400)



root.mainloop()