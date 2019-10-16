#import morse as ms

#print(ms.lookup)
#a = ms.string_to_morse("sos")
#print(a)



#person = input("Nationalität?: ")
#alter = int(input("Alter?: "))
#print(person)

person = "f"
alter = 21

if person=="f":
    if alter > 20:
        print("Ist Franzose und aelter als 20")
    else:
         print("Nicht älter als 20")
else:
    print("Kein Franzose")


x = 1
print(eval("x+1"))


n = 100
sum_of_numbers = 0
i = 10
j=str(i)
while i <= n:
    sum_of_numbers += i
    i += 1

result = "Summe von " + j + " bis " + str(n) + ": " + str(sum_of_numbers)
print(result)


print()
languages = ["C", "C++", "Perl", "Python"]
for language in languages:
    print(language)

print()
edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        #break
        print("Great, delicious " + food)
    else:
        print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")


print()
for x in range(6):
    print(x)
