paises_originais = {
    "brasil": "Brasília",
    "argentina": "Buenos Aires",
    "chile": "Santiago",
    "estados Unidos": "Washington, D.C.",
    "canadá": "Ottawa",
    "méxico": "Cidade do México",
    "japão": "Tóquio",
    "china": "Pequim",
    "alemanha": "Berlim",
    "frança": "Paris"
}

pais_solicitado = input('Informe um país para ver sua respectiva capital: ').lower().strip()


print(paises_originais.get(pais_solicitado, 'Esse país nao está no dicionário'))
