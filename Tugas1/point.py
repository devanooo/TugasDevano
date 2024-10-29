# Nama File: point.py
# Deskripsi : tipe data garis dan point
# Nama / NIM : Devano Trestanto / 24060124140149

# +=========================================================================+ #
#                   DEFINISI DAN SPESIFIKASI TYPE
# +=========================================================================+ #

# type garis <P1 : point, P2 : point>
# {<P1,P2> membentuk garis dari dua titik}

# type point <x : real, y : real>
# {<x,y> adalah sebuah point dengan x adalah absis dan y adalah ordinat}

# +=========================================================================+ #
#                   DEFINISI DAN SPESIFIKASI SELEKTOR
# +=========================================================================+ #

def absis(T):
    return T[0]
# {absis(T) memberikan absis dari sebuah titik}
def ordinat(T):
    return T[1]
# {ordinat(T) memberikan ordinat dari sebuah titik}

def T1(G):
    return G[0]
# {T1(G) memberikan titik awal dari sebuah garis}
def T2(G):
    return G[1]
# {T2(G) memberikan titik akhir dari sebuah garis}

# +=========================================================================+ #
#                   DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# +=========================================================================+ #

def makepoint(x,y):
    return[x,y]
# {makepoint(x,y) membentuk point dari x,y dimana x adalah absis dan y adalah ordinat}
def makegaris(T1,T2):
    return[T1,T2]
# {makegaris(x,y) membentuk garis dari T1,T2 dimana T1 adalah titik awal dari garis dan T2 adalah titik akhir dari garis}

# +=========================================================================+ #
#                   DEFINISI DAN SPESIFIKASI OPERATOR
# +=========================================================================+ #
# Gradien : garis -> real
# {Gradien(G) menghitung gradien dari garis G}

# PanjangGaris : garis -> real
# {PanjangGaris(G) menghitung panjang garis dari garis G}


# +=========================================================================+ #
#                      DEFINISI DAN SPESIFIKASI PREDIKAT
# +=========================================================================+ #
# isSejajar? 2 garis -> boolean
# isSejajar?(G1,G2) bernilai benar jika G1 dan G2 Sejajar 

# isTegakLurus? 2 garis -> boolean
# isTegakLurus?(G1,G2) bernilai benar jika G1 dan G2 tegak lurus 

# +=========================================================================+ #
#                                REALISASI
# +=========================================================================+ #
def Gradien(G):
    return ((ordinat(T2(G))-ordinat(T1(G))) / (absis(T2(G))-absis(T1(G))))

def PanjangGaris(G):
    return (((absis(T2(G))-absis(T1(G)))**2 + (ordinat(T1(G))-ordinat(T2(G)))**2)**0.5)
def isSejajar(G1,G2):
    return Gradien(G1) == Gradien(G2)

def isTegakLurus(G1,G2):
    return (Gradien(G1)*Gradien(G2) == -1)


# +=========================================================================+ #
#                                APLIKASI
# +=========================================================================+ #

print (Gradien(makegaris(makepoint(2,3),makepoint(4,6)))) # -> 1,5
print (PanjangGaris(makegaris(makepoint(2,3),makepoint(4,6)))) # -> 3.60555

# isSejajar?(G1,G2)
print(isSejajar(makegaris(makepoint(2,3),makepoint(4,6)),makegaris(makepoint(2,3),makepoint(4,6)))) # True
print(isSejajar(makegaris(makepoint(2,3),makepoint(4,6)),makegaris(makepoint(2,3),makepoint(4,9)))) # False

# isTegakLurus?(G1,G2)
print(isTegakLurus(makegaris(makepoint(2,3),makepoint(4,6)),makegaris(makepoint(2,3),makepoint(4,9)))) # False
print(isTegakLurus(makegaris(makepoint(0, 0), makepoint(1, 1)), makegaris(makepoint(0, 0), makepoint(1, -1))))  # True
