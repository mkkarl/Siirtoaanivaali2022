import opavote
from vaali import Vaali

print("Hello world")

# luo vaali

vaali = Vaali()

# lue tiedosto ja luo lipukkeet. anna ehdokas- ja lipukelistat opavoten käyttöön
tiedosto = "testivaali.txt"

opavote.luo_lipukkeet(tiedosto, vaali)
vaali.alusta_aanikynnys()
print(f"äänikynnys: {vaali.hae_aanikynnys()}")

# laskentakierros, toista kunnes valittuja tarpeeksi

kierros = 1

while kierros < 6:

    valitut_kierroksen_alussa = vaali.hae_valittujen_lkm()

    print(f"\nKierros {kierros}\n")

    #   1. Ehdokas:Ehdokkaat laske äänet

    # jaa ääni lipukkeella ehdokkaille ennen äänien hakemista

    vaali.jaa_aanet_lipukkeilla()

    vaali.laske_aanet()

    print(str(vaali.hae_ehdokkaat()))

    #   2. Lipukkeet äänihukka

    vaali.paivita_aanihukka()
    print(f"äänihukka: {vaali.hae_aanihukka()}")

    #   3. Äänikynnys update

    vaali.paivita_aanikynnys()
    print(f"äänikynnys: {vaali.hae_aanikynnys()}")

    vaali.valitse_ehdokkaat()
    print(str(vaali.hae_ehdokkaat()))

    #   4. Ehdokas:Ehdokkaat ehdokas.updateP

    vaali.paivita_p_arvot()
    print(str(vaali.hae_ehdokkaat()))

    print(f"Valittujen lkm: {vaali.hae_valittujen_lkm()}")

    print(str(valitut_kierroksen_alussa))

    if valitut_kierroksen_alussa - vaali.hae_valittujen_lkm() == 0:
        vaali.pudota_ehdokas()
        print("Ehdokkaat pudotuksen jälkeen")
        print(str(vaali.hae_ehdokkaat()))


    kierros += 1

# vaali.hae_ehdokkaat().paivita_p(vaali.hae_aanikynnys())

#   Ehdokkaat valitse äänikynnyksen ylittäneet tai pudota vähiten ääniä saanut
#       jos tasapeli, toista laskentakierrosta poikkeavilla säännöillä (tee laskentakierroksesta oma funktio ja kutsu sitä rekursiivisesti)

