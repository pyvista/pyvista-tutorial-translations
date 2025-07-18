"""
.. _box_widget_example:

Box Widget
~~~~~~~~~~

The box widget can be enabled and disabled by the
:func:`pyvista.Plotter.add_box_widget` and
:func:`pyvista.Plotter.clear_box_widgets` methods respectively.
When enabling the box widget, you must provide a custom callback function
otherwise the box would appear and do nothing - the callback functions are
what allow us to leverage the widget to perform a task like clipping/cropping.

Considering that using a box to clip/crop a mesh is one of the most common use
cases, we have included a helper method that will allow you to add a mesh to a
scene with a box widget that controls its extent, the
:func:`pyvista.Plotter.add_mesh_clip_box` method.

.. image:: ../../images/gifs/box-clip.gif
"""

import pyvista as pv
from pyvista import examples

mesh = examples.download_nefertiti()

# %%

pl = pv.Plotter()
pl.add_mesh_clip_box(mesh, color="white")
pl.show(cpos=[-1, -1, 0.2])


# %%
# After interacting with the scene, the clipped mesh is available as:
pl.box_clipped_meshes

# %%
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/08_widgets/a_box-widget.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
