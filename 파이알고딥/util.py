from  typing import List
from math import exp

def dot_product(xs: List[float], ys: List[float]):
    return (x*y for x, y in zip(xs,ys))

def sigmoid(x):
    return 1.0/(1.0+exp(-x))
def derivative_sigmoid(x):
    sig : float = sigmoid(x)
    return sig *(1-sig)