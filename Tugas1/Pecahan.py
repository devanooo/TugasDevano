# Nama File: Pecahan.py
# Deskripsi : tipe data pecahan
# Nama / NIM : Devano Trestanto / 24060124140149


# +=========================================================================+ #
#                   DEFINISI DAN SPESIFIKASI TYPE
# +=========================================================================+ #

# type pecahan : <pembilang : integer >=0, Penyebut : Integer > 0>
# {<pembilang,penyebut> mewakili sebuah pecahan dimana pembilang sebagai numerator dan penyebut sebagai denumerator}

#type pecahancampuran : <bil : integer, n : integer >=0 , d = integer > 0>
# {<bil,n,d> mewakili sebuah pecahan campuran dengan bil sebagai bilangan, n sebagai numerator, dan d sebagai denumerator}


# +=========================================================================+ #
#                               Selektor
# +=========================================================================+ #

def bil(p):
    return p[0]
# {bil(p) memberikan bilangan dari pecahan campuran P}
def n(p):
    return p[1] #pembilang
# {bil(p) memberikan pembilang dari pecahan campuran P}
def d(p):
    return p[2] #penyebut
# {bil(p) memberikan penyebut dari pecahan campuran P}

def pembilang(p):
    return p[0]
# {bil(p) memberikan pembilang dari pecahan  P}
def penyebut(p):
    return p[1]
# {bil(p) memberikan penyebut dari pecahan  P}

# +=========================================================================+ #
#                                Konstruktor
# +=========================================================================+ #
def makepecahancampuran(bil,pembilang,penyebut):
    return[bil,pembilang,penyebut]
# {makepecahancampuran(bil,pembilang,penyebut) membentuk pecahan campuran dimana bil adalah bilangan,
# pembilang adalah pembilang dan penyebut adalah penyebut dari pecahan campuran}
def makepecahan(pembilang,penyebut):
    return[pembilang,penyebut]
# {makepecahan(pembilang,penyebut) membentuk pecahan biasa dimana pembilang adalah pembilang dan penyebut adalah penyebut}

# +=========================================================================+ #
#                        Definisi dan Spesifikasi Operator
# +=========================================================================+ #

# konversipecahan : pecahancampuran -> pecahan 
# {konversipecahan(P) mengubah bentuk pecahan campuran menjadi bentuk pecahan biasa}

# konversireal : pecahancampuran -> real
# {konversireal(p) mengubah bentuk pecahan campuran p menjadi bentuk real}

# AddP : 2 pecahancampuran -> pecahancampuran
# {AddP(P1,P2) menjumlahkan 2 pecahan campuran}

# SubP : 2 pecahancampuran -> pecahancampuran
# {SubP(P1,P2) mengurangi 2 pecahan campuran} 

# DivP : 2 pecahancampuran -> real
# {DivP(P1,P2) memberikan hasil bagi dari 2 pecahan campuran P1 dan P2}
# MulP : 2 pecahancampuran -> real
# {MulP(P1,P2) memberikan hasil kali dari 2 pecahan campuran P1 dan P2} 


# +=========================================================================+ #
#                        Definisi dan Spesifikasi Predikat
# +=========================================================================+ #
# IsEqP?: 2 pecahancampuran -> boolean
# IsEqP?(P1,P2) bernilai benar jika nilai real P1 sama dengan P2

# IsLtP?: 2 pecahancampuran -> boolean
# IsLtP?(P1,P2) bernilai benar jika nilai real P1 lebih kecil P2

# IsLtP?: 2 pecahancampuran -> boolean
# IsLtP?(P1,P2) bernilai benar jika nilai real P1 lebih besar P2
# +=========================================================================+ #
#                               REALISASI
# +=========================================================================+ #
def IsEqP(P1,P2):
    return konversireal(P1) == konversireal(P2)
def IsLtP(P1,P2):
    return konversireal(P1) < konversireal(P2)

def konversipecahan(P):
    return makepecahan((d(P) * bil(P) + n(P)), d(P) )
def konversireal(P):
    return (d(P) * bil(P) + n(P) / d(P))

def AddP(P1,P2):
    return makepecahancampuran(bil(P1) + bil(P2),n(P1)*d(P2) + n(P2)*d(P1), d(P1)*d(P2))
 
def SubP(P1,P2):
    return makepecahancampuran(bil(P1) - bil(P2),n(P1)*d(P2) - n(P2)*d(P1), d(P1)*d(P2))


def DivP(P1,P2):
    return (pembilang(konversipecahan(P1))*penyebut(konversipecahan(P2))//(penyebut(konversipecahan(P1))*pembilang(konversipecahan(P2))))
 
def MulP(P1,P2):
    return (pembilang(konversipecahan(P1))*pembilang(konversipecahan(P2))/(penyebut(konversipecahan(P1))*penyebut(konversipecahan(P2))))
def IsGtP(P1,P2):
    return konversireal(P1) > konversireal(P2)


# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

print(konversipecahan(makepecahancampuran(2,1,3))) # [7,3]

print(konversireal(makepecahancampuran(2,1,3))) # 6.3

print(AddP(makepecahancampuran(2,1,3),makepecahancampuran(1,2,3))) #[3,9,9]

print(SubP(makepecahancampuran(2,1,3),makepecahancampuran(1,2,3))) #[1,-3,9]
