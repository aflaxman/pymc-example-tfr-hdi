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

# TODO: look at joint posterior distribution of beta_0 and beta_1 as
# well as beta_2 and gamma

# TODO: calculate posterior probability that slope becomes positive
