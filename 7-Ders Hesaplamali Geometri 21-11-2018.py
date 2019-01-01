
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import numpy as np


# In[19]:


a=5
b=3
#plot the elipse
x=np.linspace(-5.0,5.0,num=500)
y=(b**2)*(1-(x**2)/(a**2))**.5
get_ipython().magic('matplotlib inline')
plt.plot(x,y)
plt.plot(x,-y)

