from Ehdokkaat import Ehdokkaat
from lipukkeet import Lipukkeet
import math

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

    def hae_vaalin_nimi(self):
        return self.__nimi

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
    
    def hae_valittujen_lkm(self):
        #return self.__valittujen_lkm
        return self.__ehdokkaat.hae_valittujen_lkm()
    
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
            self.__ehdokkaat.hae_ehdokas(nro).aseta_kokonaisaanimaara(round(aanet[ehdokas], 5))

    def tulosta_ehdokkaat(self):
        return str(self.__ehdokkaat)
    
    def paivita_aanihukka(self):
        self.__aanihukka = round(self.__lipukkeet.aanihukka(), 5)

    def paivita_aanikynnys(self):
        aanikynnys = (self.__lipukkeet.hyvaksytyt_aanet_lkm() - self.__aanihukka) / self.__valittavien_lkm
        aanikynnys *= 100000
        aanikynnys = math.ceil(aanikynnys)
        aanikynnys /= 100000
        self.__aanikynnys = aanikynnys

    def paivita_p_arvot(self):
        self.__ehdokkaat.paivita_p(self.__aanikynnys)

    def valitse_ehdokkaat(self):
        #self.__valittujen_lkm += self.__ehdokkaat.valitse_ehdokkaat(self.__aanikynnys)
        return self.__ehdokkaat.valitse_ehdokkaat(self.__aanikynnys)

    def pudota_ehdokas(self):
        return self.__ehdokkaat.pudota_ehdokas(self.__lipukkeet.hyvaksytyt_aanet_lkm() + 1)

