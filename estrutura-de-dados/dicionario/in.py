# verifica se um elemento é pertencente ao o dicionario

contatos = {
    "stephanie@gmail.com": {"nome": "stephanie", "endereco": "um endereco qualquer n 30"},
    "joaquim@gmail.com": {"nome": "joaquim", "endereco": "um endereco qualquer n 40"},
    "luca@gmail.com": {"nome": "luca", "endereco": "um endereco qualquer n 20"},
    "joao@gmail.com": {"nome": "joao", "endereco": "um endereco qualquer n 50"},
}

resultado = "luca@gmail.com" in contatos
print(resultado)

resultado = "nome" in contatos["joaquim@gmail.com"]
print(resultado)

