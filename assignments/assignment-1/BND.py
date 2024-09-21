import numpy as np
from matplotlib import pyplot as plt

m = 1000

meanA = [-0.5, -0.5]
covA = [[1, 0.25],
        [0.25, 1]]

meanB = [0.5, 0.5]
covB = [[1, 0.25],
        [0.25, 1]]

xA, yA = np.random.multivariate_normal(meanA, covA, m).T
xB, yB = np.random.multivariate_normal(meanB, covB, m).T

plt.title("Bivariate Normal Distribution")
plt.plot(xA, yA, 'x', color='red', label='mean=(-0.5, -0.5)')
plt.plot(xB, yB, 'x', color='blue', label='mean=(0.5, 0.5)')

plt.legend()

plt.show()
