import tkinter as tk     #importing tkinter for gui
from tkinter import *
from tkinter import ttk
import pickle as pk     #importing pickle to convert object hierarchy into data stream and vice-versa
import pandas as pd     #importing pandas for dataframe

Book_dict = pk.load(open('Books_dict.pkl','rb'))  #convert data stream to object hierarchy
Books = pd.DataFrame(Book_dict)

root = tk.Tk()
def values():  #values are defined to print book list
    win2 = Toplevel(root)
    win2["bg"]="yellow"
    win2.geometry('300x400')
    win2.resizable(False,False)
    Auth = Author.get()
    Au_name = Books[Books.Author_name == Auth].Book_name.values[1:6]
    book_list = list(Au_name)
    Label(win2, text="Recommended Books", font="Arial 12 bold", bg="black",fg="white").pack(padx=40, pady=10)
    for i in book_list:
        Label(win2,text=i,font="Arial 12 bold",bg="yellow").pack()
        #print(i)

root.geometry('600x400')   #size for tkinter window is 1080 x 1080
root["bg"] = "cyan"  #background colour for tkinter
l1= Label(text="Book Recommender System", font= ("Times New Roman", 20))   #1st label is created
l1.grid()
l2= ttk.Label(root, text = "Select Author to recommend: ",font = ("Times New Roman", 10))   #2nd label is created
l2.grid(column = 0,row = 15, padx = 10, pady = 25)
n = tk.StringVar()    #data type  to store string type data
Author = ttk.Combobox(root, width = 27,textvariable = n)     #combo box is created
Author['values'] = ('Sidney Sheldon', 'Chetan Bhagat', 'Agatha Christe','Barbara Castland','Danielle Steel','Enid Blyton','J.K Rowling') #values in combo box
Author.grid(column = 1, row = 15)
btn1= Button(text = 'submit' , command=values)  #button 1 is created
btn1.grid()
root.mainloop()  #mainloop is ended
