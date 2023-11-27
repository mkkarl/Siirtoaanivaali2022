from Ehdokas import Ehdokas
import Lipukerivi

class Lipukerivi:

    def __init__(self, ehdokas: Ehdokas, edellinen_rivi : Lipukerivi, aanimaara : float):
        self.__ehdokas = ehdokas
        self.__edellinen_rivi = edellinen_rivi
        self.__aanimaara = aanimaara

    def hae_ehdokas(self):
        return self.__ehdokas

    def hae_aanimaara(self):
        return self.__aanimaara

    def __str__(self) -> str:
        return f"{str(self.__ehdokas)}, äänimäärä: {self.__aanimaara}"
    

if __name__ == "__main__":
    rivi1 = Lipukerivi(Ehdokas(1),None, 1)
    print(rivi1)
    rivi2 = Lipukerivi(Ehdokas(2),rivi1, 1)
    print(rivi2)