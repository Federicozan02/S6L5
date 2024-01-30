import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "insurance.csv"

try:
	insurance = pd.read_csv(file_name)
except:
	print("Errore caricamento")

dati = pd.DataFrame(insurance)
dati['bmi_over30']= dati['bmi'] > 30

def boxplot(numeric_column, colonne):    
    sns.boxplot(x=colonne, y=numeric_column, data = dati, palette="pastel", hue='bmi_over30', dodge=True, legend=False)
    plt.title(f'Boxplot di {numeric_column} per {colonne}', fontsize=14)
    plt.show()
    
boxplot('charges', 'smoker')
