import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 201)
y = np.sin(2*np.pi*x)
plt.plot(x, y)
plt.title(r'$e=\lim_{n \to \infty}{(1+\frac{1}{n})^n}$')
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.show()
