# -*- coding: utf-8 -*-
from slowmatrix import SlowMatrix
from matrix import AbstractMatrix
import numpy
M = AbstractMatrix([[1,2,3], [4,5,6], [7,8,9]])

class FastMatrix(SlowMatrix):
    """
    Matrika z množenjem s Strassenovim algoritmom.
    """
    def multiply(self, left, right):
        """
        V trenutno matriko zapiše produkt podanih matrik.

        Množenje izvede s Strassenovim algoritmom.
        """
        assert left.ncol() == right.nrow(), \
               "Dimenzije matrik ne dopuščajo množenja!"
        assert self.nrow() == left.nrow() and right.ncol() == self.ncol(), \
               "Dimenzije ciljne matrike ne ustrezajo dimenzijam produkta!"
        l = right.ncol()  # št.stolpcev prve = št.vrstic druge
        n = left.nrow() #št.vrstic prve
        m = right.nrow()  #št.stolpcev druge

        #skica
        #      m                l               l
        #   [       ]       [        ]      [       ]
        # n [       ]   * m [        ] =  n [       ]
        #   [       ]       [        ]      [       ]
        u = 0
        n2 = 0
        l2 = 0
        m2 = 0
        while (n2 == 0 or m2 == 0 or l2 == 0):
            #print(u)
            if 2**u > n and n2 == 0:
                n2 = 2**(u-1)
            if 2**u > l and l2 == 0:
                l2 = 2**(u-1)
            if 2**u > m and m2 == 0:
                m2 = 2**(u-1)
            u += 1
        #print(n2, l2, m2)

        if n == 2 & m == 2 & l == 2:
            blok = int(min(n,l,m)/2)
            #print(blok)

            A11 = left[0:blok,0:blok]
            A12 = left[0:blok, blok:(2 * blok)]
            A21 = left[blok:(2*blok),0:blok]
            A22 = left[blok:(2*blok),blok:(2*blok)]

            B11 = right[0:blok,0:blok]
            B12 = right[0:blok, blok:(2 * blok)]
            B21 = right[blok:(2*blok),0:blok]
            B22 = right[blok:(2*blok),blok:(2*blok)]

            M1 = (A11 + A22)*(B11 + B22)
            M2 = (A21 + A22)*B11
            M3 = A11*(B12-B22)
            M4 = A22*(B21-B11)
            M5 = (A11 + A12)*B22
            M6 = (A21 - A11)*(B11 + B12)
            M7 = (A12 - A22)*(B21 + B22)

            C11 = M1 + M4 - M5 + M7
            C12 = M3 + M5
            C21 = M2 + M4
            C22 = M1 - M2 + M3 + M6

            C = AbstractMatrix([[0,0],[0,0]])
            C[0,0] = C11
            C[0,1] = C12
            C[1,0] = C21
            C[1,1] = C22
            return C
        elif l==1 or n==1 or m==1:
            C = SlowMatrix.multiply(self,left,right)
            return C
        else:
            C = AbstractMatrix([([0, ] * l), ]*n)
            A11 = left[0:(n2//2),0:(l2//2)]
            A12 = left[0:n2//2,(l2//2):l2]
            A21 = left[n2//2:n2,0:l2//2]
            A22 = left[n2//2:n2,l2//2:l2]

            B11 = right[0:l2//2,0:m2//2]
            B12 = right[0:l2//2,(m2//2):m2]
            B21 = right[l2//2:l2,0:m2//2]
            B22 = right[l2//2:l2,m2//2:m2]

            M1 = FastMatrix.multiply(AbstractMatrix([([0, ] * (m2//2)), ] * (n2 // 2)),(A11 + A22),(B11 + B22))
            M2 = FastMatrix.multiply(AbstractMatrix([([0, ] * (m2//2)), ] * (n2 // 2)),(A21 + A22),B11)
            M3 = FastMatrix.multiply(AbstractMatrix([([0, ] * (m2//2)), ] * (n2 // 2)),A11,(B12-B22))
            M4 = FastMatrix.multiply(AbstractMatrix([([0, ] * (m2//2)), ] * (n2 // 2)),A22,(B21-B11))
            M5 = FastMatrix.multiply(AbstractMatrix([([0, ] * (m2//2)), ] * (n2 // 2)),(A11 + A12),B22)
            M6 = FastMatrix.multiply(AbstractMatrix([([0, ] * (m2//2)), ] * (n2 // 2)),(A21 - A11),(B11 + B12))
            M7 = FastMatrix.multiply(AbstractMatrix([([0, ] * (m2//2)), ] * (n2 // 2)),(A12 - A22),(B21 + B22))

            C11 = M1 + M4 - M5 + M7
            C12 = M3 + M5
            C21 = M2 + M4
            C22 = M1 - M2 + M3 + M6

            #print(C,"C")
            #print(C12,"C12")
            C[0:n2 // 2, 0:m2 // 2]= C11[0:n2//2,0:m2//2]
            #print(C, "C")
            C[0:n2//2,(m2//2):m2] = C12[0:n2//2,0:m2//2]
            C[n2//2:n2,0:m2//2] = C21[0:n2//2,0:m2//2]
            C[n2//2:n2,m2//2:m2] = C22[0:n2//2,0:m2//2]

            print(C,"vmesni del, kjer so bloki OK, rabmo še ostalo")

            "odvečni deli"
            matrika = self
            c = 0
            #print(n, m,l)
            for n1 in range(n):
                for l1 in range(l):
                    for m1 in range(m):
                        #print(n1,n-n2,"nji",m1, m-m2,"mji", l1, l - l2, "lji")
                        if not (n1 < n2 and m1 < m2 and l1 < l2):
                            C[n1, l1] += left[n1, m1] * right[m1, l1]
                            #print(C, "to je C")
            return C


A = AbstractMatrix([[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [3,3,3,3]])
B = AbstractMatrix([[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]])
F = AbstractMatrix([[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0,0,0,0]])
#print(SlowMatrix.multiply(F,A,B))
#print(FastMatrix.multiply(F,A,B))

T = AbstractMatrix([[1,2,1,0,0],
                    [2,1,0,1,0],
                    [1,2,5,3,3]])
S = AbstractMatrix([[2,8,2,0,0,1,2],
                    [1,3,0,1,8,5,2],
                    [0,2,0,1,0,1,2],
                    [2,1,2,1,2,1,2],
                    [3,4,6,2,3,1,3]])
U = AbstractMatrix([([0, ] * 7), ] * 3)

print(SlowMatrix.multiply(U,T,S))
print(FastMatrix.multiply(U,T,S))