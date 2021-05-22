#name = input("Moi ban nhap ten: ")
#print("ten cua ban la: "+name)

import numpy
from numpy import *
from operator import add
from itertools import chain
from itertools import cycle, islice
import more_itertools
def mesh(a,b):
    minlen = min(len(a),len(b))
    return "".join(["".join(x+y for x,y in zip(a,b)),a[minlen:],b[minlen:]])

a = array([2,8,'e',9])
b = array(['a',5,'b'])

# Tạo thêm biến thứ 3
result =  [None]*(len(a)+len(b))
result[::2] = a
result[1::2] = b
result
print("".join(result))
print(result)

# Không tạo thêm biến
print(mesh("".join(a),"".join(b)))


e = list(more_itertools.roundrobin(a,b))
print(e)
