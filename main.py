import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 2 * np.pi, 1000)


x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Построение графика
plt.plot(x, y, color='red')
plt.title('Heart Shape')
plt.gca().set_aspect('equal')
plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# r = 5
#
#
# t = np.linspace(0, 2 * np.pi, 1000)
#
#
# x = r * np.cos(t)
# y = r * np.sin(t)
#
#
# plt.plot(x, y, color='blue')
# plt.title('Circle')
# plt.gca().set_aspect('equal')
# plt.show()
