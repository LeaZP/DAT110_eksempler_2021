#Filer
#  Tekstfiler
#       CSV - comma separated value
#  Binærfiler

#Modus
#  r - ønsker å lese file (Read)
#  w - ønskerå skrive fila, ønsker å slette ei eventuell gammel fil (write), skriver over den gamle filen med samme navn
#  a - Ønsker å skrive fila, legger til på skutten hvis den finnes (Append)
#  x - ØNsker å skrive fila, feiler om fila allerede finnes

#Filreferanser er objekter

#Objekt
#  Datatype
#  Inneholder tilstand og metoder
#  En metode er funksjon som du bruker på et objek og som gjør ting med objektet


max = 0.0       # 0.0 er tall som er mindre enn alle
min = 1000.0    # 1000.0 er tall som er større enn alle
sum = 0.0
antall = 0

try:
    filreferanse = None             #None: den variabelen finnes, men ligner ingenting ?????
    filreferanse = open("vindmaalinger.txt", "r")
    for linje in filreferanse:      # laster inn linje
        tall = float(linje)         # konverterer linje til flyttall
        if tall > max:              # sjekke om tallet jeg har lest inn er større enn foreløpig max
            max = tall
        if tall < min:
            min = tall
        sum += tall                 # tar summen og øker den med tallet
        antall += 1                 # øker antall med 1
    gjennomsnitt = sum/antall
    print(f"Minimum vindstyrke: {min}")
    print(f"Maksimum vindstyrke: {max}")
    print(f"Gjennomsnitt vindstyrke: {gjennomsnitt}")

except IOError: # IOError handler om forskjellige typer feil som kan oppstå under filbehandling, inkluderer file not found error
    print("Feil under lesing av fil")
except ValueError:
    print("Feil format")

#  finally: Ønsker å lukke fil uanset hva som skjer, derfor finally: på slutten etter try - except blokk...
finally:
    if filreferanse:
        filreferanse.close()
