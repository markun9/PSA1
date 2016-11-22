# -*- coding: utf-8 -*-
"""
Funkcije na usmerjenih grafih.

V ocenah časovne zahtevnosti je n število vozlišč v grafu,
m število povezav v grafu, d(u) pa število sosedov vozlišča u.
Pri tem predpostavljamo, da velja n = O(m)
(graf ima O(1) povezanih komponent).
"""
from vaje5 import DFS
from vaje6 import decompose, toporder

def countPaths(G, s, t):
    """
    Prešteje poti od s do t v usmerjenem acikličnem grafu G.

    Časovna zahtevnost: O(m)
    """
    sez = toporder(G)
    poti = [0] * len(G)
    poti[s] = 1
    for v in sez[sez.index(s):sez.index(t)]:
        for u in G[v]:
            poti[u] += poti[v]
    return poti[t]

def hamiltonianPath(G):
    """
    Poišče Hamiltonovo pot v usmerjenem acikličnem grafu, če ta obstaja.

    Časovna zahtevnost: O(m)
    """
    sez = toporder(G)
    for i in range(1, len(sez)):
        if sez[i] not in G[sez[i-1]]:
            return False
    return sez

def cheapestReachable(G, p, DFS = DFS):
    """
    Za dani seznam cen vozlišč vrne seznam cen najcenejšega vozlišča,
    ki je dosegljivo iz posameznega vozlišča usmerjenega grafa G.

    Časovna zahtevnost: O(m)
    """
    n = len(G)
    assert n == len(p)
    komp, GL = decompose(G, DFS = DFS)
    seznam = [min(p[u] for u in k) for k in komp]
    for u in range(len(GL)):
        for s in GL[u]:
            if seznam[s] < seznam[u]:
                seznam[u] = seznam[s]
    c = [None] * n
    for k in range(len(komp)):
        cena = seznam[k]
        for v in komp[k]:
            c[v] = cena
    return c
