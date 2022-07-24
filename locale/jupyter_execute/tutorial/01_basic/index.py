#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Configure for panel
import pyvista
pyvista.set_jupyter_backend('panel')
pyvista.global_theme.background = 'white'
pyvista.global_theme.axes.show = False
pyvista.global_theme.smooth_shading = True
pyvista.global_theme.antialiasing = True


# In[2]:


from pyvista import examples
dataset = examples.download_saddle_surface()
dataset


# In[3]:


dataset.plot(color='tan')


# In[4]:


dataset = examples.download_frog()
dataset


# In[5]:


dataset.plot(volume=True)


# In[6]:


import pyvista as pv
dataset = pv.read('ironProt.vtk')
dataset


# In[7]:


dataset.plot(volume=True)

