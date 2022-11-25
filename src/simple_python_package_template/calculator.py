import numpy as np 

from .basic_functions import *
from .cosmo_equations import * 

def age_estimator(param, z):
    Feq = FriedmannEquation(param)
    a = z_to_a(z)
    I = lambda a: 1/a/Feq.H(a=a)
    t = lambda a: quad(I, 0, a)[0]
    return np.vectorize(t)(a) 