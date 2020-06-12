
class Settings:
    __instance = None

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
            self.seed = int(f.readline())
            self.simTime = int(f.readline())
            self.numEstanteries = int(f.readline())
            self.numCaixesAuto = int(f.readline())
            self.numCaixesTrad = int(f.readline())
            self.tempsProd = int(f.readline())
            self.prodsAuto = int(f.readline())
            self.minProds = int(f.readline())
            self.maxProds = int(f.readline())
            f.close()
