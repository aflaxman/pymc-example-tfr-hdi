""" Module for setting up statistical models
"""

import pylab as pl
import pymc as mc

import data


def linear():
    beta = mc.Uninformative('beta', value=[0., 0.])
    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    @mc.deterministic
    def y_pred(beta=beta, X=data.hdi):
        return beta[0] + beta[1]*X
    y_obs = mc.Normal('y_obs', value=data.tfr,
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
    beta = mc.Normal('beta', mu=0., tau=10.**-1, value=[0., 0., 0.])
    gamma = mc.Normal('gamma', mu=.86, tau=.05**-2,
                      value=.86)
    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    @mc.deterministic
    def y_pred(beta=beta, gamma=gamma, X=data.hdi):
        return beta[0] + beta[1]*X \
            + beta[2]*pl.maximum(0., X-gamma)
    y_obs = mc.Normal('y_obs', value=data.tfr,
                      mu=y_pred, tau=sigma**-2,
                      observed=True)

    return vars()


def fit(vars):
    mc.MAP(vars).fit(method='fmin_powell')

    m = mc.MCMC(vars)
    m.use_step_method(mc.Metropolis, m.beta)
    m.sample(iter=20000, burn=10000, thin=10)
    return m

