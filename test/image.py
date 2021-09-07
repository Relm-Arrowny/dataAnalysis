'''
Created on 15 Apr 2021

@author: wvx67826
'''

from PIL import Image
import numpy as np

# create data
d = np.ndarray(shape=(10,20), dtype=np.float32)
d[()] = np.arange(200).reshape(10, 20)

im = Image.fromarray(d, mode='F') # float32
im.save("test2.tiff", "TIFF")