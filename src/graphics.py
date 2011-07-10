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
    pl.plot(data.all.hdi[data.all.year==1975],
            data.all.tfr[data.all.year==1975],
            'bs', ms=10, mew=0, label='1975')


def plot_2005_data():
    pl.plot(data.all.hdi[data.all.year==2005],
            data.all.tfr[data.all.year==2005],
            'r^', ms=12, mew=0, label='2005')


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
    pl.legend(numpoints=1, prop=dict(size=20), fancybox=True)
    pl.xticks(fontsize=16)
    pl.xlabel('Human development index', fontsize=20)
    pl.yticks(fontsize=16)
    pl.ylabel('Total fertility rate', fontsize=20)


def plot_each_country(axis_bounds=[.8, .99, 1.1, 3.]):
    years = range(1975, 2006)
    for i, c in enumerate(pl.unique(data.all.country)):
        pl.subplot(3, 4, i/12+1)
        pl.plot(data.all.hdi[data.all.country==c],
                data.all.tfr[data.all.country==c],
                linewidth=4, alpha=.8)
        pl.axis(axis_bounds)
    
    for r in range(3):
        for c in range(4):
            pl.subplot(3, 4, r*4+c+1)
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

def jitter(x):
    return x + pl.randn(len(x))*.01*x.std()

def plot_predicted_distribution(x, y_pred):
    for y_t in y_pred.trace():
        pl.plot(jitter(x), jitter(y_t), 'k,', alpha=.5)

def plot_predicted_sample(x, y_pred):
    t = pl.rand() * len(y_pred.trace())
    y_t = y_pred.trace()[t]
    pl.plot(x, y_t, 'g^', ms=12, mew=0, label='Prediction')

def plot_predicted_data(y_pred, bounds=[.3, .99, .1, 8.]):
    pl.subplot(3,1,1)
    plot_2005_data()
    decorate_plot()
    pl.xlabel('')
    pl.ylabel('')
    pl.axis(bounds)

    pl.subplot(3,1,2)
    plot_predicted_sample(data.hdi2005, y_pred)
    decorate_plot()
    pl.xlabel('')
    pl.axis(bounds)

    pl.subplot(3,1,3)
    plot_predicted_sample(data.hdi2005, y_pred)
    decorate_plot()
    pl.ylabel('')
    pl.axis(bounds)

    pl.subplots_adjust(hspace=0.)
