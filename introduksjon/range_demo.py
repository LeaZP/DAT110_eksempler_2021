for tall in range(1, 10):
    print(tall)
print()
print("-------")
print()
for tall in range(10):
    print(tall)
print("-------")
for tall in range(5, 10):
    print(tall)
print("-------")
for tall in range(-5, 10):
    print(tall)
print("-------")
for tall in range(-5, 12, 3):
    print(tall)
print("-------")
for tall in range(10, 0, -1):  # telle nedover, fra og med 10, til men ikke med 0, negativ steg -1
    print(tall)
print("-------")
print("-------")

liste = [1, 3, 6, 9, 11]

for element in liste:
    print(element)
print("-------")
for element in liste:
    element = 2*element  #dette skal ikke påvirke liste som helhet
    print(element)

#For å modifisere elementet i liste
for index in range(len(liste)):
    liste[index] = 2*liste[index]

print("-------")
print("-------")

for potens in range(20):
    print(2**potens)
