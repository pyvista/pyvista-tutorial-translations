
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "tutorial/08_widgets/f_slider-bar-widget.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_tutorial_08_widgets_f_slider-bar-widget.py>`
        to download the full example code. or to run this example in your browser via Binder

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_tutorial_08_widgets_f_slider-bar-widget.py:


.. _slider_bar_widget_example:

Slider Bar Widget
~~~~~~~~~~~~~~~~~

The slider widget can be enabled and disabled by the
:func:`pyvista.Plotter.add_slider_widget` and
:func:`pyvista.Plotter.clear_slider_widgets` methods respectively.
This is one of the most versatile widgets as it can control a value that can
be used for just about anything.

.. GENERATED FROM PYTHON SOURCE LINES 13-15

.. code-block:: Python
   :dedent: 1










.. GENERATED FROM PYTHON SOURCE LINES 17-20

One helper method we've added is the
:func:`pyvista.Plotter.add_mesh_threshold` method which leverages the
slider widget to control a thresholding value.

.. GENERATED FROM PYTHON SOURCE LINES 20-30

.. code-block:: Python


    import pyvista as pv
    from pyvista import examples

    mesh = examples.download_knee_full()

    pl = pv.Plotter()
    pl.add_mesh_threshold(mesh)
    pl.show()








.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /tutorial/08_widgets/images/sphx_glr_f_slider-bar-widget_001.png
        :alt: f slider bar widget
        :srcset: /tutorial/08_widgets/images/sphx_glr_f_slider-bar-widget_001.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-tutorial-translations/pyvista-tutorial-translations/pyvista-tutorial/doc/source/tutorial/08_widgets/images/sphx_glr_f_slider-bar-widget_001.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 31-32

After interacting with the scene, the threshold mesh is available as:

.. GENERATED FROM PYTHON SOURCE LINES 32-34

.. code-block:: Python

    pl.threshold_meshes





.. rst-class:: sphx-glr-script-out

 .. code-block:: none


    [UnstructuredGrid (0x7feed6705b40)
      N Cells:    295424
      N Points:   394455
      X Bounds:   3.615e+01, 1.178e+02
      Y Bounds:   1.085e+01, 1.345e+02
      Z Bounds:   0.000e+00, 2.000e+02
      N Arrays:   1]



.. GENERATED FROM PYTHON SOURCE LINES 35-38

And here is a screen capture of a user interacting with this

.. image:: ../../images/gifs/slider-widget-threshold.gif

.. GENERATED FROM PYTHON SOURCE LINES 40-46

Custom Callback
+++++++++++++++

Or you could leverage a custom callback function that takes a single value
from the slider as its argument to do something like control the resolution
of a mesh. Again note the use of the ``name`` argument in ``add_mesh``:

.. GENERATED FROM PYTHON SOURCE LINES 46-59

.. code-block:: Python


    pl = pv.Plotter()


    def create_mesh(value) -> None:
        res = int(value)
        sphere = pv.Sphere(phi_resolution=res, theta_resolution=res)
        pl.add_mesh(sphere, name="sphere", show_edges=True)


    pl.add_slider_widget(create_mesh, [5, 100], title="Resolution")
    pl.show()








.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /tutorial/08_widgets/images/sphx_glr_f_slider-bar-widget_002.png
        :alt: f slider bar widget
        :srcset: /tutorial/08_widgets/images/sphx_glr_f_slider-bar-widget_002.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-tutorial-translations/pyvista-tutorial-translations/pyvista-tutorial/doc/source/tutorial/08_widgets/images/sphx_glr_f_slider-bar-widget_002.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 60-63

And here is a screen capture of a user interacting with this

.. image:: ../../images/gifs/slider-widget-resolution.gif

.. GENERATED FROM PYTHON SOURCE LINES 65-72

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/08_widgets/f_slider-bar-widget.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
      </a>
    </center>


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 3.080 seconds)


.. _sphx_glr_download_tutorial_08_widgets_f_slider-bar-widget.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: binder-badge

      .. image:: images/binder_badge_logo.svg
        :target: https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks/tutorial/08_widgets/f_slider-bar-widget.ipynb
        :alt: Launch binder
        :width: 150 px

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: f_slider-bar-widget.ipynb <f_slider-bar-widget.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: f_slider-bar-widget.py <f_slider-bar-widget.py>`

    .. container:: sphx-glr-download sphx-glr-download-zip

      :download:`Download zipped: f_slider-bar-widget.zip <f_slider-bar-widget.zip>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
