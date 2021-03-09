# du kan oppgi default verdi, tegn="*"
# da skal den skrive default verdi, hvis ikke oppgitt noe annet senere
# !HUSK: den som har default/standard verdi må alltid komme etter den
#        som ikke har standard verdi i rekkefølge!!!
# def skriv_tegnfirkant(bredde=3, hoyde, tegn="*")  ---> ikke bra, Python blir forviret
# def skriv_tegnfirkant(hoyde, bredde=3, tegn="*")  ---> OK


def lag_firkant_av_tegn(bredde, hoyde, tegn="*"):
    for linje in range(hoyde):
        for tall in range(bredde):
            print(tegn, end="")
        print()

def funksjon_uten_parametre():
    print("Test")


if __name__ == "__main__":
    lag_firkant_av_tegn(6, 4)
    print()
    lag_firkant_av_tegn(5, 6, "#")
    print()
    lag_firkant_av_tegn(3, 2, "%")
    print()
    lag_firkant_av_tegn(8, 7, ".")
    print()
    lag_firkant_av_tegn(tegn="%", bredde=3, hoyde=2)
    print()
    lag_firkant_av_tegn(hoyde=5, bredde=3)

    # Kall til funksjoner uten parametre må fortsatt ha parenteser etter.
    # Dette skiller funksjoner fra variabler
    funksjon_uten_parametre()
