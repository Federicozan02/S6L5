import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "insurance.csv"

#Leggo e importo i dati del csv in un dataframe 
try:
	insurance = pd.read_csv(file_name)
except:
	print("Errore caricamento")
	
dati = pd.DataFrame(insurance)

#funzione che mi consente di avere il nome di una colonna in entrata per creare un istogramma
def creaGrafico(nome):
    plt.figure(figsize=(10, 6))
    sns.histplot(dati[nome], kde=True, color="darkgreen")
    plt.title(f'Distribution for {nome}')
    plt.show()
    
creaGrafico('age')
creaGrafico('charges')
creaGrafico('bmi')
