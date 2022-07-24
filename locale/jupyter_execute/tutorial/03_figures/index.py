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


import pyvista as pv
from pyvista import examples

mesh = pv.Wavelet()

p = pv.Plotter()
p.add_mesh(mesh)
p.show()


# In[3]:


p = pv.Plotter()
p.add_mesh(mesh, cmap='coolwarm')
p.show()


# In[4]:


p = pv.Plotter()
p.add_mesh(mesh, show_edges=True)
p.show()

