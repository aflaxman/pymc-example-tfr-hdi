""" Class for wrangling data
"""

import pylab as pl
import pymc as mc

all_data = pl.csv2rec('nature08230-s2.csv')

years = range(1975, 2006)
hdi = [d['hdi%d'%y] for y in years for d in all_data]
hdi = pl.ma.masked_array(hdi, pl.isnan(hdi))

tfr = [d['tfr%d'%y] for y in years for d in all_data]
tfr = pl.ma.masked_array(tfr, pl.isnan(tfr))

