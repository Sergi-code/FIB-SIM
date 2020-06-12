import simpy
from Settings import Settings as st

class Supermercat:
    __instance = None
    st = st.getInstance() 
    estanteries = {}
    cues = {}
    caixesAuto = {}
    caixesTrad = {}
    
    @staticmethod 
    def getInstance():
        if Supermercat.__instance == None:
            Supermercat()
        return Supermercat.__instance

    def __init__(self):
        if Supermercat.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Supermercat.__instance = self

    def creaSupermercat(self, env):
        ## Estanteries
        for i in range(self.st.numEstanteries):
            self.estanteries[i] = simpy.Resource(env, capacity = 1)
        
        ## Cues
        for i in range(2):
            self.cues[i] = simpy.Resource(env, capacity = 1)
        
        # Caixa autoservei
        for i in range(self.st.numCaixesAuto):
            self.caixesAuto[i] = simpy.Resource(env, capacity = 1)
        
        # Caixa tradicional
        for i in range(self.st.numCaixesTrad):
            self.caixesTrad[i] = simpy.Resource(env, capacity = 1)
            