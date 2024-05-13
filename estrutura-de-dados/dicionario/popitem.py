# remove valores na ordem e não permite setar mensagem caso nao exista o elemento


contatos = {
    "stephanie@gmail.com": {"nome": "stephanie", "endereco": "um endereco qualquer n 30"},
    "joaquim@gmail.com": {"nome": "joaquim", "endereco": "um endereco qualquer n 40"},
    "luca@gmail.com": {"nome": "luca", "endereco": "um endereco qualquer n 20"},
    "joao@gmail.com": {"nome": "joao", "endereco": "um endereco qualquer n 50"},
}

resultado = contatos.popitem()

print(resultado)

resultado = contatos.popitem() 
print(resultado)