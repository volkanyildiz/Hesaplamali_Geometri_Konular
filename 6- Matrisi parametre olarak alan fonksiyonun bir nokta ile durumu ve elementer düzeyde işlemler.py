
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
get_ipython().run_line_magic('matplotlib', 'inline')

def my_function(matrix):

    point1= np.array([0,0,0])

    normal1=np.array(matrix[0])
    normal2=np.array(matrix[1])
    normal3=np.array(matrix[2])

    d1=-np.sum(point1*normal1)
    d2=-np.sum(point1*normal2)
    d3=-np.sum(point1*normal3)

    xx,yy=np.meshgrid(range(5),range(5))

    z1=(-normal1[0]*xx-normal1[1]*yy -d1)*1./normal1[2]
    z2=(-normal2[0]*xx-normal2[1]*yy -d2)*1./normal2[2]
    z3=(-normal3[0]*xx-normal3[1]*yy -d3)*1./normal3[2]

    plt3d=plt.figure().gca(projection='3d')
    plt3d.plot_surface(xx,yy,z1,color='green')
    plt3d.plot_surface(xx,yy,z2,color='red')
    plt3d.plot_surface(xx,yy,z3,color='blue')





# In[8]:


matrix= np.zeros((3,3))
matrix[0,0]=4
matrix[0,1]=5
matrix[0,2]=6
matrix[1,0]=7
matrix[1,1]=8
matrix[1,2]=9
matrix[2,0]=10
matrix[2,1]=11
matrix[2,2]=12
    
    
my_function(matrix)


# In[11]:


matrix[1]=matrix[1]+matrix[2]*matrix[1]
my_function(matrix)


# In[12]:


matrix[0]=matrix[0]-matrix[1]*matrix[1]
my_function(matrix)

