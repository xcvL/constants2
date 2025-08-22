import functions
from numpy import sqrt

#                                        name                    value

pi = 3.14159265358979323846            # pi                      -
e = 2.71828182845904523536             # Euler's number          -
G = 1 / functions.agm(1, sqrt(2))
print(G)