# -*- coding: utf-8 -*-
"""
Funkcije na usmerjenih grafih.

V ocenah časovne zahtevnosti je n število vozlišč v grafu,
m število povezav v grafu, d(u) pa število sosedov vozlišča u.
Pri tem predpostavljamo, da velja n = O(m)
(graf ima O(1) povezanih komponent).
"""
from vaje5 import DFS

def reverseGraph(G):
    """
    Vrne graf, katerega povezave so ravno nasprotne povezavam iz G.

    Časovna zahtevnost: O(m)
    """
    n = len(G)
    R = [[] for u in range(n)]
    for u in range(n):
        for v in G[u]:
            R[v].append(u)
    return R

def decompose(G, DFS = DFS):
    """
    Vrne seznam krepko povezanih komponent (seznam seznamov vozlišč)
    in metagraf usmerjenega grafa G (vozlišča ustrezajo vrnjenim komponentam).
    Komponente so podane v obratni topološki ureditvi glede na metagraf.

    Časovna zahtevnost: O(m)
    """
    n = len(G)
    R = reverseGraph(G)
    post = []
    def postorder(u, v):
        """
        Doda vozlišče v seznam ob njegovem zadnjem obisku.

        Časovna zahtevnost: O(1)
        """
        post.append(u)
        return True
    DFS(R, postvisit = postorder)
    l = [None] * n
    M = []
    c = 0
    comp = []
    def previsit(u, v):
        """
        Vozlišču dodeli krepko povezano komponento.

        Časovna zahtevnost: O(1)
        """
        if v is None:
            comp.append([])
            M.append(set())
        l[u] = c
        comp[c].append(u)
        return True
    def postvisit(u, v):
        """
        Doda povezave v metagraf.

        Časovna zahtevnost: O(d(u))
        """
        nonlocal c
        for w in G[u]:
            if l[w] != c:
                M[c].add(l[w])
        if v is None:
            c += 1
        return True
    DFS(G, roots = reversed(post), previsit = previsit, postvisit = postvisit)
    return (comp, [list(s) for s in M])
