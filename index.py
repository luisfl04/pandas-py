import pandas as pd

#criando uma series:
series = pd.Series([1,2,5])

# Personalizando índices:
series2 = pd.Series([1,2,3], index= ["alfa", "loser", "perfect"])

# Criando um data frame:
carros = {"modelos": ["Siena", "Cronos", "Fastback"],
          "anos": ["2001", "2017", "2019"],
          "potência": [1.1 , 1.3, 1.4]}

dataframe = pd.DataFrame(carros)

# criando um dataframe para cidades e suas populações:
cidades = pd.Series(["Timon", "Teresina", "Angical do piauí", "Presidente dutra"])
estados = pd.Series( ["Maranão", "Piauí", "Piauí", "Maranhão"])
populacoes = pd.Series([100.34, 111, 11, 1])

togheter = pd.DataFrame({"cidades": cidades, "Estados": estados, "Polulação": populacoes})

# juntando as series "cidades"  e "populações" em m diicionario:
populacoes_cidades = dict(zip(cidades, populacoes))

# verificando:
"Timon" in populacoes_cidades

#Adicionado elementos:
populacoes_cidades["Caxias"] = 100.222

#deletando:
del populacoes_cidades["Timon"]

# criando um data frame e criando um arquivo csv para ele:

autor = ["luis felipe"]
livro = ["O homen que calculava"]
ano = 2023

infos_livro = {
    "Autor": autor,
    "Livro": livro,
    "Ano de lançamento": ano
}

meu_livro = pd.DataFrame(infos_livro)
meu_livro.to_csv("Meu.livro.csv")
# visualizando de outra forma:
meu_livro = pd.read_csv("Meu.livro.csv", index_col = 0)
# obtendo as informações do data frame:
meu_livro.info()
# retornando somente as colunas:
meu_livro.columns
#retornando somente as infos:
meu_livro.index
#retornando apenas infos gerais:
meu_livro.head()
# Sumarizando a tabela:
print(togheter.describe())


