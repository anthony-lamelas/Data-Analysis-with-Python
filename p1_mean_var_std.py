import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3,3)

    rmean = arr.mean(axis=1).tolist()
    cmean = arr.mean(axis=0).tolist()
    emean = arr.mean().tolist()

    rvar = arr.var(axis=1).tolist()
    cvar = arr.var(axis=0).tolist()
    evar = arr.var().tolist()

    rstd = arr.std(axis=1).tolist()
    cstd = arr.std(axis=0).tolist()
    estd = arr.std().tolist()


    rmax = arr.max(axis=1).tolist()
    cmax = arr.max(axis=0).tolist()
    emax = arr.max().tolist()

    rmin = arr.min(axis=1).tolist()
    cmin = arr.min(axis=0).tolist()
    emin = arr.min().tolist()

    rsum = arr.sum(axis=1).tolist()
    csum = arr.sum(axis=0).tolist()
    esum = arr.sum().tolist()


    calculations = {'mean': [cmean, rmean, emean],
                    'variance' : [cvar, rvar, evar],
                    'standard deviation': [cstd, rstd, estd],
                    'max':[cmax,rmax,emax],
                    'min':[cmin,rmin,emin],
                    'sum':[csum, rsum, esum]}


    return calculations

lst = [0,1,2,3,4,5,6,7,8]
print(calculate(lst))