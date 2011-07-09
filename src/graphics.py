import networkx as nx
import pylab as pl
import data

# put messy matplotlib code here so I don't have to look at it if I
# don't want to
def plot_all_data():
    #pl.plot(data.hdi, data.tfr, 'ko', ms=6, mew=0)
    plot_1975_data()
    plot_2005_data()
    decorate_plot()


def plot_1975_data():
    pl.plot(data.all.hdi1975, data.all.tfr1975, 'bs',
            ms=10, mew=0, label='1975')


def plot_2005_data():
    pl.plot(data.all.hdi2005, data.all.tfr2005, 'r^',
            ms=12, mew=0, label='2005')


def plot_linear_model(m):
    hdi = pl.arange(0., 1., .01)
    for beta_t in m.beta.trace():
        tfr = beta_t[0] + beta_t[1]*hdi
        pl.plot(hdi, tfr,
                color='gray', alpha=.75, zorder=-1)

    beta = m.beta.stats()['mean']
    tfr = beta[0] + beta[1]*hdi
    pl.plot(hdi, tfr,
            color='purple', linewidth=5,
            label='Linear')
    decorate_plot()


def plot_nonlinear_model(m, color='green', label='Nonlinear'):
    X = pl.arange(0., 1., .01)
    tfr_trace = []
    for beta, gamma in zip(m.beta.trace(), m.gamma.trace()):
        y = beta[0] + beta[1]*X + pl.maximum(0., beta[2]*(X-gamma))
        pl.plot(X, y,
                color='gray', alpha=.75, zorder=-1)
        tfr_trace.append(y)

    pl.plot(X, pl.mean(tfr_trace, axis=0),
            color=color, linewidth=5,
            label=label)
    decorate_plot()


def decorate_plot():    
    pl.axis([.3, .99, 1., 8.])
    pl.legend()
    pl.xlabel('Human development index', fontsize=18)
    pl.ylabel('Total fertility rate', fontsize=18)


def plot_each_country(axis_bounds=[.8, .99, 1.1, 3.]):
    years = range(1975, 2006)
    for r in range(3):
        for c in range(4):
            pl.subplot(3, 4, r*4+c+1)
            for i in range(12):
                row_index = (r*4 + c)*12 + i
                if row_index >= len(data.all):
                    continue
                row = data.all[row_index]
                pl.plot([row['hdi%d'%y] for y in years],
                        [row['tfr%d'%y] for y in years],
                        linewidth=4, alpha=.8)
            pl.axis(axis_bounds)
            if r != 2:
                pl.xticks([])
            if c != 0:
                pl.yticks([])
    pl.subplots_adjust(.05, .05, .95, .95, 0, 0)

def plot_joint_density(X, Y, bounds=None):
    if bounds:
        X_min, X_max, Y_min, Y_max = bounds
    else:
        X_min = X.min()
        X_max = X.max()
        Y_min = Y.min()
        Y_max = Y.max()

    pl.plot(X, Y,
         linestyle='none', marker='o', color='green', mec='green',
         alpha=.75, zorder=-99)

    import scipy.stats
    gkde = scipy.stats.gaussian_kde([X, Y])
    x,y = pl.mgrid[X_min:X_max:(X_max-X_min)/25.,
                   Y_min:Y_max:(Y_max-Y_min)/25.]
    z = pl.array(gkde.evaluate([x.flatten(), y.flatten()])).reshape(x.shape)
    pl.contour(x, y, z, linewidths=2)

    pl.axis([X_min, X_max, Y_min, Y_max])


