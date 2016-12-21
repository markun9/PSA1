# -*- coding: utf-8 -*-
from .slowmatrix import SlowMatrix

class CheapMatrix(SlowMatrix):
    """
    Matrika s prostorsko nepotratnim množenjem.
    """
    def multiply(self, left, right, work = None):
        """
        V trenutno matriko zapiše produkt podanih matrik.

        Kot neobvezen argument lahko podamo še delovno matriko.
        """
        assert left.ncol() == right.nrow(), \
               "Dimenzije matrik ne dopuščajo množenja!"
        assert self.nrow() == left.nrow() and right.ncol() == self.ncol(), \
               "Dimenzije ciljne matrike ne ustrezajo dimenzijam produkta!"
        if work is None:
            work = self.__class__(nrow = self.nrow(), ncol = self.ncol())
        else:
            assert self.nrow() == work.nrow() and self.ncol() == work.ncol(), \
               "Dimenzije delovne matrike ne ustrezajo dimenzijam produkta!"
        raise NotImplementedError("Naredi sam!")
        n2 = 0
        l2 = 0
        m2 = 0
        #n2,m2 in l2 predstavljajo največje število, ki je večkratnik 2 in manjše od indeksov n,m in l
        if n%2==0:
            n2 = n
        else:
            n2 = (n-1)
        if m%2==0:
            m2 = m
        else:
            m2 = (m-1)
            m2 = (m-1)
        if l%2==0:
            l2 = l
        else:
            l2 = (l-1)

        print(n2, l2, m2)
        if l==1 or n==1 or m==1: #robni pogoj, ko postane eden od parametrov l,m ali n enak 1. V tem primeru uporabimo naivno množenj
            work = SlowMatrix.multiply(self,left,right)
            return work
        else: #primer, kjer nobena od komponent ni enaka 1
            work = AbstractMatrix([([0, ] * l), ]*n) #velikost ciljne matrike. Moral bi biti self, vendar potem pride narobe.

            #print(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)))
            C22 = CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),(left[0:(n2//2),0:(m2//2)] + left[n2//2:n2,m2//2:m2]),(right[0:(m2//2),0:(l2//2)] + right[m2//2:m2,l2//2:l2])) - \
                  CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2 // 2)), ] * (n2 // 2)),
                                       (left[n2 // 2:n2, 0:m2 // 2] + left[n2 // 2:n2, m2 // 2:m2]),
                                       right[0:(m2 // 2), 0:(l2 // 2)])\
                  +            CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),left[0:(n2//2),0:(m2//2)],(right[0:m2//2,(l2//2):l2]-right[m2//2:m2,l2//2:l2])) \
            + CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),(left[n2//2:n2,0:m2//2] - left[0:(n2//2),0:(m2//2)]),(right[0:(m2//2),0:(l2//2)] + right[0:m2//2,(l2//2):l2]))

            work[0:n2 // 2, 0:l2 // 2]= CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),(left[0:(n2//2),0:(m2//2)] + left[n2//2:n2,m2//2:m2]),(right[0:(m2//2),0:(l2//2)] + right[m2//2:m2,l2//2:l2])) + \
                  CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2 // 2)), ] * (n2 // 2)),
                                       left[n2 // 2:n2, m2 // 2:m2],
                                       (right[m2 // 2:m2, 0:l2 // 2] - right[0:(m2 // 2), 0:(l2 // 2)])) \
                  - CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),(left[0:(n2//2),0:(m2//2)] + left[0:n2//2,(m2//2):m2]),right[m2//2:m2,l2//2:l2]) \
                  + CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),(left[0:n2//2,(m2//2):m2] - left[n2//2:n2,m2//2:m2]),(right[m2//2:m2,0:l2//2] + right[m2//2:m2,l2//2:l2]))[0:n2//2,0:l2//2] #združitev komponent v C
            work[0:n2//2,(l2//2):l2] = CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),left[0:(n2//2),0:(m2//2)],(right[0:m2//2,(l2//2):l2]-right[m2//2:m2,l2//2:l2])) + \
                    CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2 // 2)), ] * (n2 // 2)),
                                         (left[0:(n2 // 2), 0:(m2 // 2)] + left[0:n2 // 2, (m2 // 2):m2]),
                                         right[m2 // 2:m2, l2 // 2:l2])[0:n2//2,0:l2//2]
            work[n2//2:n2,0:l2//2] = CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),(left[n2//2:n2,0:m2//2] + left[n2//2:n2,m2//2:m2]),right[0:(m2//2),0:(l2//2)]) + \
                  CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2 // 2)), ] * (n2 // 2)),
                                       left[n2 // 2:n2, m2 // 2:m2],
                                       (right[m2 // 2:m2, 0:l2 // 2] - right[0:(m2 // 2), 0:(l2 // 2)]))[0:n2//2,0:l2//2]
            work[n2//2:n2,l2//2:l2] = CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),(left[0:(n2//2),0:(m2//2)] + left[n2//2:n2,m2//2:m2]),(right[0:(m2//2),0:(l2//2)] + right[m2//2:m2,l2//2:l2])) - \
                  CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2 // 2)), ] * (n2 // 2)),
                                       (left[n2 // 2:n2, 0:m2 // 2] + left[n2 // 2:n2, m2 // 2:m2]),
                                       right[0:(m2 // 2), 0:(l2 // 2)])\
                  +            CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),left[0:(n2//2),0:(m2//2)],(right[0:m2//2,(l2//2):l2]-right[m2//2:m2,l2//2:l2])) \
            + CheapMatrix.multiply(AbstractMatrix([([0, ] * (l2//2)), ] * (n2 // 2)),(left[n2//2:n2,0:m2//2] - left[0:(n2//2),0:(m2//2)]),(right[0:(m2//2),0:(l2//2)] + right[0:m2//2,(l2//2):l2]))[0:n2//2,0:l2//2]

            #odvečni deli, ki niso deli bloka
            #print(n, m,l)
            for n1 in range(n):
                for l1 in range(l):
                    for m1 in range(m):
                        #print(n1,n-n2,"nji",m1, m-m2,"mji", l1, l - l2, "lji")
                        if not (n1 < n2 and m1 < m2 and l1 < l2):
                            work[n1, l1] += left[n1, m1] * right[m1, l1]
            return work


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

T = AbstractMatrix([[1,2,1,0,0,3,3,3,3,3,5],
                    [2,1,0,1,0,4,5,6,7,8,8],
                    [1,2,5,3,3,5,5,6,2,7,7]])
S = AbstractMatrix([[2,8,2,0,0,1,2],
                    [1,3,0,1,8,5,2],
                    [0,2,0,1,0,1,2],
                    [2,1,2,1,2,1,2],
                    [3,4,6,2,3,1,3],
                    [2, 1, 2, 1, 2, 1, 2],
                    [2, 1, 2, 1, 2, 1, 2],
                    [2, 1, 2, 1, 2, 1, 2],
                    [2, 1, 2, 1, 2, 1, 2],
                    [2, 1, 2, 1, 2, 1, 2],
                    [2, 1, 2, 1, 2, 1, 2],])
U = AbstractMatrix([([0, ] * 7), ] * 3)

print(SlowMatrix.multiply(U,T,S))
print(FastMatrix.multiply(U,T,S))

#hitrejša koda, upošteva še sodost, lihost