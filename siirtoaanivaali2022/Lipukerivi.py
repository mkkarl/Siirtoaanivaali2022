import siirtoaanivaali2022.Ehdokas as Ehdokas
import Lipukerivi

class Lipukerivi:

    def __init__(self, ehdokas: Ehdokas, edellinen_rivi : Lipukerivi, aanimaara : float):
        self.ehdokas = ehdokas
        self.edellinen_rivi = edellinen_rivi
        self.aanimaara = aanimaara