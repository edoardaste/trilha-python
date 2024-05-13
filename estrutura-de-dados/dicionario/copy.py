contatos = {
    "stephanie@gmail.com": {"nome": "stephanie", "endereco": "um endereco qualquer n 30"},
}

contatos_copia = contatos.copy()

contatos["stephanie@gmail.com"]
contatos_copia["stephanie@gmail.com"]

#sobrescrevendo copy

contatos_copia["stephanie@gmail.com"] = {"nome": "ste"}
contatos_copia["stephanie@gmail.com"]