import numpy as np

import matplotlib.pyplot as plt

#从-π到π取201个变量（取得多点线就圆滑一点，这是源码写的例子201不知道有啥特殊之处，反正取100也行）

x = np.linspace(-np.pi, np.pi, 201)
print(np.sin(x),np.cos(x))
plt.plot(x, np.sin(x))
c=np.correlate(np.sin(x),np.cos(x),'same')
print(c)
plt.plot(x, np.cos(x))
# plt.plot(x,c)

plt.show()
