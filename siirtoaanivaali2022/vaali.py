from Ehdokkaat import Ehdokkaat
from lipukkeet import Lipukkeet

class Vaali:

    def __init__(self) -> None:
        self.nimi = ""
        self.ehdokkaat = Ehdokkaat()
        self.lipukkeet = Lipukkeet()
        self.valittavien_lkm = 0

    def aseta_vaalin_nimi(self, nimi :str):
        self.nimi = nimi

    def aseta_ehdokkaat(self, ehdokkaat : Ehdokkaat):
        self.ehdokkaat = ehdokkaat

    def hae_ehdokkaat(self):
        return self.ehdokkaat

    def aseta_lipukkeet(self, lipukkeet : Lipukkeet):
        self.lipukkeet = lipukkeet

    def hae_lipukkeet(self):
        return self.lipukkeet

    def aseta_valittavien_lkm(self, valittavien_lkm : int):
        self.valittavien_lkm = valittavien_lkm

    def hae_valittavien_lkm(self):
        return self.valittavien_lkm