import numpy as np

# Lager en array med 10 0-ere, det skal være lang 10 celler, floats
array = np.zeros(10)

# Kan indeksere og tilordne som ei liste, men kan ikke legge til elementer da
# numpy arrays har en fast størrelse, definert nbår du lager den
array[5] = 3

# en annet mæte å lage numpy array
# Lager en array med elementene fra og med 0, til men ikke med 10, og med
# 0.2 mellom hvert element
# støtter floats, både start, slutt og slutt kan være flyttall
array2 = np.arange(0, 10, 0.2)

#standard python range funksjon tar bare heltall( int), mens numpy array tar flyttall (floats)

print(array)
print(array2)

# kan lage en numpy array fra en liste
liste = [1, 3, 5, 7, 9]
array4 = np.array(liste)
print(array4)
print()

#man kan gjøre mye matematikk med numpy arrays
array4 = array4 + 5
print(array4)
print()

array4 = array4 * 2
print(array4)
print()

# Kan summere og multiplisere to arrays med samme dimensjoner (må være like lang), dette gjøres
# element for element.
liste3 = [1, 1, 1, 1, 1]
array3 = np.array(liste3)
array5 = array3 + array4

print(array5)
print()

# Kan gjøre matematiske operasjoner på numpy arrays:
print(array2 + 10)
print(array2 * 5)  # ganges alle elementene med 5



# Numpy inneholder matematiske funksjoner som opererer element-for-element
# på numpy arrays. Eksempel sinus:
print(np.sin(array2))








# LAger en 4*3 matrise gjennom å oppgi et tuppel med to elementer i stedet for
# en enkeltverdi
matrise = np.zeros((4, 3))

print(matrise)

# Vanlig matrisemultiplikasjon gjøres med @ operatoren på numpy arrays
