


from tkinter import *


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)


        self.master=master
        self.master.resizable(width=False,height=False)
        self.master.geometry('400x200')
        self.master.title('Check Files')
        self.master.config(bg='#002240')

        self.btn_browse=Button(self.master,text='Browse...',font=("Helvetica",12),fg='#002240',bg='white')
        self.btn_browse.grid(row=1,column=0,rowspan=2,padx=(30,0),pady=(60,0),sticky=S)

        self.btn_browse2=Button(self.master,text='Browse...',font=("Helvetica",12),fg='#002240',bg='white')
        self.btn_browse2.grid(row=3,column=0,padx=(30,0),pady=(30,0))

        self.btn_checkforfiles=Button(self.master,text='Check for Files...',font=("Helvetica",12),fg='#002240',bg='white')
        self.btn_checkforfiles.grid(row=4,column=0,padx=(30,0),pady=(30,0))

        self.btn_closeprogram=Button(self.master,text='Close Program',font=("Helvetica",12),fg='#002240',bg='white')
        self.btn_closeprogram.grid(row=4,column=3,padx=(0,0),pady=(30,0),sticky=W)

        self.lbl_top=Label(self.master,text='',font=("Helvetica",12),fg='#002240',bg='white')
        self.lbl_top.grid(row=2,column=3,columnspan=2,padx=(0,0),pady=(30,0),sticky=W)

        self.lbl_bottom=Label(self.master,text='',font=("Helvetica",12),fg='#002240',bg='white')
        self.lbl_bottom.grid(row=3,column=3,columnspan=2,padx=(0,0),pady=(30,0),sticky=W)















if __name__=="__main__":
    root=Tk()
    App=ParentWindow(root)
    root.mainloop()

