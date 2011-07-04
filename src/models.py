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
                      mu=y_pred, tau=sigma**-2, observed=True)

    return vars()

def fit_linear():
    vars = linear()

    mc.MAP(vars).fit(method='fmin_powell', verbose=1)

    m = mc.MCMC(vars)
    m.sample(iter=10000, burn=5000, thin=5)
    return m
