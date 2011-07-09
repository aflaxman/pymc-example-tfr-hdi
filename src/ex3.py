import pylab as pl
import pymc as mc

import models
import graphics

# make and fit model twice
vars = models.nonlinear()
vars['beta'].value = [10, -10, 15]  # carefully choosen initial value, for demonstration purposes only
m1 = models.fit(vars)

vars = models.nonlinear()
vars['beta'].value = [8, -8, 10]  # as above
m2 = models.fit(vars)

# display results
pl.figure(figsize=(12,9))
graphics.plot_2005_data()
graphics.plot_nonlinear_model(m1, color='g', label='Replicate 1')
pl.axis([.8, .99, 1., 3.])

pl.savefig('../tex/ex3_a.png')

graphics.plot_nonlinear_model(m2, color='b', label='Replicate 2')
pl.axis([.8, .99, 1., 3.])

pl.savefig('../tex/ex3_b.png')

# explore model convergence
mc.Matplot.plot(m1, path='../tex/ex3')
