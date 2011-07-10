import pylab as pl
import pymc as mc

import models
import graphics

# make model
vars = models.linear()

# fit model with MCMC
m = mc.MCMC(vars)
m.sample(iter=10000, burn=5000, thin=5)

# display results
pl.figure(figsize=(12,9))
graphics.plot_2005_data()
graphics.plot_linear_model(m)

pl.savefig('../tex/ex1.png')
