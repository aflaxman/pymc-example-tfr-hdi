""" Module for setting up statistical models
"""

import pylab as pl
import pymc as mc

import data

def linear():
    beta = mc.Uninformative('beta', value=[0., 0.])
    sigma = mc.Uninformative('sigma', value=1.)

    @mc.deterministic
    def y_pred(beta=beta, X=data.hdi):
        return beta[0] + beta[1]*X
    y_obs = mc.Normal('y_obs', value=data.tfr,
                      mu=y_pred, tau=sigma**-2)

    return vars()

def fit_linear():
    m = mc.MCMC(linear())
    m.sample(iter=100000, burn=50000, thin=50)
    return m
