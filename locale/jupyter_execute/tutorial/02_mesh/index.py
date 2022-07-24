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


import numpy as np
import pyvista as pv

points = np.random.rand(100, 3)
mesh = pv.PolyData(points)
mesh.plot(point_size=10, style='points', color='tan')


# In[3]:


from pyvista import examples

mesh = examples.load_hexbeam()
cpos = [(6.20, 3.00, 7.50),
        (0.16, 0.13, 2.65),
        (-0.28, 0.94, -0.21)]

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_points(mesh.points, color='red', point_size=20)
pl.camera_position = cpos
pl.show()


# In[4]:


mesh = examples.download_bunny_coarse()

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_points(mesh.points, color='red', point_size=20)
pl.camera_position = [(0.02, 0.30, 0.73),
                      (0.02, 0.03, -0.022),
                      (-0.03, 0.94, -0.34)]
pl.show()


# In[5]:


mesh = examples.load_hexbeam()

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_points(mesh.points, color='red', point_size=20)

single_cell = mesh.extract_cells(mesh.n_cells - 1)
pl.add_mesh(single_cell, color='pink', edge_color='blue',
            line_width=5, show_edges=True)

pl.camera_position = [(6.20, 3.00, 7.50),
                      (0.16, 0.13, 2.65),
                      (-0.28, 0.94, -0.21)]
pl.show()


# In[6]:


mesh.point_data['my point values'] = np.arange(mesh.n_points)
mesh.plot(scalars='my point values', cpos=cpos, show_edges=True)


# In[7]:


mesh.cell_data['my cell values'] = np.arange(mesh.n_cells)
mesh.plot(scalars='my cell values', cpos=cpos, show_edges=True)


# In[8]:


cube = pv.Cube()
cube.cell_data['myscalars'] = range(6)

other_cube = cube.copy()
other_cube.point_data['myscalars'] = range(8)

pl = pv.Plotter(shape=(1, 2), border_width=1)
pl.add_mesh(cube, cmap='coolwarm')
pl.subplot(0, 1)
pl.add_mesh(other_cube, cmap='coolwarm')
pl.show()

