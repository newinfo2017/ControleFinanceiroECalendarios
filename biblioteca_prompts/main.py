from prompts.scripts import adicionar_prompt, visualizar_prompts, buscar_prompts, atualizar_prompt, fechar_conexao

# Exemplo: Adicionar um novo prompt
adicionar_prompt(
    titulo="Cliente ficou satisfeito com o produto",
    categoria="Atendimento",
    nivel_complexidade="Básico",
    descricao="Prompt para resumir atendimento ao cliente satisfeito com o produto",
    texto_prompt="O cliente disse que ficou muito satisfeito com o produto, pois atendeu as suas necessidades.",
    tags="resumo, atendimento, cliente",
    exemplo_uso="Atendimento resolvido com sucesso, cliente satisfeito."
)

# Exemplo: Visualizar todos os prompts
visualizar_prompts()

# Exemplo: Buscar por palavra-chave
buscar_prompts("Atendimento")

# Exemplo: Atualizar um prompt
atualizar_prompt(1, "Novo texto do prompt atualizado")

# Fechar a conexão com o banco de dados ao final do programa
fechar_conexao()
