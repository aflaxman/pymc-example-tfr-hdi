import pylab as pl
import pymc as mc

import models
import graphics

# make model
vars = models.nonlinear()

# fit model with MCMC, starting with MAP initial value
mc.MAP(vars).fit(method='fmin_powell', verbose=1)

m = mc.MCMC(vars)
m.sample(iter=10000, burn=5000, thin=5)

# display results
graphics.plot_2005_data()
graphics.plot_nonlinear_model(m)

pl.savefig('../tex/ex2.png')
