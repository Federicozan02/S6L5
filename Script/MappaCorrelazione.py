import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "insurance.csv"

#Inserisco i dati del csv in un dataframe
try:
	insurance = pd.read_csv(file_name)
except:
	print("Errore caricamento")

dati = pd.DataFrame(insurance)

#Limito i valori alle colonne fumatori, bmi e rate
insurance_data = dati[['smoker', 'bmi', 'charges']]
insurance_data['smoker'] = insurance_data['smoker'].map({'yes': 1, 'no': 0})

#creo la mappa di correlazione con i valori limitati
correlation_matrix = insurance_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Matrice di Correlazione")
plt.show()
