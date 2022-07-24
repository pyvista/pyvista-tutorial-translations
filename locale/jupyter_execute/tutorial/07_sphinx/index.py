#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = 'world'
print('hello ' + name + '!')


# In[2]:


from pyvista import examples
dataset = examples.download_urn()
dataset.plot(color='tan', jupyter_backend='pythreejs', window_size=(700, 400))


# In[3]:


from pyvista import demos
demos.plot_logo(background='white', jupyter_backend='panel')


# In[4]:


import pyvista as pv
from pyvista import examples

# create a point cloud from lidar data and add height scalars
dataset = examples.download_lidar()
point_cloud = pv.PolyData(dataset.points[::100])
point_cloud['height'] = point_cloud.points[:, 2]
point_cloud.plot(window_size=[500, 500],
                 jupyter_backend='panel',
                 cmap='jet',
                 point_size=2,
                 background='w')


# In[5]:


import pyvista as pv
pv.set_jupyter_backend('panel')


# In[6]:


from pyvista import examples
dataset = examples.download_dragon()
dataset.plot(cpos="xy")

