![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)

# PoliForm

PoliForm é uma iniciativa que opera com formulários em Python, 
com o objetivo de obter dados sobre assuntos políticos e controversos
de cidadãos. Seu propósito é promover a aprendizagem e a investigação,
buscando compreender mais a fundo as opiniões e visões de indivíduos
em temas conflitantes.

## Status do projeto
— Em andamento

### Checklist do Projeto

- [ ] Ter todo o código comentado.
- [X] Implementar a lógica para sair do loop quando a idade for digitada como 0.
- [X] Passar a data e a hora para o arquivo CSV formatada como `strftime("%Y-%m-%d %H:%M")`.
- [ ] Adicionar as opções nas questões, como `[1] Sim [2] Não [3] Não sei responder]`, com números ou sem.
- [X] Processo de envios CSV deve ser formatado corretamente ao abrir excel.
    - [X] Utilizar a codificação UTF-8 no envio para o CSV para permitir a inclusão de acentos e caracteres especiais, exemplo "ç".
    - [X] Garantir que os dados estejam em celulás separadas
- [ ] Adicionar uma coluna chamada ou Local, ou Bairro no Data Frame.
- [ ] Adicionar input para receber o Local/Bairro
- [ ] Renomear as variáveis, funções para seguir o estilo snake_case.
- [ ] Implementar a estilização (opcional) com cores e etc, para embelezar o projeto.

## Recursos

```python
     language_used = "Python"
     description = f"Projeto feito com {language_used}"
```

- Coleta de informações pessoais, como nome, idade, gênero e localidade.
Armazenamento somente para questão de controle, seus dados estão protegidos.
- Perguntas sobre tópicos políticos e polêmicos:
  - Liberdade de expressão
  - Legalização do aborto
  - Legalização das drogas
  - Política
  - E outros tópicos controversos.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.x
- Biblioteca para criação de formulários (insira o nome da biblioteca, se aplicável)
- Outras dependências (caso existam)

## Como Usar

1. Clone este repositório em sua máquina local:

```git clone https://github.com/IsabelaAthayde/politics-group2-mod2.git```

2. Navegue até o diretório do projeto:

```cd politics-group2-mod2```

3. Execute o programa Python para iniciar o formulário:

```python dataFrame.py```


4. O formulário será iniciado, permitindo que os participantes respondam às perguntas.

5. Após a coleta de dados, caso deseje manter o padrão, para o nome do arquivo digite: politicsForm

6. Pronto! Os resultados serão exportados para análise em arquivo csv.

## Ética e Privacidade

A coleta de informações sobre tópicos polêmicos deve ser realizada com sensibilidade e respeito. Siga as regulamentações de privacidade e obtenha o consentimento adequado dos participantes, se necessário.

# 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/arthurgosi">
        <img src="https://avatars.githubusercontent.com/u/86735609?v=4" width="100px;" alt="Foto do Arthur Gosi Santos"/><br>
        <sub>
          <b>Arthur Santos</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/IsabelaAthayde">
        <img src="https://avatars.githubusercontent.com/u/100873483?v=4" width="100px;" alt="Foto da Isabela Athayde"/><br>
        <sub>
          <b>Isabela Athayde</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <!-- <a href="https://github.com/samarabm_s">
         <img src="" width="100px;" alt="Foto da Samara Barbosa"/><br> -->
        <sub>
          <b>Samara Barbosa</b>
        </sub>
      </a>
    </td>
  <td align="center">
      <!-- <a href="https://github.com/samuelgalvao">
        <img src="" width="100px;" alt="Foto do Samuel Galvão"/><br> -->
        <sub>
          <b>Samuel Galvão</b>
        </sub>
      </a>
    </td>
  <td align="center">
      <!-- <a href="https://github.com/handdsonamorim">
        <img src="" width="100px;" alt="Foto do Handdson Amorim"/><br> -->
        <sub>
          <b>Handdson Amorim</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## Contribuições

Se você desejar contribuir para o projeto, sinta-se à vontade para fazer um fork do repositório e enviar um pull request com melhorias ou correções.

## Licença

Este projeto é licenciado sob a licença [--].

