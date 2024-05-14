def chama_nome():
    print("Hello stranger!")
    

def chama_nome_com_parametro(nome):
    print(f"Hello {nome}")
    
    
def chama_nome_com_parametro_e_valor_default(nome = "Stranger"):
    print(f"Hello {nome}")
    
chama_nome()
chama_nome_com_parametro(nome="ste")
chama_nome_com_parametro_e_valor_default(nome="joaquim")
chama_nome_com_parametro_e_valor_default()
    
