"""
Tests for nod.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nod

# import ipdb; ipdb.set_trace()

print('test remove_duplicates()')
x = ['a', 'b', 'b', 'c']
x_set = nod.remove_duplicates(x)
print('x = ', x)
print('x_set = ', x_set)

print('test jitter_scatter()')
data = {'index': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
        'val'  : [  1, 1.1, 0.8,   2, 2.1, 1.5,   1, 1.1, 0.8]}

df = pd.DataFrame(data)
df = df.set_index('index')


fig, ax = plt.subplots()
nod.jitter_scatter(ax, df.index, df.val)
plt.show()

# define label order
x_set = ['a', 'c', 'b']
fig, ax = plt.subplots()
nod.jitter_scatter(ax, df.index, df.val, x_set=x_set)
plt.show()

