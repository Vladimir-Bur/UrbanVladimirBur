import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


"""x = np.linspace(0, 4 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()"""

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

im_0 = Image.open('Command joke.jpg')
im_1 = im_0.resize((600, 260))
im_1.show()
