


from tkinter import *
from tkinter import filedialog
import os
import sqlite3
import shutil


 


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master=master
        self.master.resizable(width=False,height=False)

        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()
        x=int((screen_width/2)-(480/2))
        y=int((screen_height/2)-(200/2))
        self.master.geometry('{}x{}+{}+{}'.format(480,200,x,y))
        
        self.master.title("Check Files")
        self.master.config(bg='#002240')     

        self.button1=Button(self.master,text="Move txt Files\n from this directory:",width=14,height=2,command=self.get_filepath)
        self.button1.grid(row=0,column=0,padx=(20,0),pady=(30,0),sticky=W)
        
        self.button2=Button(self.master,text="Move txt Files\n to this directory:",width=14,height=2,command=self.get_filepath2)
        self.button2.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky=W)
        
        self.button3=Button(self.master,text="Move Files",width=14,height=3,command=self.movefiles)
        self.button3.grid(row=2,column=0,padx=(20,0),pady=(10,0),sticky=E)
        
        self.button4=Button(self.master,text="Close Program",width=14,height=3,command=self.closeprogram)
        self.button4.grid(row=2,column=2,sticky=E)
        
        self.textbox1=Entry(self.master,text="",font=12,width=30)
        self.textbox1.grid(row=0, column=1, columnspan=2, padx=(25, 0), pady=(30, 0))
        
        self.textbox2=Entry(self.master,text="",font=12,width=30)
        self.textbox2.grid(row=1,column=1,columnspan=2,padx=(25,0),pady=(10,0))


    def get_filepath(self):
        self.textbox1.delete(0,END)
        filepath=filedialog.askdirectory()
        self.textbox1.insert(END,filepath)

    def get_filepath2(self):
        self.textbox2.delete(0,END)
        filepath=filedialog.askdirectory()
        self.textbox2.insert(END,filepath)

    def movefiles(self):
        conn=sqlite3.connect('txtfilelist.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                filename TEXT \
                )")
            conn.commit()
        conn.close()
        
        originalfilepath = self.textbox1.get()
        filelist = os.listdir(originalfilepath)
        destinationfilepath = self.textbox2.get()
        
        for files in filelist:
            if files.endswith("txt"):
                filepath=os.path.join(originalfilepath,files)
                file_getmtime = os.path.getmtime(filepath) 
                print("Thses files were moved:\n{}, time: {}".format(filepath,file_getmtime))
                shutil.move(filepath,destinationfilepath)
                conn = sqlite3.connect('txtfilelist.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO tbl_txtfiles (filename) VALUES (?) ",(files,))
                    conn.commit()
                conn.close()
                self.textbox1.delete(0,END)
                self.textbox2.delete(0,END)


    def closeprogram(self):
        self.master.destroy()
        os._exit(0)
        



if __name__ =="__main__":
    root=Tk()
    App=ParentWindow(root)
    root.mainloop()
