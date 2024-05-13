# altera valores do dicionário

contatos = {
    "stephanie@gmail.com": {"nome": "stephanie", "endereco": "um endereco qualquer n 30"},
}

sobrescreve = contatos.update({"stephanie@gmai.com": {"nome": "ste"}}) # se der update em um registro existente ele sobrescreve

print(sobrescreve)

insere = contatos.update({"joao@gmail.com": {"nome": "joao"}}) # se inserir uma chave diferente ele atualiza o dicionario

print(insere)
