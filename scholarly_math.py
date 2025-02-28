#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:38:56 2025

@author: scholarly-punk
"""

def is_positive(n):
    return n > 0

def is_negative(n):
    return n < 0

def is_integer(n):
    return isinstance(n, int)

def is_positive_integer(n):
    return is_integer(n) and is_positive(n)

def is_negative_integer(n):
    return is_integer(n) and is_negative(n)

def is_non_negative(n):
    return not is_negative(n)

def is_non_positive(n):
    return not is_positive(n)

def is_non_negative_integer(n):
    return is_integer(n) and is_non_negative(n)

def is_non_positive_integer(n):
    return is_integer(n) and is_non_positive(n)

def is_non_zero(n):
    return not n == 0

def is_non_zero_integer(n):
    return is_integer(n) and is_non_zero(n)

def sum_1_to(n):
    assert is_non_negative_integer(n)
    return (n * (n + 1)) // 2
