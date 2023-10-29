
###SORU1###

from colorama import Fore, Style, init

def a_kucuk(a, sıra):
    if a > 0 and a <= len(sıra):

        sıra.sort()

        return sıra[a - 1]
    else:
        return None


sıra = [7, 10, 4, 3, 20, 15]
a_degeri = 3

veri = a_kucuk(a_degeri, sıra)


###SORU2###
def yakın_sayılar(sayı, sıra):
    sıra.sort()
    yakın = None
    aradaki_fark = float('inf')

    for a in range(len(sıra) - 1):
        for b in range(a + 1, len(sıra)):
            toplam = sıra[a] + sıra[b]
            fark = abs(sayı - toplam)

            if fark < aradaki_fark:
                aradaki_fark = fark
                yakın = (sıra[a], sıra[b])

    return yakın

kullanımı = yakın_sayılar(90, [70, 22, 25, 178, 13, 230])





###SORU3###
def main(liste):
    return list({x for x in liste if liste.count(x) > 1})


liste = [1, 1, 2, 3, 3, 5, 6, 11, 8, 7, 7]
sırala = main(liste)




###SORU4###



def islem(matrisa, matrisb):
    if len(matrisa[0]) != len(matrisb):
        return "Matrislerin boyutları uyumlu değil."

    matris_bulma = list(map(list, zip(*matrisb)))

    sonuc = [[sum(ele1 * ele2 for ele1, ele2 in zip(row1, row2)) for row2 in matris_bulma] for row1 in matrisa]

    return sonuc


matrisa = [[1, 2, 3], [4, 5, 6]]
matrisb = [[7, 8], [9, 10], [11, 12]]
sonuc = islem(matrisa, matrisb)



###SORU5###
from collections import Counter

def kelime_tekrarı(dosyanın_yeri):
    try:
        with open(dosyanın_yeri, 'r') as dosya:
            metin = dosya.read()
            kelimeler = metin.split()  

            kelimelerin_sayisi= Counter(kelimeler)  
            return kelimelerin_sayisi

    except FileNotFoundError:
        return "Dosya bulunamadı."


dosyanın_yeri = "/Users/maclock/Desktop/giris_metnii.txt"
tekrarlama = kelime_tekrarı(dosyanın_yeri)

###SORU6###

def en_küçük_değer_bulma(liste):
    
    if not liste:
        return None

    if len(liste) == 1:
        return liste[0]


    küçük_değer = en_küçük_değer_bulma(liste[1:])
    if not liste[0] >= küçük_değer:
        return liste[0]
    else:
        return küçük_değer
Liste=[-35, 98, 42, 120, 45, -23]



###SORU7###

def kare_kok(C, x, toplam=1e-10, karekök=10):
    for y in range(karekök):
        nz = 0.5 * (x + C / x)
        yanlıs = abs(nz**2 - C)
        if yanlıs < toplam:
            return nz
        x = nz
    print(f"{karekök} iterasyonda sonuca ulaşılamadı. 'yanlıs' veya 'karekök' değerlerini değiştirin")
    return nz








###SORU8###


def ebob(x, y):
    
    if y == 0:
        return abs(x)
    else:
        return ebob(y, x % y)

sayi1 = 36
sayi2 = 48
result = ebob(sayi1, sayi2)




###soru9###


def asal_bulma(a, b=2):
    if a < 2:
        return "False"
    if a == 2:
        return "True"
    if a % b == 0:
        return "False"
    if b * b > a:
        return "True"
    return asal_bulma(a, b + 1)




###soru10###
def fibonacci_dizisi(x, y, z, t):
    if x == y:
        return z
    else:
        return fibonacci_dizisi(x, y + 1, z + t, z)

def hızlı_fibonacci(x):
    return fibonacci_dizisi(x, 1, 1, 0)


terim_sayısı = 13
sonuçç = hızlı_fibonacci(terim_sayısı)




#############CONSOLEEEE#############

def main():
    while True:
        print(Fore.GREEN +"1- a’nıncı En Küçük Elemanı Bulma")
        print(Fore.BLUE+"2- En Yakın Çifti Bulma")
        print(Fore.RESET+"3- Bir Listenin Tekrar Eden Elemanlarını Bulma")
        print(Fore.YELLOW+"4- Matris Çarpımı")
        print(Fore.BLACK+"5- Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
        print(Fore. WHITE+"6- Liste İçinde En Küçük Değeri Bulma")
        print(Fore.CYAN+"7- Karekök Fonksiyonu")
        print(Fore.MAGENTA +"8- En Büyük Ortak Bölen")
        print(Fore.BLUE+"9- Asallık Testi")
        print(Fore.RED +"10- Daha Hızlı Fibonacci Hesabı")
        print(Fore.YELLOW +"11- EXIT")

        seçenek_seç = input("Yapmak istediğiniz işlemi tuşlayabilir misiniz? ")




  
        if seçenek_seç == "1":
            if veri is not None:
              print(f"Listenin {a_degeri}. en küçük elemanı: {veri}")
            else:
               print("Geçersiz a değeri.")



        elif seçenek_seç == "2":
            kullanımı = yakın_sayılar(90, [70, 22, 25, 178, 13, 230])
            print( "En yakın sayılar" ,kullanımı)  





        elif seçenek_seç == "3":
         print("Tekrar eden elemanlar:", sırala)



        elif seçenek_seç =="4":
         for row in sonuc:
          print(row)




        elif seçenek_seç == "5":
            if isinstance(tekrarlama, str):
                print(tekrarlama)
            else:
              for kelime, sayi in tekrarlama.items():
                print(f"{kelime}={sayi}")






        elif seçenek_seç == "6":
            print(en_küçük_değer_bulma(Liste))  



        elif seçenek_seç=="7":
            sonuc_1 = kare_kok(C=10, x=1)
            print(sonuc_1)

            sonuc_2 = kare_kok(C=10000, x=0.1)
            print(sonuc_2)

            sonuc_3 = kare_kok(C=10000, x=0.1, karekök=15)
            print(sonuc_3)




        elif seçenek_seç=="8":
            print(f"SAYILARIN EBOB'U {result}")



        elif seçenek_seç=="9":
           print(asal_bulma(87))
           print(asal_bulma(43)) 


        elif seçenek_seç=="10":
            print(f"Fibonaccinin {terim_sayısı}.teriminin değeri  = {sonuçç}")









if __name__ == "__main__":
   main()
       
     
