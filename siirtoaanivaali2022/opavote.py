from Ehdokkaat import Ehdokkaat
from lipukkeet import Lipukkeet


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
                    # TODO: tee numerolistan pohjalta ehdokaslista
                    # TODO: luo lipuke listaan
                    # TODO: luo lipukerivit lipukkeelle
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
    luo_lipukkeet("testivaali.txt", ehdokaslista)