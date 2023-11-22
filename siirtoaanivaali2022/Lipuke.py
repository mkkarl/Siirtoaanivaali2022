from Ehdokas import Ehdokas
from Lipukerivi import Lipukerivi

class Lipuke:

    def __init__(self, aanet :list):
        # ehdokas pitää saada haettua ehdokaslistasta
        self.rivit = []
        self.rivit.append(Lipukerivi(aanet[0], None, 1))

        for n in range(1,len(aanet)):
            self.rivit.append(Lipukerivi(aanet[n], self.rivit[n - 1], 0))

    def __str__(self) -> str:
        mjono = ""
        for rivi in self.rivit:
            mjono += str(rivi) + "\n"

        return mjono.strip()
    

if __name__ == "__main__":
    ehdokaslista = [Ehdokas(1), Ehdokas(2)]
    lipuke = Lipuke(ehdokaslista)
    print(lipuke)