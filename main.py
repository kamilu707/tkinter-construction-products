from tkinter import *
from tkinter import ttk
import datetime 
import openpyxl
from openpyxl import Workbook
from PIL import Image,ImageTk

#Create the main window wizzard.
root = Tk()


# control the size of the wizzard.
root.geometry('950x552')
# change the wizzard icon.
root.iconbitmap('img/icons8-dental-16.ico')
root.title('Market for dental Products [ متجر مواد صناعة الأسنان ]')

# split the wizzard to different zones or frames.\




# ====================== Functions ===================

def bill():
    total = 0
    for item in trv.get_children():
        trv.delete(item)
    for i in range(len(sb)):
        if(int(sb[i].get()) > 0):
            price = int(sb[i].get()) * menu[i][1]
            total = total + price
            myst = (str(menu[i][1]), str(sb[i].get()), str(price))
            trv.insert("", 'end', iid=i, text=menu[i][0], values=myst)
 




#========== [Frame 1]
F1 = Frame(root, bg='silver', width=600, height=550)
F1.place(x=1, y=1)

# ============= Images ==========

resized_image1= Image.open("img/img_products/1.png").resize((55,55))
img_menu1 = ImageTk.PhotoImage(resized_image1)

resized_image2= Image.open("img/img_products/2.png").resize((55,55))
img_menu2 = ImageTk.PhotoImage(resized_image2)

resized_image3= Image.open("img/img_products/3.png").resize((55,55))
img_menu3 = ImageTk.PhotoImage(resized_image3)

resized_image4= Image.open("img/img_products/4.png").resize((55,55))
img_menu4 = ImageTk.PhotoImage(resized_image4)

resized_image5= Image.open("img/img_products/5.png").resize((55,55))
img_menu5 = ImageTk.PhotoImage(resized_image5)

resized_image6= Image.open("img/img_products/6.png").resize((55,55))
img_menu6 = ImageTk.PhotoImage(resized_image6)

resized_image7= Image.open("img/img_products/7.png").resize((55,55))
img_menu7 = ImageTk.PhotoImage(resized_image7)

resized_image8= Image.open("img/img_products/8.png").resize((55,55))
img_menu8 = ImageTk.PhotoImage(resized_image8)

resized_image9= Image.open("img/img_products/9.png").resize((55,55))
img_menu9 = ImageTk.PhotoImage(resized_image9)

resized_image10= Image.open("img/img_products/10.png").resize((55,55))
img_menu10 = ImageTk.PhotoImage(resized_image10)

resized_image11= Image.open("img/img_products/11.png").resize((55,55))
img_menu11 = ImageTk.PhotoImage(resized_image11)

resized_image12= Image.open("img/img_products/12.png").resize((55,55))
img_menu12 = ImageTk.PhotoImage(resized_image12)





title = Label(F1, text='مشروع بيع معدات البناء', font=('Tajawl 13'),fg='white', bg='#5F7161', width=70)
title.place(x=0, y=0)

menu1 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu1, text='وعاء' , compound=TOP )
menu1.place(x=30, y=45)

menu2 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu2, text='قبغة سلامة' , compound=TOP )
menu2.place(x=170, y=45)

menu3 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu3, text='معول' , compound=TOP )
menu3.place(x=310, y=45)

menu4 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu4, text='مطرقة' , compound=TOP )
menu4.place(x=450, y=45)

menu5 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu5, text='سلم' , compound=TOP )
menu5.place(x=30, y=180)

menu6 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu6, text='فرشاة' , compound=TOP )
menu6.place(x=170, y=180)


menu7 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu7, text='منشار كهربائي' , compound=TOP )
menu7.place(x=310, y=180)


menu8 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu8, text='مشار دكي' , compound=TOP )
menu8.place(x=450, y=180)

menu9 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu9, text='قطاعة' , compound=TOP )
menu9.place(x=30, y=320)

menu10 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu10, text='مفك براغي' , compound=TOP )
menu10.place(x=170, y=320)


menu11 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu11, text='دريل' , compound=TOP )
menu11.place(x=310, y=320)


menu12 = Button(F1, width=88, bg='#EFEAD8', bd=1, relief=SOLID, cursor='hand2', height=85, image=img_menu12, text='بنسة' , compound=TOP )
menu12.place(x=450, y=320)


# ========== Varialble + count ==========
sb = []
font1 = ('Times', 12, 'normal')

sv1=IntVar()
sv2=IntVar()
sv3=IntVar()
sv4=IntVar()
sv5=IntVar()
sv6=IntVar()
sv7=IntVar()
sv8=IntVar()
sv9=IntVar()
sv10=IntVar()
sv11=IntVar()
sv12=IntVar()

sb1 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv1 )
sb1.place(x=30, y=140)
sb.append(sv1)

sb2 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv2 )
sb2.place(x=170, y=140)
sb.append(sv2)

sb3 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv3 )
sb3.place(x=310, y=140)
sb.append(sv3)

sb4 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv4 )
sb4.place(x=450, y=140)
sb.append(sv4)

sb5 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv5 )
sb5.place(x=30, y=275)
sb.append(sv5)

sb6 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv6 )
sb6.place(x=170, y=275)
sb.append(sv6)

sb7 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv7 )
sb7.place(x=310, y=275)
sb.append(sv7)

sb8 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv8 )
sb8.place(x=450, y=275)
sb.append(sv8)

sb9 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv9 )
sb9.place(x=30, y=415)
sb.append(sv9)

sb10 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv10 )
sb10.place(x=170, y=415)
sb.append(sv10)

sb11 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv11 )
sb11.place(x=310, y=415)
sb.append(sv11)

sb12 = Spinbox(F1, from_=0, to_=5, font=font1, width=10, textvariable=sv12 )
sb12.place(x=450, y=415)
sb.append(sv12)

#============ Buttons =============
b1= Button(F1, text='شراء المواد', fg='white', font=('Tajawal 12'), width=15, bg='#6D8B74', bd=1, relief=SOLID, cursor='hand2',height=1, command=bill)
b1.place(x=30, y=500)

b2= Button(F1, text='فاتورة جديدة', fg='white', font=('Tajawal 12'), width=15, bg='#6D8B74', bd=1, relief=SOLID, cursor='hand2',height=1)
b2.place(x=160, y=500)

b3= Button(F1, text='استئجار المواد', fg='white', font=('Tajawal 12'), width=15, bg='#6D8B74', bd=1, relief=SOLID, cursor='hand2',height=1)
b3.place(x=290, y=500)

b4= Button(F1, text='إغلاق البرنامج', fg='white', font=('Tajawal 12'), width=15, bg='#6D8B74', bd=1, relief=SOLID, cursor='hand2',height=1)
b4.place(x=420, y=500)

# =============  Frame [2] ==============
F2= Frame(root, bg='gray', width=343, height=550)
F2.place(x=604, y=1)

# Create Treeview to show data in colums and rows.
trv = ttk.Treeview(F2, selectmode='browse')
trv.place(x=1, y=1, width=340, height=550)

trv["columns"]= ('1','2','3')
trv.column("#0", width=80, anchor='c')
trv.column("1", width=50, anchor='c')
trv.column("2", width=50, anchor='c')
trv.column("3", width=60, anchor='c')
trv.heading("#0", text='المواد', anchor='c')
trv.heading("1", text='السعر', anchor='c')
trv.heading("2", text='العدد', anchor='c')
trv.heading("3", text='الحساب الكلي', anchor='c')

# =============  Price ===========

menu= {
    0:['وعاء', 20],
    1:['قبعة سلامة', 40],
    2:['معول', 40],
    3:['مطرقة', 40],
    4:['سلم', 40],
    5:['فرشاة', 60],
    6:['منشار كهرباء', 20],
    7:['مشار دكي', 40],
    8:['قطاعة', 80],
    9:['مفك براغي', 10],
    10:['دريل', 30],
    11:['بنسة', 130],
}






# Loop for making the wizzard live.
root.mainloop()
