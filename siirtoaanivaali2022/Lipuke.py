import siirtoaanivaali2022.Ehdokas as Ehdokas
import siirtoaanivaali2022.Lipukerivi as Lipukerivi

class Lipuke:

    def __init__(self, aanet :list):
        # ehdokas pitää saada haettua ehdokaslistasta
        self.rivit = Lipukerivi(aanet[0], None, 1)

        for n in range(1,len(aanet)):
            self.rivit.append(Lipukerivi(aanet[n], self.rivit[n - 1], 0))
        
        
        
