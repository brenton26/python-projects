


import os
from tkinter import *
import tkinter as tk
import sqlite3

# Be sure to import our other modules to have access to them
import phonebook_main
import phonebook_gui


def center_window(self,w,h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width=self.master.winfo_screenwidth()
    screen_height=self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x=int((screenwidth/2)-(w/2))
    y=int((screenheight/2)-(h/2))
    centerGeo=self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

# catch if the user clicks on the upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # this closes the app
        self.master.destroy()
        os._exit(0)

#=============================================
def create_db(self):
    conn=sqlite3.connect('phonebook.db')
    with conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook(\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                    col_fname TEXT,\
                    col_lname TEXT,\
                    col_fullname TEXT,\
                    col_phone TEXT,\
                    col_email TEXT\
                    );")
        # You must commit() to save changes and close the database connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data=('John','Doe','John Doe','123-456-7890','jdoe@gmail.com')
    conn=sqlite3.connect('phonebook.db')
    with conn:
        cur=conn.cursor()
        cur,count=count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) \
                        VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close()

def count_records(cur):
    count=""
    cur.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
    count=cur.fetchone()[0]
    return cur,count

# Select item in Listbox
def onSelect(self,event):
    # calling the event is the self.lstList1 widget
    varList=event.widget
    select=varList.curselection()[0]
    value=varList.get(select)
    conn=sqlite3.connect('phonebook.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody=cursor.fetchall()
        # this returns a tuple and we slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname=self.txt_fname.get()
    var_lname=self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname=var_fname.strip() # removes any blank spaces before or after each entry
    var_lname=var_lname.strip()
    var_fname=var_fname.title() # capitalizes the first character in each word
    var_lname=var_lname.title()
    var_fullname=("{} {}".format(var_fname,var_lname)) # combines the normalized first names and last names
    print("var_fullname: {}".format(var_fullname))
    var_phone=var_phone.strip()
    var_email-var_email.strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
    if (len(var_fname) > 0 and len(var_fname) > 0 and len(var_phone) > 0 and len(var_email) > 0): # forces users to insert all info
        conn=sqlite3.connect('phonebook.db')
        with conn:
            cursor=conn.cursor()
            # Check the database for existence of the fullname, if so, we will alert the user and disregard the request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count=cursor.fetchone()[0]
            chkname=count
            if chkname==0: #if this is 0 then there is no existence of the fullname and we can add new data
                print("chkname: {}".format(chkname))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                count=
                
                

#########################
        
    









    
            











