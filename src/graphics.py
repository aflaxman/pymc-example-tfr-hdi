import networkx as nx
import pylab as pl
import data

# put messy matplotlib code here so I don't have to look at it if I
# don't want to
def plot_all_data():
    pl.plot(data.hdi, data.tfr, 'ko', ms=6, mew=0)
    pl.plot(data.all.hdi1975, data.all.tfr1975, 'bs',
            ms=10, mew=0, label='1975')
    pl.plot(data.all.hdi2005, data.all.tfr2005, 'r^',
            ms=12, mew=0, label='2005')
    
    pl.axis([.3, .99, 1., 8.])
    pl.legend()
    pl.xlabel('Human development index', fontsize=18)
    pl.ylabel('Total fertility rate', fontsize=18)

def plot_linear_model(m):
    hdi = pl.arange(0., 1., .01)
    for beta_t in m.beta.trace():
        tfr = beta_t[0] + beta_t[1]*hdi
        pl.plot(hdi, tfr, color='gray', alpha=.75, zorder=-1)

    beta = m.beta.stats()['mean']
    tfr = beta[0] + beta[1]*hdi
    pl.plot(hdi, tfr, color='purple', linewidth=2, label='Linear')

    pl.legend()
    pl.axis([.3, .99, 1., 8.])

def plot_nonlinear_model(m):
    X = pl.arange(0., 1., .01)
    tfr_trace = []
    for beta, gamma in zip(m.beta.trace(), m.gamma.trace()):
        y = beta[0] + beta[1]*X + pl.maximum(0., beta[2]*(X-gamma))
        pl.plot(X, y, color='gray', alpha=.75, zorder=-1)
        tfr_trace.append(y)

    pl.plot(X, pl.mean(tfr_trace, axis=0), color='green', linewidth=2, label='Nonlinear')

    pl.legend()
    pl.axis([.3, .99, 1., 8.])
