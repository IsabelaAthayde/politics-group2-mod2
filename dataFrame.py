import pandas as pd

def convertArquive(arquive):
    try:
        # Verifica se o arquivo existe
        csvArquive = pd.read_csv(f"{arquive}.csv")

        # Converte o arquivo csv para xlsc (excel)
        csvArquive.to_excel(f"{arquive}.xlsx", index=False)

    except FileNotFoundError as error:
        # Caso o arquivo não exista retornar Falso
        return False

    return True
 

def create_or_add_csv(form):
    
    # Recebe o nome do arquivo a ser utilizado 
    arquive = input("Digite o nome do arquivo: ")

    csvExists = convertArquive(arquive)

    # Cria um dataframe (Dados Tabulares) do formulário
    dataframe = pd.DataFrame({
        "idade": form["age"],
        "gênero": form["gender"],
        "pergunta_1": form["response_1"],
        "pergunta_2": form["response_2"],
        "pergunta_3": form["response_3"],
        "pergunta_4": form["response_4"],
        "pergunta_5": form["response_5"],
        "pergunta_6": form["response_6"],
        "data/hora": form["time"]
        })

    if csvExists:
        # Envia os dados ao arquivo existente. 
        # mode='a' de append
        dataframe.to_csv(f"{arquive}.csv", mode='a', index=False, header=False)
        print("Dados adicionados com sucesso!")
    else:
        # Cria um arquivo enviando os dados. 
        # O mode='x' cria o arquivo caso ele não exista
        dataframe.to_csv(f"{arquive}.csv", mode='x', index=False, header=True)
        print("CSV criado com sucesso!!")

    # Converte o arquivo csv existente em xlsx para leitura em panilhas
    convertArquive(arquive)
