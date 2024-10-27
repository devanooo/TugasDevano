# Nama File: Pecahan.py
# Deskripsi : 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: / /

# +=========================================================================+ #
#                               Selektor
# +=========================================================================+ #

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
#                                Konstruktor
# +=========================================================================+ #
def makepecahancampuran(bil,pemcampur,penyecampur):
    return[bil,pemcampur,penyecampur]

def makepecahan(pembilang,penyebut):
    return[pembilang,penyebut]

# +=========================================================================+ #
#                               Operator
# +=========================================================================+ #

def konversipecahan(P):
    return makepecahan((d(P) * bil(P) + n(P)), d(P) )

def konversireal(P):
    return (d(P) * bil(P) + n(P) / d(P))

def AddP(P1,P2):
    return makepecahancampuran(bil(P1) + bil(P2),n(P1)*d(P2) + n(P2)*d(P1), d(P1)*d(P2))

def SubP(P1,P2):
    return makepecahancampuran(bil(P1) - bil(P2),n(P1)*d(P2) - n(P2)*d(P1), d(P1)*d(P2))

def DifP(P1,P2):
    return (pembilang(konversipecahan(P1))*penyebut(konversipecahan(P2))//(penyebut(konversipecahan(P1))*pembilang(konversipecahan(P2))))

def MulP(P1,P2):
    return (pembilang(konversipecahan(P1))*pembilang(konversipecahan(P2))/(penyebut(konversipecahan(P1))*penyebut(konversipecahan(P2))))

# +=========================================================================+ #
#                               Predikat
# +=========================================================================+ #
def IsEqP(P1,P2):
    return konversireal(P1) == konversireal(P2)
def IsLtP(P1,P2):
    return konversireal(P1) < konversireal(P2)
def IsLtP(P1,P2):
    return konversireal(P1) > konversireal(P2)

# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

print(konversipecahan(makepecahancampuran(2,1,3))) # [7,3]

print(konversireal(makepecahancampuran(2,1,3))) # 6.3

print(AddP(makepecahancampuran(2,1,3),makepecahancampuran(1,2,3))) #[3,9,9]

print(SubP(makepecahancampuran(2,1,3),makepecahancampuran(1,2,3))) #[1,-3,9]
