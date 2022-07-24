#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyvista as pv
pv.set_plot_theme('document')
pv.global_theme.jupyter_backend = 'static'


# In[2]:


import pyvista as pv
from pyvista import examples

dataset = examples.download_lucy()
dataset.plot(smooth_shading=True, color='white')


# In[3]:


import pyvista as pv
from pyvista import examples
pv.global_theme.jupyter_backend = 'panel'

dataset = examples.download_lidar()
dataset.plot(cmap="gist_earth")


# In[4]:


import pyvista as pv
from pyvista import examples
pv.global_theme.jupyter_backend = 'pythreejs'
pv.global_theme.window_size = (700, 300)
pv.global_theme.antialiasing = True

dataset = examples.download_cad_model()
dataset.plot(background='w', pbr=True, metallic=0.6, roughness=0.4, split_sharp_edges=True)

