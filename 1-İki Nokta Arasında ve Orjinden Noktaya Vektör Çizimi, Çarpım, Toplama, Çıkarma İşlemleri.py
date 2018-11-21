
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
x=[4,0]
y=[0,3]
get_ipython().magic('matplotlib inline')
plt.plot(x,y)


# In[3]:


def my_draw_a_vector_from_origin(v): # from origin to v
    plt.axes().set_aspect('equal')
    x=[0,v[0]]
    y=[0,v[1]]
    plt.xlim(0,20) #x ekseni sınır değerleri ayarladık
    plt.ylim(0,20) #y ekseni sınır değerleri ayarladık
    plt.plot(x,y)
my_draw_a_vector_from_origin([15,10])


# In[4]:


def my_draw_a_vector_from_v_to_w(v,w): # from v to w
    x=[v[0],w[0]]
    y=[v[1],w[1]]
    plt.xlim(2,6)
    plt.ylim(5,25)
    plt.plot(x,y)
my_draw_a_vector_from_v_to_w([5,10],[5,20])


# In[17]:


# iki vektorün skaler carpımı
def my_scalar_product(a,b):
    return (a[0]*b[0]+a[1]*b[1])
v=[3,4]
w=[4,7]
my_scalar_product(v,w)


# In[18]:


def distance(v,w):
    return (((v[0]-w[0])**2) + ((v[1]-w[1])**2))**.5


# In[19]:


def my_vector_add(v,w):
    return [v[0]+w[0],v[1]+w[1]]


# In[20]:


def my_vector_substract(v,w):
    return [v[0]-w[0],v[1]-w[1]]


# In[21]:


def my_vector_multiply_with_scalar(c,v):
    return [c*v[0],c*v[1]]


# In[23]:


a=[3,0]
b=[0,4]
print("Toplam  : ",my_vector_add(a,b))
print("Fark    : ",my_vector_substract(a,b))
print("B 5 katı: ",my_vector_multiply_with_scalar(5,b))
print("Uzunluk : ",distance(a,b))

