from tkinter import *
import tkinter.messagebox as msg
import mysql.connector

def connect_database():
    return mysql.connector.connect(
            database = "python_practice_1",
            user = "root",
            password = "Only4950*",
            host = "localhost"
        )

def insert_data():
    if e_fname.get() == "" or e_lname.get() == "" or e_email.get() == "" or e_mobile.get() == "":
        msg.showinfo("insert status", "Please fill all information")
    else:
        conn = connect_database()
        cursor = conn.cursor()    
        query = "insert into practice_table_1 (fname, lname, email, mobile) values (%s, %s, %s, %s)"
        values = (e_fname.get(), e_lname.get(), e_email.get(), e_mobile.get())

        cursor.execute(query, values)
        conn.commit()
        conn.close()
        msg.showinfo("insert status", "Data inserted succesfully")

        e_fname.delete(0, 'end')
        e_lname.delete(0, 'end')
        e_email.delete(0, 'end')
        e_mobile.delete(0, 'end')

def search_data():
    if e_id.get() == "":
        msg.showinfo("search status", "Enter a valid id")
    else:
        conn = connect_database()
        cursor = conn.cursor()
        query = "select * from practice_table_1 where id = %s"
        values = (e_id.get(),)

        cursor.execute(query, values)
        row = cursor.fetchall()
        conn.close()

        e_fname.delete(0, 'end')
        e_lname.delete(0, 'end')
        e_email.delete(0, 'end')
        e_mobile.delete(0, 'end')

        e_fname.insert(0, row[0][1])
        e_lname.insert(0, row[0][2])
        e_email.insert(0, row[0][3])
        e_mobile.insert(0, row[0][4])

def update_data():
    if e_id.get() == "" or e_fname.get() == "" or e_lname.get() == "" or e_email.get() == "" or e_mobile.get() == "":
        msg.showinfo("update status", "Please fill all information")
    else:
        conn = connect_database()
        cursor = conn.cursor()    
        query = "update practice_table_1 set fname = %s, lname = %s, email = %s, mobile = %s where id = %s"
        values = (e_fname.get(), e_lname.get(), e_email.get(), e_mobile.get(), e_id.get())

        cursor.execute(query, values)
        conn.commit()
        conn.close()
        msg.showinfo("update status", "Data updated succesfully")

        e_fname.delete(0, 'end')
        e_lname.delete(0, 'end')
        e_email.delete(0, 'end')
        e_mobile.delete(0, 'end')

def delete_data():
    if e_id.get() == "":
        msg.showinfo("delete status", "Enter a valid id")
    else:
        conn = connect_database()
        cursor = conn.cursor()
        query = "delete from practice_table_1 where id = %s"
        values = (e_id.get(),)

        cursor.execute(query, values)
        conn.commit()
        conn.close()
        msg.showinfo("delete status", "Data deleted successfully")
  
        

root = Tk()
root.geometry("500x500")
root.title("student data")

# defining variables :-
l_id = Label(root, text="Id", font=("Arial", 10))
l_fname = Label(root, text="First name", font=("Arial", 10))
l_lname = Label(root, text="Last name", font=("Arial", 10))
l_email = Label(root, text="Email", font=("Arial", 10))
l_mobile = Label(root, text="Mobile", font=("Arial", 10))

e_id = Entry(root)
e_fname = Entry(root)
e_lname = Entry(root)
e_email = Entry(root)
e_mobile = Entry(root)

insert = Button(root, text="Insert", bg="black", fg="white", font=("Arial", 12), command=insert_data)
search = Button(root, text="Search", bg="black", fg="white", font=("Arial", 12), command=search_data)
update = Button(root, text="Update", bg="black", fg="white", font=("Arial", 12), command=update_data)
delete = Button(root, text="Delete", bg="black", fg="white", font=("Arial", 12), command=delete_data)

# placing variables :-
l_id.place(x=50, y=50)
l_fname.place(x=50, y=100)
l_lname.place(x=50, y=150)
l_email.place(x=50, y=200)
l_mobile.place(x=50, y=250)

e_id.place(x=140, y=50)
e_fname.place(x=140, y=100)
e_lname.place(x=140, y=150)
e_email.place(x=140, y=200)
e_mobile.place(x=140, y=250)

insert.place(x=50, y=300)
search.place(x=100, y=300)
update.place(x=163, y=300)
delete.place(x=227, y=300)
