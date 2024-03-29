import simpy
import random
from matplotlib import pyplot as plt
from Supermercat import Supermercat
from Client import Client
from Settings import Settings as st


def font(env, number, interval):
    f = open("schedule.txt", "r")
    num = 0
    for i in range(48):
        time = float(f.readline()) * 60.0
        numClients = int(f.readline())

        while True:
            if env.now >= time:
                break
            yield env.timeout(60) ##temps espera
        
        for j in range(numClients):
            c = Client(env, num)
            env.process(c.comprant())
            num = num + 1

#setup and start
print('Supermercat')

st = st.getInstance()
sp = Supermercat.getInstance()

random.seed(st.seed)
env = simpy.Environment()

sp.creaSupermercat(env)

env.process(font(env, 5, 10))
env.run(until = st.simTime)
st.estadistiques()


stats = open("stats.txt","w")
stats.write("Estadistiques Clients de caixes d'autoservei\n")
stats.write("Clients: " + str(st.numAuto) + "\n")
stats.write("Temps mitjana buscant productes dels clients d'autoservei: " + "{:.3f}".format(st.meanTempsBuscantAuto) + " min\n")
stats.write("Espera mitjana a la cua d'autoservei: " + "{:.3f}".format(st.meanCuaAuto) + " min\n")
stats.write("Espera maxima a la cua d'autoservei: " + "{:.3f}".format(st.esperaCuaMaxAuto) + " min\n")
stats.write("Temps passant els productes per la caixa: " + "{:.3f}".format(st.meanTempsCaixaAuto)+ " min\n")
stats.write("Temps mitja que passa un client de caixes d'autoservei al supermercat: " + "{:.3f}".format(st.meanTempsSuperAuto) + " min\n")

stats.write("\n")

stats.write("Estadistiques Clients de caixes tradicionals\n")
stats.write("Clients: " + str(st.numTrad) + "\n")
stats.write("Temps mitjana buscant productes dels clients tradicionals: " + "{:.3f}".format(st.meanTempsBuscantTrad) + " min\n")
stats.write("Espera mitjana a la cua tradicional: " + "{:.3f}".format(st.meanCuaTrad) + " min\n")
stats.write("Espera maxima a la cua tradicional: " + "{:.3f}".format(st.esperaCuaMaxTrad) + " min\n")
stats.write("Temps passant els productes per la caixa: " + "{:.3f}".format(st.meanTempsCaixaTrad) + " min\n")
stats.write("Temps mitja que passa un client de caixes tradicional al supermercat: " + "{:.3f}".format(st.meanTempsSuperTrad) + " min\n")

stats.write("\n")

stats.write("Estadistiques Clients\n")
stats.write("Clients: " + str(st.numClients) + "\n")
stats.write("Percentatge d'utlització caixes d'autoservei: " + "{:.3f}".format(st.numAuto * 100 / st.numClients) + " % \n")
stats.write("Percentatge d'utlització caixes tradicionals: " + "{:.3f}".format(st.numTrad * 100 / st.numClients) + " % \n")
stats.write("Temps mitjana buscant productes: " + "{:.3f}".format(st.meanTempsBuscant) + " min\n")
stats.write("Espera mitjana a les cues: " + "{:.3f}".format(st.meanCua) + " min\n")
stats.write("Temps passant els productes per les caixes: " + "{:.3f}".format(st.meanTempsCaixa) + " min\n")
stats.write("Temps mitja que passa un client al supermercat: " + "{:.3f}".format(st.meanTempsSuper) + " min\n")


# Some data
labelNada = ' ', ' ', ' '
labelsGlobal = 'Buscant', 'Cua', 'Caixes'
labelsAuto = 'Buscant', 'Cua', 'Caixes'
labelsTrad = 'Buscant', 'Cua', 'Caixes'

fracsGlobal = [st.meanTempsBuscant, st.meanCua, st.meanTempsCaixa]
fracsAuto = [st.meanTempsBuscantAuto, st.meanCuaAuto, st.meanTempsCaixaAuto]
fracsTrad = [st.meanTempsBuscantTrad, st.meanCuaTrad, st.meanTempsCaixaTrad]

# Make figure and axes
fig, axs = plt.subplots(2, 2)

axs[0, 0].set(aspect="equal", title='Global')
axs[1, 0].set(aspect="equal", title='Autoservei')
axs[1, 1].set(aspect="equal", title='Tradicional')

# A standard pie plot
axs[0, 0].pie(fracsGlobal, labels=labelsGlobal, autopct='%1.1f%%', shadow=True)
axs[1, 0].pie(fracsAuto, labels=labelsGlobal, autopct='%1.1f%%', shadow=True)
axs[1, 1].pie(fracsTrad, labels=labelsGlobal, autopct='%1.1f%%', shadow=True)

# Adapt radius and text size for a smaller pie
patches, texts, autotexts = axs[0, 1].pie(fracsGlobal, labels=labelNada,
                                          autopct='%.0f%%',
                                          textprops={'size': 'smaller'},
                                          shadow=False, radius=0.0)
# Make percent texts even smaller
plt.setp(autotexts, size='x-small')
autotexts[0].set_color('white')
autotexts[1].set_color('white')
autotexts[2].set_color('white')

plt.show()
