import numpy as np

positions = np.arange(1, 6)
print(positions)
testes = np.isin(positions, 5)
positions = positions[~testes]
print(positions)