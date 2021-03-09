# as plt: for å gi matplotlib.pyplot litt kortere navn - plt
import matplotlib.pyplot as plt
import numpy



# List comprehension: liste av alle elementene fra og med 0, til men ikke med 20
x_koordinater = [x for x in range(0, 20)]

# List comprehension: For hvert element i x-koordinater, regn ut x**2 og sett
# inn i den nye lista.
y_koordinater = [x**2 for x in x_koordinater]

plt.plot(x_koordinater, y_koordinater, label="x**2")
plt.title("Tester plotting")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)   # for å lage grid (mrezo), moras imeti True

# for å plote enkelte punkter istedenfor linje, dodas zraven "o". punkter blir små sirkler
# istedenfor o kan man bruke andre bokstaver for å få andre typer punkter
plt.plot(x_koordinater, y_koordinater, "o")

# for å tegne flere dataset i samme plot
y_koordinater_2 = [5*x for x in x_koordinater]      # ny y koordinater i liste
plt.plot(x_koordinater, y_koordinater_2, label="5*x")       # x-koordinate rblir samme
plt.plot(x_koordinater, y_koordinater_2, "v")
plt.legend()  # for å få label i legend
plt.show()  # for å få se plot
