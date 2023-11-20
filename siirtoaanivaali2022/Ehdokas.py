class Ehdokas:

    def __init__(self, nro:int):
        self.nro = nro
        self.nimi = ""
        self.p = 1
        self.status = "toiveikas"

    def set_nimi(self, nimi:str):
        self.nimi = nimi