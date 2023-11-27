from Ehdokkaat import Ehdokkaat
from lipukkeet import Lipukkeet

class Vaali:

    def __init__(self) -> None:
        self.__nimi = ""
        self.__ehdokkaat = Ehdokkaat()
        self.__lipukkeet = Lipukkeet()
        self.__valittavien_lkm = 0
        self.__valittujen_lkm = 0
        self.__aanihukka = 0
        self.__aanikynnys = 0

    # muuttujien käsittely

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
    
    def hae_aanihukka(self):
        return self.__aanihukka
    
    def alusta_aanikynnys(self):
        self.__aanikynnys = self.__lipukkeet.hyvaksytyt_aanet_lkm() + 1

    def hae_aanikynnys(self):
        return self.__aanikynnys
    
    # metodit
    
    def jaa_aanet_lipukkeilla(self):
        self.__lipukkeet.jaa_aanet()

    def laske_aanet(self):
        aanet = self.__lipukkeet.hae_aanet()

        for ehdokas in aanet:
            nro = ehdokas.hae_nro()
            self.__ehdokkaat.hae_ehdokas(nro).aseta_kokonaisaanimaara(aanet[ehdokas])

    def tulosta_ehdokkaat(self):
        return str(self.__ehdokkaat)
    
    def paivita_aanihukka(self):
        self.__lipukkeet.aanihukka()

    def paivita_aanikynnys(self):
        self.__aanikynnys = (self.__lipukkeet.hyvaksytyt_aanet_lkm() - self.__aanihukka) / self.__valittavien_lkm

    def paivita_p_arvot(self):
        self.__ehdokkaat.paivita_p(self.__aanikynnys)

    def valitse_ehdokkaat(self):
        self.__ehdokkaat.valitse_ehdokkaat(self.__aanikynnys)
