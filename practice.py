import numpy as np

list = [0,1,2,3,4,5,6,7,8]

lst=np.array([
            [list[0:3]],
              [list[3:6]],
              [list[6:9]]])


print(lst[0:3], axis=0)

