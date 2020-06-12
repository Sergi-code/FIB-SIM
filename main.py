import simpy
import random
from Supermercat import Supermercat
from Client import Client
from Settings import Settings as st

def font(env, number, interval):
    for i in range(number):
        c = Client(env, i)
        env.process(c.comprant()) ##si en comprant pones yield hay que meterlo en process
        ##c.comprant()
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)


#setup and start
print('Supermercat')

st = st.getInstance()
sp = Supermercat.getInstance()

random.seed(st.seed)
env = simpy.Environment()

sp.creaSupermercat(env)

env.process(font(env, 5, 10))
env.run(until = st.simTime)