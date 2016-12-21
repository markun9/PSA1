# -*- coding: utf-8 -*-
from matrix import AbstractMatrix

class SlowMatrix(AbstractMatrix):
    """
    Matrika z naivnim množenjem.
    """
    def multiply(self, left, right):
        """
        V trenutno matriko zapiše produkt podanih matrik.

        Množenje izvede z izračunom skalarnih produktov
        vrstic prve in stolpcev druge matrike."""""
        m = right.nrow()  # št. stolpcev prve = št.vrstic druge
        n = left.nrow() #št.vrstic prve
        l = right.ncol()  #št.stolpcev druge

        #skica
        #      m                l               l
        #   [       ]       [        ]      [       ]
        # n [       ]   * m [        ] =  n [       ]
        #   [       ]       [        ]      [       ]
        assert left.ncol() == right.nrow(), \
            "Dimenzije matrik ne dopuščajo množenja!"

        assert self.nrow() == left.nrow() and right.ncol() == self.ncol(), \
             "Dimenzije ciljne matrike ne ustrezajo dimenzijam produkta!"
        matrika = self
        c= 0
        #print(n,l,m)
        for n1 in range(n):
            for l1 in range(l):
                for m1 in range(m):
                    #print(n1,m1,l1,"prva")
                    matrika[n1,l1] += left[n1,m1]*right[m1,l1]
        return matrika

C = [[3,2,1],[3,5,1]]
D = [[1],[8],[5]]
E = [[0,0]]

#print(SlowMatrix.multiply(E,C,D))

#Ciljna matrika more bit matrika ničel.