from tkinter import *
import pyperclip as pp
import os


output = ""
data = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","?"]

def _copp():
    global output
    pp.copy(output)
def _encrypt():
    global output
    output = ""
    inp = ent1.get()
    for i in inp:
        if i == data[0]:
            output += "00"
            output += " "
        elif i == data[1]:
            output += "1"
            output += " "
        elif i == data[2]:
            output += "2"
            output += " "
        elif i == data[3]:
            output += "3"
            output += " "
        elif i == data[4]:
            output += "4"
            output += " "
        elif i == data[5]:
            output += "5"
            output += " "
        elif i == data[6]:
            output += "6"
            output += " "
        elif i == data[7]:
            output += "7"
            output += " "
        elif i == data[8]:
            output += "8"
            output += " "
        elif i == data[9]:
            output += "9"
            output += " "
        elif i == data[10]:
            output += "10"
            output += " "
        elif i == data[11]:
            output += "11"
            output += " "
        elif i == data[12]:
            output += "12"
            output += " "
        elif i == data[13]:
            output += "13"
            output += " "
        elif i == data[14]:
            output += "14"
            output += " "
        elif i == data[15]:
            output += "15"
            output += " "
        elif i == data[16]:
            output += "16"
            output += " "
        elif i == data[17]:
            output += "17"
            output += " "
        elif i == data[18]:
            output += "18"
            output += " "
        elif i == data[19]:
            output += "19"
            output += " "
        elif i == data[20]:
            output += "20"
            output += " "
        elif i == data[21]:
            output += "21"
            output += " "
        elif i == data[22]:
            output += "22"
            output += " "
        elif i == data[23]:
            output += "23"
            output += " "
        elif i == data[24]:
            output += "24"
            output += " "
        elif i == data[25]:
            output += "25"
            output += " "
        elif i == data[26]:
            output += "26"
            output += " "
        elif i == data[27]:
            output += "27"
            output += " "
        else:
            output += "𑨩"
    lbl1["text"] = output
    win.update()
    ent1.delete(0,END)

def _decrypt():
    global output
    output = ""
    inp = ent1.get()
    inp = inp.split(sep=" ")
    for i in inp:
        if i == "00":
            output += data[0]
        elif  i == "1":
            output += data[1]
        elif  i == "2":
            output += data[2]
        elif  i == "3":
            output += data[3]
        elif  i == "4":
            output += data[4]
        elif  i == "5":
            output += data[5]
        elif  i == "5":
            output += data[5]
        elif  i == "6":
            output += data[6]
        elif  i == "7":
            output += data[7]
        elif  i == "8":
            output += data[8]
        elif  i == "9":
            output += data[9]
        elif  i == "10":
            output += data[10]
        elif  i == "11":
            output += data[11]
        elif  i == "12":
            output += data[12]
        elif  i == "13":
            output += data[13]
        elif  i == "14":
            output += data[14]
        elif  i == "15":
            output += data[15]
        elif  i == "16":
            output += data[16]
        elif  i == "17":
            output += data[17]
        elif  i == "18":
            output += data[18]
        elif  i == "19":
            output += data[19]
        elif  i == "20":
            output += data[20]
        elif  i == "21":
            output += data[21]
        elif  i == "22":
            output += data[22]
        elif  i == "23":
            output += data[23]
        elif  i == "24":
            output += data[24]
        elif  i == "25":
            output += data[25]
        elif  i == "26":
            output += data[26]
        elif  i == "27":
            output += data[27]
        else:
            output += "𑨩"
    lbl1["text"] = output
    win.update()
    ent1.delete(0,END)



def _darkm():
    if btn4["text"] == "darkmode is : off":
        win.configure(bg='gray')
        btn4["text"] = "darkmode is : on"
    elif btn4["text"] == "darkmode is : on":
        win.configure(bg='dark gray')
        btn4["text"] = "darkmode is : off"

def  _about():
    os.startfile("https://alfacod.github.io/suport.html")

def  _api():
    os.startfile("https://alfacod.github.io/encapi.html")




win = Tk()
win.title("text encryptor");win.geometry('350x234');win.resizable(False, False)

lbl1 = Label(win, text="matn shoma inja namyesh dade mishavad");lbl1.pack(pady=3)
btn1 = Button(win,text="copy output text",width=42,command=_copp);btn1.pack(pady=3)
ent1 = Entry(win, width=50);ent1.pack(pady=3)
btn2 = Button(win,text="encrypt",width=42,command=_encrypt);btn2.pack(pady=3)
btn3 = Button(win,text="decrypt",width=42,command=_decrypt);btn3.pack(pady=3)
btn4 = Button(win,text='darkmode is : off', command=_darkm);btn4.pack(pady=3)
btn5 = Button(win, text="api", command=_api);btn5.pack()
btn6 = Button(win, text="about", command=_about);btn6.pack(side=LEFT,padx=3,pady=3)






win.mainloop()