p = pv.Plotter()
p.add_mesh(outline, color="k")
p.add_mesh(result, scalars="Elevation")
p.view_isometric()
p.show()