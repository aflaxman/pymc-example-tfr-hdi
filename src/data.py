import pylab as pl

all = pl.csv2rec('nature08230-s2.csv')

years = range(1975, 2006)
hdi = []
tfr = []
for row in all:
    for y in years:
        if pl.isnan(row['hdi%d'%y]) or pl.isnan(row['tfr%d'%y]):
            continue
        hdi.append(row['hdi%d'%y])
        tfr.append(row['tfr%d'%y])
hdi = pl.array(hdi)
tfr = pl.array(tfr)
