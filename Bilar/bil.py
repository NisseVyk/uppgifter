class bil:
    #constructor körs först
    def __init__(self, fabrikat, color, lager):
        self.fabrikat = fabrikat
        self.color = color
        self.lager = lager

    def getFabrikat(self):
        return self.fabrikat
    def setFabrikat(self, fabrikat):
        self.fabrikat = fabrikat

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setLager(self, lager):
        self.lager = lager
    def getLager(self):
        return self.lager
