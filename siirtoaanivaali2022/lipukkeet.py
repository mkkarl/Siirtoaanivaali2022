from Lipuke import Lipuke
from Ehdokas import Ehdokas

class Lipukkeet:

    def __init__(self) -> None:
        self.lipukkeet = []

    def lisaa_lipuke(self, lipuke : Lipuke):
        self.lipukkeet.append(lipuke)

    def hae_aanet(self):
        aanet = {}
        for lipuke in self.lipukkeet:
            lipukkeen_aanet = lipuke.hae_aanet()
            for aani in lipukkeen_aanet:
                if aani[0] not in aanet:
                    aanet[aani[0]] = 0
                aanet[aani[0]] += aani[1]

        return aanet
    
    def aanihukka(self):
        aanihukka = 0
        for lipuke in self.lipukkeet:
            aanihukka += lipuke.aanihukka()

        return aanihukka
    
    def hyvaksytyt_aanet_lkm(self):
        # TODO: hyväksyttyjen äänien validointi
        return len(self.lipukkeet)
    
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