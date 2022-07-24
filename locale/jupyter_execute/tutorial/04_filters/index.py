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

dataset = examples.load_uniform()
dataset.set_active_scalars("Spatial Point Data")

# Apply a threshold over a data range
threshed = dataset.threshold([100, 500])

outline = dataset.outline()


# In[3]:


p = pv.Plotter()
p.add_mesh(outline, color="k")
p.add_mesh(threshed)
p.camera_position = [-2, 5, 3]
p.show()


# In[4]:


result = dataset.threshold().elevation().clip(normal="z").slice_orthogonal()


# In[5]:


p = pv.Plotter()
p.add_mesh(outline, color="k")
p.add_mesh(result, scalars="Elevation")
p.view_isometric()
p.show()

