# -*- coding: utf-8 -*-
class StackRecord:
    """Vnos v skladu"""
    def __init__(self, x = None, next = None):
        """
        Inicializacija vnosa v skladu.
        Časovna zahtevnost: O(1)
        """
        pass

    def __repr__(self):
        """
        Znakovna predstavitev vnosa v skladu.
        Časovna zahtevnost: O(1)
        """
        pass

class Stack:
    """Sklad (LIFO)"""
    def __init__(self):
        """
        Inicializacija sklada.
        Časovna zahtevnost: O(1)
        """
        pass

    def __len__(self):
        """
        Velikost sklada.
        Časovna zahtevnost: O(1)
        """
        pass

    def __repr__(self):
        """
        Znakovna predstavitev sklada.
        Časovna zahtevnost: O(n)
        """
        pass

    def clear(self):
        """
        Izprazni sklad.
        Časovna zahtevnost: O(1)
        """
        pass

    def peek(self):
        """
        Vrni vrhnji element v skladu.
        Časovna zahtevnost: O(1)
        """
        pass

    def pop(self):
        """
        Odstrani in vrni vrhnji element v skladu.
        Časovna zahtevnost: O(1)
        """
        pass

    def push(self, x):
        """
        Dodaj element na vrh sklada.
        Časovna zahtevnost: O(1)
        """
        pass

class QueueRecord:
    """Vnos v vrsti"""
    def __init__(self, x = None, prev = None, next = None):
        """
        Inicializacija vnosa v vrsti.
        Časovna zahtevnost: O(1)
        """
        pass

    def __repr__(self):
        """
        Znakovna predstavitev vnosa v vrsti.
        Časovna zahtevnost: O(1)
        """
        pass

class Queue:
    """Vrsta (FIFO)"""
    def __init__(self):
        """
        Inicializacija vrste.
        Časovna zahtevnost: O(1)
        """
        pass

    def __len__(self):
        """
        Dolžina vrste.
        Časovna zahtevnost: O(1)
        """
        pass

    def __repr__(self):
        """
        Znakovna predstavitev vrste.
        Časovna zahtevnost: O(n)
        """
        pass

    def clear(self):
        """
        Izprazni vrsto.
        Časovna zahtevnost: O(1)
        """
        pass

    def dequeue(self):
        """
        Odstrani in vrni prednji element vrste.
        Časovna zahtevnost: O(1)
        """
        pass

    def enqueue(self, x):
        """
        Dodaj element na konec vrste.
        Časovna zahtevnost: O(1)
        """
        pass

    def peek(self):
        """
        Vrni prednji element vrste.
        Časovna zahtevnost: O(1)
        """
        pass
