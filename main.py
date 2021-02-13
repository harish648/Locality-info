from tkinter import *
from tkinter import messagebox
import webbrowser
from PIL import ImageTk,Image

root=Tk()
root.title('ITC Ltd. Bhadrachalam')
root.iconbitmap("C:/Users/Pushpa/Desktop/Python/ITC Ltd/itc.ico")
root.configure(background='light blue')
root.geometry("500x300")

welcome = LabelFrame(root,text='WELCOME',padx=50,pady=20,bd=1)
welcome.pack(side= TOP , padx=1,pady=1 )
wlabel = Label(welcome,text='Welcome TO ITC PSPD Ltd. Bhadrachalam')
wlabel.pack()

bframe = LabelFrame(root,text='PLEASE CHOOSE ONE OF THEM',padx=5,pady=20,bd=1)
bframe.pack( side = BOTTOM, padx= 1, pady=1)
hlabel = Label(bframe,text='Hello everyone!!!')
hlabel.grid(row=0,column=0)

def button_info():
	first = Toplevel()
	first.title('INFORMATION')
	first.iconbitmap("C:/Users/Pushpa/Desktop/Python/ITC Ltd/itc.ico")
	first.configure(background='light blue')
	first.geometry("500x300")

	infor = LabelFrame(first,text='INFORMATION',padx=50,pady=20,bd=1)
	infor.pack(side= TOP )
	label = Label(infor,text='ITC PSPD Ltd.')
	label.pack()

	i = LabelFrame(first,text='DO YOU KNOW!!!',padx=5,pady=20,bd=1)
	i.pack( side = BOTTOM)
	label1 = Label(i,text="ITC's Paperboards and Specialty Papers Division (ITC-PSPD), is amongst the leading names in the business worldwide.\n Our innovative solutions to meet a diverse cross-section of packaging and communication needs have helped us carve a unique niche for ourselves. \n With emphasis on harnessing state-of-the-art technology, we have emerged as the largest manufacturer of Packaging and Graphic Boards in South Asia. \n In the endeavor to move up the value chain, our portfolio of products and services has consistently grown over the years. Today, our products and pool of knowledge-based services are much sought-after by discerning customers,\n both in India and internationally, for sustaining and improving their competitiveness.")
	label2 = Label(i,text="7 machines with production capacity of 493,000 TPA of Paperboard and 124,700 TPA of Paper \n Specialty boards for playing cards and scratch cards,C2S Art Boards and Ivory Boards. \n Commissioned India's first Elemental Chlorine Free bleaching line, later followed by another line incorporating Light ECF process with a combined capacity of 260,000 TPA.\n ISO 9001, ISO 14001 and OHSAS 18001 accredited.\n Forest Stewardship Council - Chain of Custody certified.\n BRC Global Standard certified for food grade boards.")
	label1.grid(row=0,column=0)
	label2.grid(row=6,column=0)
	
	def button_more():
		webbrowser.open_new(r"https://www.itcpspd.com/aboutus.aspx")


	button_more = Button(i,text='CLICK HERE FOR MORE INFO',padx=50,pady=20,command=button_more)
	button_close = Button(i,text='CLOSE',padx=50,pady=20,command=first.destroy)

	button_more.grid(row=11,column=0)
	button_close.grid(row=11,column=1)


def button_gallery():
	second = Toplevel()
	second.title('Gallery')
	second.iconbitmap("C:/Users/Pushpa/Desktop/Python/ITC Ltd/itc.ico")
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

	def back():
		global my_label
		global button_forward
		global button_back

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


	button_back = Button(second,text='<<',command= back)
	button_clo = Button(second,text='Close',command=second.quit)
	button_forward = Button(second,text='>>',command=lambda: forward(2))

	button_back.grid(row=1,column=0)
	button_clo.grid(row=1,column=1)
	button_forward.grid(row=1,column=2)

def button_map():
	webbrowser.open_new(r"https://www.google.com/maps/place/ITC+bcm+Guest+House/@17.70327,80.856908,17z/data=!3m1!4b1!4m8!1m2!2m1!1sitc+ltd+bhadrachalam!3m4!1s0x3a36a90612289f3d:0x9884c7a61458019e!8m2!3d17.7032649!4d80.8590967")

def button_pd():
	pass

def button_query():
	messagebox.showinfo('Our E-Mail ID',"Please e-mail to 'tirumallaharish@gmail.com'")



button_info=Button(bframe,text='INFO',command=button_info)
button_gallery=Button(bframe,text='Gallery',command=button_gallery)
button_map=Button(bframe,text='Map',command=button_map)
button_pd=Button(bframe,text='Phone Directory',command=button_pd)
button_query=Button(bframe,text='Query',command=button_query)

button_info.grid(row=1,column=0)
button_gallery.grid(row=2,column=0)
button_map.grid(row=3,column=0)
button_pd.grid(row=4,column=0)
button_query.grid(row=5,column=0)

root.mainloop()
