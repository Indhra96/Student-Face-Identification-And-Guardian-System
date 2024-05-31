from tkinter import *
import shutil
from PIL import ImageTk, Image
from subprocess import call

def student():
    call(["python","student.py"])

def register():
    call(["python", "registerGUI.py"])

def VideoSurveillance():
    call(["python", "surveillance.py"])   

def detectCriminal():
    call(["python", "detect.py"])

root = Tk()
root.geometry('800x500')
root.minsize(1350,720)
root.title("Student Face Identification and Complaint System")
root.configure(bg="#DEEFF5")
def center_window(width, height):
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

center_window(800, 500)

image = Image.open("image.jpg")
photo = ImageTk.PhotoImage(image)
image_label = Label(root, image=photo)
image_label.pack(pady=30)

label_0 = Label(root, text="Student Face Identification and Complaint System", width=50, font=("bold", 20), anchor=CENTER, bg="#386184", fg="white")
label_0.pack(pady=10)

Button(root, text='STUDENT REGISTER', width=35, height=3, bg='#BBADE6', fg='white', font=("bold", 11), command=student).pack(pady=10)
Button(root, text='REGISTER COMPLAINT', width=35, height=3, bg='#BBADE6', fg='white', font=("bold", 11), command=register).pack(pady=10)
Button(root, text='PHOTO / VIDEO MATCH', width=35, height=3, bg='#4BAAC8', fg='white', font=("bold", 11), command=detectCriminal).pack(pady=10)
Button(root, text='VIDEO SURVEILLANCE', width=35, height=3, bg='#4BAAC8', fg='white', font=("bold", 11), command=VideoSurveillance).pack(pady=10)

root.mainloop()
