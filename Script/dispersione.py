import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "insurance.csv"

try:
	insurance = pd.read_csv(file_name)
except:
	print("Errore caricamento")

dati = pd.DataFrame(insurance)

#Converto i valori yes e no di smoker in numeri da 0 e 1
dati['smoker_numeric'] = dati['smoker'].map({'yes': 1, 'no': 0})

#Stampo il grafico a dispersione per fumatori, spese e bmi
plt.figure(figsize=(12, 8))
sns.scatterplot(x='bmi', y='charges', hue='smoker_numeric', data=dati, palette={0: 'blue', 1: 'red'}, alpha=0.7)
plt.title('Grafico a Dispersione tra Spese, BMI e Fumatori')
plt.xlabel('BMI')
plt.ylabel('Spese Assicurative')
plt.legend(['Fumatori', 'Non Fumatori'])
plt.show()
