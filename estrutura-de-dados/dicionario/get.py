contatos = {
    "stephanie@gmail.com": {"nome": "stephanie", "endereco": "um endereco qualquer n 30"},
}


resultado = contatos.get("stephanie@gmail.com", {})

resultado2 = contatos.get("stephanie@gmail.com", {"nome"})

print(resultado)


print(resultado2)