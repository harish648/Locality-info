from tkinter import *
from tkinter import messagebox
import webbrowser
from PIL import ImageTk,Image

second = Toplevel()
second.title('Gallery')
second.iconbitmap("C:/Users/Pushpa/Desktop/Python/time.ico")
second.configure(background='light blue')
second.geometry("500x300")

global img1
global img2
global img3
global img4
global img5

img1=ImageTk.PhotoImage(Image.open("C:/Users/Pushpa/Desktop/Python/ITC Ltd/1.jpg"))
img2=ImageTk.PhotoImage(Image.open("C:/Users/Pushpa/Desktop/Python/ITC Ltd/2.jpg"))
img3=ImageTk.PhotoImage(Image.open("C:/Users/Pushpa/Desktop/Python/ITC Ltd/3.jpg"))
img4=ImageTk.PhotoImage(Image.open("C:/Users/Pushpa/Desktop/Python/ITC Ltd/4.jpg"))
img5=ImageTk.PhotoImage(Image.open("C:/Users/Pushpa/Desktop/Python/ITC Ltd/5.jpg"))
	
image_list=[img1,img2,img3,img4,img5]

my_label = Label(image=img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number - 1])
	button_forward = Button(second, text='>>',command=lambda: forward(image_number + 1))
	button_back = Button(second, text='<<',command=lambda: back(image_number - 1))
	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)


def back():
	global my_label
	global button_forward
	global button_back



button_back = Button(second,text='<<',command= back)
button_clo = Button(second,text='Close',command=second.quit)
button_forward = Button(second,text='>>',command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_clo.grid(row=1,column=1)
button_forward.grid(row=1,column=2)


second.mainloop()