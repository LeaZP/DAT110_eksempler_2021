# Navnekonvensjon:
#   - mellom metoder: en tom linje
#   - etter en class definisjon og mellom funksjoner og: to tome linjer

import math

class Punkt:
    # Konstruktør: en metode som lager objekter
    def __init__(self, start_x=0, start_y=0):           # dette heter konstruktør, kan ta inn parametre, også med default verdi
        self.x_koordinat = start_x                      # instans variabler
        self.y_koordinat = start_y

    def flytt(self, delta_x, delta_y):                  # Metode som flytter et punkt; self skal alltid være med
        self.x_koordinat += delta_x                     # += økes med
        self.y_koordinat += delta_y

    @property
    def x_koordinat(self):
        return self.__x_koordinat

    @x_koordinat.setter
    def x_koordinat(self, ny_x):
        if ny_x >= 0:
            self.__x_koordinat = ny_x
        else:
            raise ValueError("X-koordinatet i denne applikasjonen kan ikke være negativt")  # En måte å gjøre exception

    @property
    def r(self):
        return math.sqrt(self.x_koordinat**2 + self.y_koordinat**2)  # sqrt: square root; standard euklidisk distanse

    @property
    def theta(self):
        return math.acos(self.x_koordinat/self.r)                    # arccos, cos-1 : acos

    def __str__(self):                                         # skal returnere en streng representasjon av objektet
       return f"Punkt: ({self.x_koordinat}, {self.y_koordinat})"

if __name__ == "__main__":
    p1 = Punkt()
