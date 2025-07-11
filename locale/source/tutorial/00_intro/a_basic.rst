
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "tutorial/00_intro/a_basic.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_tutorial_00_intro_a_basic.py>`
        to download the full example code. or to run this example in your browser via Binder

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_tutorial_00_intro_a_basic.py:


.. _ref_geometric_example:

Create Basic Geometric Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the "Hello, world!" of PyVista.

.. GENERATED FROM PYTHON SOURCE LINES 9-12

.. code-block:: Python


    import pyvista as pv








.. GENERATED FROM PYTHON SOURCE LINES 13-17

This runs through several of the available geometric objects available in
VTK which PyVista provides simple convenience methods for generating.

Let's run through creating a few geometric objects!

.. GENERATED FROM PYTHON SOURCE LINES 17-28

.. code-block:: Python


    cyl = pv.Cylinder()
    arrow = pv.Arrow()
    sphere = pv.Sphere()
    plane = pv.Plane()
    line = pv.Line()
    box = pv.Box()
    cone = pv.Cone()
    poly = pv.Polygon()
    disc = pv.Disc()








.. GENERATED FROM PYTHON SOURCE LINES 29-30

Now let's plot them all in one window

.. GENERATED FROM PYTHON SOURCE LINES 30-58

.. code-block:: Python


    pl = pv.Plotter(shape=(3, 3))
    # Top row
    pl.subplot(0, 0)
    pl.add_mesh(cyl, color="tan", show_edges=True)
    pl.subplot(0, 1)
    pl.add_mesh(arrow, color="tan", show_edges=True)
    pl.subplot(0, 2)
    pl.add_mesh(sphere, color="tan", show_edges=True)
    # Middle row
    pl.subplot(1, 0)
    pl.add_mesh(plane, color="tan", show_edges=True)
    pl.subplot(1, 1)
    pl.add_mesh(line, color="tan", line_width=3)
    pl.subplot(1, 2)
    pl.add_mesh(box, color="tan", show_edges=True)
    # Bottom row
    pl.subplot(2, 0)
    pl.add_mesh(cone, color="tan", show_edges=True)
    pl.subplot(2, 1)
    pl.add_mesh(poly, color="tan", show_edges=True)
    pl.subplot(2, 2)
    pl.add_mesh(disc, color="tan", show_edges=True)
    # Render all of them
    pl.show()
    # Export this plotter as an interactive scene to a HTML file.
    # p.export_html("a_basic.html")








.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /tutorial/00_intro/images/sphx_glr_a_basic_001.png
        :alt: a basic
        :srcset: /tutorial/00_intro/images/sphx_glr_a_basic_001.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-tutorial-translations/pyvista-tutorial-translations/pyvista-tutorial/doc/source/tutorial/00_intro/images/sphx_glr_a_basic_001.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 59-66

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/00_intro/a_basic.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
      </a>
    </center>


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 3.007 seconds)


.. _sphx_glr_download_tutorial_00_intro_a_basic.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: binder-badge

      .. image:: images/binder_badge_logo.svg
        :target: https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks/tutorial/00_intro/a_basic.ipynb
        :alt: Launch binder
        :width: 150 px

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: a_basic.ipynb <a_basic.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: a_basic.py <a_basic.py>`

    .. container:: sphx-glr-download sphx-glr-download-zip

      :download:`Download zipped: a_basic.zip <a_basic.zip>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
