from matplotlib import pyplot as plt
import numpy as np

# limits of integration
a = 0
b = np.pi

# evaluate function N times
N = 1000

# sin function to integrate
def func(x):
    return np.sin(x)

areas = []

for i in range(1000):
    # array of random numbers between zero and pi
    for i in range(N):
        xrand = np.random.uniform(a, b, N)

    integral = 0.0

    for i in range(N):
        integral += func(xrand[i])

    answer = (b - a) / float(N) * integral
    areas.append(answer)

plt.hist(areas, bins=10, ec='black')
plt.show()
