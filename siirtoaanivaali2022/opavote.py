from Ehdokkaat import Ehdokkaat
from lipukkeet import Lipukkeet
from Lipuke import Lipuke


def opavoteTest():
    return "OpaVote says hello!"

def luo_lipukkeet(tiedosto: str, ehdokkaat : Ehdokkaat, lipukkeet : Lipukkeet):
    with open(tiedosto) as tiedosto:
        tila = "ekarivi"
        laskuri = 1
        for rivi in tiedosto:
            rivi = rivi.strip()
            if tila == "ekarivi":
                osat = rivi.split(" ")
                ehdokas_lkm = int(osat[0])
                # lisää ehdokkaat listaan
                ehdokkaat.lisaa_ehdokkaat(ehdokas_lkm)
                valittavat_lkm = int(osat[1])
                tila = "lipukkeet"
            elif tila == "lipukkeet":
                osat = rivi.split(" ")
                if osat[0] == '0':
                    tila = "ehdokkaat"
                else:
                    print(osat[1:-1])
                    # tee numerolistan pohjalta ehdokaslista
                    ehdokaslista = []
                    for ehdokas_nro in osat[1:-1]:
                        ehdokaslista.append(ehdokkaat.hae_ehdokas(int(ehdokas_nro)))
                    # TODO: luo lipuke listaan
                    # TODO: luo lipukerivit lipukkeelle
                    lipukelista.lisaa_lipuke(Lipuke(ehdokaslista))

                    # lipuketta luodessa anna paremetrina ehdokkaat järjestyksessä
            elif tila == "ehdokkaat":
                if laskuri <= ehdokas_lkm:
                    print(f"{laskuri} {rivi}")
                    # TODO: lisää ehdokkaalle nimi
                    laskuri = laskuri + 1
                else:
                    print("Vaalin nimi: " + rivi.strip('"'))
                    # TODO: tallenna vaalin nimi sopivaan paikkaan

if __name__ == "__main__":
    ehdokaslista = Ehdokkaat()
    lipukelista = Lipukkeet()
    luo_lipukkeet("testivaali.txt", ehdokaslista, lipukelista)
    print(ehdokaslista)
    print(lipukelista)