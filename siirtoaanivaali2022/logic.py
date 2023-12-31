import opavote
from vaali import Vaali
from datetime import datetime
import locale

class Aantenlasku:

    def __init__(self) -> None:
        self.__vaali = Vaali()

    def suorita_vaali(self, lipukedata : str, pudotusvaali=False, vertailtavat=[]):

        # luo vaali

        # self.__vaali = Vaali()

        # lue tiedosto ja luo lipukkeet. anna ehdokas- ja lipukelistat opavoten käyttöön
        # tiedosto = "testivaali.txt"

        opavote.luo_lipukkeet(lipukedata, self.__vaali)

        # NÄITÄ EI TARVITA, jos ehdokkaiden valinta tapahtuu kohtien 1 ja 4 välissä
        # vaali.alusta_aanikynnys()
        # print(f"äänikynnys: {vaali.hae_aanikynnys()}")

        if pudotusvaali:
            self.__vaali.aseta_valittavien_lkm(len(vertailtavat) - 1)
            self.__vaali.hae_ehdokkaat().pudota_ylimaaraiset_ehdokkaat(vertailtavat)

            


        pudotettavien_lkm = self.__vaali.hae_ehdokkaat().hae_ehdokkaiden_lkm() - self.__vaali.hae_valittavien_lkm()

        # luo tiedostot laskennan ja tulosten tallentamiseen

        loc = locale.setlocale(locale.LC_ALL, 'fi_FI.UTF-8')

        aika = datetime.now()
        tulokset = f"vaalit/{self.__vaali.hae_vaalin_nimi().replace(' ', '_')}_{aika.strftime('%Y%m%d-%H%M%S-%f')}_tulokset.txt"
        laskenta = f"vaalit/{self.__vaali.hae_vaalin_nimi().replace(' ', '_')}_{aika.strftime('%Y%m%d-%H%M%S-%f')}_laskenta.txt"

        mjono = self.__vaali.hae_vaalin_nimi() + "\n"
        mjono += aika.strftime("%x %X") + "\n"
        mjono += f"Ehdokkaita: {self.__vaali.hae_ehdokkaat().hae_ehdokkaiden_lkm()}\tValitaan: {self.__vaali.hae_valittavien_lkm()}\n"
        mjono += f"Hyväksyttyjä ääniä: {self.__vaali.hae_lipukkeet().hyvaksytyt_aanet_lkm()}\tHylättyjä ääniä: {self.__vaali.hae_hylatyt_aanet()}\tÄäniä yhteensä: {self.__vaali.hae_lipukkeet().hyvaksytyt_aanet_lkm() + self.__vaali.hae_hylatyt_aanet()}\n\n"
        mjono += str(self.__vaali.hae_ehdokkaat()) + "\n\n"

        print(mjono)

        with open(tulokset, "w") as tiedosto:
            tiedosto.write(mjono)

        with open(laskenta, "w") as tiedosto:
            tiedosto.write(mjono)
            tiedosto.write(f"Pudotettavien ehdokkaiden lkm: {pudotettavien_lkm}\n\n")


        # laskentakierros, toista kunnes valittuja tarpeeksi

        kierros = 1
        uusi_kierros = True

        while pudotettavien_lkm > 0 and self.__vaali.hae_valittujen_lkm() < self.__vaali.hae_valittavien_lkm():

            valitut_kierroksen_alussa = self.__vaali.hae_valittujen_lkm()

            if uusi_kierros:
                print(f"Kierros {kierros}")

                with open(tulokset, "a") as tiedosto:
                    mjono = f"Kierros {kierros}"
                    tiedosto.write(f"\n{mjono}\n")
                    tiedosto.write("=" * len(mjono) + "\n\n")

                with open(laskenta, "a") as tiedosto:
                    mjono = f"Kierros {kierros}"
                    tiedosto.write(f"\n{mjono}\n")
                    tiedosto.write("=" * len(mjono) + "\n\n")
                    tiedosto.write(f"Valittujen lkm kierroksen alussa: {valitut_kierroksen_alussa}\n\n")

                uusi_kierros = False

            #   1. Ehdokas:Ehdokkaat laske äänet

            # jaa ääni lipukkeella ehdokkaille ennen äänien hakemista

            self.__vaali.jaa_aanet_lipukkeilla()

            self.__vaali.laske_aanet()

            with open(laskenta, "a") as tiedosto:
                tiedosto.write("Äänien jako ja laskenta\n\n")
                tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")

            #   2. Lipukkeet äänihukka

            self.__vaali.paivita_aanihukka()

            with open(laskenta, "a") as tiedosto:
                tiedosto.write(f"äänihukka: {self.__vaali.hae_aanihukka()}\n")

            #   3. Äänikynnys update

            self.__vaali.paivita_aanikynnys()
            
            with open(laskenta, "a") as tiedosto:
                tiedosto.write(f"äänikynnys: {self.__vaali.hae_aanikynnys()}\n\n")

            #   Jos kaikilla valituilla ehdokkailla suhdeluku on oikea, valitaan tai pudotetaan ehdokkaita
            #   ja siirrytään kohdan 4 jälkeen uudelle kierrokselle.

            if self.__vaali.paatetaan_kierros():

                #   Ehdokkaiden valinta

                with open(laskenta, "a") as tiedosto:
                    tiedosto.write("Ehdokkaat ennen valintaa/pudotusta\n\n")
                    tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")

                kierroksella_valitut = self.__vaali.valitse_ehdokkaat()

                with open(tulokset, "a") as tiedosto:
                    if len(kierroksella_valitut) > 0:
                        tiedosto.write("Kierroksella valitut ehdokkaat:\n")
                        for valittu in kierroksella_valitut:
                            tiedosto.write(valittu + "\n")
                        tiedosto.write("\n")
                    else:
                        tiedosto.write("Kierroksella ei valittu ehdokkaita.\n\n")

                with open(laskenta, "a") as tiedosto:
                    if len(kierroksella_valitut) > 0:
                        tiedosto.write("Kierroksella valitut ehdokkaat:\n")
                        for valittu in kierroksella_valitut:
                            tiedosto.write(valittu + "\n")
                        tiedosto.write("\n")
                    else:
                        tiedosto.write("Kierroksella ei valittu ehdokkaita.\n\n")


                #   Ehdokkaiden pudotus

                if valitut_kierroksen_alussa - self.__vaali.hae_valittujen_lkm() == 0:
                    pudotettava = self.__vaali.pudota_ehdokas(vertailtavat)

                    if (pudotettava[0]):
                        if len(pudotettava) == 3:
                            with open(laskenta, "a") as tiedosto:
                                tiedosto.write(f"Suoritettiin arvonta. Seed: {pudotettava[2]}\n\n")
                        pudotettava = pudotettava[1]
                    else:
                        with open(tulokset, "a") as tiedosto:
                            tiedosto.write(f"SUORITETAAN PUDOTUSVAALI\n\n")

                        with open(laskenta, "a") as tiedosto:
                            tiedosto.write(f"SUORITETAAN PUDOTUSVAALI\n\n")

                        pudotuslaskenta = Aantenlasku()
                        ehdokas_nro = pudotuslaskenta.suorita_vaali(lipukedata, True, pudotettava[1])
                        pudotettava = self.__vaali.hae_ehdokkaat().hae_ehdokas(ehdokas_nro).pudota()


                    if pudotusvaali:
                        with open(laskenta, "a") as tiedosto:
                            tiedosto.write(f"Pudotetaan ehdokas: {pudotettava.hae_nimi()}\n\n")
                        return pudotettava.hae_nro()

                    pudotettavien_lkm -= 1

                    with open(tulokset, "a") as tiedosto:
                        tiedosto.write(f"Pudotetaan ehdokas: {pudotettava.hae_nimi()}\n\n")

                    with open(laskenta, "a") as tiedosto:
                        tiedosto.write(f"Pudotetaan ehdokas: {pudotettava.hae_nimi()}\n\n")
                        tiedosto.write(f"Pudotettavien ehdokkaiden lkm: {pudotettavien_lkm}\n\n")

                kierros += 1
                uusi_kierros = True

                print(f"Ehdokkaita valittu: {self.__vaali.hae_valittujen_lkm()}/{self.__vaali.hae_valittavien_lkm()}")
                print(f"Ehdokkaita pudottamatta: {pudotettavien_lkm}")

                with open(tulokset, "a") as tiedosto:
                    tiedosto.write("Ehdokkaat kierroksen lopussa\n\n")
                    tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")
                    tiedosto.write(f"äänihukka: {self.__vaali.hae_aanihukka()}\n")
                    tiedosto.write(f"äänikynnys: {self.__vaali.hae_aanikynnys()}\n\n")
                
                with open(laskenta, "a") as tiedosto:
                    tiedosto.write("Ehdokkaat valinnan/pudotuksen jälkeen\n\n")
                    tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")

            else:
                with open(laskenta, "a") as tiedosto:
                    tiedosto.write("Jatketaan iterointia\n\n")

            #   4. Ehdokas:Ehdokkaat ehdokas.updateP

            self.__vaali.paivita_p_arvot()

            with open(laskenta, "a") as tiedosto:
                tiedosto.write("Päivitetään p-arvot\n\n")
                tiedosto.write("Ehdokkaat p-arvon päivityksen jälkeen\n\n")
                tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")
                tiedosto.write(f"Valittujen lkm: {self.__vaali.hae_valittujen_lkm()}\n\n")

        # pudotusvaalissa viimeisen toiveikkaan ehdokkaan valinta pudotettavaksi
        
        if pudotusvaali and self.__vaali.hae_valittujen_lkm() == self.__vaali.hae_valittavien_lkm():
            return self.__vaali.hae_ehdokkaat().hae_toiveikas().hae_nro()

        # Jäljellä olevien toiveikkaiden ehdokkaiden valinta

        if self.__vaali.hae_valittujen_lkm() < self.__vaali.hae_valittavien_lkm():
            print("Valitaan loput toiveikkaat ehdokkaat")
            valitut = self.__vaali.valitse_loput_toiveikkaat()

            with open(tulokset, "a") as tiedosto:
                mjono = "Valitaan loput toiveikkaat ehdokkaat"
                tiedosto.write(f"\n{mjono}\n")
                tiedosto.write("=" * len(mjono) + "\n\n")

                for valittu in valitut:
                    tiedosto.write(valittu + "\n")

            with open(laskenta, "a") as tiedosto:
                mjono = "Valitaan loput toiveikkaat ehdokkaat"
                tiedosto.write(f"\n{mjono}\n")
                tiedosto.write("=" * len(mjono) + "\n\n")

                for valittu in valitut:
                    tiedosto.write(valittu + "\n")

        # Vaalin lopputulos

        with open(tulokset, "a") as tiedosto:
            mjono = "VAALIN TULOS"
            tiedosto.write(f"\n{mjono}\n")
            tiedosto.write("=" * len(mjono) + "\n\n")

            tiedosto.write("Valitut ehdokkaat:\n\n")
            valitut = self.__vaali.hae_ehdokkaat().hae_valitut()
            for valittu in valitut:
                tiedosto.write(valittu + "\n")

        with open(laskenta, "a") as tiedosto:
            mjono = "VAALIN TULOS"
            tiedosto.write(f"\n{mjono}\n")
            tiedosto.write("=" * len(mjono) + "\n\n")

            tiedosto.write("Valitut ehdokkaat:\n\n")
            valitut = self.__vaali.hae_ehdokkaat().hae_valitut()
            for valittu in valitut:
                tiedosto.write(valittu + "\n")





