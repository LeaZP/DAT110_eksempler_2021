# Eksempel: Ønsker å skrive ut en forkant av stjerner, hvor brukeren
# angir høyde og bredde
#
#Bredde 5, høyde 3
# * * * * *
# * * * * *
# * * * * *

#skriver hoyde ikke høyde, brukker ikke norske bokstaver i Python, men kan bruke ø i en streng
bredde = int(input("Bredde: "))
hoyde = int(input("Høyde: "))
for linje in range(hoyde):
    for tall in range(bredde):
        print("*", end="")  #for å ikke ha linjeskift mellom * skriver: end=""
    print()  #for å skrive ut en linjeskift
