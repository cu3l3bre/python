# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:48:34 2019

@author: Alfa
"""

mytuple = (1,2,3)

mylist = list(mytuple)

mylist[0] = 4

mytuple = tuple(mylist)

#mytuple[0] = 100



myString = "HalloWelt"
#myString[0]= "h" # ist so nicht erlaubt
print(myString)
print(myString[:1])
print(myString[2:])
myString = myString[:1] + "E" + myString[2:];

print(myString)


myString2 = "GutenTag"
print(myString2)
myList2 = list(myString2)
myList2[6] = "A"
myList2[7] = "G"
myString2 = ''.join(myList2)
print(myString2)


x = 0
while(x < 10):
    print(x)
    x += 1


y = 10
z = 20
print(id(y),id(z))
y = z
print(id(y),id(z))

#print(id(3))
#print(id(1‬))
print(id(2))
print(id(3))
#print(id(2))
#print(id(1))

a = 42949672967

# key values
u = {"a":1, "b":2, "c": "bla"}
print(u["a"])
print(u["b"])
print(u["c"])
print(type(u))


v = {1:10,2:20,"3abc":30}
print(v[1])
print(v[2])
print(v["3abc"])

en_de = {"red":"rot","green":"gruen","blue":"blau","yellow":"gelb"}
print(en_de["red"])
#print(en_de.())

dicttest = {"a":2, "a":3}
print(dicttest["a"])


dic = { (1,2,3):"abc", 3.1415:"abc"}
print(dic[(1,2,3)])



de_en = {"rot":"red","blau":"blue"}
de_fr = {"rot":"rouge", "blue":"bleu"}

dics = {"de_en" : de_en, "de_fr" : de_fr}
print()
print(dics["de_en"]["blau"])
print(dics["de_fr"]["rot"])


capitals = {"Hessen":"Wiesbaden", "Saarland":"Saarbrücken", "Baden-Württemberg":"Stuttgart", "Rheinland-Pfalz":"Mainz", "NordrheinWestfalen":"Düsseldorf"}


print(capitals.pop("Hessen","unbekannt"))
print(capitals.pop("Hessen","unbekannt"))

(land, capital) = capitals.popitem()
pair = capitals.popitem()
print(pair)