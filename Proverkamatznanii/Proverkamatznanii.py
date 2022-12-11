from math import *
from random import *

print("Проверка математических знаний")
j=0
arv1= randint(1,10)
arv11= randint(1,10)
arv2= randint(-10,10)
arv22= randint(-10,10)
arv3= randint(-10,100)
arv33= randint(-10,100)

dificulty=int(input("Выберите сложность от 1(просто) до 3(сложно): "))
if dificulty==1:
    print(arv1,"+",arv11,"=")
    vastus=float(input("Ответ: "))
    while arv1+arv11==vastus:
        j+=20
        
        break

    print(arv1,"-",arv11,"=")
    vastus2=float(input("Ответ :"))
    while arv1-arv11==vastus2:
        j+=20
        
        break

    print(arv1,"*",arv11,"=")
    vastus3=float(input("Ответ: "))
    while arv1*arv11==vastus3:
        j+=20
      
        break

    print(arv1,"/",arv11,"=")
    vastus4=float(input("Ответ :"))
    while arv1/arv11==vastus4:
        j+=20
        
        break

    print(arv1,"^2","=")
    vastus5=float(input("Ответ: "))
    while arv1**2==vastus5:
        j+=20
      
        break
elif dificulty==2:
    print(arv2,"+","(",arv22,")","=")
    vastus=float(input("Ответ: "))
    while arv2+arv22==vastus:
        j+=20
        
        break

    print(arv2,"-","(",arv22,")","=")
    vastus2=float(input("Ответ :"))
    while arv2-arv22==vastus2:
        j+=20
       
        break

    print(arv2,"*","(",arv22,")","=")
    vastus3=float(input("Ответ: "))
    while arv2*arv22==vastus3:
        j+=20
        
        break

    print(arv2,"/","(",arv22,")","=")
    vastus4=float(input("Ответ :"))
    while arv2/arv22==vastus4:
        j+=20
      
        break

    print("(",arv2,")","^2","=")
    vastus5=float(input("Ответ: "))
    while arv2**2==vastus5:
        j+=20
       
        break
elif dificulty==3:
    print(arv3,"+","(",arv33,")","=")
    vastus=float(input("Ответ: "))
    while arv3+arv33==vastus:
        j+=20
        
        break

    print(arv3,"-","(",arv33,")","=")
    vastus2=float(input("Ответ :"))
    while arv3-arv33==vastus2:
        j+=20
       
        break

    print(arv3,"*","(",arv33,")","=")
    vastus3=float(input("Ответ: "))
    while arv3*arv33==vastus3:
        j+=20
        
        break

    print(arv3,"/","(",arv33,")","=")
    vastus4=float(input("Ответ :"))
    while arv3/arv33==vastus4:
        j+=20
        break

    print("(",arv3,")","^2","=")
    vastus5=float(input("Ответ: "))
    while arv3**2==vastus5:
        j+=20
        break
else:
    print("Нет такой сложности ¯\_(ツ)_/¯")
if j<60:
    print("Оценка: 2")
elif j>=60 and j<=75:
    print("Оценка: 3")
elif j>=75 and j<=90:
    print("Оценка: 4")
else:
    print("Оценка: 5")