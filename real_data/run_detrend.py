#!/usr/bin/env python

import arfit.carma_pack_posterior as cpp
import emcee
import numpy as np
import os
import plotutils.runner as pr

if __name__ == '__main__':
    nwalkers = 512
    neff = 8
    p=6
    q=p-1
    direc = 'p{:02d}q{:02d}'.format(p,q)

    data = np.loadtxt('time_vel.txt')
    logpost = cpp.Posterior(data[:,0], data[:,1], data[:,2], p=p, q=q)
    sampler = emcee.EnsembleSampler(nwalkers, logpost.nparams, logpost)
    runner = pr.EnsembleSamplerRunner(sampler, np.random.randn(nwalkers, logpost.nparams))

    runner.load_state(direc)

    try:
        with open(os.path.join(direc, 'reset'), 'r') as inp:
            pass
        runner.reset()
        os.remove(os.path.join(direc, 'reset'))
    except:
        pass
        

    runner.run_to_neff(neff, savedir=direc)
