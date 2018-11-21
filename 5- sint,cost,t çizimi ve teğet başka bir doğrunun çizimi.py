
# coding: utf-8

# In[6]:


# define a vectorel function and
# define its derivative
# comment them
# draw the derivative dor a point in the curve
# https://calculus-notes.readthedocs.io/en/latest/1.2_calc_derivatives.html

# sin t cos t  t  vektör değerli fonk grafiğini çiziniz
# teğet olan vektörü çiziniz

# sint,cost,t
# cost,sint,1  türevi
# t=10

#b şıkkı
#x=a cos t
#y=b sin t  olarak tanımlanmış eğrinin t = 3*pi/2 deki teğet doğrusunu çiziniz

#c şıkkı   x=6t  y=3t^2  z=t  olan eğrinin t=10 daki teğetini çiziniz


# In[14]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math


# In[21]:


get_ipython().magic('matplotlib notebook')
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)  
x = np.sin(theta)
y = np.cos(theta)
z = theta
ax.plot(x, y, z, 'b', lw=2)


# In[19]:


theta_current = 3 * np.pi/2  #türev.çalışılan nokta 3*np.pi/2 olsun. 
x_1=math.cos(theta_current)  #Teğet olan vektörün büyüklüğü
y_1=math.sin(theta_current)
z_1=1

x_2=math.sin(theta_current) 
y_2=-math.cos(theta_current)
z_2=theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]

ax.plot(x_s,y_s,z_s)
plt.show()


# In[20]:


t=10
sorub1,sorub2,sorub3 = 6*t, 3*t**2, t
sorubt1,sorubt2,sorubt3 = 6, 6*t, 1

soruSonuc1,soruSonuc2,soruSonuc3 = sorub1+sorubt1, sorub2+sorubt2, sorub3+sorubt3
soru_x_s, soru_y_s, soru_z_s = [soruSonuc1,sorub1],[soruSonuc2,sorub2],[soruSonuc3,sorub3]


ax.plot(soru_x_s,soru_y_s,soru_z_s)
plt.show()

