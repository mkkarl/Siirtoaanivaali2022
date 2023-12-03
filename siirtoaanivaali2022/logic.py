import opavote
from vaali import Vaali
from datetime import datetime
import locale

print("Hello world")

# luo vaali

vaali = Vaali()

# lue tiedosto ja luo lipukkeet. anna ehdokas- ja lipukelistat opavoten käyttöön
tiedosto = "testivaali.txt"

opavote.luo_lipukkeet(tiedosto, vaali)
# vaali.alusta_aanikynnys()
# print(f"äänikynnys: {vaali.hae_aanikynnys()}")

pudotettavien_lkm = vaali.hae_ehdokkaat().hae_ehdokkaiden_lkm() - vaali.hae_valittavien_lkm()

# luo tiedostot laskennan ja tulosten tallentamiseen

loc = locale.setlocale(locale.LC_ALL, 'fi_FI.UTF-8')

aika = datetime.now()
tulokset = f"vaalit/{vaali.hae_vaalin_nimi().replace(' ', '_')}_{aika.strftime('%Y%m%d%_H%M%S')}_tulokset.txt"
laskenta = f"vaalit/{vaali.hae_vaalin_nimi().replace(' ', '_')}_{aika.strftime('%Y%m%d%_H%M%S')}_laskenta.txt"

mjono = vaali.hae_vaalin_nimi() + "\n"
mjono += aika.strftime("%x %X") + "\n"
mjono += f"Ehdokkaita: {vaali.hae_ehdokkaat().hae_ehdokkaiden_lkm()}\tValitaan: {vaali.hae_valittavien_lkm()}\n\n"
mjono += str(vaali.hae_ehdokkaat()) + "\n\n"

with open(tulokset, "w") as tiedosto:
    tiedosto.write(mjono)

with open(laskenta, "w") as tiedosto:
    tiedosto.write(mjono)
    tiedosto.write(f"Pudotettavien ehdokkaiden lkm: {pudotettavien_lkm}\n\n")


# laskentakierros, toista kunnes valittuja tarpeeksi

kierros = 1

while pudotettavien_lkm > 0:

    valitut_kierroksen_alussa = vaali.hae_valittujen_lkm()

    with open(laskenta, "a") as tiedosto:
        mjono = f"Kierros {kierros}"
        tiedosto.write(f"\n{mjono}\n")
        tiedosto.write("=" * len(mjono) + "\n\n")
        tiedosto.write(f"Valittujen lkm kierroksen alussa: {valitut_kierroksen_alussa}\n\n")

    #   1. Ehdokas:Ehdokkaat laske äänet

    # jaa ääni lipukkeella ehdokkaille ennen äänien hakemista

    vaali.jaa_aanet_lipukkeilla()

    vaali.laske_aanet()

    with open(laskenta, "a") as tiedosto:
        tiedosto.write(str(vaali.hae_ehdokkaat()) + "\n\n")

    #   2. Lipukkeet äänihukka

    vaali.paivita_aanihukka()

    with open(laskenta, "a") as tiedosto:
        tiedosto.write(f"äänihukka: {vaali.hae_aanihukka()}\n")

    #   3. Äänikynnys update

    vaali.paivita_aanikynnys()
    
    with open(laskenta, "a") as tiedosto:
        tiedosto.write(f"äänikynnys: {vaali.hae_aanikynnys()}\n\n")

    #   Ehdokkaiden valinta

    kierroksella_valitut = vaali.valitse_ehdokkaat()

    with open(laskenta, "a") as tiedosto:
        tiedosto.write(str(vaali.hae_ehdokkaat()) + "\n\n")

        if len(kierroksella_valitut) > 0:
            tiedosto.write("Kierroksella valitut ehdokkaat:\n")
            for valittu in kierroksella_valitut:
                tiedosto.write(valittu + "\n")
            tiedosto.write("\n")
        else:
            tiedosto.write("Kierroksella ei valittu ehdokkaita.\n\n")

    #   Ehdokkaiden pudotus

    if valitut_kierroksen_alussa - vaali.hae_valittujen_lkm() == 0:
        pudotettava = vaali.pudota_ehdokas()
        pudotettavien_lkm -= 1
        with open(laskenta, "a") as tiedosto:
            tiedosto.write(f"Pudotetaan ehdokas: {pudotettava}\n\n")
            tiedosto.write(f"Pudotettavien ehdokkaiden lkm: {pudotettavien_lkm}\n\n")
            #tiedosto.write(str(vaali.hae_ehdokkaat()) + "\n")

    #   4. Ehdokas:Ehdokkaat ehdokas.updateP

    vaali.paivita_p_arvot()

    with open(laskenta, "a") as tiedosto:
        tiedosto.write("Päivitetään p-arvot\n\n")
        tiedosto.write(str(vaali.hae_ehdokkaat()) + "\n\n")

    with open(laskenta, "a") as tiedosto:
        tiedosto.write(f"Valittujen lkm: {vaali.hae_valittujen_lkm()}\n\n")

    with open(laskenta, "a") as tiedosto:
        tiedosto.write("Ehdokkaat kierroksen lopussa\n\n")
        tiedosto.write(str(vaali.hae_ehdokkaat()) + "\n\n")

    kierros += 1

if vaali.hae_valittujen_lkm() < vaali.hae_valittavien_lkm():
    valitut = vaali.valitse_loput_toiveikkaat()

    with open(laskenta, "a") as tiedosto:
        mjono = "Valitaan loput toiveikkaat ehdokkaat"
        tiedosto.write(f"\n{mjono}\n")
        tiedosto.write("=" * len(mjono) + "\n\n")

        for valittu in valitut:
            tiedosto.write(valittu + "\n")

with open(laskenta, "a") as tiedosto:
    mjono = "VAALIN TULOS"
    tiedosto.write(f"\n{mjono}\n")
    tiedosto.write("=" * len(mjono) + "\n\n")

    tiedosto.write("Valitut ehdokkaat:\n\n")
    valitut = vaali.hae_ehdokkaat().hae_valitut()
    for valittu in valitut:
        tiedosto.write(valittu + "\n")





