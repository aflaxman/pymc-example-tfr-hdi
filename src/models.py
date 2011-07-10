""" Module for setting up statistical models
"""

import pylab as pl
import pymc as mc

import data


def linear():
    beta = mc.Uninformative('beta', value=[0., 0.])
    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    @mc.deterministic
    def y_pred(beta=beta, X=data.hdi2005):
        return beta[0] + beta[1]*X
    y_obs = mc.Normal('y_obs', value=data.tfr2005,
                      mu=y_pred, tau=sigma**-2,
                      observed=True)

    return vars()


def fit_linear():
    vars = linear()

    mc.MAP(vars).fit(method='fmin_powell')

    m = mc.MCMC(vars)
    m.sample(iter=10000, burn=5000, thin=5)
    return m


def nonlinear():
    beta = mc.Uninformative('beta', value=[0., 0., 0.])
    gamma = mc.Normal('gamma', mu=.9, tau=.05**-2,
                      value=.9)
    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    @mc.deterministic
    def y_mean(beta=beta, gamma=gamma, X=data.hdi2005):
        return beta[0] + beta[1]*X \
            + beta[2]*pl.maximum(0., X-gamma)
    y_obs = mc.Normal('y_obs', value=data.tfr2005,
                      mu=y_mean, tau=sigma**-2,
                      observed=True)

    return vars()


def fit(vars):
    mc.MAP(vars).fit(method='fmin_powell')

    m = mc.MCMC(vars)
    m.sample(iter=20000, burn=10000, thin=10)
    return m

