import pylab as pl

orig = pl.csv2rec('nature08230-s2.csv')

country = []
year = []
hdi = []
tfr = []
for row in orig:
    for y in range(1975, 2006):
        if pl.isnan(row['hdi%d'%y]) \
                or pl.isnan(row['tfr%d'%y]):
            continue
        country.append(row['country'])
        year.append(y)
        hdi.append(row['hdi%d'%y])
        tfr.append(row['tfr%d'%y])

all = pl.np.core.rec.fromarrays([country, year, hdi, tfr],
                                names='country year hdi tfr'.split())

hdi = all.hdi[(all.year==1975) | (all.year==2005)]
tfr = all.tfr[(all.year==1975) | (all.year==2005)]
hdi2005 = all.hdi[all.year==2005]
tfr2005 = all.tfr[all.year==2005]
