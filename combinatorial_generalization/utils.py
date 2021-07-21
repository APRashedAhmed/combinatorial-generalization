"""Utility functions"""
import logging
from collections.abc import Iterable

logger = logging.getLogger(__file__)

def isiterable(obj):
    """Function that determines if an object is an iterable, not including str.
    
    Parameters
    ----------
    obj : object
        Object to test if it is an iterable.
    
    Returns
    -------
    bool : bool
        True if the obj is an iterable, False if not.
    """
    if isinstance(obj, str):
        return False
    else:
        return isinstance(obj, Iterable)

def flatten(inp_iter):
    """Recursively iterate through values in nested iterables, and return a
    flattened list of the inputted iterable.
    
    Parameters
    ----------
    inp_iter : iterable
        The iterable to flatten.
    
    Returns
    -------
    value : object
    	The contents of the iterable as a flat list.
    """
    def inner(inp):
        for val in inp:
            if isiterable(val):
                for ival in inner(val):
                    yield ival
            else:
                yield val
    return list(inner(inp_iter))
