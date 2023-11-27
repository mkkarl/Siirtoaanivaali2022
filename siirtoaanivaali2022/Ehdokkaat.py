from Ehdokas import Ehdokas

class Ehdokkaat:

    def __init__(self) -> None:
        self.ehdokkaat = {}

    def lisaa_ehdokkaat(self, ehdokkaat_lkm : int):
        for n in range(ehdokkaat_lkm):
            self.ehdokkaat[n+1] = Ehdokas(n+1)

    def hae_ehdokas(self, ehdokas_nro : int):
        return self.ehdokkaat[ehdokas_nro]
    
    def paivita_p(self, aanikynnys):
        for ehdokas in self.ehdokkaat:
            ehdokas.paivita_p(aanikynnys)
    
    def __str__(self) -> str:
        mjono = ""
        for ehdokas in self.ehdokkaat:
            mjono += str(self.ehdokkaat[ehdokas]) + "\n"
        return mjono.strip()
    

if __name__ == "__main__":
    ehdokaslista = Ehdokkaat()
    ehdokaslista.lisaa_ehdokkaat(2)
    print(ehdokaslista)
    print(ehdokaslista.hae_ehdokas(1))