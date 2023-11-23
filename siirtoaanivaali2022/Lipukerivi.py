from Ehdokas import Ehdokas
import Lipukerivi

class Lipukerivi:

    def __init__(self, ehdokas: Ehdokas, edellinen_rivi : Lipukerivi, aanimaara : float):
        self.ehdokas = ehdokas
        self.edellinen_rivi = edellinen_rivi
        self.aanimaara = aanimaara

    def hae_ehdokas(self):
        return self.ehdokas

    def hae_aanimaara(self):
        return self.aanimaara

    def __str__(self) -> str:
        return f"{str(self.ehdokas)}, äänimäärä: {self.aanimaara}"
    

if __name__ == "__main__":
    rivi1 = Lipukerivi(Ehdokas(1),None, 1)
    print(rivi1)
    rivi2 = Lipukerivi(Ehdokas(2),rivi1, 1)
    print(rivi2)