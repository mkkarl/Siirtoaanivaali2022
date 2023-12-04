from Ehdokkaat import Ehdokkaat
from lipukkeet import Lipukkeet
from Lipuke import Lipuke
from vaali import Vaali


def opavoteTest():
    return "OpaVote says hello!"

def luo_lipukkeet(tiedosto: str, vaali : Vaali):
    with open(tiedosto) as tiedosto:
        tila = "ekarivi"
        laskuri = 1
        for rivi in tiedosto:
            rivi = rivi.strip()
            if tila == "ekarivi":
                osat = rivi.split(" ")
                ehdokas_lkm = int(osat[0])
                # lisää ehdokkaat listaan
                vaali.hae_ehdokkaat().lisaa_ehdokkaat(ehdokas_lkm)
                vaali.aseta_valittavien_lkm(int(osat[1]))
                tila = "lipukkeet"
            elif tila == "lipukkeet":
                osat = rivi.split(" ")
                if osat[0] == '0':
                    tila = "ehdokkaat"
                else:
                    # tee numerolistan pohjalta ehdokaslista
                    ehdokaslista = []
                    for ehdokas_nro in osat[1:-1]:
                        ehdokaslista.append(vaali.hae_ehdokkaat().hae_ehdokas(int(ehdokas_nro)))
                    # luo lipuke listaan
                    # luo lipukerivit lipukkeelle
                    vaali.hae_lipukkeet().lisaa_lipuke(Lipuke(ehdokaslista))
            elif tila == "ehdokkaat":
                if laskuri <= ehdokas_lkm:
                    # lisää ehdokkaalle nimi
                    vaali.hae_ehdokkaat().hae_ehdokas(laskuri).set_nimi(rivi.strip('"'))
                    laskuri = laskuri + 1
                else:
                    # tallenna vaalin nimi sopivaan paikkaan
                    vaali.aseta_vaalin_nimi(rivi.strip('"'))
                    return

if __name__ == "__main__":
    vaali = Vaali()
    luo_lipukkeet("testivaali.txt", vaali)
    print(vaali.hae_ehdokkaat())
    print(vaali.hae_lipukkeet())