:orphan:



.. _sphx_glr_tutorial_08_widgets:

.. _widgets:

Widgets in PyVista
==================

PyVista has several widgets that can be added to the rendering scene to control
filters like clipping, slicing, and thresholding - specifically there are
widgets to control the positions of boxes, planes, and lines or slider bars
which can all be highly customized through the use of custom callback
functions.

Here we’ll take a look at the various widgets, some helper methods that
leverage those widgets to do common tasks, and demonstrate how to leverage the
widgets for user defined tasks and processing routines.

.. tip::

    This section of the tutorial was adopted from the `widgets section
    <https://docs.pyvista.org/examples/index.html?highlight=widgets#widgets>`_
    of the PyVista example documentation.


Widget Examples
---------------

.. leave blank after this point for Sphinx-Gallery to populate examples



.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The box widget can be enabled and disabled by the pyvista.Plotter.add_box_widget and pyvista.Pl...">

.. only:: html

 .. figure:: /tutorial/08_widgets/images/thumb/sphx_glr_a_box-widget_thumb.png
     :alt: Box Widget

     :ref:`sphx_glr_tutorial_08_widgets_a_box-widget.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/a_box-widget

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a checkbox to turn on/off the visibility of meshes in a scene.">

.. only:: html

 .. figure:: /tutorial/08_widgets/images/thumb/sphx_glr_b_checkbox-widget_thumb.png
     :alt: Checkbox Widget

     :ref:`sphx_glr_tutorial_08_widgets_b_checkbox-widget.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/b_checkbox-widget

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The line widget can be enabled and disabled by the pyvista.Plotter.add_line_widget and pyvista....">

.. only:: html

 .. figure:: /tutorial/08_widgets/images/thumb/sphx_glr_c_line-widget_thumb.png
     :alt: Line Widget

     :ref:`sphx_glr_tutorial_08_widgets_c_line-widget.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/c_line-widget

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a class based callback to track multiple slider widgets for updating a single mesh.">

.. only:: html

 .. figure:: /tutorial/08_widgets/images/thumb/sphx_glr_d_multi-slider-widget_thumb.png
     :alt: Multiple Slider Widgets

     :ref:`sphx_glr_tutorial_08_widgets_d_multi-slider-widget.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/d_multi-slider-widget

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The plane widget can be enabled and disabled by the pyvista.Plotter.add_plane_widget and pyvist...">

.. only:: html

 .. figure:: /tutorial/08_widgets/images/thumb/sphx_glr_e_plane-widget_thumb.png
     :alt: Plane Widget

     :ref:`sphx_glr_tutorial_08_widgets_e_plane-widget.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/e_plane-widget

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The slider widget can be enabled and disabled by the pyvista.Plotter.add_slider_widget and pyvi...">

.. only:: html

 .. figure:: /tutorial/08_widgets/images/thumb/sphx_glr_f_slider-bar-widget_thumb.png
     :alt: Slider Bar Widget

     :ref:`sphx_glr_tutorial_08_widgets_f_slider-bar-widget.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/f_slider-bar-widget

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The sphere widget can be enabled and disabled by the pyvista.Plotter.add_sphere_widget and pyvi...">

.. only:: html

 .. figure:: /tutorial/08_widgets/images/thumb/sphx_glr_g_sphere-widget_thumb.png
     :alt: Sphere Widget

     :ref:`sphx_glr_tutorial_08_widgets_g_sphere-widget.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/g_sphere-widget

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" A spline widget can be enabled and disabled by the pyvista.Plotter.add_spline_widget and pyvis...">

.. only:: html

 .. figure:: /tutorial/08_widgets/images/thumb/sphx_glr_h_spline-widget_thumb.png
     :alt: Spline Widget

     :ref:`sphx_glr_tutorial_08_widgets_h_spline-widget.py`

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/h_spline-widget
.. raw:: html

    <div class="sphx-glr-clear"></div>



.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_