from Ehdokas import Ehdokas
from datetime import datetime
import random

class Ehdokkaat:

    def __init__(self) -> None:
        self.__ehdokkaat = {}
        self.__valitut = []

    def lisaa_ehdokkaat(self, ehdokkaat_lkm : int):
        for n in range(ehdokkaat_lkm):
            self.__ehdokkaat[n+1] = Ehdokas(n+1)

    def hae_ehdokas(self, ehdokas_nro : int):
        return self.__ehdokkaat[ehdokas_nro]
    
    def hae_ehdokkaiden_lkm(self):
        return len(self.__ehdokkaat)
    
    def hae_valitut(self):
        return self.__valitut
    
    def hae_valittujen_lkm(self):
        return len(self.__valitut)
    
    def paivita_p(self, aanikynnys):
        for ehdokas in self.__ehdokkaat:
            self.__ehdokkaat[ehdokas].paivita_p(aanikynnys)

    def valitse_ehdokkaat(self, aanikynnys):
        kierroksella_valitut = []
        for nro in self.__ehdokkaat:
            ehdokas = self.__ehdokkaat[nro]
            if ehdokas.hae_status() == "toiveikas" and ehdokas.hae_kokonaisaanimaara() > aanikynnys:
                ehdokas.valitse()
                kierroksella_valitut.append(ehdokas.hae_nimi())
                self.__valitut.append(ehdokas.hae_nimi())

        return kierroksella_valitut
    
    def pudota_ehdokas(self, maksimi, vanhat_vertailtavat=[]):
        minimi = maksimi
        pudotettava = None
        vertailtavat = []
        for nro in self.__ehdokkaat:
            ehdokas = self.__ehdokkaat[nro]
            aanimaara = ehdokas.hae_kokonaisaanimaara()
            # TODO: tasatilanne
            if ehdokas.hae_status() == "toiveikas" and aanimaara < minimi:
                minimi = aanimaara
                pudotettava = ehdokas
                vertailtavat = []
                vertailtavat.append(ehdokas.hae_nro())
            elif ehdokas.hae_status() == "toiveikas" and aanimaara == minimi:
                vertailtavat.append(ehdokas.hae_nro())

        if len(vertailtavat) == 1:
            # pudotettava.pudota()
            return (True, pudotettava.pudota())
        elif len(vanhat_vertailtavat) == len(vertailtavat): #todellinen tasapeli
            time = datetime.now()
            seed = int(time.strftime("%f")) % 256
            random.seed(seed)
            valittava = random.randint(0, len(vertailtavat)) - 1
            pudotettava = self.__ehdokkaat[vertailtavat[valittava]]
            return (True, pudotettava.pudota(), seed)
        else:
            return (False, vertailtavat)

    def pudota_ylimaaraiset_ehdokkaat(self, vertailtavat):
        for nro in self.__ehdokkaat:
            ehdokas = self.__ehdokkaat[nro]
            if ehdokas.hae_nro() not in vertailtavat:
                ehdokas.pudota()
    
    def valitse_loput_toiveikkaat(self):
        kierroksella_valitut = []
        for nro in self.__ehdokkaat:
            ehdokas = self.__ehdokkaat[nro]
            if ehdokas.hae_status() == "toiveikas":
                ehdokas.valitse()
                kierroksella_valitut.append(ehdokas.hae_nimi())
                self.__valitut.append(ehdokas.hae_nimi())

        return kierroksella_valitut
    
    def paatetaan_kierros(self, aanikynnys):
        for nro in self.__ehdokkaat:
            ehdokas = self.__ehdokkaat[nro]
            if not ehdokas.suhdeluku_oikea(aanikynnys):
                return False
        
        return True
    
    def hae_toiveikas(self):
        for nro in self.__ehdokkaat:
            ehdokas = self.__ehdokkaat[nro]
            if ehdokas.hae_status() == "toiveikas":
                return ehdokas.hae_nro()
    
    def __str__(self) -> str:
        mjono = "Ehdokkaat\n"
        for ehdokas in self.__ehdokkaat:
            mjono += str(self.__ehdokkaat[ehdokas]) + "\n"
        return mjono.strip()
    

if __name__ == "__main__":
    ehdokaslista = Ehdokkaat()
    ehdokaslista.lisaa_ehdokkaat(2)
    print(ehdokaslista)
    print(ehdokaslista.hae_ehdokas(1))