# remove valores

contatos = {
    "stephanie@gmail.com": {"nome": "stephanie", "endereco": "um endereco qualquer n 30"},
    "joaquim@gmail.com": {"nome": "joaquim", "endereco": "um endereco qualquer n 40"},
    "luca@gmail.com": {"nome": "luca", "endereco": "um endereco qualquer n 20"},
    "joao@gmail.com": {"nome": "joao", "endereco": "um endereco qualquer n 50"},
}

resultado = contatos.pop("stephanie@gmail.com")

print(resultado)

resultado = contatos.pop("stephanie@gmail.com", "não encontrou") # caso o elemento não exista no dicionário, podemos colocar um valor padrão de mensagem no pop

print(resultado)