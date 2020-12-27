# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:27:58 2020

@author: hp
"""
"""ilk defa bu programda kod yazdım açıkçası problemi çözemedim.Kendime 
özgü bir şey olmadığı içinde kopyala yapıştır yamak istemedim farklı bir kaynaktan
Top leaner programına katılmayı çok isterim ama şans"""       
name = "Hilal"
surname = "ATAMAN"

counter=3
while True:
    
   if (counter>0):
       student_name= input("Write your student name: ")
       student_surname= input("Write your student surname: ") 
       if student_name== name and  student_surname == surname:
           print("Welcome") 
           break
       elif student_name== name and  student_surname != surname: 
           print("Student_surname is false\n")    
       elif student_name != name and  student_surname == surname: 
           print("Student_name is false\n")     
       elif not student_name.strip() and not student_surname .strip(): 
           print("You must write string value.") 
       else: 
           print("student_name and student_name are false=\n")
           
       counter -=1  
   else :
       print("çok fazla denem yaptınız daha sonra tekrar deneyiniz")
       break 


arasınav= input("Vize 1 notunuzu girin; ")
final= input("Vize 2 notunuzu girin; ")
proje= input("Final notunuzu girin; ")


derece =int(int(arasınav)*3/10 + int(proje)*2/10 +int(final)*5/10)

if (derece > 90):
    print ("Ders notunuz A")

elif (derece>=70 or derece<90):
    print ( "Ders notunuz B")

elif (derece>=50 or derece<70):
    print ("Ders notunuz C")

elif (derece>=30 or derece<50):
    print ("Ders notunuz D")

else:
    print ("Dersten kaldınız")