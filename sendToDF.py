import pandas as pd
from principal import getData


data = getData()
    

nome = data[0]
idade = data[1]
saude = data[2]


def convertArquive(arquive):
    try:
        #Verifica se o arquivo existe
        dataframe = pd.read_csv(f"{arquive}.csv")

        #Converte o arquivo csv para xlsc (excel)
        dataframe.to_excel(f"{arquive}.xlsx", index=False)

    except FileNotFoundError as error:
        return False

    return True
 

def create_or_add_csv(dict):
    form = dict.item()
    
    arquive = input("Digite o nome do arquivo: ")
    csvExists = convertArquive(arquive)

    dataframe = pd.DataFrame({
        "idade": age,
        "gênero": gender,
        "pergunta_1": response_1,
        "pergunta_2": response_2,
        "pergunta_3": response_3,
        "pergunta_4": response_4,
        "pergunta_5": response_5,
        "pergunta_6": response_6,
        "data/hora": time
        })

    if csvExists:
        dataframe.to_csv(f"{arquive}.csv", mode='a', index=False, header=False)
        print("Dados adicionados com sucesso!")
    else:
        dataframe.to_csv(f"{arquive}.csv", mode='x', index=False, header=True)
        print("CSV criado com sucesso!!")

    convertArquive()


