class Ehdokas:

    def __init__(self, nro:int):
        self.__nro = nro
        self.__nimi = ""
        self.__p = 1
        self.__status = "toiveikas"
        self.__kokonaisaanimaara = 0

    def hae_nro(self):
        return self.__nro

    def set_nimi(self, nimi:str):
        self.__nimi = nimi

    def hae_nimi(self):
        return self.__nimi
    
    def paivita_p(self, aanikynnys):
        if self.__status == "valittu":
            self.__p = aanikynnys * self.__p / self.__kokonaisaanimaara

    def hae_p(self):
        return self.__p
    
    def hae_status(self):
        return self.__status
    
    def valitse(self):
        self.__status = "valittu"

    def pudota(self):
        self.__status = "pudotettu"
        self.__p = 0
        return self.__nimi
    
    def aseta_kokonaisaanimaara(self, kokonaisaanimaara):
        self.__kokonaisaanimaara = kokonaisaanimaara

    def hae_kokonaisaanimaara(self):
        return self.__kokonaisaanimaara
    
    def suhdeluku_oikea(self, aanikynnys):
        if self.__status != "valittu":
            return True
        elif self.__status == "valittu":
            suhdeluku = aanikynnys / self.__kokonaisaanimaara
            suhdeluku = round(suhdeluku, 5)
            if suhdeluku >= 0.99999 and suhdeluku <= 1.00001:
                return True
            
        return False
    
    def __str__(self) -> str:
        return f"Ehdokas {self.__nro}\t{self.__nimi}\täänimäärä {self.__kokonaisaanimaara}\tp: {self.__p}\tstatus: {self.__status}"
    

if __name__ == "__main__":
    ehdokas = Ehdokas(1)
    print(ehdokas)
    ehdokas.set_nimi("Maija Meikäläinen")
    print(ehdokas)