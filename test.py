import base
import numpy as np
# import base.AbstractULDSampler as ULD
import matplotlib.pyplot as plt
def logGaussian(x):
    return 0.5*(x[0]**2+x[1]**2)


if __name__ == '__main__':
    dt = 0.1
    sampler = base.AbstractULDSampler(logGaussian, 1)
    init = np.array([.0,.0])
    pos_samples, vel_samples = sampler.get_samples(init, 0.5, 100)
    plt.scatter(pos_samples[:,0],pos_samples[:,1])
    plt.show()

    print(pos_samples)