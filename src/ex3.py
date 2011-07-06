import pylab as pl
import pymc as mc

import models
import graphics

# make and fit model twice
m1 = models.fit(models.nonlinear())
m2 = models.fit(models.nonlinear())

# display results
graphics.plot_2005_data()
graphics.plot_nonlinear_model(m1, color='g', label='Replicate 1')
pl.axis([.8, .99, 1., 3.])

pl.savefig('../tex/ex3_a.png')

graphics.plot_nonlinear_model(m2, color='b', label='Replicate 2')
pl.axis([.8, .99, 1., 3.])

pl.savefig('../tex/ex3_b.png')

# explore model convergence
mc.Matplot.plot(m1, path='../tex/ex3')
