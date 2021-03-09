# Eksempel: Ønsker åskrive ut en firkant av stjerner, hvor brukeren angir høyde og bredde
#
# Bredde 5, høyde 3
# *****
# *****
# *****

bredde = int(input("Bredde: "))
hoyde = int(input("Høyde: "))

for linje in range(hoyde):
    for tall in range(bredde):
        print("*", end="")
    print()


