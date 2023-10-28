import pandas as pd
from datetime import datetime
import os
from time import sleep

# Lista de perguntas
questions = {
    "1": '''No ano passado, um apresentador de um podcast famoso no Brasil defendeu que um partido nazista deveria ter
        o direito de existir legalmente com base na liberdade de expressão. Você apoia a ideia de uma liberdade de expressão irrestrita?  ''',

    "2": '''No Rio de Janeiro, já há um bom tempo, possuímos uma política de intervenção político-militar nas comunidades.
        Tais intervenções e operações têm sido alvo de crítica por alguns, devido ao alto número de mortes, e apoiadas por outros, 
        devido à necessidade de combater poderes paralelos ao Estado. Você é a favor da legalização das drogas?  ''',

    "3": '''No Brasil, estima-se que cerca de 800 mil mulheres pratiquem aborto por ano. Há quem defenda que a legalização poderia
        diminuir o número de abortos, pois estaria sob o controle do Estado e reduziria o número de mulheres mortas em clínicas
        clandestinas. Por outro lado, o argumento é que um feto é uma vida, e realizar o aborto seria uma espécie de assassinato. 
        Você é a favor da legalização do aborto?  ''',

    "4": '''Que durante a história o papel da mulher tem modificado ao longo do tempo, quase ninguém discorda. Há quem acredite que
        os movimentos feministas em defesa dos direitos das mulheres em uma sociedade patriarcal contribuíram para a melhoria da sociedade.
        Por outro lado, há quem afirme que o movimento feminista não conquistou esses direitos, ou que apenas serve para criar uma guerra
        dos sexos. Você acredita que o feminismo é importante?  ''',

    "5": '''Nas últimas eleições, testemunhou-se um intenso confronto, especialmente no segundo turno. De um lado, havia apoiadores da volta
        de Lula, que enfatizavam a necessidade do seu compromisso com o bem-estar das camadas mais pobres do Brasil, enquanto criticavam Bolsonaro
        por sua abordagem na pandemia e sua postura perante o Poder Judiciário. Já os defensores de Bolsonaro argumentavam que ele era fundamental
        para endireitar o país, preservando valores morais e costumes conservadores. Além disso, expressavam preocupações sobre uma suposta
        agenda comunista de Lula e o fechamento de igrejas. Você acredita que Lula é um governante melhor?  ''',

    "6": '''Recentemente, temos acompanhado o conflito entre Israel e as forças de resistência da Palestina, um embate que resultou em perdas
        de vidas de ambos os lados. Os defensores da causa Palestina argumentam que o atual Estado de Israel, outrora território Palestino, foi adquirido
        através de meios violentos, forçando a expulsão dos habitantes locais para regiões mais reduzidas e economicamente menos prósperas.
        Eles também apontam que, estatisticamente, o conflito tem impactado mais fortemente a população Palestina, com um número maior de mortes do lado Palestino.
        Por outro lado, os apoiadores de Israel sustentam a crença de que a terra pertence a eles, baseando-se na promessa divina registrada na Torah.
        Além disso, eles caracterizam os grupos paramilitares Palestinos como organizações terroristas e radicais islâmicos. 
        Argumentam também que Israel deve ser mantido, pois representa um compromisso com a democracia e o princípio de um Estado laico. 
        Você crê que Israel tem razão nesse conflito?  ''',
}


class ArquiveController():
    def __init__(self):
        self.__arquive = 'politicsForm'

    def readArquive(self):
        try:
            # Verifica se o arquivo existe
            pd.read_csv(f"{self.__arquive}.csv", encoding="utf-8-sig")
            return True
        except FileNotFoundError as error:
            # Caso o arquivo não exista retornar Falso
            return False

        return True

    def create_or_add_csv(self, form: dict):
        csvExists = self.readArquive()

        # Recebe o nome do arquivo a ser utilizado
        if csvExists:
            confirm = input("\nDeseja mudar de arquivo? [S/N]\nR:  ").upper()
            if confirm == 'S':
                confirm = input("\nDigite o nome do arquivo: ")

                self.__arquive = confirm
        else:
            self.__arquive = input("\nDigite o nome do arquivo: ")

        # Cria um dataframe (Dados Tabulares) do formulário
        dataframe = pd.DataFrame([
            {
                "idade": form["age"],
                "gênero": form["gender"],
                "Bairro": form["neighborhood"],
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
            dataframe.to_csv(f"{self.__arquive}.csv", mode='a', index=False, header=False, encoding="utf-8-sig", sep=";")
        else:
            # Cria um arquivo enviando os dados.
            # O mode='x' cria o arquivo caso ele não exista
            dataframe.to_csv(f"{self.__arquive}.csv", mode='x', index=False, header=True, encoding="utf-8-sig", sep=";")
        print(f"\n\033[32mEnvio realizado com sucesso!\033[0m")


# Função criada para iniciar a aplicação

class User():
    def __init__(self):
        # Recebe os dados do usuário
        self.__age = int(input("\nInforme qual é a sua idade:\n(para sair digite 0) -->  "))

        if self.__age == 0:
            return
        
        self.__gender = input("\nInforme qual é o seu genero [Feminino/Masculino/Outros]: ").capitalize()
        self.__neighborhood = input("\nInforme seu Bairro: ").capitalize()

    # Retorna os dados dos usuário
    def get_age(self) -> int :
        return self.__age
    
    def get_gender(self) -> str :
        return self.__gender
    
    def get_neighborhood(self) -> str :
        return self.__neighborhood


# Classe que controla as questões
class QuestionsController():
    def __init__(self, cache : dict, questions : dict, user : User ):
        self.__cache = cache
        self.__questions = questions
        self.__user =  user

    #Retorna as questão do dicionário questions
    def get_questions(self) -> dict:
        return print(self.__questions.items())

    def get_user(self):
        return self.__user


    def send_response_to_cache(self):
        for key, value in self.__questions.items():
            os.system("cls")

            #Exibi as perguntas e armazena a resposta
            result = int(input(f"{value}\n\n[1] Sim [2] Não [3] Não sei responder\nR: "))

            #Faz a conversão das respostas
            if result == 1:
                result = "Sim"
            elif result == 2:
                result = "Não"
            elif result == 3:
                result = "Não sei responder"

            #Envia todas as respostas para o cache
            if key in self.__questions.keys():
                self.__cache[f"response_{int(key)}"] = result

        if not f"response_{int(key)}" in self.__cache:
            self.__cache[f"response_{int(key)}"] = result
            return True
        return False
    

def Application():
    cache = {}
    user = User()

    #Envia os dados do usuário para o armazenamento cache
    cache = {
        'age': user.get_age(),
        'gender': user.get_gender(),
        'neighborhood': user.get_neighborhood(),
    }
    

    questions_Controller = QuestionsController(cache, questions, user)

    os.system("cls")
    print("\nPara as perguntas a seguir, \033[31mcaso deseje sair digite: 0\033[0m")
    sleep(3)
            
    #Faz as perguntas e envia as respostas das questões para o cache
    questions_Controller.send_response_to_cache()

    #Recebe a data e horário do envio
    date = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    #Envia a data e hora para o dicionário
    cache["data/hora"] = str(date)

    #Inicia o controlador do arquivo e chama a função que cria o CSV
    arquiveController = ArquiveController()
    arquiveController.create_or_add_csv(cache)


Application()
