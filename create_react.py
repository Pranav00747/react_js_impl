from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import webbrowser
class create_react:
 def get():
   ask_path=""
   tt = Tk()
   tt.overrideredirect(True)
   tt.geometry(("%dx%d")%(tt.winfo_screenwidth(), tt.winfo_screenheight()))
   tt.configure(bg="#000000")
   tt.attributes('-alpha', 0.8)
   l1 = Label(tt, text="React JS Implementor", font=("Calibri", 29), bg="#000000", fg="#ffffff")
   l1.place(x=429, y=30)
   l3 = Label(tt, text="x", font=("Arial", 12), bg="#000000", fg="#ffffff")
   l3.place(x=tt.winfo_screenwidth()-29, y=29)
   def be1(e):
      l3.config(font=("Arial", 18), fg="yellow")
   def  bl1(e):
    l3.config(font=("Arial", 12), fg="#ffffff")
   def bb1(e):
    tt.destroy()
   l3.bind('<Enter>', be1)
   l3.bind('<Leave>', bl1) 
   l3.bind('<Button-1>', bb1)
   l4 = Label(tt, text="App.js", bg="#000000", fg="#ffffff", font=("Calibri", 10))
   l4.place(x=100, y=100)
   txt = Text(tt, bg="#000000", fg="#ffffff", font=("Calibri", 12), width="120", height="25")
   txt.place(x=100, y=120)
   save = Label(tt, text="Save", bg="#ffffff", fg="#000000", font=("Arial", 12))
   def sb1(e):
    save.config(bg="yellow", fg="#ffffff")
   def sb2(e):
     save.config(bg="#ffffff", fg="#000000")
   def sb3(e): 
      ask_path = filedialog.askdirectory()
      if len(ask_path) >0:
        path=ask_path+"/src/App.js"
        if os.path.isfile(path):
          os.remove(path)
          fp =open(path, "w")
          fp.write(txt.get("1.0", "end-1c"))
          fp.close()
   save.place(x=820, y=620)
   save.bind('<Enter>', sb1)
   save.bind('<Leave>', sb2)
   save.bind('<Button-1>', sb3)
   clear = Label(tt, text="Clear", bg="#ffffff", fg="#000000", font=("Arial", 12))
   def cb1(e):
    clear.config(bg="yellow", fg="#ffffff")
   def cb2(e):
     clear.config(bg="#ffffff", fg="#000000")
   def cb3(e):
       txt.insert(END, "")
   clear.place(x=900, y=620)
   clear.bind('<Enter>', cb1)
   clear.bind('<Leave>', cb2)
   clear.bind('<Button-1>', cb3)
   upload = Label(tt, text="Upload", bg="#ffffff", fg="#000000", font=("Arial", 12))
   def up1(e):
    upload.config(bg="yellow", fg="#ffffff")
   def up2(e):
     upload.config(bg="#ffffff", fg="#000000")
   def up3(e):
     ask_path=  filedialog.askdirectory()
     if len(ask_path) >0:
        path=ask_path+"/src/App.js"
        if os.path.isfile(path):
          fp =open(path, "r")
          txt.insert(END, fp.read())
          fp.close()
   upload.place(x=740, y=620)
   upload.bind('<Enter>', up1)
   upload.bind('<Leave>', up2)
   upload.bind('<Button-1>', up3)
   run = Label(tt, text="Run", bg="#ffffff", fg="#000000", font=("Arial", 12))
   def rn1(e):
    run.config(bg="yellow", fg="#ffffff")
   def rn2(e):
     run.config(bg="#ffffff", fg="#000000")
   def rn3(e):
        ask_path = filedialog.askdirectory()
        print(ask_path)
        if len(ask_path) >0:
           os.chdir(ask_path)
           os.system("start powershell npm start")
   run.place(x=980, y=620)
   run.bind('<Enter>', rn1)
   run.bind('<Leave>', rn2)
   run.bind('<Button-1>', rn3)
   """l5 = Label(tt, text="Create App:", bg="#000000", fg="#ffffff", font=("Arial", 10))
   l5.place(x=100, y=620)
   et = Entry(tt, bg="#000000", width="60", fg="#ffffff")
   et.place(x=200, y=620)
   crt = Label(tt, text="Create", bg="#ffffff", fg="#000000", font=("Arial", 12))
   def cc1(e):
    crt.config(bg="yellow", fg="#ffffff")
   def cc2(e):
     crt.config(bg="#ffffff", fg="#000000")
   crt.place(x=600, y=620)
   crt.bind('<Enter>', cc1)
   crt.bind('<Leave>', cc2)"""
   copy = Label(tt, text="Dev Pranav", bg="#000000", fg="#ffffff", font=("Arial", 10))
   copy.place(x=tt.winfo_screenwidth()/2-100, y=tt.winfo_screenheight()-60)
   def cce(e):
     copy.config(fg="yellow")
   def ccl(e):
     copy.config(fg="#ffffff")
   def ccb(e):
       webbrowser.open("https://github.com/Pranav00747")
   copy.bind('<Enter>', cce)
   copy.bind('<Leave>', ccl)
   copy.bind('<Button-1>', ccb)
   tt.mainloop()

if __name__=="__main__":
  cr = create_react
  cr.get()
   