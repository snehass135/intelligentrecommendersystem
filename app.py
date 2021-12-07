import tkinter as tk
from tkinter import *
import pickle as pk
import pandas as pd

Book_dict = pk.load(open('Books_dict.pkl','rb'))
Books = pd.DataFrame(Book_dict)

def values():
    Auth = Author.get()
    Au_name= Books[Books.Author_name == Auth].Book_name.values[1:6]
    book_list=list(Au_name)

    for i in book_list:
        print(i)   

window = Tk()
window.geometry('1080x1080')
window['bg']="yellow"

Label(text="Book Reccomondation system", font= ("Times New Roman", 20)).grid()

# font = ("Times New Roman", 20))

ttk.Label(window, text = "Select Author to recommend: ", 
        font = ("Times New Roman", 15)).grid(column = 0,
        row = 15, padx = 10, pady = 25)

n = tk.StringVar()
Author = ttk.Combobox(window, width = 27, 
                            textvariable = n)
  
# Adding combobox drop down list
Author['values'] = ('Sidney Sheldon', 'Chetan Bhagat', 'Agatha Christe','Barbara Castland','Danielle Steel','Enid Blyton','J.K Rowling')
  
Author.grid(column = 1, row = 15)
Button(text = 'submit' , command=values).grid()
window.mainloop()
