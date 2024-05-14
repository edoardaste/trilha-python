# args é definido com um asteristico é um dicionário, já kwargs definido com ** 

def exibir_texto(introducao, *args, **kwargs):
		texto = "\n".join(args) #pulando uma linha a cada elemento da lista, é separado por virgula e entr parenteses
		meta_dados = "\n".join([f"{chave.title()} : {valor}" for chave, valor in kwargs.items()])
		mensagem = f"{introducao}\n\n{texto}\n\n{meta_dados}"
		print(mensagem)


exibir_texto(
    "Prezado",
	"Espero que esta mensagem o encontre bem. Gostaria de agendar uma reunião para discutir o",
	"andamento do nosso projeto. Seguem os detalhes:",
	"Data: [Data da Reunião]",
	"Data: [Data da Reunião]",
	"Por favor, confirme sua disponibilidade e, se necessário, sugira uma data alternativa. Fico à",
	"disposição para esclarecer qualquer dúvida.",
	nome="Stephanie",
	local="cidade qualquer"
 )





