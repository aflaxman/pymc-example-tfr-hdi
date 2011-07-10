import pylab as pl
import pymc as mc

import models
import graphics

# make model
vars = models.nonlinear()
#vars['beta'].value = [10, -9, 15]  # carefully choosen initial value, for demonstration purposes only

m = mc.MCMC(vars)
m.sample(iter=20000, burn=10000, thin=10)

# display results
pl.figure(figsize=(12,9))
graphics.plot_2005_data()
graphics.plot_nonlinear_model(m)

pl.savefig('../tex/ex2.png')
