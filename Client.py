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
        #self.arribada = env.now
        self.numProds = random.randint(self.st.minProds, self.st.maxProds)
        self.num = 0  
        hora = (env.now / 3600)
        print(str(hora) + ' ' + str(ident) + ": Acabo d'arribar")
        ##print("%7.4f %s: Acabo d'arribar" % (env.now, ident))
        print("Vull comprar " + str(self.numProds) + " productes")

    def comprant(self):
        for i in range(self.numProds):
            numEstanteria = random.randint(0, self.st.numEstanteries - 1)
            with self.sp.estanteries[numEstanteria].request() as req:
                yield req

                self.num += 1
                print("Client " + str(self.id) + ": porto:" + str(self.num) + " productes")

        if self.numProds <= self.st.prodsAuto:
            print("Client " + str(self.id) + ": estic esperant a la cua d'autoservei")
            with self.sp.cues[0].request() as req:
                yield req

                print("Client " + str(self.id) + ": em toca el següent")
                trobat = 0
                numCaixa = 0
                while trobat == 0:
                    for i in range(self.st.numCaixesAuto - 1):
                        if self.sp.caixesAuto[i].count == 0: 
                            trobat = 1
                            numCaixa = i
                            break
                    yield self.env.timeout(1) ##temps espera
            with self.sp.caixesAuto[numCaixa].request() as req:
                yield req
                print("Client " + str(self.id) + ": estic comprant a la caixa d'autoservei " + str(numCaixa))
                yield self.env.timeout(self.st.tempsProd * self.numProds)
                print("Client " + str(self.id) + ": me las piro vampiro")

        else:
            print("Client: " + str(self.id) + " estic a la cua tradicional")
            with self.sp.cues[1].request() as req:
                yield req

                print("Client: " + str(self.id) + " em toca el següent")
                trobat = 0
                numCaixa = 0
                while trobat == 0:
                    for i in range(self.st.numCaixesTrad - 1):
                        if self.sp.caixesTrad[i].count == 0: 
                            trobat = 1
                            numCaixa = i
                            break
                    yield self.env.timeout(1) ##temps espera
            with self.sp.caixesTrad[numCaixa].request() as req:
                yield req
                print("Client " + str(self.id) + ": estic comprant a la caixa tradicional " + str(numCaixa))
                yield self.env.timeout(self.st.tempsProd * self.numProds)
                print("Client " + str(self.id) + ": me las piro vampiro")
            

    '''def agafarProd(self):
        print("hey") #debug
        numEstanteria = math.floor(random.uniform(0, 5.99))
        with self.sp.estanteries[numEstanteria].request() as req:
            print("hey2") #debug
            yield req
            print("hey3") #debug
            self.num += 1
            print("Client: " + str(self.id) + ", porto:" + str(self.num) + " productes")'''
    
    '''def anarCuaAuto(self):
        print("Client: " + str(self.id) + " estic esperant a la cua d'autoservei")
        with self.sp.cues[0].request() as req:
            yield req

            print("Client: " + str(self.id) + " sóc el primer de la cua d'autoservei")

            while(1):
                if self.sp.caixesAuto[0].count == 1: self.utilitzaCaixaAuto(0)
                elif self.sp.caixesAuto[1].count == 1: self.utilitzaCaixaAuto(1)'''

    def utilitzaCaixaAuto(self, numCaixa):
        '''with self.sp.caixesAuto[numCaixa].request() as req:
            yield req
            print("Client: " + str(self.id) + " estic comprant a la caixa d'autoservei " + numCaixa)
            #Aqui haremos un delay dependiendo de los objetos que lleve el señor
            pass
        
        print("Client: " + str(self.id) + "me las piro vampiro")'''
        pass
                    
    def anarCuaTrad(self):
        '''print("Client: " + str(self.id) + " estic a la cua tradicional")
        with self.sp.cues[1].request() as req:
            yield req

            print("Client: " + str(self.id) + " sóc el primer de la cua tradicional")

            while(1):
                if self.sp.caixesTrad[0].count == 1: self.utilitzaCaixaTrad(0)
                elif self.sp.caixesTrad[1].count == 1: self.utilitzaCaixaTrad(1)
                elif self.sp.caixesTrad[2].count == 1: self.utilitzaCaixaTrad(2)
                elif self.sp.caixesTrad[3].count == 1: self.utilitzaCaixaTrad(3)'''
        pass
    
    def utilitzaCaixaTrad(self, numCaixa):
        '''with self.sp.caixesTrad[numCaixa].request() as req:
            yield req
            #Aqui haremos un delay dependiendo de los objetos que lleve el señor
            pass'''
        pass