import siirtoaanivaali2022.Ehdokas as Ehdokas

class Lipukerivi:

    def __init__(self, ehdokas: Ehdokas, edellinen_ehdokas : Ehdokas, aanimaara : float):
        self.ehdokas = ehdokas
        self.edellinen_ehdokas = edellinen_ehdokas
        self.aanimaara = aanimaara