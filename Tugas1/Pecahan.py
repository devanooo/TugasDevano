# Nama File: Pecahan.py
# Deskripsi : 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: / /

# +=========================================================================+ #
#                       Definisi dan Spesifikasi Selektor
# +=========================================================================+ #

# (variable) = (input) -> (output)
# (detailed description)

def bil(p):
    return p[0]
def n(p):
    return p[1] #pembilang
def d(p):
    return p[2] #penyebut

def pembilang(p):
    return p[0]
def penyebut(p):
    return p[1]

# +=========================================================================+ #
#                        Definisi dan Spesifikasi Konstruktor
# +=========================================================================+ #
def makepecahancampuran(bil,pemcampur,penyecampur):
    return[bil,pemcampur,penyecampur]

def makepecahan(pembilang,penyebut):
    return[pembilang,penyebut]

# +=========================================================================+ #
#                         Definisi dan Spesifikasi Operator
# +=========================================================================+ #

def konversipecahan(P):
    return makepecahan((d(P) * bil(P) + n(P)), d(P) )

def konversireal(P):
    return (d(P) * bil(P) + n(P) / d(P))

def AddP(P1,P2):
    return makepecahancampuran(bil(P1) + bil(P2),n(P1)*d(P2) + n(P2)*d(P1), d(P1)*d(P2))

def SubP(P1,P2):
    return makepecahancampuran(bil(P1) - bil(P2),n(P1)*d(P2) - n(P2)*d(P1), d(P1)*d(P2))


# +=========================================================================+ #
#                               Realisasi
# +=========================================================================+ #


# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #