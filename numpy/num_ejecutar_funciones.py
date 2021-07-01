import numpy as np

def simple_operation(val):

    return val * 10

a=np.random.randint(1,10,10)

simple_operation(a[0])

for i in a:
    print(simple_operation(i))

func_vec = np.vectorize(simple_operation)

print(func_vec(a))