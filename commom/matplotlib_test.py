import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 6, 50)
y1 = x*x + x
y2 = x - x*x
plt.figure()
plt.xlabel('time')
plt.ylabel('order')
plt.plot(x, y1, color='pink', linestyle='-')
plt.plot(x, y2, color='red', linestyle='--')
plt.show()