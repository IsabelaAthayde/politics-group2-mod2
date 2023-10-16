import pandas as pd
from principal import getData

data = getData()

nome = data[0]
idade = data[1]
saude = data[2]

def findArquive():
    try:
        df = pd.read_csv('zoo.csv')
    except FileNotFoundError as error:
        return False

    return True
 
csvExists = findArquive()

df = pd.DataFrame({'Nome': [nome], 'idade': [idade], 'saude': [saude]})

if csvExists:
    df.to_csv("zoo.csv", mode='a', index=False, header=False)
    print("Adicionado!!")
else:
    df.to_csv("zoo.csv", mode='x', index=False, header=True)
    print("CSV criado!!")


