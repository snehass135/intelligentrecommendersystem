import tkinter as tk     #importing tkinter for gui
from tkinter import *
from tkinter import ttk
import pickle as pk     #importing pickle to convert object hierarchy into data stream and vice-versa
import pandas as pd     #importing pandas for dataframe
Book_dict = pk.load(open('Books_dict.pkl','rb'))  #convert data stream to object hierarchy
Books = pd.DataFrame(Book_dict)
def values():  #values are defined to print book list
    Auth = Author.get()
    Au_name = Books[Books.Author_name == Auth].Book_name.values[1:6]
    book_list = list(Au_name)
    for i in book_list:
        print(i)
root = tk.Tk()   #starting mainloop
root.geometry('1080x1080')   #size for tkinter window is 1080 x 1080
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
