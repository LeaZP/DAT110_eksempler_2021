tall_streng = input("skriv inn et tall: ")
tall = float(tall_streng)

if tall < 0.0:
    print("Tallet er lavere enn 0")
    print("Tester ei linje til")
elif tall ==\
        0.0:
    print("Tallet eksakt 0")
else:
    print("Tallet er høyere enn 0")
    print("Tester....")
print("Avslutter")

#Ta inn en alder og sjekk om personen er tenåring: tallet er mellom 13 og 19

tall_streng = input("Skriv inn en alder: ")
tall = float(tall_streng)
if tall >= 13 and tall <= 19:
    print("Personen er tenåring")
