import opavote
from vaali import Vaali

print("Hello world")

# luo vaali

vaali = Vaali()

# lue tiedosto ja luo lipukkeet. anna ehdokas- ja lipukelistat opavoten käyttöön
tiedosto = "testivaali.txt"

opavote.luo_lipukkeet(tiedosto, vaali)

# laskentakierros, toista kunnes valittuja tarpeeksi

#   1. Ehdokas:Ehdokkaat laske äänet

aanet = vaali.hae_lipukkeet().hae_aanet()

for ehdokas in aanet:
    print(f"{ehdokas.hae_nro()} {ehdokas.hae_nimi()}\t{aanet[ehdokas]}")

#   2. Lipukkeet äänihukka

aanihukka = vaali.hae_lipukkeet().aanihukka()

print(f"äänihukka: {aanihukka}")

#   3. Äänikynnys update

#   4. Ehdokas:Ehdokkaat ehdokas.updateP

#   Ehdokkaat valitse äänikynnyksen ylittäneet tai pudota vähiten ääniä saanut
#       jos tasapeli, toista laskentakierrosta poikkeavilla säännöillä (tee laskentakierroksesta oma funktio ja kutsu sitä rekursiivisesti)

