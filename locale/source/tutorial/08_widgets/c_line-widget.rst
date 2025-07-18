
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "tutorial/08_widgets/c_line-widget.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_tutorial_08_widgets_c_line-widget.py>`
        to download the full example code. or to run this example in your browser via Binder

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_tutorial_08_widgets_c_line-widget.py:


.. _line_widget_example:

Line Widget
~~~~~~~~~~~

The line widget can be enabled and disabled by the
:func:`pyvista.Plotter.add_line_widget` and
:func:`pyvista.Plotter.clear_line_widgets` methods respectively.
Unfortunately, PyVista does not have any helper methods to utilize this
widget, so it is necessary to pass a custom callback method.

One particularly fun example is to use the line widget to create a source for
the :func:`pyvista.DataSetFilters.streamlines` filter. Again note the use of
the ``name`` argument in ``add_mesh``.

.. GENERATED FROM PYTHON SOURCE LINES 17-30

.. code-block:: Python


    import numpy as np
    import pyvista as pv
    from pyvista import examples

    pv.set_plot_theme("document")

    mesh = examples.download_kitchen()
    furniture = examples.download_kitchen(split=True)

    arr = np.linalg.norm(mesh["velocity"], axis=1)
    clim = [arr.min(), arr.max()]








.. GENERATED FROM PYTHON SOURCE LINES 31-50

.. code-block:: Python


    pl = pv.Plotter()
    pl.add_mesh(furniture, name="furniture", color=True)
    pl.add_mesh(mesh.outline(), color="black")
    pl.add_axes()


    def simulate(pointa, pointb) -> None:
        streamlines = mesh.streamlines(
            n_points=10, max_steps=100, pointa=pointa, pointb=pointb, integration_direction="forward"
        )
        pl.add_mesh(
            streamlines, name="streamlines", line_width=5, render_lines_as_tubes=True, clim=clim
        )


    pl.add_line_widget(callback=simulate, use_vertices=True)
    pl.show()








.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /tutorial/08_widgets/images/sphx_glr_c_line-widget_001.png
        :alt: c line widget
        :srcset: /tutorial/08_widgets/images/sphx_glr_c_line-widget_001.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-tutorial-translations/pyvista-tutorial-translations/pyvista-tutorial/doc/source/tutorial/08_widgets/images/sphx_glr_c_line-widget_001.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 51-54

And here is a screen capture of a user interacting with this

.. image:: ../../images/gifs/line-widget-streamlines.gif

.. GENERATED FROM PYTHON SOURCE LINES 56-63

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/08_widgets/c_line-widget.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
      </a>
    </center>


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 1.248 seconds)


.. _sphx_glr_download_tutorial_08_widgets_c_line-widget.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: binder-badge

      .. image:: images/binder_badge_logo.svg
        :target: https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks/tutorial/08_widgets/c_line-widget.ipynb
        :alt: Launch binder
        :width: 150 px

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: c_line-widget.ipynb <c_line-widget.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: c_line-widget.py <c_line-widget.py>`

    .. container:: sphx-glr-download sphx-glr-download-zip

      :download:`Download zipped: c_line-widget.zip <c_line-widget.zip>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
