"""
External Parameters

This is a useful file if this package is a simulator. 
All the parameter can be initialised and them passed as 
an param object to the simulator functions and classes.
"""

import numpy as np

class Bunch(object):
    """
    translates dic['name'] into dic.name 
    """

    def __init__(self, data):
        self.__dict__.update(data)


def code_par(): 
    # This is an example showing a few parameters for a cosmological simulations.
    par = {
        "zmin": 6.0,                # min redshift
        "zmax": 60.0,               # max redshift (not tested below 40)
        "Nz": 100,                  # Nb of redshift bins
        "verbose": True,            # If True, then the simulator prints messages.
        }
    return Bunch(par)

def cosmo_par(): 
    # This is an example showing a few parameters for a cosmological simulations.
    par = {
        "Om" : 0.31,                # min redshift
        "Ode": 0.69,               # max redshift (not tested below 40)
        "h"  : 0.68,                  # Nb of redshift bins
        }
    return Bunch(par)

def param():
    par = Bunch({
        "cosmo": cosmo_par(),
        "code": code_par(),
        })
    return par