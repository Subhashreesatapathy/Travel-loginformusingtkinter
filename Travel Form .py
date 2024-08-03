
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.configure(bg='lightcoral')
root.title("KEEP EXPLORING")
def getvals():
    print("It works!")
     print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")



    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")


root.geometry("444x544")
root.maxsize(444,544)
Label(root, text="Explore Your  Dream Destination ", font="comicsansms 13 italic", pady=15,background="lightcoral").grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name :",background="lightcoral")
phone = Label(root, text="Phone :",background="lightcoral")
gender = Label(root, text="Gender :",background="lightcoral")
emergency = Label(root, text="Emergency Contact :",background="lightcoral")
paymentmode = Label(root, text="Payment Mode :",background="lightcoral")
chose = Label(root, text="Chose vehicle :",background="lightcoral")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)
chose .grid(row=6,column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
chosevalue=StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevalue, relief=SUNKEN,borderwidth=4)
phoneentry = Entry(root, textvariable=phonevalue,relief=SUNKEN,borderwidth=4)
genderentry = Entry(root, textvariable=gendervalue,relief=SUNKEN,borderwidth=4)
emergencyentry = Entry(root, textvariable=emergencyvalue,relief=SUNKEN,borderwidth=4)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue,relief=SUNKEN,borderwidth=4)
choseentry=Entry(root, textvariable=chosevalue,relief=SUNKEN,borderwidth=4)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)
choseentry.grid(row=6,column=3)

#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", background="lightcoral",variable = foodservicevalue,borderwidth=13)
foodservice.grid(row=9, column=3)

#Button & packing it and assigning it a command
Button(text="BOOK NOW!", command=getvals,background="light blue",borderwidth=5).grid(row=10, column=3)

image = Image.open("images (3).jpeg")
ph = ImageTk.PhotoImage(image)
l1 = Label(image=ph,anchor="ne",relief=SUNKEN)
l1.grid(row=17, column=3)

root.mainloop()
