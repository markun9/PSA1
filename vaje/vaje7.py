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
    sez = toporder(G)
    poti = [0] * len(G)
    poti[s] = 1
    for v in sez[sez.index(s):sez.index(t)]:
        for u in G[v]:
            poti[u] += poti[v]
    return poti[t]

def hamiltonianPath(G):
    sez = toporder(G)
    for i in range(1, len(sez)):
        if sez[i] not in G[sez[i-1]]:
            return False
    return True

def cheapestReachable(G, p, DFS = DFS):
    n = len(G)
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
