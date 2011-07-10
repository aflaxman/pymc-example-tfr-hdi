import pymc as mc
import models

# fit with MCMC, save results in a database db can be one of the
# following: no_trace, ram, pickle, txt, sqlite, mysql, hdf5

vars = models.nonlinear()
mcmc = mc.MCMC(vars, db='sqlite', dbname='nonlinear.sqlite')
mcmc.use_step_method(mc.AdaptiveMetropolis, [mcmc.beta, mcmc.gamma])
mcmc.sample(5000, 2500, 5)

# load the database from disk
db = mc.database.sqlite.load('nonlinear.sqlite')
print db.beta.stats()

# do it again with txt to compare size of output

vars = models.nonlinear()
mcmc = mc.MCMC(vars, db='txt', dbname='nonlinear.txt')
mcmc.use_step_method(mc.AdaptiveMetropolis, [mcmc.beta, mcmc.gamma])
mcmc.sample(5000, 2500, 5)

# load the database from disk
db = mc.database.txt.load('nonlinear.txt')
print db.beta.stats()
