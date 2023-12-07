import opavote
from vaali import Vaali
from datetime import datetime
import locale
import textwrap

class Aantenlasku:

    def __init__(self) -> None:
        self.__vaali = Vaali()
        self.vaalin_nimi = self.__vaali.hae_vaalin_nimi()

        # alustetaan alusta_tiedostot-funktiossa
        self.tulokset = None
        self.laskenta = None

    def alusta_tiedostot(self):
        loc = locale.setlocale(locale.LC_ALL, 'fi_FI.UTF-8')

        aika = datetime.now()
        tiedostojen_aikaleima = aika.strftime('%Y%m%d-%H%M%S-%f')        
        aikaleima = aika.strftime("%x %X")
        vaalin_nimi = self.__vaali.hae_vaalin_nimi()

        self.tulokset = f"vaalit/{vaalin_nimi.replace(' ', '_')}_{tiedostojen_aikaleima}_tulokset.txt"
        self.laskenta = f"vaalit/{vaalin_nimi.replace(' ', '_')}_{tiedostojen_aikaleima}_laskenta.txt"

        ehdokkaat = self.__vaali.hae_ehdokkaat()
        valittavat = self.__vaali.hae_valittavien_lkm()
        hyvaksytyt = self.__vaali.hae_lipukkeet().hyvaksytyt_aanet_lkm()
        hylatyt = self.__vaali.hae_hylatyt_aanet()

        mjono = textwrap.dedent(f"""\
                {vaalin_nimi}
                {aikaleima}
                Ehdokkaita: {ehdokkaat.hae_ehdokkaiden_lkm()}\tValitaan: {valittavat}
                Hyväksyttyjä ääniä: {hyvaksytyt}\tHylättyjä ääniä: {hylatyt}\tÄäniä yhteensä: {hyvaksytyt}\n\n""")
        mjono += str(ehdokkaat) + "\n\n"

        print(mjono)

        with open(self.tulokset, "w") as tiedosto:
            tiedosto.write(mjono)

        with open(self.laskenta, "w") as tiedosto:
            tiedosto.write(mjono)
            tiedosto.write(f"Pudotettavien ehdokkaiden lkm: {self.pudotettavien_lkm}\n\n")

    def tallenna_uusi_kierros(self, kierros, valitut_kierroksen_alussa):
        
        print(f"Kierros {kierros}")

        with open(self.tulokset, "a") as tiedosto:
            mjono = f"Kierros {kierros}"
            tiedosto.write(f"\n{mjono}\n")
            tiedosto.write("=" * len(mjono) + "\n\n")

        with open(self.laskenta, "a") as tiedosto:
            mjono = f"Kierros {kierros}"
            tiedosto.write(f"\n{mjono}\n")
            tiedosto.write("=" * len(mjono) + "\n\n")
            tiedosto.write(f"Valittujen lkm kierroksen alussa: {valitut_kierroksen_alussa}\n\n")

    # vaihe 1
    def laske_aanet(self):

        # jaa ääni lipukkeella ehdokkaille ennen äänien hakemista

        self.__vaali.jaa_aanet_lipukkeilla()

        self.__vaali.laske_aanet()

        with open(self.laskenta, "a") as tiedosto:
            tiedosto.write("Äänien jako ja laskenta\n\n")
            tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")

    # vaihe 2
    def laske_aanihukka(self):
        self.__vaali.paivita_aanihukka()

        with open(self.laskenta, "a") as tiedosto:
            tiedosto.write(f"äänihukka: {self.__vaali.hae_aanihukka()}\n")

    # vaihe 3
    def laske_aanikynnys(self):
        self.__vaali.paivita_aanikynnys()
        
        with open(self.laskenta, "a") as tiedosto:
            tiedosto.write(f"äänikynnys: {self.__vaali.hae_aanikynnys()}\n\n")

    def valitse_ehdokkaat(self):
        
        with open(self.laskenta, "a") as tiedosto:
            tiedosto.write("Ehdokkaat ennen valintaa/pudotusta\n\n")
            tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")

        kierroksella_valitut = self.__vaali.valitse_ehdokkaat()

        with open(self.tulokset, "a") as tiedosto:
            if len(kierroksella_valitut) > 0:
                tiedosto.write("Kierroksella valitut ehdokkaat:\n")
                for valittu in kierroksella_valitut:
                    tiedosto.write(valittu + "\n")
                tiedosto.write("\n")
            else:
                tiedosto.write("Kierroksella ei valittu ehdokkaita.\n\n")

        with open(self.laskenta, "a") as tiedosto:
            if len(kierroksella_valitut) > 0:
                tiedosto.write("Kierroksella valitut ehdokkaat:\n")
                for valittu in kierroksella_valitut:
                    tiedosto.write(valittu + "\n")
                tiedosto.write("\n")
            else:
                tiedosto.write("Kierroksella ei valittu ehdokkaita.\n\n")

    def pudota_ehdokkaat(self, vertailtavat):
      
            pudotettava = self.__vaali.pudota_ehdokas(vertailtavat)

            if (pudotettava[0]):
                if len(pudotettava) == 3:
                    with open(self.laskenta, "a") as tiedosto:
                        tiedosto.write(f"Suoritettiin arvonta. Seed: {pudotettava[2]}\n\n")
                pudotettava = pudotettava[1]
            else:
                with open(self.tulokset, "a") as tiedosto:
                    tiedosto.write(f"SUORITETAAN PUDOTUSVAALI\n\n")

                with open(self.laskenta, "a") as tiedosto:
                    tiedosto.write(f"SUORITETAAN PUDOTUSVAALI\n\n")

                pudotuslaskenta = Aantenlasku()
                ehdokas_nro = pudotuslaskenta.suorita_vaali(lipukedata, True, pudotettava[1])
                pudotettava = self.__vaali.hae_ehdokkaat().hae_ehdokas(ehdokas_nro).pudota()

            if self.pudotusvaali:
                with open(self.laskenta, "a") as tiedosto:
                    tiedosto.write(f"Pudotetaan ehdokas: {pudotettava.hae_nimi()}\n\n")
                return pudotettava.hae_nro()

            self.pudotettavien_lkm -= 1

            with open(self.tulokset, "a") as tiedosto:
                tiedosto.write(f"Pudotetaan ehdokas: {pudotettava.hae_nimi()}\n\n")

            with open(self.laskenta, "a") as tiedosto:
                tiedosto.write(f"Pudotetaan ehdokas: {pudotettava.hae_nimi()}\n\n")
                tiedosto.write(f"Pudotettavien ehdokkaiden lkm: {self.pudotettavien_lkm}\n\n")

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
            self.__vaali.aseta_valittavien_lkm = len(vertailtavat) - 1
            self.__vaali.hae_ehdokkaat().pudota_ylimaaraiset_ehdokkaat(vertailtavat)

        self.pudotettavien_lkm = self.__vaali.hae_ehdokkaat().hae_ehdokkaiden_lkm() - self.__vaali.hae_valittavien_lkm()

        self.pudotusvaali = pudotusvaali

        # luo tiedostot laskennan ja tulosten tallentamiseen

        self.alusta_tiedostot()

        # laskentakierros, toista kunnes valittuja tarpeeksi

        kierros = 1
        uusi_kierros = True

        while self.pudotettavien_lkm > 0 and self.__vaali.hae_valittujen_lkm() < self.__vaali.hae_valittavien_lkm():

            valitut_kierroksen_alussa = self.__vaali.hae_valittujen_lkm()

            if uusi_kierros:
                self.tallenna_uusi_kierros(kierros, valitut_kierroksen_alussa)
                uusi_kierros = False

            #   1. Ehdokas:Ehdokkaat laske äänet

            self.laske_aanet()

            #   2. Lipukkeet äänihukka

            self.laske_aanihukka()

            #   3. Äänikynnys update

            self.laske_aanikynnys()
            
            #   Jos kaikilla valituilla ehdokkailla suhdeluku on oikea, valitaan tai pudotetaan ehdokkaita
            #   ja siirrytään kohdan 4 jälkeen uudelle kierrokselle.

            if self.__vaali.paatetaan_kierros():

                #   Ehdokkaiden valinta

                self.valitse_ehdokkaat()

                #   Ehdokkaiden pudotus
                if valitut_kierroksen_alussa - self.__vaali.hae_valittujen_lkm() == 0:
                    self.pudota_ehdokkaat(vertailtavat)
                
                kierros += 1
                uusi_kierros = True

                print(f"Ehdokkaita valittu: {self.__vaali.hae_valittujen_lkm()}/{self.__vaali.hae_valittavien_lkm()}")
                print(f"Ehdokkaita pudottamatta: {self.pudotettavien_lkm}")

                with open(self.tulokset, "a") as tiedosto:
                    tiedosto.write("Ehdokkaat kierroksen lopussa\n\n")
                    tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")
                    tiedosto.write(f"äänihukka: {self.__vaali.hae_aanihukka()}\n")
                    tiedosto.write(f"äänikynnys: {self.__vaali.hae_aanikynnys()}\n\n")
                
                with open(self.laskenta, "a") as tiedosto:
                    tiedosto.write("Ehdokkaat valinnan/pudotuksen jälkeen\n\n")
                    tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")

            else:
                with open(self.laskenta, "a") as tiedosto:
                    tiedosto.write("Jatketaan iterointia\n\n")

            #   4. Ehdokas:Ehdokkaat ehdokas.updateP

            self.__vaali.paivita_p_arvot()

            with open(self.laskenta, "a") as tiedosto:
                tiedosto.write("Päivitetään p-arvot\n\n")
                tiedosto.write("Ehdokkaat p-arvon päivityksen jälkeen\n\n")
                tiedosto.write(str(self.__vaali.hae_ehdokkaat()) + "\n\n")
                tiedosto.write(f"Valittujen lkm: {self.__vaali.hae_valittujen_lkm()}\n\n")

        # pudotusvaalissa viimeisen toiveikkaan ehdokkaan valinta pudotettavaksi
        
        if self.pudotusvaali and self.__vaali.hae_valittujen_lkm() == self.__vaali.hae_valittavien_lkm():
            return self.__vaali.hae_ehdokkaat().hae_toiveikas().hae_nro()

        # Jäljellä olevien toiveikkaiden ehdokkaiden valinta

        if self.__vaali.hae_valittujen_lkm() < self.__vaali.hae_valittavien_lkm():
            print("Valitaan loput toiveikkaat ehdokkaat")
            valitut = self.__vaali.valitse_loput_toiveikkaat()

            with open(self.tulokset, "a") as tiedosto:
                mjono = "Valitaan loput toiveikkaat ehdokkaat"
                tiedosto.write(f"\n{mjono}\n")
                tiedosto.write("=" * len(mjono) + "\n\n")

                for valittu in valitut:
                    tiedosto.write(valittu + "\n")

            with open(self.laskenta, "a") as tiedosto:
                mjono = "Valitaan loput toiveikkaat ehdokkaat"
                tiedosto.write(f"\n{mjono}\n")
                tiedosto.write("=" * len(mjono) + "\n\n")

                for valittu in valitut:
                    tiedosto.write(valittu + "\n")

        # Vaalin lopputulos

        with open(self.tulokset, "a") as tiedosto:
            mjono = "VAALIN TULOS"
            tiedosto.write(f"\n{mjono}\n")
            tiedosto.write("=" * len(mjono) + "\n\n")

            tiedosto.write("Valitut ehdokkaat:\n\n")
            valitut = self.__vaali.hae_ehdokkaat().hae_valitut()
            for valittu in valitut:
                tiedosto.write(valittu + "\n")

        with open(self.laskenta, "a") as tiedosto:
            mjono = "VAALIN TULOS"
            tiedosto.write(f"\n{mjono}\n")
            tiedosto.write("=" * len(mjono) + "\n\n")

            tiedosto.write("Valitut ehdokkaat:\n\n")
            valitut = self.__vaali.hae_ehdokkaat().hae_valitut()
            for valittu in valitut:
                tiedosto.write(valittu + "\n")





