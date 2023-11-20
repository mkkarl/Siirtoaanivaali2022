from Ehdokas import Ehdokas

class Ehdokkaat:

    def __init__(self) -> None:
        self.ehdokkaat = {}

    def lisaa_ehdokkaat(self, ehdokkaat_lkm : int):
        for n in range(ehdokkaat_lkm):
            self.ehdokkaat[n+1] = Ehdokas(n+1)
    