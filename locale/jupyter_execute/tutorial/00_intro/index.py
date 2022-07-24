#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Configure for panel
import pyvista
pyvista.set_jupyter_backend('panel')
pyvista.global_theme.background = 'white'
pyvista.global_theme.window_size = [600, 400]
pyvista.global_theme.axes.show = False
pyvista.global_theme.smooth_shading = True
pyvista.global_theme.antialiasing = True


# In[2]:


from pyvista import examples
mesh = examples.download_bunny()
mesh.plot(cpos='xy')


# In[3]:


import pyvista as pv
import numpy as np
points = np.random.random((1000, 3))
pc = pv.PolyData(points)
pc.plot(scalars=points[:, 2], point_size=5.0, cmap='jet')

