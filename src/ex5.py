import pylab as pl
import pymc as mc

import data
import models
import graphics

# make model
vars = models.nonlinear()

# fit with MAP, find AIC and BIC
map = mc.MAP(vars)
map.fit(method='fmin_powell', verbose=1)
print 'AIC=%f' % map.AIC
print 'BIC=%f' % map.BIC

# add a data posterior prediction determinisitic
@mc.deterministic
def y_pred(mu=vars['y_mean'], sigma=vars['sigma']):
    return mc.rnormal(mu, sigma**-2)
vars['y_pred'] = y_pred

# fit with MCMC, but not with default step methods
mcmc = mc.MCMC(vars)
mcmc.use_step_method(mc.AdaptiveMetropolis, [mcmc.beta, mcmc.gamma])
mcmc.sample(50000, 25000, 50)

# find DIC
print 'DIC=%f' % mcmc.dic

# generate a posterior predictive check
pl.figure(figsize=(12,9))
graphics.plot_predicted_data(y_pred)
pl.savefig('../tex/ex5_a.png')

# zoom in on area of interest
pl.figure(figsize=(12,9))
graphics.plot_predicted_data(y_pred, [.7, .99, .1, 5.])
pl.savefig('../tex/ex5_b.png')
