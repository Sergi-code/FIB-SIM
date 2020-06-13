import simpy
import math
import random
from Supermercat import Supermercat
from Settings import Settings as st

class Client:
    st = st.getInstance()
    sp = Supermercat.getInstance()

    def __init__(self, env, ident):
        self.env = env
        self.id = ident
        self.op = open("output.txt","a+")
        self.numProds = random.randint(self.st.minProds, self.st.maxProds)
        self.auto = self.numProds <= self.st.prodsAuto
        self.num = 0  
        hora = (env.now / 3600)
        self.op.write(str(hora) + ' ' + str(ident) + ": Acabo d'arribar\n")
        self.op.write("Vull comprar " + str(self.numProds) + " productes\n")

    def comprant(self):
        self.tempsEntraSuper = self.env.now
        for i in range(self.numProds):
            numEstanteria = random.randint(0, self.st.numEstanteries - 1)
            with self.sp.estanteries[numEstanteria].request() as req:
                yield req

                yield self.env.timeout(10) ##temps Camina de passadis a passadis
                yield self.env.timeout(25) ##temps Mirar caducitat i compara preus
                
                self.num += 1
                self.op.write("Client " + str(self.id) + ": porto:" + str(self.num) + " productes\n")
                
        if self.st.numCaixesTrad == 0 : self.st.setTempsBuscant(1, self.env.now - self.tempsEntraSuper, self.numProds)
        elif self.st.numCaixesAuto == 0: self.st.setTempsBuscant(0, self.env.now - self.tempsEntraSuper, self.numProds)
        else: self.st.setTempsBuscant(self.auto, self.env.now - self.tempsEntraSuper, self.numProds)

        yield self.env.timeout(10) ##temps Camina a cua

        if self.st.numCaixesTrad == 0 or (self.st.numCaixesAuto != 0 and self.auto):
            self.tempsEntraCuaAuto = self.env.now
            self.op.write("Client " + str(self.id) + ": estic esperant a la cua d'autoservei\n")
            with self.sp.cues[0].request() as req:
                yield req

                self.op.write("Client " + str(self.id) + ": em toca el següent\n")
                trobat = 0
                numCaixa = 0
                while trobat == 0:
                    for i in range(self.st.numCaixesAuto):
                        if self.sp.caixesAuto[i].count == 0: 
                            trobat = 1
                            numCaixa = i
                            break
                    yield self.env.timeout(1) ##temps espera
            self.st.setTempsAuto(self.env.now - self.tempsEntraCuaAuto)
            self.entroCaixaAuto = self.env.now
            with self.sp.caixesAuto[numCaixa].request() as req:
                yield req
                self.op.write("Client " + str(self.id) + ": estic comprant a la caixa d'autoservei " + str(numCaixa) + "\n")
                yield self.env.timeout(random.gauss(self.st.tempsProd - 5, 5) * self.numProds)
                self.st.setTempsCaixaAuto(self.env.now - self.entroCaixaAuto)


        else:
            self.op.write("Client: " + str(self.id) + " estic a la cua tradicional\n")
            self.tempsEntraCuaTrad = self.env.now
            with self.sp.cues[1].request() as req:
                yield req

                self.op.write("Client: " + str(self.id) + " em toca el següent\n")
                trobat = 0
                numCaixa = 0
                while trobat == 0:
                    for i in range(self.st.numCaixesTrad):
                        if self.sp.caixesTrad[i].count == 0: 
                            trobat = 1
                            numCaixa = i
                            break
                    yield self.env.timeout(1) ##temps espera
            self.st.setTempsTrad(self.env.now - self.tempsEntraCuaTrad)
            self.entroCaixaTrad = self.env.now
            with self.sp.caixesTrad[numCaixa].request() as req:
                yield req
                self.op.write("Client " + str(self.id) + ": estic comprant a la caixa tradicional " + str(numCaixa) + "\n")
                yield self.env.timeout(random.gauss(self.st.tempsProd, 5) * self.numProds)
                self.st.setTempsCaixaTrad(self.env.now - self.entroCaixaTrad)

        self.op.write("Client " + str(self.id) + ": surto del supermercat\n")
        
        if self.st.numCaixesTrad == 0 : self.st.setTempsSuper(1, self.env.now - self.tempsEntraSuper)
        elif self.st.numCaixesAuto == 0: self.st.setTempsSuper(0, self.env.now - self.tempsEntraSuper)
        else: self.st.setTempsSuper(self.auto, self.env.now - self.tempsEntraSuper)