import pylab as pl
import pymc as mc

import models
import graphics

# make model
vars = models.nonlinear()

# fit with MCMC, but not with default step methods
m = mc.MCMC(vars)
m.use_step_method(mc.AdaptiveMetropolis, [m.beta, m.gamma])
m.sample(50000, 25000, 50)

# explore model convergence
mc.Matplot.plot(m, path='../tex/ex4')

# look at joint posterior distribution of beta_0 and beta_1 as
# well as beta_2 and gamma

pl.figure(figsize=(12,9))
graphics.plot_joint_density(m.beta.trace()[:,2], m.gamma.trace(), [-10, 10, .6, 1.])
pl.xlabel('$\\beta_2$', fontsize=20)
pl.ylabel('$\\gamma$', fontsize=20)
pl.savefig('../tex/ex4_a.png')

pl.figure(figsize=(12,9))
graphics.plot_joint_density(m.beta.trace()[:,0], m.beta.trace()[:,1], [9., 10.5, -10.5, -7.5])
pl.xlabel('$\\beta_0$', fontsize=20)
pl.ylabel('$\\beta_1$', fontsize=20)
pl.savefig('../tex/ex4_b.png')

# TODO: calculate posterior probability that slope becomes positive
