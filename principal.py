def getData():

    animal = input("Digite o animal a ser adicionado: ")
    idade = int(input("Qual a idade dele? "))
    condicao = int(input("Como está a saúde dele? \n[1]Bom \n[2]Em tratamento \n[3]Ruim \n"))

    if condicao == 1:
        saude = "Bom"
    elif condicao == 2:
        saude = "Em tratamento"
    elif condicao == 3:
        saude = "Ruim"

    result = [animal, idade, saude]

    return result



