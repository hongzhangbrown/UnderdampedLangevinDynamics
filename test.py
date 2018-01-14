import base
import numpy as np
# import base.AbstractULDSampler as ULD
import matplotlib.pyplot as plt

# the log likelihood functions
def logGaussian(x):
    return 0.5*(0.1*x[0]**2+0.5*x[1]**2)

def bananashaped(x):
    return -0.5*(x[0]**2*x[1]**2+x[0]**2+x[1]**2-2*3*x[0]-2*3*x[1])




if __name__ == '__main__':
    dt = 0.1
    sampler = base.AbstractULDSampler(logGaussian, L=1)
    # sampler = base.AbstractULDSampler(bananashaped, 1)
    init = np.array([.0,.0])
    #dt = delta, init initial position
    pos_samples, vel_samples = sampler.get_samples(init, dt=0.1, n_sample=10000)
    plt.scatter(pos_samples[:,0],pos_samples[:,1])
    plt.show()

    print(pos_samples)