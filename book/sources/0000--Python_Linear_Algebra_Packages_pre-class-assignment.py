# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

#

# # Supplemental Materials: Python Linear Algebra Packages
#
# This course uses Python to help students gain a practical understanding of how to use Linear Algebra to solve problems. Although students will likely become better programmers this course does not teach programming and assumes that that students have a basic understanding of Python.  
#
# This notebook is designed to provide a review of the major Python Packages we will be using in this course and includes some common techniques you can use to avoid problems. 
#
# I hope all students will learn something from the videos. However, feel free to run them at a faster speed and/or skip ahead if you feel you know what you are doing.  
#

# ---
# ### Overview
# 1. [Matplotlib](#Matplotlib)
# 2. [Review of Python Math Package](#Review_of_Python_Math_Package)
# 3. [Review of Python Numpy Package](#Review_of_Python_Numpy_Package)
# 4. [Advanced Python Indexing](#Advanced_Python_Indexing)
# 5. [LaTeX Math](#LaTeX_Math)
# 6. [Jupyter Tips and Tricks](#More_about_Jupyter)

# ----
# <a name="Matplotlib"></a>
#
# ## 1. Matplotlib
#
# We will be using the ```matplotlib``` library quite a bit to visualize the concepts in this course.  This is a very big library with a lot of components.  Here are some basics to get you started.
#
# First, in order to see the figures generated by the ```matplotlib``` library in a jupyter notebook you will need to add the following like to a code cell somewhere near the top of the notebook. This like of code must run before any figures will display.

# %matplotlib inline

# Next, we typically we import either the ```pylab```  or ```pyplot``` packages from the ```matplotlib``` library using one of the following import statements.  In most cases these statements are interchangeable, however, in this class we will generally stick to using ```pyplot``` because it has a little more functionality. 

import matplotlib.pylab as plt

# or

import matplotlib.pyplot as plt

# The basic way to plot values is to use the ```plot``` function as follows:

y = [0,1,4,9,16,25,36]
plt.plot(y);

# The ```matplotlib``` library is big!!! There is no way we can cover all of the topics in this notebook. However, it is not that hard to use and there are plenty of tutorials  and examples on the Internet.  
#
#
# &#9989; <font color=red>**DO THIS:**</font> Review the ```matplotlib``` examples in the [Matplotlib Example Gallary](https://matplotlib.org/gallery/index.html).

# ----
#
# <a name="Review_of_Python_Math_Package"></a>
#
# ## 2. Review of Python Math Package

# [Direct Link](https://youtu.be/PBlKeuzUf5g) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("PBlKeuzUf5g",width=640,height=320, cc_load_policy=True)

# &#9989; <font color=red>**DO THIS:**</font>   In the following cell, load the math package and run the ```hypot``` function with inputs (3,4).  

# +
#Put your answer here
# -

# &#9989; <font color=red>**QUESTION:**</font>   What does the ```hypot``` function do?

# Put your answer to the above question here.

# ----
# <a name="Review_of_Python_Numpy_Package"></a>
#
# ## 3. Review of Python Numpy Package

# [Direct Link](https://youtu.be/_hbWtNgstlI) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("_hbWtNgstlI",width=640,height=320, cc_load_policy=True)

# The Python Numpy library has a "Matrix" object which can be initialized as follows:

import numpy as np
A = np.matrix([[1,1], [20,25]])
b = np.matrix([[30],[690]])
print("A="+str(A))
print("b="+str(b))

# Python can solve equations in the $Ax=b$ format with the ```numpy.linalg``` library.  For example:

# +
import numpy as sp

x = sp.linalg.solve(A, b)
print("X="+str(x))
# -

# The ```numpy.linalg``` library is just a subset of the ```scipy.linalg``` library.  Oddly you can't load the SciPy library the same way.  Instead you can call it as follows:

# +
import scipy.linalg as la

x = la.solve(A, b)
print("X="+str(x))
# -

# &#9989; <font color=red>**DO THIS:**</font>    Convert the following system of linear equations to numpy matrices and solve using a python linear algebra solver
# $$ 18x+21y = 226$$
# $$ 72x-3y = 644$$

# +
##Put your answer to the above question here.
# -

# ----
#
# <a name="Advanced_Python_Indexing"></a>
#
# ## 4. Advanced Python Indexing
#
# This one is a little long and reviews some of the information from the last video. However, I really like using images as a way to talk about array and matrix indexing in ```Numpy```.

# [Direct Link](https://youtu.be/XSyiafkKerQ) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("XSyiafkKerQ",width=640,height=360, cc_load_policy=True)

# +
# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import imageio

#from urllib.request import urlopen, urlretrieve
from imageio import imsave

url = 'https://res.cloudinary.com/miles-extranet-dev/image/upload/ar_16:9,c_fill,w_1000,g_face,q_50/Michigan/migration_photos/G21696/G21696-msubeaumonttower01.jpg'
im = imageio.imread(url)

im[10,10,0] = 255
im[10,10,1] = 255
im[10,10,2] = 255

#Show the image
plt.imshow(im);
# -

im[20,20,:] = 255
plt.imshow(im)

cropped = im[0:50,0:50,:]
plt.imshow(cropped)

cropped = im[50:,350:610,:]
plt.imshow(cropped)

red = im[:,:,0]
plt.imshow(red)
plt.colorbar()

# +
#Note python changed slightly since the making of the video.  
# We added the astype funciton to ensure that values are between 0-255
red_only = np.zeros(im.shape).astype(int)
red_only[:,:,0] = red

plt.imshow(red_only)

# +
green_only = np.zeros(im.shape).astype(int)
green_only[:,:,1] = im[:,:,1]

plt.imshow(green_only)

# +
blue_only = np.zeros(im.shape).astype(int)
blue_only[:,:,2] = im[:,:,2]

plt.imshow(blue_only)
# -

# &#9989; <font color=red>**DO THIS:**</font>   Modify the following code to set all of the values in the blue channel to zero using only one simple line of indexing code. 
#

# +
no_blue = im.copy()

#put your code here

plt.imshow(no_blue)
# -

# &#9989; <font color=red>**QUESTION:**</font>   What was the command you use to set all of the values of blue inside no_blue to zero?

# &#9989; Put your answer here. Copy and paste your answer to the form in the Assignment wrap-up.

# ----
# <a name="LaTeX_Math"></a>
# ## 6. LaTeX Math
#

# [Direct Link](https://youtu.be/qgSa7n_zQ3A) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("qgSa7n_zQ3A",width=640,height=320, cc_load_policy=True)

# Since this is a "Matrix Algebra" course, we need to learn how to do 'matrices' in LaTeX. Double click on the following cell to see the LaTeX code to build a matrix:
#

# Basic matrix notation:
#
# $$ 
# \left[
# \begin{matrix}
#     1   & 0 & 4  \\
#     0   & 2 & -2  \\
#     0   & 1 & 2 
# \end{matrix}
# \right] 
# $$
#
# Augmented matrix notation:
#
# $$ 
# \left[
# \begin{matrix}
#     1   & 0 & 4  \\
#     0   & 2 & -2  \\
#     0   & 1 & 2 
#  \end{matrix}
# \, \middle\vert \,
# \begin{matrix}
# -10 \\ 3 \\ 1
# \end{matrix}
# \right] 
# $$

# &#9989; <font color=red>**DO THIS:**</font>   Using LaTeX, create an augmented matrix for the following system of equations:
#
# $$4x + 2y -7z = 3$$
# $$12x + z = 10$$
# $$-3x -y + 2z = 30$$
#

# Put your LaTeX code here. (Hint, copy and paste from above)

# &#9989; <font color=red>**QUESTION:**</font>  In LaTeX, what special characters is used to separate elements inside a row?

# Put your answer here.

# -----
# <a name="More_about_Jupyter"></a>
#
# ## 7. Jupyter Tips and Tricks
# For those of you new to Jupyter notebooks you may want to consider watching the following video as well. 
# More about Jupyter Notebooks.
#
# [Direct Link](https://youtu.be/zSDfRY8-3QE)

from IPython.display import YouTubeVideo
YouTubeVideo("zSDfRY8-3QE",width=640,height=320, cc_load_policy=True)

#
#
