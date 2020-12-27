# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 19:01:09 2020

@author: hp
"""


kullanıcı = list()
ad = input("Adınızı giriniz : ")
kullanıcı.append(["ad",ad])

soyad = input("Soyadınızı giriniz : ")
kullanıcı.append(["soyad", sayad])

yas = int(input("Yasınızı giriniz : "))
kullanıcı.append(["yas", yas])

tarih = int(input("Tarih giriniz : "))
kullanıcı.append(["tarih",tarih])

print(kullanıcı)

for i in kullanıcı:
    print(i)
    
if (yas>18):
    if (yas=='18'):
        print(f'{ad} Yaşın 18 den küçük evde kalmalısın .')
    else:
        print(f'{ad} Yasın 18 den büyük dışarı çıkabilirsin.')