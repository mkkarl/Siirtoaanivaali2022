class Ehdokas:

    def __init__(self, nro:int):
        self.nro = nro
        self.nimi = ""
        self.p = 1
        self.status = "toiveikas"
        self.kokonaisaanimaara = 0

    def hae_nro(self):
        return self.nro

    def set_nimi(self, nimi:str):
        self.nimi = nimi

    def hae_nimi(self):
        return self.nimi

    def __str__(self) -> str:
        return f"Ehdokas {self.nro} {self.nimi}, p: {self.p}, status: {self.status}"
    
    def paivita_p(self, aanikynnys):
        if self.status == "valittu":
            p = aanikynnys * p / self.kokonaisaanimaara

    def hae_p(self):
        return self.p
    

if __name__ == "__main__":
    ehdokas = Ehdokas(1)
    print(ehdokas)
    ehdokas.set_nimi("Maija Meikäläinen")
    print(ehdokas)