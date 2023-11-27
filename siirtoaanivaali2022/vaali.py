from Ehdokkaat import Ehdokkaat
from lipukkeet import Lipukkeet

class Vaali:

    def __init__(self) -> None:
        self.__nimi = ""
        self.__ehdokkaat = Ehdokkaat()
        self.__lipukkeet = Lipukkeet()
        self.__valittavien_lkm = 0

    def aseta_vaalin_nimi(self, nimi :str):
        self.__nimi = nimi

    def aseta_ehdokkaat(self, ehdokkaat : Ehdokkaat):
        self.__ehdokkaat = ehdokkaat

    def hae_ehdokkaat(self):
        return self.__ehdokkaat

    def aseta_lipukkeet(self, lipukkeet : Lipukkeet):
        self.__lipukkeet = lipukkeet

    def hae_lipukkeet(self):
        return self.__lipukkeet

    def aseta_valittavien_lkm(self, valittavien_lkm : int):
        self.__valittavien_lkm = valittavien_lkm

    def hae_valittavien_lkm(self):
        return self.__valittavien_lkm