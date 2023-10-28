import pandas as pd
from datetime import datetime
import os
from time import sleep

# Lista de perguntas
questions = {
    "1": '''No ano passado, um apresentador de um podcast famoso no Brasil defendeu que um partido nazista deveria ter
o direito de existir legalmente com base na liberdade de expressão. \033[4;30;45mVocê apoia a ideia de uma liberdade de expressão irrestrita?\033[m  ''',

    "2": '''No Rio de Janeiro, políticas de intervenção em comunidades têm gerado discussões. 
Algumas pessoas apoiam tais intervenções como necessárias para combater poderes paralelos ao Estado,
enquanto outros criticam devido ao alto número de mortes resultantes. \033[4;30;45mVocê acredita que a legalização das drogas
é uma solução para parte desses problemas?\033[m  ''',

    "3": '''No Brasil, estima-se que cerca de 800 mil mulheres pratiquem aborto por ano. Há quem defenda que
a legalização poderia diminuir o número de abortos, pois estaria sob o controle do Estado e reduziria o número de
mulheres mortas em clínicas clandestinas. Por outro lado, o argumento é que um feto é uma vida, e realizar o aborto seria
uma espécie de assassinato. \033[4;30;45mVocê é a favor da legalização do aborto?\033[m  ''',

    "4": '''Há quem acredite que os movimentos feministas em defesa dos direitos das mulheres em uma sociedade patriarcal
contribuíram para a melhoria da sociedade. Por outro lado, há quem afirme que o movimento feminista não conquistou
esses direitos, ou que apenas serve para criar uma guerra dos sexos. \033[4;30;45mVocê acredita que o feminismo é importante?\033[m  ''',

    "5": '''Nas últimas eleições, testemunhou-se um intenso confronto, especialmente no segundo turno. De um lado,
havia apoiadores da volta de Lula, que enfatizavam a necessidade do seu compromisso com o bem-estar das camadas
mais pobres do Brasil, enquanto criticavam Bolsonaro por sua abordagem na pandemia e sua postura perante o Poder Judiciário.
Já os defensores de Bolsonaro argumentavam que ele era fundamental para endireitar o país, preservando valores morais e
costumes conservadores. Além disso, expressavam preocupações sobre uma suposta agenda comunista de Lula e o fechamento de igrejas.
\033[4;30;45mVocê acredita que Lula é um governante melhor?\033[m  ''',

    "6": '''Recentemente, temos acompanhado o conflito entre Israel e as forças de resistência da Palestina, um embate que resultou
em perdas de vidas de ambos os lados. Os defensores da causa Palestina argumentam que o atual Estado de Israel, 
outrora território Palestino, foi adquirido através de meios violentos, forçando a expulsão dos habitantes locais para regiões mais 
reduzidas e economicamente menos prósperas. Eles também apontam que, estatisticamente, o conflito tem impactado mais fortemente a 
população Palestina, com um número maior de mortes do lado Palestino. Por outro lado, os apoiadores de Israel sustentam a crença de que
a terra pertence a eles, baseando-se na promessa divina registrada na Torah. Além disso, eles caracterizam os grupos paramilitares 
Palestinos como organizações terroristas e radicais islâmicos. Argumentam também que Israel deve ser mantido, pois representa
um compromisso com a democracia e o princípio de um Estado laico. \033[4;30;45mVocê crê que Israel tem razão nesse conflito?\033[m  ''',
}

class ArquiveController:
    def __init__(self):
        self.__arquive = 'politicsForm'

    def read_arquive(self):
        try:
            # Verifica se o arquivo CSV existe
            pd.read_csv(f"{self.__arquive}.csv", encoding="utf-8-sig")
            return True
        except FileNotFoundError as error:
            # Caso o arquivo não exista, retorna Falso
            return False

        return True

    def create_or_add_csv(self, form: dict):
        csv_exists = self.read_arquive()

        # Recebe o nome do arquivo a ser utilizado
        if csv_exists:
            confirm = input("\nDeseja mudar de arquivo? [S/N]\nR:  ").upper()
            if confirm == 'S':
                confirm = input("\nDigite o nome do arquivo: ")

                self.__arquive = confirm
        else:
            self.__arquive = input("\nDigite o nome do arquivo: ")

        # Cria um dataframe (Dados Tabulares) com os dados do formulário
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

        if csv_exists:
            # Adiciona os dados ao arquivo existente (modo 'a' de append)
            dataframe.to_csv(f"{self.__arquive}.csv", mode='a', index=False, header=False, encoding="utf-8-sig", sep=";")
        else:
            # Cria um novo arquivo com os dados (modo 'x' cria o arquivo se ele não existir)
            dataframe.to_csv(f"{self.__arquive}.csv", mode='x', index=False, header=True, encoding="utf-8-sig", sep=";")
        print(f"\n\033[32mEnvio realizado com sucesso!\033[0m")

class User:
    def __init__(self):
        self.exit = False  # Novo atributo para controlar a saída
        # Recebe os dados do usuário
        self.__age = int(input("\nInforme qual é a sua idade:\n(para sair digite 0) -->  "))
        if self.__age == 0:
            self.exit = True  # Define como True para sair
            return

        self.__gender = input("\nInforme qual é o seu gênero [Feminino/Masculino/Outros]: ").capitalize()
        if self.__gender == '0':  # Verifica se o usuário deseja sair após a entrada do gênero
            self.exit = True
            return

        self.__neighborhood = input("\nInforme seu Bairro: ").capitalize()
        if self.__neighborhood == '0':  # Verifica se o usuário deseja sair após a entrada do bairro
            self.exit = True
            return

    # Retorna os dados do usuário
    def get_age(self) -> int:
        return self.__age
    
    def get_gender(self) -> str:
        return self.__gender
    
    def get_neighborhood(self) -> str:
        return self.__neighborhood

class QuestionsController:
    def __init__(self, cache : dict, questions : dict, user : User):
        self.__cache = cache
        self.__questions = questions
        self.__user =  user

    # Retorna as questões do dicionário questions
    def get_questions(self) -> dict:
        return print(self.__questions.items())

    def get_user(self):
        return self.__user

    def send_response_to_cache(self):
        for key, value in self.__questions.items():
            os.system("cls")

            if self.__user.exit:  # Verifica se o usuário deseja sair
                return

            # Exibe as perguntas e armazena a resposta
            result = int(input(f"{value}\n\n[1] Sim [2] Não [3] Não sei responder\nR: "))

            if result == 0:  # Verifica se o usuário deseja sair
                self.__user.exit = True
                return

            # Converte as respostas
            if result == 1:
                result = "Sim"
            elif result == 2:
                result = "Não"
            elif result == 3:
                result = "Não sei responder"

            # Envia todas as respostas para o cache
            if key in self.__questions.keys():
                self.__cache[f"response_{int(key)}"] = result

        if not f"response_{int(key)}" in self.__cache:
            self.__cache[f"response_{int(key)}"] = result
            return True
        return False

def application():
    cache = {}
    user = User()

    # Verifica se o usuário deseja sair
    if user.exit:
        return

    # Envia os dados do usuário para o armazenamento no cache
    cache = {
        'age': user.get_age(),
        'gender': user.get_gender(),
        'neighborhood': user.get_neighborhood(),
    }

    questions_controller = QuestionsController(cache, questions, user)

    os.system("cls")
    print("\nPara as perguntas a seguir, \033[31mcaso deseje sair digite: 0\033[0m")
    sleep(2)
            
    # Faz as perguntas e envia as respostas das questões para o cache
    questions_controller.send_response_to_cache()

    if user.exit:  # Verifica se o usuário deseja sair novamente
        return

    # Recebe a data e hora do envio
    date = datetime.now().strftime('%d/%m/%Y %H:M')
    
    # Envia a data e hora para o dicionário
    cache["data/hora"] = str(date)

    # Inicia o controlador do arquivo e chama a função que cria o CSV
    arquive_controller = ArquiveController()
    arquive_controller.create_or_add_csv(cache)

application()
