# -*- coding: utf-8 -*-
class StackRecord:
    """Vnos v skladu"""
    def __init__(self, x = None, next = None):
        """
        Inicializacija vnosa v skladu.
        Časovna zahtevnost: O(1)
        """
        self.x = x
        self.next = next

    def __repr__(self):
        """
        Znakovna predstavitev vnosa v skladu.
        Časovna zahtevnost: O(1)
        """
        return repr(self.x)

class Stack:
    """Sklad (LIFO)"""
    def __init__(self):
        """
        Inicializacija sklada.
        Časovna zahtevnost: O(1)
        """
        self.clear()

    def __len__(self):
        """
        Velikost sklada.
        Časovna zahtevnost: O(1)
        """
        return self.len

    def __repr__(self):
        """
        Znakovna predstavitev sklada.
        Časovna zahtevnost: O(n)
        """
        cur = self.top
        out = '<| '
        while cur is not None:
            out += '%s, ' % repr(cur)
            cur = cur.next
        return out + '#'

    def clear(self):
        """
        Izprazni sklad.
        Časovna zahtevnost: O(1)
        """
        self.len = 0
        self.top = None

    def peek(self):
        """
        Vrni vrhnji element v skladu.
        Časovna zahtevnost: O(1)
        """
        if self.top is None:
            raise IndexError("sklad je prazen")
        return self.top.x

    def pop(self):
        """
        Odstrani in vrni vrhnji element v skladu.
        Časovna zahtevnost: O(1)
        """
        if self.top is None:
            raise IndexError("sklad je prazen")
        top = self.top
        self.top = top.next
        self.len -= 1
        return top.x

    def push(self, x):
        """
        Dodaj element na vrh sklada.
        Časovna zahtevnost: O(1)
        """
        self.top = StackRecord(x, self.top)
        self.len += 1

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
