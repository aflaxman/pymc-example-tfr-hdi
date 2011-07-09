import pylab as pl
import pymc as mc

import graphics

# plot 1975/2005 data
pl.figure(figsize=(12,9))
graphics.plot_all_data()
pl.savefig('../tex/ex0_a.png')

# plot all country data
pl.figure(figsize=(12,9))
graphics.plot_each_country([.3, .99, 1., 7.9])
pl.savefig('../tex/ex0_b.png')

# plot all country data zoomed
pl.figure(figsize=(12,9))
graphics.plot_each_country([.8, .99, 1.1, 3.])
pl.savefig('../tex/ex0_c.png')

# plot 1975 data
pl.figure(figsize=(12,9))
graphics.plot_1975_data()
graphics.decorate_plot()
pl.savefig('../tex/ex0_d.png')

# plot 2005 data zoomed
pl.figure(figsize=(12,9))
graphics.plot_all_data()
pl.axis([.5, .99, 1., 5.])
pl.savefig('../tex/ex0_d.png')
