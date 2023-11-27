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
            p = aanikynnys * p / self.__kokonaisaanimaara

    def hae_p(self):
        return self.__p
    
    def hae_status(self):
        return self.__status
    
    def __str__(self) -> str:
        return f"Ehdokas {self.__nro} {self.__nimi}, p: {self.__p}, status: {self.__status}"
    

if __name__ == "__main__":
    ehdokas = Ehdokas(1)
    print(ehdokas)
    ehdokas.set_nimi("Maija Meikäläinen")
    print(ehdokas)