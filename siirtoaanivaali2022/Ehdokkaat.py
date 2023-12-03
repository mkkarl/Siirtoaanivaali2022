from Ehdokas import Ehdokas

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
        #valittujen_lkm = 0
        kierroksella_valitut = []
        for nro in self.__ehdokkaat:
            ehdokas = self.__ehdokkaat[nro]
            if ehdokas.hae_status() == "toiveikas" and ehdokas.hae_kokonaisaanimaara() > aanikynnys:
                ehdokas.valitse()
                kierroksella_valitut.append(ehdokas.hae_nimi())
                self.__valitut.append(ehdokas.hae_nimi())
                #valittujen_lkm += 1

        #return valittujen_lkm
        return kierroksella_valitut
    
    def pudota_ehdokas(self, maksimi):
        minimi = maksimi
        pudotettava = None
        for nro in self.__ehdokkaat:
            ehdokas = self.__ehdokkaat[nro]
            aanimaara = ehdokas.hae_kokonaisaanimaara()
            # TODO: tasatilanne
            if ehdokas.hae_status() == "toiveikas" and aanimaara < minimi:
                minimi = aanimaara
                pudotettava = ehdokas

        return pudotettava.pudota()
    
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