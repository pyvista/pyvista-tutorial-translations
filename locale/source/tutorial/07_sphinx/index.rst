:orphan:

.. _sphinx:

PyVista and Sphinx
==================

Leverage PyVista to make some awesome interactive web documentation.

.. tip::

    This section of the tutorial was adopted from `Plotting Themes
    <https://docs.pyvista.org/user-guide/themes.html>`_ and `Sphinx PyVista
    Plot Directive <https://docs.pyvista.org/extras/plot_directive.html>`_
    chapter of the PyVista documentation.

Dynamically Generating 3D Plots in your Documentation
-----------------------------------------------------
PyVista allows you to generate static or dynamic images directly within Sphinx
much like the `Matplotlib plot_directive
<https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html>`_. Rather
than manually creating and adding plots after code sections, you can instead
dynamically generate images and embed them directly within your
documentation. This also works seamlessly with `sphinx-gallery
<https://sphinx-gallery.github.io/>`_, so you can create notebook examples just
like the `Matplotlib Example Gallery
<https://matplotlib.org/stable/gallery/index.html>`_.

As an added side benefit, you can be sure that the documentation you generate
matches your project API. If you include this within a `GitHub Workflow
<https://docs.github.com/en/actions/using-workflows/about-workflows>`_

This section covers the following topics.

- :ref:`static_plots`
- :ref:`dynamic_plots`

.. _static_plots:

Static Plotting - Sphinx PyVista Plot Directive
-----------------------------------------------
You can generate static images of PyVista plots within sphinx using the
``pyvista-plot`` directive by adding the following to your ``conf.py``
when building your documentation using Sphinx.

.. code:: python

   extensions = [
       "sphinx.ext.napoleon",
       "pyvista.ext.plot_directive",
   ]

You can then issue the plotting directive within your sphinx
documentation files::

   .. pyvista-plot::
      :caption: A sphere
      :include-source: True

      >>> import pyvista
      >>> sphere = pyvista.Sphere()
      >>> out = sphere.plot()

Which will be rendered as:

.. pyvista-plot::
   :caption: This is a default sphere
   :include-source: True

   >>> import pyvista
   >>> sphere = pyvista.Sphere()
   >>> out = sphere.plot()


.. _dynamic_plots:

Dynamic Plotting Using the Jupyter Sphinx Extension
---------------------------------------------------
PyVista also supports the `jupyter-sphinx
<https://jupyter-sphinx.readthedocs.io/>`_ extension. With this extension you
can execute code blocks within a sphinx ``*.rst`` file using the
``jupyter-execute`` directive::

  .. jupyter-execute::

     name = 'world'
     print('hello ' + name + '!')

Will be rendered as:

.. jupyter-execute::

   name = 'world'
   print('hello ' + name + '!')

|

Likewise, output from PyVista that would normally be rendered within a notebook
will be rendered in the output cell from the ``jupyter-execute`` directive. For
example, here's a plot using the `trame
<https://github.com/Kitware/trame>`_ backend::

  .. jupyter-execute::

     from pyvista import examples
     dataset = examples.download_urn()
     dataset.plot(color='tan', jupyter_backend='trame', window_size=(700, 400))

Which is rendered as:

.. jupyter-execute::

   from pyvista import examples
   dataset = examples.download_urn()
   dataset.plot(color='tan', jupyter_backend='trame', window_size=(700, 400))


Using the ``Trame`` backend with PyVista
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PyVista supports the usage of the `trame <https://github.com/Kitware/trame>`_
library as a ``vtk.js`` jupyterlab plotting backend that can be utilized as
either a standalone VTK viewer, or as a tightly integrated ``pyvista`` plotting
backend.  For example, within a Jupyter notebook environment, you can pass
``jupyter_backend='trame'`` to ``plot``, or ``Plotter.show`` to automatically
enable plotting with Juptyer and ``trame``.

For example, here's the ``PyVista`` logo::

   .. jupyter-execute::

      from pyvista import demos
      demos.plot_logo(background='white', jupyter_backend='trame')

Which is shown within the documentation as:

.. jupyter-execute::

   from pyvista import demos
   demos.plot_logo(background='white', jupyter_backend='trame')

|

Examples and Usage
~~~~~~~~~~~~~~~~~~
There are two ways to use `trame <https://github.com/Kitware/trame>`_ within
Jupyter notebooks.  You can use it on a plot by plot basis by setting the
``jupyter_backend`` in ``mesh.plot()``::

   .. jupyter-execute::

       import pyvista as pv
       from pyvista import examples

       # create a point cloud from lidar data and add height scalars
       dataset = examples.download_lidar()
       point_cloud = pv.PolyData(dataset.points[::100])
       point_cloud['height'] = point_cloud.points[:, 2]
       point_cloud.plot(window_size=[500, 500],
                        cmap='jet',
                        point_size=2,
                        background='w')

And here's the resulting output in Sphinx:

.. jupyter-execute::

    import pyvista as pv
    from pyvista import examples

    # create a point cloud from lidar data and add height scalars
    dataset = examples.download_lidar()
    point_cloud = pv.PolyData(dataset.points[::100])
    point_cloud['height'] = point_cloud.points[:, 2]
    point_cloud.plot(window_size=[500, 500],
                     cmap='jet',
                     point_size=2,
                     background='w')

|

Or you can first hide code that sets up the plotting backend and global theme::

   .. jupyter-execute::
       :hide-code:

       import pyvista as pv

       # Set the global jupyterlab backend.  All plots from this point
       # onward will use the ``trame`` backend and do not have to be
       # specified in ``show``

.. jupyter-execute::
   :hide-code:

   import pyvista as pv

And now just directly execute ``plot`` on any dataset::

   .. jupyter-execute::

      from pyvista import examples
      dataset = examples.download_dragon()
      dataset.plot(cpos="xy")

Which looks like:

.. jupyter-execute::

   from pyvista import examples
   dataset = examples.download_dragon()
   dataset.plot(cpos="xy")


.. note::
   You have the option of choosing `trame <https://github.com/Kitware/trame>`_
   or `trame <https://github.com/Kitware/trame>`_ as a backend,
   but you might find that `trame <https://github.com/Kitware/trame>`_ has
   better support as it's being actively developed.


Exercises
---------

Generate Sphinx documentation on your own using the
`pyvista/pyvista-doc-example <https://github.com/pyvista/pyvista-doc-example>`_
repository. Either clone the repository with::

  git clone https://github.com/pyvista/pyvista-doc-example

Or just download the zip of the repository.

.. button-link:: https://github.com/pyvista/pyvista-doc-example/archive/refs/heads/main.zip
    :color: primary
    :shadow:

    pyvista-doc-example-main.zip


Build the documentation
~~~~~~~~~~~~~~~~~~~~~~~

Once you've downloaded `pyvista/pyvista-doc-example
<https://github.com/pyvista/pyvista-doc-example>`_, cd into the directory and
install the documentation build requirements with::

  cd pyvista-doc-example
  pip install -r requirements_docs.txt

Finally, build the documentation locally with::

  cd doc
  make html

Or, if on Windows::

  cd doc
  make.bat

You will then find the generated documentation within the ``doc/_build``
directory. Open up ``index.html`` using your browser to see the documentation.



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    </div>



.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
