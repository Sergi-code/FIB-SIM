
class Settings:
    __instance = None

    ##  Auto
    meanTempsBuscantAuto = 0.0
    numAuto = 0

    meanCuaAuto = 0.0
    esperaCuaMaxAuto = 0.0

    meanTempsCaixaAuto = 0.0

    meanTempsSuperAuto = 0.0

    ##  Trad
    meanTempsBuscantTrad = 0.0
    numTrad = 0

    meanCuaTrad = 0.0
    esperaCuaMaxTrad = 0.0

    meanTempsCaixaTrad = 0.0

    meanTempsSuperTrad = 0.0

    ## Global
    meanProd = 0.0
    meanTempsBuscant = 0.0
    numClients = 0

    meanCua = 0.0

    meanTempsCaixa = 0.0

    meanTempsSuper = 0.0
    tempsMaxSuper = 0.0


    @staticmethod 
    def getInstance():
        if Settings.__instance == None:
            Settings()
        return Settings.__instance

    def __init__(self):
        if Settings.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Settings.__instance = self

            f = open("input.txt", "r")
            self.comentaris = f.readline()
            self.seed = int(f.readline())
            self.comentaris = f.readline()
            self.simTime = int(f.readline())
            self.comentaris = f.readline()
            self.numEstanteries = int(f.readline())
            self.comentaris = f.readline()
            self.numCaixesAuto = int(f.readline())
            self.comentaris = f.readline()
            self.numCaixesTrad = int(f.readline())
            self.comentaris = f.readline()
            self.tempsProd = int(f.readline())
            self.comentaris = f.readline()
            self.prodsAuto = int(f.readline())
            self.comentaris = f.readline()
            self.minProds = int(f.readline())
            self.comentaris = f.readline()
            self.maxProds = int(f.readline())
            f.close()
    
    def setTempsBuscant(self, auto, temps, prods):
        if auto:
            self.meanTempsBuscantAuto += temps
            self.numAuto += 1
        else:
            self.meanTempsBuscantTrad += temps
            self.numTrad += 1

        self.meanTempsBuscant += temps
        self.numClients += 1
        self.meanProd += prods
    
    def setTempsAuto(self, temps):
        self.meanCuaAuto += temps
        self.meanCua += temps
        if temps > self.esperaCuaMaxAuto:
            self.esperaCuaMaxAuto = temps
    
    def setTempsTrad(self, temps):
        self.meanCuaTrad += temps
        self.meanCua += temps
        if temps > self.esperaCuaMaxTrad:
            self.esperaCuaMaxTrad = temps
    
    def setTempsCaixaAuto(self, temps):
        self.meanTempsCaixaAuto += temps
        self.meanTempsCaixa += temps

    def setTempsCaixaTrad(self, temps):
        self.meanTempsCaixaTrad += temps
        self.meanTempsCaixa += temps
    
    def setTempsSuper(self, auto, temps):
        self.meanTempsSuper += temps
        if auto:
            self.meanTempsSuperAuto += temps
        else:
            self.meanTempsSuperTrad += temps

        if temps > self.tempsMaxSuper:
            self.tempsMaxSuper = temps

    def estadistiques(self):
        ## Auto
        if self.numAuto != 0:
            self.meanTempsBuscantAuto = (self.meanTempsBuscantAuto / self.numAuto) / 60
            self.meanCuaAuto = (self.meanCuaAuto / self.numAuto) / 60
            self.esperaCuaMaxAuto = self.esperaCuaMaxAuto / 60
            self.meanTempsCaixaAuto = (self.meanTempsCaixaAuto / self.numAuto) / 60
            self.meanTempsSuperAuto = (self.meanTempsSuperAuto / self.numAuto) / 60

        ## Trad
        if self.numTrad != 0:
            self.meanTempsBuscantTrad = (self.meanTempsBuscantTrad / self.numTrad) / 60
            self.meanCuaTrad = (self.meanCuaTrad / self.numTrad) / 60
            self.esperaCuaMaxTrad = self.esperaCuaMaxTrad / 60
            self.meanTempsCaixaTrad = (self.meanTempsCaixaTrad / self.numTrad) / 60
            self.meanTempsSuperTrad = (self.meanTempsSuperTrad / self.numTrad) / 60

        # Global
        self.meanTempsBuscant = (self.meanTempsBuscant / self.numClients) / 60
        self.meanCua = (self.meanCua / self.numClients) / 60
        self.meanTempsCaixa = (self.meanTempsCaixa / self.numClients) / 60
        self.meanTempsSuper = (self.meanTempsSuper / self.numClients) / 60
        self.tempsMaxSuper = self.tempsMaxSuper / 60