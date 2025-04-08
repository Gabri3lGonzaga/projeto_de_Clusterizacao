import pandas as pd
import random

# Gêneros possíveis de livros
generos = ['Ficção', 'Não-ficção', 'Romance', 'Fantasia', 'Mistério', 'Biografia', 'História', 'Ciência']

# Sexos possíveis
sexos = ['Masculino', 'Feminino', 'Outro']

# Gerar dados fictícios para 100 registros
data = []
for _ in range(100):
    idade = random.randint(10, 80)  # Idade do leitor
    genero_livro = random.choice(generos)
    qtd_paginas = random.randint(50, 1000)  # Quantidade de páginas do livro
    sexo = random.choice(sexos)
    data.append([idade, genero_livro, qtd_paginas, sexo])

# Criar DataFrame
df = pd.DataFrame(data, columns=['Idade', 'Gênero do Livro', 'Quantidade de Páginas', 'Sexo'])

# Salvar como CSV
file_path = '/mnt/data/livros_clusterizacao.csv'
df.to_csv(file_path, index=False)

file_path
