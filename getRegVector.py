import numpy as np
def getRegVector(ordem, y, u, isArx, e, t):
    new_fi = np.array([])
    for i in range(1, ordem + 1):
        new_fi = np.append(new_fi, y[t - i])
    for i in range(1, ordem + 1):
        new_fi = np.append(new_fi, u[t - i])
    if not isArx:
        for i in range(1, ordem + 1):
            new_fi = np.append(new_fi, e[t - i])
    new_fi = new_fi.reshape(len(new_fi), 1)
    return new_fi