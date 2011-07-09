import pylab as pl
import pymc as mc

import models
import graphics

# make model
vars = models.nonlinear()
vars['beta'].value = [10, -10, 15]  # carefully choosen initial value, for demonstration purposes only
# fit model with MCMC, starting with MAP initial value
mc.MAP(vars).fit(method='fmin_powell', verbose=1)

m = mc.MCMC(vars)
m.sample(iter=10000, burn=5000, thin=5)

# display results
pl.figure(figsize=(12,9))
graphics.plot_all_data()
graphics.plot_nonlinear_model(m)

pl.savefig('../tex/ex2.png')
