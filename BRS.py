#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd



# In[2]:





# In[3]:


ratings = pd.read_csv("ratings.csv")
ratings.head()


# In[4]:


books = pd.read_csv("books.csv")
books.head()


# In[5]:


n_ratings = len(ratings)
n_books = len(ratings['Book_Id'].unique())
n_authors = len(ratings['Author_Id'].unique())


# In[6]:


print(f"Number of ratings: {n_ratings}")
print(f"Number of unique movieId's: {n_books}")
print(f"Number of unique users: {n_authors}")
print(f"Average ratings per books: {round(n_ratings/n_books, 2)}")
print(f"Average ratings per author: {round(n_ratings/n_authors, 2)}")


# In[7]:


author_freq = ratings[['Author_Id', 'Book_Id']].groupby('Author_Id').count().reset_index()
author_freq.columns = ['Author_Id', 'n_ratings']
author_freq.head()


# In[8]:


# Find Lowest and Highest rated movies:
mean_rating = ratings.groupby('Book_Id')[['Rating']].mean()
# Lowest rated movies
lowest_rated = mean_rating['Rating'].idxmin()
books.loc[books['Book_Id'] == lowest_rated]


# In[9]:


# Highest rated movies
highest_rated = mean_rating['Rating'].idxmax()
books.loc[books['Book_Id'] == highest_rated]


# In[10]:


# show number of people who rated movies rated movie highest
ratings[ratings['Book_Id']==highest_rated]


# In[11]:


# show number of people who rated movies rated movie lowest
ratings[ratings['Book_Id']==lowest_rated]


# In[12]:


Book_stats = ratings.groupby('Book_Id')[['Rating']].agg(['count', 'mean'])
Book_stats.columns = Book_stats.columns.droplevel()
Book_stats


# In[13]:


def recommend(author):
    Au_name= books[books.Author_name == author].Book_name.values
    book_list=list(Au_name)
    
    for i in book_list:
        print(i)


# In[14]:


def recommend(author):
    Au_name = books[books.Author_name == author].Book_name.values
    book_list = list(Au_name)

    for i in book_list:
        print(i)


# In[15]:


recommend('Sidney Sheldon')


# In[16]:


mergedDf = books.merge(ratings, on='Book_Id')


# In[17]:


mergedDf


# In[18]:


def reccommend(author):
    Au_name= mergedDf[mergedDf.Author_name == author].Book_name.values
    book_list=list(Au_name)
    
    for i in book_list:
        print(i)


# In[19]:


reccommend('Chetan Bhagat')


# In[21]:


import pickle as pk


# In[24]:


pk.dump(mergedDf.to_dict(),open('Books_dict.pkl','wb'))


# In[26]:


mergedDf[mergedDf.Author_name == 'J.K Rowling'].Book_name.values[1:6]


# In[ ]:




