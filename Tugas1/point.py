# Nama File: point.py
# Deskripsi : 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: / /

# +=========================================================================+ #
#                               Selektor
# +=========================================================================+ #

def absis(T):
    return T[0]
def ordinat(T):
    return T[1]

def T1(G):
    return G[0]
def T2(G):
    return G[1]
# +=========================================================================+ #
#                               Konstruktor
# +=========================================================================+ #

def maketitik(x,y):
    return[x,y]

def makegaris(T1,T2):
    return[T1,T2]

# +=========================================================================+ #
#                               Operator
# +=========================================================================+ #
def Gradien(G):
    return ((ordinat(T2(G))-ordinat(T1(G))) / (absis(T2(G))-absis(T1(G))))

def PanjangGaris(G):
    return (((absis(T2(G))-absis(T1(G)))**2 + (ordinat(T1(G))-ordinat(T2(G)))**2)**0.5)

# +=========================================================================+ #
#                                Predikat
# +=========================================================================+ #
def isSejajar(G1,G2):
    return Gradien(G1) == Gradien(G2)
def isTegakLurus(G1,G2):
    return (Gradien(G1)*Gradien(G2) == -1)
# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

print (Gradien(makegaris(maketitik(2,3),maketitik(4,6)))) # -> 1,5
print (PanjangGaris(makegaris(maketitik(2,3),maketitik(4,6)))) # -> 3.60555

# isSejajar?(G1,G2)
print(isSejajar(makegaris(maketitik(2,3),maketitik(4,6)),makegaris(maketitik(2,3),maketitik(4,6)))) # True
print(isSejajar(makegaris(maketitik(2,3),maketitik(4,6)),makegaris(maketitik(2,3),maketitik(4,9)))) # False

# isTegakLurus?(G1,G2)
print(isTegakLurus(makegaris(maketitik(2,3),maketitik(4,6)),makegaris(maketitik(2,3),maketitik(4,9)))) # False
print(isTegakLurus(makegaris(maketitik(0, 0), maketitik(1, 1)), makegaris(maketitik(0, 0), maketitik(1, -1))))  # True
