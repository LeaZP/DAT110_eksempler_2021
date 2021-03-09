print("Test", end=" ")
print("En test til")
print("Tredje test")
print("Tester linjeskift. \n Dette kommer på ei ny linje \n\tEtter tabulator")
print("Spesialtegn: \" \\")

tall = 5/3
test = "to"
streng = format(tall, "8.4f")
print(streng)
print(f"Tallet er: {tall:8.4f} og strengen er {test}")

#Formatteringskoder
#   5.2f: Flyttall med 5 siffer (inkludert kommaet), hvorav 2 er bak komma.
#   8d: Heltall på vanlig format hvor den setter av 8 siffer
