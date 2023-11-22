class Ehdokas:

    def __init__(self, nro:int):
        self.nro = nro
        self.nimi = ""
        self.p = 1
        self.status = "toiveikas"

    def set_nimi(self, nimi:str):
        self.nimi = nimi

    def __str__(self) -> str:
        return f"Ehdokas {self.nro} {self.nimi}, p: {self.p}, status: {self.status}"
    

if __name__ == "__main__":
    ehdokas = Ehdokas(1)
    print(ehdokas)
    ehdokas.set_nimi("Maija Meikäläinen")
    print(ehdokas)