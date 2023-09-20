import matplotlib.pyplot as plt
import numpy as np

plt.style.use('https://github.com/kaiuki2000/PitayaRemix/raw/main/PitayaRemix.mplstyle')

x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x), label = r'$\sin(x)$')
plt.plot(x, np.cos(x), label = r'$\cos(x)$')
plt.plot(x, np.tanh(x), label = r'$\tanh(x)$')
plt.title('Trigonometric functions')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
plt.show()
