from Lipuke import Lipuke
from Ehdokas import Ehdokas

class Lipukkeet:

    def __init__(self) -> None:
        self.lipukkeet = []

    def lisaa_lipuke(self, lipuke : Lipuke):
        self.lipukkeet.append(lipuke)

    def __str__(self) -> str:
        mjono = ""
        n = 1

        for lipuke in self.lipukkeet:
            mjono += f"Lipuke # {n}\n"
            mjono += str(lipuke) + "\n"
            n += 1
        
        return mjono.strip()
    
if __name__ == "__main__":
    lipukelista = Lipukkeet()
    ehdokas1 = Ehdokas(1)
    ehdokas2 = Ehdokas(2)
    lipukelista.lisaa_lipuke(Lipuke([ehdokas1, ehdokas2]))
    lipukelista.lisaa_lipuke(Lipuke([ehdokas2, ehdokas1]))
    print(lipukelista)