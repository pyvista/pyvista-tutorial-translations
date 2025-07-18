
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "tutorial/03_figures/bonus/g_orbit.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_tutorial_03_figures_bonus_g_orbit.py>`
        to download the full example code. or to run this example in your browser via Binder

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_tutorial_03_figures_bonus_g_orbit.py:


.. _orbiting_example:

Orbiting
~~~~~~~~

Orbit around a scene.

.. note::
   The quality of the movie will be better when using
   ``pl.open_movie('orbit.mp4')`` instead of
   ``pl.open_gif('orbit.gif')``

For orbiting to work you first have to show the scene and leave the plotter open
with ``.show(auto_close=False)``.  You may also have to set
``pv.Plotter(off_screen=True)``

.. note::
   Use ``lighting=False`` to reduce the size of the color space to avoid
   "jittery" GIFs when showing the scalar bar.

.. GENERATED FROM PYTHON SOURCE LINES 23-29

.. code-block:: Python


    import pyvista as pv
    from pyvista import examples

    mesh = examples.download_st_helens().warp_by_scalar()








.. GENERATED FROM PYTHON SOURCE LINES 31-32

Orbit around the Mt. St Helens dataset.

.. GENERATED FROM PYTHON SOURCE LINES 32-43

.. code-block:: Python


    pl = pv.Plotter()
    pl.add_mesh(mesh, lighting=False)
    pl.camera.zoom(1.5)
    pl.show(auto_close=False)
    path = pl.generate_orbital_path(n_points=36, shift=mesh.length)
    pl.open_gif("orbit.gif")
    pl.orbit_on_path(path, write_frames=True)
    pl.close()






.. image-sg:: /tutorial/03_figures/bonus/images/sphx_glr_g_orbit_001.gif
   :alt: g orbit
   :srcset: /tutorial/03_figures/bonus/images/sphx_glr_g_orbit_001.gif
   :class: sphx-glr-single-img







.. GENERATED FROM PYTHON SOURCE LINES 44-56

.. code-block:: Python


    pl = pv.Plotter()
    pl.add_mesh(mesh, lighting=False)
    pl.show_grid()
    pl.show(auto_close=False)
    viewup = [0.5, 0.5, 1]
    path = pl.generate_orbital_path(factor=2.0, shift=10000, viewup=viewup, n_points=36)
    pl.open_gif("orbit.gif")
    pl.orbit_on_path(path, write_frames=True, viewup=[0, 0, 1], step=0.05)
    pl.close()






.. image-sg:: /tutorial/03_figures/bonus/images/sphx_glr_g_orbit_002.gif
   :alt: g orbit
   :srcset: /tutorial/03_figures/bonus/images/sphx_glr_g_orbit_002.gif
   :class: sphx-glr-single-img







.. GENERATED FROM PYTHON SOURCE LINES 57-61

.. code-block:: Python


    mesh = examples.download_dragon()
    viewup = [0, 1, 0]








.. GENERATED FROM PYTHON SOURCE LINES 62-70

.. code-block:: Python

    pl = pv.Plotter()
    pl.add_mesh(mesh)
    pl.show(auto_close=False)
    path = pl.generate_orbital_path(factor=2.0, n_points=36, viewup=viewup, shift=0.2)
    pl.open_gif("orbit.gif")
    pl.orbit_on_path(path, write_frames=True, viewup=viewup, step=0.05)
    pl.close()





.. image-sg:: /tutorial/03_figures/bonus/images/sphx_glr_g_orbit_003.gif
   :alt: g orbit
   :srcset: /tutorial/03_figures/bonus/images/sphx_glr_g_orbit_003.gif
   :class: sphx-glr-single-img







.. GENERATED FROM PYTHON SOURCE LINES 71-78

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/03_figures/bonus/g_orbit.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
      </a>
    </center>


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 56.355 seconds)


.. _sphx_glr_download_tutorial_03_figures_bonus_g_orbit.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: binder-badge

      .. image:: images/binder_badge_logo.svg
        :target: https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks/tutorial/03_figures/bonus/g_orbit.ipynb
        :alt: Launch binder
        :width: 150 px

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: g_orbit.ipynb <g_orbit.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: g_orbit.py <g_orbit.py>`

    .. container:: sphx-glr-download sphx-glr-download-zip

      :download:`Download zipped: g_orbit.zip <g_orbit.zip>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
