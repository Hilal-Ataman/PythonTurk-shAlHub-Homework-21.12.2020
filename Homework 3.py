# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:59:57 2020

@author: hp
"""

kullanıcı1= input("İlk önce adınızı ve soyadınızı girin")

print("Hoşgeldiniz", kullanıcı1, end="!\n")
import random

kelime_list = ["kitap" , "bilgisayar" , "sözlük" , "müzik" , "tren" ,"agac","elma","armut"]
tahminSayisi= 5
kelime = random.choice(kelime_list)
harfler = [] 
a= len(kelime)
b= list('_' * a)
print(' '.join(b), end='\n')

while tahminSayisi > 0:
    c = input("Bir harf giriniz : ")
    if c in harfler:
        print("Lutfen her harfi bir defa kullanınız...")
        continue

    elif len(c) > 1:
        print("Bir harf giriniz .")
        continue

    elif c not in kelime:   #girilen harf kelime icinde yoksa eger
        tahminSayisi -= 1
        print("hatalı tahmin!. {} tane harf hakkiniz kaldi.".format(tahminSayisi))


    else:
        for i in range(len(kelime)):
            if c == kelime[i]:
                print("Dogru Tahmin")
                b[i] = c
                harfler.append(c)
        print(' '.join(b), end='\n')

    cevap = input("Kelimenin tamamini tahmin etmek için ['i' veya 'k'] : ")

    if cevap == "i":
        tahmin = input("Kelimenin tamamini tahmin edeniz : ")
        if tahmin == kelime:
            print("Doğru Cevap!")
            break
        else:
            tahminSayisi-= 1
            print("Yanlis tahmin ettiniz. {} tane tahmin hakkiniz kaldi.". format(tahminSayisi))


    if tahminSayisi == 0:
        print("Tahmin hakkiniz kalmadi. Kaybettiniz!")
        break     
