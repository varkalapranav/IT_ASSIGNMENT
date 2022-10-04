import numpy as np
n1=np.array([10,20])
n2=np.array([30,40])
print(np.vstack((n1,n2)))

print(np.column_stack((n1,n2)))

print(np.hstack((n1,n2)))

s=np.sum((n1,n2))

print(s)
#vertical addition
s1=np.sum((n1,n2),axis=0)
print(s1)
#horizontal addition
s2=np.sum((n1,n2),axis=1)
print(s2)