# strenger oppfører seg mer som tupler, man kan gjøre mye av det samme ting

streng = "En teststreng for å demonstrere bruk av strenger"
print("Streng er: En teststreng for å demonstrere bruk av strenger")
print("---")


# kan printe en element av streng
streng[5]
print("Element 5 av streng er: ")
print(streng[5])
print("---")


# kan gjøre slicing på strenger
print("Kan gjøre slicing på strenger: ")
streng_sliced = streng[5:15]
print("Slicing på strenger: [5:15]")
print(streng_sliced)
print("---")


# spørre lengden av en streng
lengden_av_streng = len(streng)
print(f"Lengden av streng er: {lengden_av_streng}")
print("---")

# Splite strenger
# Split metoden tar en streng og slipe den
ordliste = streng.split()
print("Tester split metoden")
print(ordliste)
print("---")

#printer ut hver tegn for seg
for tegn in streng:
    print(tegn)
print("---")

# konvertere fra store bokstaver til små
print("konvertere fra store bokstaver til små:")
print(streng.lower())
print("---")

# konvertere fra små bokstaver til små
print("konvertere fra små bokstaver til store:")
print(streng.upper())
print("---")

# for å fjerne newline tegne på slutten av linje
# kan oppgi en parameter til strip, for eksempel . , :
streng4 = "Flere setninger. En til, to til."
ordliste = streng4.split()
print(ordliste)
for i in range(len(ordliste)):
    ordliste[i] = ordliste[i].strip(".,;")
print(ordliste)
print(", og . er borte nå :)")
print("---")


# finne ord i bruk  b erførste bokstaven i bruk
streng.find("bruk")
print(streng.find("bruk"))

streng[32:36]
print(streng[32:36])
print("---")

#noe som ikke finnes
streng.find("finne")
print(streng.find("finne"))
print("Når du får -1, betyr dette at det finnes ikke dette ordet i strengen")
print("---")
