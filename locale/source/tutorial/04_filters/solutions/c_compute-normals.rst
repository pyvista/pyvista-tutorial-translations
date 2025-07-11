
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "tutorial/04_filters/solutions/c_compute-normals.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_tutorial_04_filters_solutions_c_compute-normals.py>`
        to download the full example code. or to run this example in your browser via Binder

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_tutorial_04_filters_solutions_c_compute-normals.py:


.. _surface_normal_example:

Computing Surface Normals
~~~~~~~~~~~~~~~~~~~~~~~~~


Compute normals on a surface.

.. GENERATED FROM PYTHON SOURCE LINES 10-18

.. code-block:: Python


    import numpy as np

    from pyvista import examples

    mesh = examples.download_topo_global()
    mesh.plot(cmap="gist_earth", show_scalar_bar=False)








.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_001.png
        :alt: c compute normals
        :srcset: /tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_001.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-tutorial-translations/pyvista-tutorial-translations/pyvista-tutorial/doc/source/tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_001.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 20-26

Now we have a surface dataset of the globe loaded - unfortunately, the
dataset shows the globe with a uniform radius which hides topographic relief.
Using :func:`pyvista.PolyData.compute_normals`, we can compute the normal
vectors on the globe at all points in the dataset, then use the values given
in the dataset to warp the surface in the normals direction to create some
exaggerated topographic relief.

.. GENERATED FROM PYTHON SOURCE LINES 26-30

.. code-block:: Python


    # Compute the normals in-place and use them to warp the globe
    mesh.compute_normals(inplace=True)  # this activates the normals as well






.. raw:: html

    <div class="output_subarea output_html rendered_html output_result">
    <table style='width: 100%;'><tr><th>Header</th><th>Data Arrays</th></tr><tr><td>
    <table style='width: 100%;'>
    <tr><th>PolyData</th><th>Information</th></tr>
    <tr><td>N Cells</td><td>2333880</td></tr>
    <tr><td>N Points</td><td>2336041</td></tr>
    <tr><td>N Strips</td><td>0</td></tr>
    <tr><td>X Bounds</td><td>-1.000e+00, 1.000e+00</td></tr>
    <tr><td>Y Bounds</td><td>-1.000e+00, 1.000e+00</td></tr>
    <tr><td>Z Bounds</td><td>-1.000e+00, 1.000e+00</td></tr>
    <tr><td>N Arrays</td><td>3</td></tr>
    </table>

    </td><td>
    <table style='width: 100%;'>
    <tr><th>Name</th><th>Field</th><th>Type</th><th>N Comp</th><th>Min</th><th>Max</th></tr>
    <tr><td><b>altitude</b></td><td>Points</td><td>float32</td><td>1</td><td>-1.042e+04</td><td>6.527e+03</td></tr>
    <tr><td>Normals</td><td>Points</td><td>float32</td><td>3</td><td>-1.000e+00</td><td>1.000e+00</td></tr>
    <tr><td>Normals</td><td>Cells</td><td>float32</td><td>3</td><td>-1.000e+00</td><td>1.000e+00</td></tr>
    </table>

    </td></tr> </table>
    </div>
    <br />
    <br />

.. GENERATED FROM PYTHON SOURCE LINES 31-32

Now use those normals to warp the surface

.. GENERATED FROM PYTHON SOURCE LINES 32-34

.. code-block:: Python

    warp = mesh.warp_by_scalar(factor=0.5e-5)








.. GENERATED FROM PYTHON SOURCE LINES 35-36

And let's see it!

.. GENERATED FROM PYTHON SOURCE LINES 36-39

.. code-block:: Python

    warp.plot(cmap="gist_earth", show_scalar_bar=False)









.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_002.png
        :alt: c compute normals
        :srcset: /tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_002.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-tutorial-translations/pyvista-tutorial-translations/pyvista-tutorial/doc/source/tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_002.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 40-43

We could also use face or cell normals to extract all the faces of a mesh
facing a general direction. In the following snippet, we take a mesh, compute
the normals along its cell faces, and extract the faces that face upward.

.. GENERATED FROM PYTHON SOURCE LINES 43-62

.. code-block:: Python


    mesh = examples.download_nefertiti()
    # Compute normals
    mesh.compute_normals(cell_normals=True, point_normals=False, inplace=True)

    # Get list of cell IDs that meet condition
    ids = np.arange(mesh.n_cells)[mesh["Normals"][:, 2] > 0.0]

    # Extract those cells
    top = mesh.extract_cells(ids)

    cpos = [
        (-834.3184529757553, -918.4677714398535, 236.5468795300025),
        (11.03829376004883, -13.642289291587957, -35.91218884207208),
        (0.19212361465657216, 0.11401076390090074, 0.9747256344254143),
    ]

    top.plot(cpos=cpos, color=True)








.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_003.png
        :alt: c compute normals
        :srcset: /tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_003.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-tutorial-translations/pyvista-tutorial-translations/pyvista-tutorial/doc/source/tutorial/04_filters/solutions/images/sphx_glr_c_compute-normals_003.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 63-70

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/04_filters/solutions/c_compute-normals.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
      </a>
    </center>


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 38.512 seconds)


.. _sphx_glr_download_tutorial_04_filters_solutions_c_compute-normals.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: binder-badge

      .. image:: images/binder_badge_logo.svg
        :target: https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks/tutorial/04_filters/solutions/c_compute-normals.ipynb
        :alt: Launch binder
        :width: 150 px

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: c_compute-normals.ipynb <c_compute-normals.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: c_compute-normals.py <c_compute-normals.py>`

    .. container:: sphx-glr-download sphx-glr-download-zip

      :download:`Download zipped: c_compute-normals.zip <c_compute-normals.zip>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
