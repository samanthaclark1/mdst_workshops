#!/usr/bin/env python
# coding: utf-8

# # Python Lists

# ## Creating

# In[ ]:


# this is a python list
a = [42, 7, 13, 24601, 2001, 3.50]


# In[ ]:


# this is a list comprehension -- think of it as a sexy for loop

# the following gives us a list in which we multiplied each element in a by 2
z = [i * 2 for i in a]
z


# ## Indexing

# In[ ]:


# you can index into it
a[0]


# In[7]:


# what's the 3rd element?
a[2]


# In[ ]:


# indices can also be negative
# this gives you the last element
a[-1]


# ## Slicing

# In[ ]:


# you can also get subsets of the list with slicing
#     a[start:end]
# [start, end)

# this returns the 3rd and 4th entries (indices 2 and 3 -- note we exclude 4!)
a[2:4]


# In[ ]:


# if you leave one side blank, it automatically goes all the way
# first five:
a[:5]


# In[ ]:


# how do you get the last three elements?
a[3:6]


# In[ ]:


# slices can also skip numbers
# a[start:end:interval]

# this gives us every other number, starting with the first
a[::2]


# In[ ]:


# the interval can also be negative
# what does that do?

a[::-2]


# # Numpy

# In[ ]:


import numpy as np


# ## Creating

# In[ ]:


# numpy arrays can be created from a python list
b = np.array(a)
b


# Right now, it looks an awful like a python list, but there are some key points you should know.
# 
# numpy arrays are:
# - homogeneous (all elements in an array have the same type)
# - multidimensional

# In[ ]:


# Homogeneous: all numpy arrays have an associated data type.
# numbers are usually ints or floats
b.dtype


# In[ ]:


# Multidimensional: numpy arrays can have multiple dimensions, like a nested list.
# We can reshape b into a 3x2 matrix
# Note: this doesn't change b. That's why we assign it to a new variable: m
m = b.reshape(3, 2)
m


# In[ ]:


# Each dimension is called an axis
# The size across each axis is called the shape
# These are two very important concepts!
m.shape


# ## Indexing

# In[ ]:


# We index into numpy arrays much the same way as python lists.
b[0]


# In[ ]:


# But N-dimensional arrays mean we can be more expressive with indexing
# This gives us [0th index of axis 0, 1st index of axis 1]
# You can think of this as a grid
# Alternatively, this is like m[0][1]
m[0, 1]


# In[ ]:


# We can also pass in multiple indices as a list
# This gives us the 1st, 2nd, and 5th values of b
b[[0, 1, 4]]


# In[25]:


# Let's combine these two facts to get the 2nd and 3rd items in the second column of m
m[[1, 2]]


# In[ ]:


# We can also incorporate our previous knowledge of slices.
# So to get the second column
# This gives us the entire range on axis 0, and only the 1st index on axis 1
m[:,1]


# ## Math

# In[ ]:


# numpy gives us a lot of math functions to work with
# I'll only show you a couple, but you can find them all in the documentation

np.sum(b)  # guess what this does?


# In[ ]:


np.mean(b)  # and this?


# In[ ]:


# for convenience, you can also call
b.mean()


# In[ ]:


# you can also apply these functions to only one axis
# only sum across rows (read: apply the sum to axis 1)
np.sum(m, axis=1)


# In[ ]:


# numpy has a concept called podcasting
# It tries to coerce non-matching shapes.
# 2 is a scalar, but we can still multiply m by it
# it just repeats the 2 across all instances of m
m * 2


# # Pandas

# In[ ]:


import pandas as pd


# ## Creating
# 
# Pandas lets us read all sorts of data into a Dataframe. Think of this as a series of lists. Let's look at an example.

# In[ ]:


df = pd.read_csv("./cereal.csv")
type(df)


# In[ ]:


# head() gives us the first 10 rows in the dataframe (pd.DataFrame)
df.head()


# In[ ]:


# you can think of each column as a list (or a 1D numpy array)
# in practice, these are called pandas Series (pd.Series)
# you can index into the dataframe with a string to get one column
df["name"]


# In[ ]:


type(df["name"])


# ## Pandas Series vs Numpy Arrays

# In[ ]:


# There are many similarities between pd.Series and np.ndarray
# for example:
df["carbo"].mean()


# In[ ]:


# In fact, we can turn pd.Series into a numpy array
# again, this returns a numpy array -- df["carbo"] doesn't change.
df["carbo"].to_numpy()


# In[ ]:


# The key difference is that Series are indexed
# See the 0, 1, ... 76 on the left? That is the index of each item.
# Right now they are just positions, but theoretically they can be any unique identifier for the row
# Think: ID, username, etc
df["carbo"].index


# ## Indexing into DataFrames and Series

# In[ ]:


# Indexing is a little bit different in pandas.
# One parallel to what you've been used to is .loc[]
# this is the row at index 0
df.loc[0]


# In[ ]:


# multiple indices work
df.loc[[1, 2, 3]]


# In[ ]:


# caveat: remember that pandas doesn't require zero-indexing. indices can be anything.
# this means slicing might not work all the time (what would df.loc["asdf":"hjkl"] even mean?)
# in the cases that you actually want to index by row number, you can always do that with .iloc[]
# again, this will behave the same as .loc[] with our dataset because our data is 0-indexed
df.iloc[0]


# In[ ]:


# We can also use boolean indexing by passing a list of booleans like so:
df[[True] + [False] * 76]
# Let me explain:
# - [True] + [False] * 76 gives us a list that looks like [True, False, ..., False] with 1 True and 76 Falses
# - This matches the number of rows in our data (77)
# - pandas returns all the rows with a corresponding True (in this case, only the first one)


# In[ ]:


# This is powerful because we can also make comparisons with Series and values.
df["protein"] > 3


# In[ ]:


# Combining these two things, we have a very expressive way of filtering.
# This gives us all the rows in which the protein is greater than 3.
df[df["protein"] > 3]


# ## Manipulating Series
# 
# Often when we're preprocessing data, we want to make uniform changes to a specific column. We can do this by applying functions.

# In[ ]:


# Suppose we want to make the cereals more appetizing.
# Let's add "Delicious " to the beginning of every name.

# The pattern is we define a function for a single entry
def make_delicious(name):
    return "Delicious " + name

# and then call apply on the series to apply the function to each element in the series
df["name"].apply(make_delicious)


# In[ ]:


# this returns the changes, but doesn't apply them in place.
# that means on our original dataframe, the cereals are still bland
df.head()


# In[ ]:


# we can fix this by assigning the new names to the column.
df["name"] = df["name"].apply(make_delicious)
df.head()


# In[5]:


# here's another example.
# Jackson is a skeptic and doesn't believe calling things "Delicious" makes them taste better.
# But he does think adding sugar will make them taste better.
# How can we add 10 grams of sugar to every cereal?
df["sugars"] = ???


# ## Groups and Aggregates
# 
# When we have lots and lots of data, it's more useful to look at aggregate statistics like the mean or median. But sometimes we lose too much detail aggregating across the whole dataset.
# 
# The solution is to aggregate across groups. For example, maybe we're less interested in the mean calorie count of all cereals and more interested in the mean for each manufacturer.

# In[6]:


# First, we can see how many (and which) unique manufacturers there are
# Note: this gives us a numpy array
df["mfr"].unique()


# In[ ]:


# Now let's group by the manufacturers
# This gives us a groupby object across the dataframe
mfrs = df.groupby("mfr")
mfrs


# In[ ]:


# what happens if we try to access the calories column?
mfrs["calories"]


# In[ ]:


# now let's try to get the mean
mfrs["calories"].mean()


# In[ ]:


# we can also aggregate across multiple columns, and even use different aggregations
# let's get the average calorie count but the maximum protein
mfrs[["calories", "protein"]].agg({"calories": "mean", "protein": "max"})


# # Exercises
# 
# Unless otherwise noted, these should be one line of code.

# In[14]:


# here is a Python list:

a = [1, 2, 3, 4, 5, 6]

# get a list containing the last 3 elements of a
x= a[3:6]
x

# reverse the list
y=a[::-1]
y

# get a list where each entry in a is cubed (so the new list is [1, 4, 9, 16, 25, 36])
z = [i ** 3 for i in a]
z


# In[21]:


# create a numpy array from this list
b = [1, 2, 3, 4, 5, 6] # change this
import numpy as np
s = np.array(b)
s


# In[18]:


# find the mean of b
np.mean(b)


# In[23]:


# change b from a length-6 list to a 2x3 matrix
m = s.reshape(2, 3)
m


# In[33]:


# find the mean value of each row
f = m.mean(1)
f


# In[34]:


# find the mean value of each column
f = m.mean(0)
f


# In[40]:


# find the third column of b
f = m[:,2]
f


# In[41]:


# get a list where each entry in b is cubed (so the new numpy array is [1, 4, 9, 16, 25, 36])
# use a different (numpy-specific) approach
s**3


# In[52]:


# load in the "starbucks.csv" dataset]
import pandas as pd
df = pd.read_csv("starbucks.csv")
type(df)
df.head()


# In[54]:


# this is nutritional info for starbucks items
# let's see if we can answer some questions

# what is the average # calories across all items?
df["Calories"].mean()


# In[56]:


# how many different categories of beverages are there?
df["Beverage"].unique


# In[110]:


# what is the average # calories for each beverage category?
bc = df.groupby("Beverage_category")
bc
bc["Calories"].mean()


# In[109]:


# what beverage preparation includes the most sugar?
bp = df.groupby("Beverage_prep")
bp
(bp[" Sugars (g)"].mean()).argmax()


# In[123]:


# what is the average % daily value calcium content for each beverage?
# HINT: make sure your columns have the datatypes you want
# (you can use more than one line for this one)
b = df.groupby("Beverage")
b

def make_non(calc):
    return calc.rstrip("%")

# and then call apply on the series to apply the function to each element in the series
w = df[" Calcium (% DV) "].apply(make_non)
b[w].mean()


# In[125]:


# It's bulking season. What drink should Jackson get so that he maximizes protein but minimizes fat?
# (you can use more than one line for this one)
r = df[" Protein (g) "]/df[" Total Fat (g)"]
r
r.max()


# In[ ]:




