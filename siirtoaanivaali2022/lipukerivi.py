import ehdokas

class Lipukerivi:

    def __init__(self, ehdokas: ehdokas, edellinen_ehdokas : ehdokas, aanimaara : float):
        self.ehdokas = ehdokas
        self.edellinen_ehdokas = edellinen_ehdokas
        self.aanimaara = aanimaara