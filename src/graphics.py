import networkx as nx
import pylab as pl

# put messy matplotlib code here so I don't have to look at it if I
# don't want to
def plot_all_data():
    import data
    pl.clf()
    pl.plot(data.hdi, data.tfr, 'ko', ms=6, mew=0)
    pl.plot(data.all.hdi1975, data.all.tfr1975, 'bs',
            ms=10, mew=0, label='1975')
    pl.plot(data.all.hdi2005, data.all.tfr2005, 'r^',
            ms=12, mew=0, label='2005')
    
    pl.axis([.3, .99, 1., 8.])
    pl.legend()
    pl.xlabel('Human development index', fontsize=18)
    pl.ylabel('Total fertility rate', fontsize=18)
