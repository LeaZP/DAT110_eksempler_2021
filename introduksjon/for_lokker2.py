#Fakultet
#Testing av lovlig input med while, mer bruker vennlig...

# Ber brukeren om input og konverter dette til et heltall
parameter = int(input("Hvilket tall vil du ha fakultet til? "))  #int parameter konverterer den til heltall

while parameter < 0:
    print("Fakultet av et negativt tall finnes ikke!")
    parameter = int(input("Hvilket tall vil du ha fakultet til? "))
#Range: går gjennom alle tall fra 0 til men ikke med parameteren
resultat = 1
for tall in range(1, parameter+1):
    resultat *= tall
    print(f"tall: {tall} Foreløpig resultat: {resultat}")
print(resultat)
