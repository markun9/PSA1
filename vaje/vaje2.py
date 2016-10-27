# -*- coding: utf-8 -*-
# Algoritmi z drugih vaj

def euclid(m, n):
    """Evklidov algoritem"""
    while n != 0:
        m, n = n, m % n
    return m

def karatsuba(m, n, b):
    """Množenje z metodo deli in vladaj"""
    if b == 0:
        return m*n
    m1, m2 = m >> b, m & ~(-1 << b)
    n1, n2 = n >> b, n & ~(-1 << b)
    mn1 = karatsuba(m1, n1, b//2)
    mn2 = karatsuba(m2, n2, b//2)
    mn0 = karatsuba(m1+m2, n1+n2, b//2) - mn1 - mn2
    return (mn1 << 2*b) + (mn0 << b) + mn2
