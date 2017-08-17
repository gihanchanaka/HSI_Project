
from PIL import Image
import numpy as np
import matplotlib.pyplot as mp

im = Image.open('a_image.tif')
#im.show()
ar=np.array(im)
print(ar.shape)

mp.plot(ar)
mp.show()