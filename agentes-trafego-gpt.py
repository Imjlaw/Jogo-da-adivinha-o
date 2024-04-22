import crew

# Carregar o conjunto de dados
data = [
    "Campanha 1: Cliques - 100, Conversões - 10, Custo - $50",
    "Campanha 2: Cliques - 120, Conversões - 15, Custo - $60",
    "Campanha 3: Cliques - 80, Conversões - 8, Custo - $40",
]

# Inicializar e configurar o modelo GPT
model = crew.load_model("gpt3", "standard")

# Fazer uma análise de campanha usando o modelo treinado
campaign_analysis = model.generate("Analisar o desempenho da campanha")
print('Análise da Campanha:', campaign_analysis)

# Gerar texto para um novo anúncio
new_ad_text = model.generate("Gerar texto para anúncio")
print('Novo texto de anúncio:', new_ad_text)

# Otimizar uma estratégia de anúncios
optimization_strategy = model.generate("Otimizar estratégia de anúncios")
print("Estratégia de Otimização:", optimization_strategy)