# -*- coding: utf-8 -*-
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

#

# # 12 In-Class Assignment: Matrix Representation
#
# <img alt="Alternative visual representation showing how the four Fundamental Subspaces spaces map to each other" src="https://upload.wikimedia.org/wikipedia/commons/4/4c/KerIm_2015Joz_L2.png" width="50%">
#
# Image from: [wikipedia](https://en.wikipedia.org/wiki/Kernel_(linear_algebra))
#

# ### Agenda for today's class (80 minutes)
#
# 1. [(20 minutes) Review Pre-class assignment](#Review_Pre-class_assignment)
# 1. [(30 minutes) Matrix Representation of Vector Spaces](#Matrix_Representation_of_Vector_Spaces)
# 1. [(30 minutes) Practice Example](#Practice_Example)

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing(use_unicode=True)

# ----
# <a name="Review_Pre-class_assignment"></a>
# ## 1. Review Pre-class assignment
#
# * [12--Change_Basis_pre-class-assignment.ipynb](12--Change_Basis_pre-class-assignment.ipynb)

# ----
# <a name="Matrix_Representation_of_Vector_Spaces"></a>
# ## 2. Matrix Representation of Vector Spaces

# Consider the following matrix $A$. 
#
# $$ 
# \left[
# \begin{matrix}
#     1 & 0 & 3  \\
#     0 & 1 & 5  \\
#     1 & 1 & 8 
# \end{matrix}
# \right] 
# $$

# &#9989; **<font color=red>QUESTION:</font>** What is the reduced row echelon form of $A$?

# +
# Put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer.matrix(rref,'1731818a1555cc33a778a4eb76af945c');
# -

# **ROW SPACE** The first and second (non zero) rows of the above matrix "spans" the same space as the orignal three row vectors in $A$. We often call this the "row space" and it can be written as a linear combination of the non-zero rows of the reduced row echelon form:
#
# $$row(A) = r(1,0,3)^\top+s(0,1,5)^\top$$

# &#9989; **<font color=red>DO THIS:</font>** Calculate  the solutions to the system of homogeneous equations $Ax=0$. This is often called the **NULL SPACE** or sometimes **KERNEL** of $A$.

# +
#Put your asnwer here
# -

# &#9989; **<font color=red>DO THIS:</font>** We introduced two subspaces. 
# Pick one vector from the row space of $A$ and another vector from the null space of $A$. 
# Find the dot product of these two vector.

# +
#Put your answer here
# -

# &#9989; **<font color=red>Question:</font>** Did you get the same value for the dot product? Explain your answer. 

# Put your answer to the above question here

# &#9989; **<font color=red>DO THIS:</font>** What is the reduced row echelon form of $A^T$?

# +
#Put your answer here
# -

# **COLUMN SPACE:** The first and second (non zero) rows of the above matrix "spans" the same space as the original three column vectors in $A$. We often call this the "column space" (or "image space") of $A$ and it can be written as a linear combination of the non-zero rows of the reduced row echelon form of $A^T$:
#
# $$col(A) = a(1,0,1)^\top+b(0,1,1)^\top$$

# &#9989; **<font color=red>DO THIS:</font>** Calculate the solutions to the system of homogeneous equations $A^Tx=0$. This is often called the **NULL SPACE** of $A^T$.

# <font size=8 color="#009600">&#9998;</font> Do This - Erase the contents of this cell and replace it with your answer to the above question!  (double-click on this text to edit this cell, and hit shift+enter to save the text)

# ---
# ### Example #1 

# Consider the following system of linear equations.
#
# $$ x_1 - x_2 + x_3 = 3 $$
# $$ -2x_1 + 2x_2 - 2x_3 = -6 $$

# &#9989; **<font color=red>DO THIS:</font>** What are the solutions to the above system of equations?

# +
# Put your code here
# -

# &#9989; **<font color=red>DO THIS:</font>** Come up with a specific arbitrary solution (any solution will do) to the above set of equations.

# Put your answer to the above question here.

# &#9989; **<font color=red>DO THIS:</font>** Now consider only the left hand side of the above matrix and solve for the kernel (null Space) of A:
#
#
# $$ A = 
# \left[
# \begin{matrix}
#     1 & -1 & 1  \\
#     -2 & 2 & -2  
# \end{matrix}
# \right] 
# $$

# +
#Put your answer here
# -

# &#9989; **<font color=red>DO THIS:</font>** Express an arbitrary solution as the sum of an element of the kernel of the transformation defined by the matrix of coefficients and a particular solution.

# Put your answer to the above question here.

# &#9989; **<font color=red>DO THIS:</font>** Discuss in your group and the class your solution from above. How does the solution to $Ax=b$ relate to the solution to $Ax=0$.  If you were to plot all solutions, what shape does it take? How does this shape relate to the kernel?

# Put your answer to the above question here.

# ----
# <a name="Practice_Example"></a>
# ## 3. Practice Nutrition
#
# Big Annie's Mac and Cheese fans want to improve the levels of protein and fiber for lunch by adding broccoli and canned chicken. 
# The nutrition information for the foods in this problem are 
#
#
# |Nutrient    | Mac and Cheese           |  Broccoli        |    Chicken   | Shells and White Cheddar |
# |----|-----------------|----------------|----------|----------|
# |Calories| 270 | 51 |  70 | 260 |
# |Protein (g) | 10 | 5.4 |  15| 9|
# |Fiber (g)| 2   |  5.2 |  0| 5|
#
#
# <img alt="Logo for Annie's Mac and Cheese" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Annies_logo.png" width="50%">

# She wants to achieve the goals with exactly 400 calories, 30 g of protein, and 10 g of fiber by choosing the combination of these three or four serving. (Assume that we can have non-integer proportions for each serving.)

# &#9989; **<font color=red>Question a</font>**: We consider all **four** choices of food together. Formulate the problem into a system of equations 
# $$Ax = b.$$
# Create your matrix $A$ and the column vector $b$ in *np.matrix*. 

import numpy as np
#####Start your code here #####
A = np.matrix()
b = np.matrix()
#####End of your code here#####

# &#9989; **<font color=red>Question b</font>**: In this and next question, we only consider **three** out of the four choices. What proportions of these servings of the **three** food (Mac and Cheese, Broccoli, and Chicken) should be used to meet the goal? (Hint: formulate it as a system of equations and solve it).

# +
#Put your answer here
# -

# &#9989; **<font color=red>Question c</font>**: She found that there was too much broccoli in the proportions from part (b), so she decided to switch from classical Mac and Cheese to Annie’s Whole Wheat Shells and White Cheddar. What proportions of servings of the new **three** food should she use to meet the goals?

# +
#Put your answer here
# -

# &#9989; **<font color=red>Question d</font>**: Based on the solutions to parts (b) and (c), what are the possible proportions of serving for the **four** food that meet the goal. 

# **Put your answer here**

# &#9989; **<font color=red>Question e</font>**: Solve the system of equations from part (a). You need to first decide the three outcomes: One solution, None solution, Infinite many solutions. Then for *One solution*, write down the solution; for *Infinite many solutions*, write down all the solutions with free variables. 

# +
#Put your answer here
# -

# **Put your answer here**

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
