from Ehdokas import Ehdokas
from Lipukerivi import Lipukerivi

class Lipuke:

    def __init__(self, aanet :list):
        # ehdokas pitää saada haettua ehdokaslistasta
        self.__rivit = []
        self.__rivit.append(Lipukerivi(aanet[0], None, 1))

        for n in range(1,len(aanet)):
            self.__rivit.append(Lipukerivi(aanet[n], self.__rivit[n - 1], 0))

    def hae_aanet(self):
        aanet = []
        for rivi in self.__rivit:
            aanet.append((rivi.hae_ehdokas(), rivi.hae_aanimaara()))
        
        return aanet
    
    def aanihukka(self):
        aanien_summa = 0
        for rivi in self.__rivit:
            aanien_summa += rivi.hae_aanimaara()

        return (1 - aanien_summa)

    def __str__(self) -> str:
        mjono = ""
        for rivi in self.__rivit:
            mjono += str(rivi) + "\n"

        return mjono.strip()
    

if __name__ == "__main__":
    ehdokaslista = [Ehdokas(1), Ehdokas(2)]
    lipuke = Lipuke(ehdokaslista)
    print(lipuke)