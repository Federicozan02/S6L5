import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_name = "insurance.csv"

try:
	insurance = pd.read_csv(file_name)
except:
	print("Errore caricamento")
	
dati = pd.DataFrame(insurance)

#Set dei valori di riferimento per il BMI
normal_bmi = 26

#Creo le nuove colonne dove ci saranno i valori maggiorati 
dati['Risk_bmi'] = np.where(dati['bmi'] >= 28, 0.05*dati['charges'], 0)
dati['Risk_smoker'] = np.where(dati['smoker'] == 'yes', 0.05*dati['charges'], 0)
dati['Total_risk'] = (dati['Risk_bmi']+ dati['Risk_smoker'])*dati['children']
dati['New_total'] = (dati['charges']+dati['Total_risk'])

#Si raggruppa per età e si sommano i valori delle charges e il nuovo totale
tab = dati.groupby('age')[['New_total','charges']].sum()

#creazione del grafico
tab.plot(kind = "bar")

plt.xlabel("Età", color = "k")
plt.ylabel("Valore", color = "k")
plt.title("Charge assicurativa prima e dopo l'aumento'", color = "k")
plt.legend(["Nuova rata", "Vecchia rata"])

plt.show()
