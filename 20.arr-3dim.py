# 19)Create 3d array.

import numpy as np
a=np.arange(10,20)
print(a)

print("\n3 Dim array:-\n")

a.resize(1,2,5)
print(a)
print(a.ndim)