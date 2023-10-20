import pandas as pd
from datetime import datetime
import os


# Lista de perguntas
questions = {
    "1":  "No ano passado, um apresentador de um podcast famoso no Brasil defendeu que um partido nazista deveria ter o direito de existir legalmente com base na liberdade de expressão. Você apoia a ideia de uma liberdade de expressão irrestrita?",
    "2":  "No Rio de Janeiro, já há um bom tempo, possuímos uma política de intervenção político-militar nas comunidades. Tais intervenções e operações têm sido alvo de crítica por alguns, devido ao alto número de mortes, e apoiadas por outros, devido à necessidade de combater poderes paralelos ao Estado. Você é a favor da legalização das drogas?",
    "3":  "No Brasil, estima-se que cerca de 800 mil mulheres pratiquem aborto por ano. Há quem defenda que a legalização poderia diminuir o número de abortos, pois estaria sob o controle do Estado e reduziria o número de mulheres mortas em clínicas clandestinas. Por outro lado, o argumento é que um feto é uma vida, e realizar o aborto seria uma espécie de assassinato. Você é a favor da legalização do aborto?",
    "4":  "Que durante a história o papel da mulher tem modificado ao longo do tempo, quase ninguém discorda. Há quem acredite que os movimentos feministas em defesa dos direitos das mulheres em uma sociedade patriarcal contribuíram para a melhoria da sociedade. Por outro lado, há quem afirme que o movimento feminista não conquistou esses direitos, ou que apenas serve para criar uma guerra dos sexos. Você acredita que o feminismo é importante?",
    "5":  "Nas últimas eleições, testemunhamos um intenso confronto, especialmente no segundo turno. De um lado, havia apoiadores da volta de Lula, que enfatizavam a necessidade do seu compromisso com o bem-estar das camadas mais pobres do Brasil, enquanto criticavam Bolsonaro por sua abordagem na pandemia e seu desrespeito ao Poder Judiciário. Já os defensores de Bolsonaro argumentavam que ele era fundamental para endireitar o país, preservando valores morais e costumes tradicionais. Além disso, expressavam preocupações sobre uma suposta agenda comunista de Lula e o fechamento de igrejas. Você acredita que Lula é um governante melhor?",
    "6":  "Recentemente, temos acompanhado o conflito entre Israel e as forças de resistência da Palestina, um embate que resultou em perdas de vidas de ambos os lados. Os defensores da causa Palestina argumentam que o atual Estado de Israel, outrora território Palestino, foi adquirido através de meios violentos, forçando a expulsão dos habitantes locais para regiões mais reduzidas e economicamente menos prósperas. Eles também apontam que, estatisticamente, o conflito tem impactado mais fortemente a população Palestina, com um número maior de mortes do lado Palestino. Por outro lado, os apoiadores de Israel sustentam a crença de que a terra pertence a eles, baseando-se na promessa divina registrada na Torah. Além disso, eles caracterizam os grupos paramilitares Palestinos como organizações terroristas e radicais islâmicos. Argumentam também que Israel deve ser mantido, pois representa um compromisso com a democracia e o princípio de um Estado laico. Você crê que Israel tem razão nesse conflito?",
}

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
 

def create_or_add_csv(form : dict,nameUser: str):

    print(questions["1"])
    # Recebe o nome do arquivo a ser utilizado 
    arquive = input("Digite o nome do arquivo: ")

    csvExists = convertArquive(arquive)

    # Cria um dataframe (Dados Tabulares) do formulário
    dataframe = pd.DataFrame([
        {
            "name": nameUser,
            "idade": form["age"],
            "gênero": form["gender"],
            "pergunta_1": form["response_1"],
            "pergunta_2": form["response_2"],
            "pergunta_3": form["response_3"],
            "pergunta_4": form["response_4"],
            "pergunta_5": form["response_5"],
            "pergunta_6": form["response_6"],
            "data/hora": form["data/hora"]
        }
    ])

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





# Função criada para iniciar a aplicação
def Application(): 
    cache = {}
    finishLoop = False
    while not finishLoop:
        name = input("Informe qual e o seu nome:")
        age = input("Informe qual e a sua idade:")
        gender = input("Informe qual e o seu genero:")
        if not name in cache: 
            cache[name] = {
                'age': age,
                'gender': gender,
            }
        print("Caso deseje sair e somente digitar:0")
        for k,v in questions.items(): 
            os.system("cls")
            result = input(v)
            if result == '0': 
                finishLoop = True 
                os.system("cls")
                print("Programa finalizado!")
                break
            if k in questions.keys():
               cache[name][f"response_{int(k)}"] = result
        date = datetime.now()
        cache[name]["data/hora"] = f"{date.day}/{date.month}/{date.year}"
        print(cache)
        create_or_add_csv(cache[name],name)
    
Application()
            
