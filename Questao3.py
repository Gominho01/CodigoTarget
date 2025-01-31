import json

# Simulação do JSON com faturamento diário
dados = {
    "faturamento": [0, 1500, 2000, 2500, 1800, 0, 2200, 3000, 0, 1700, 2800, 3100, 0, 0, 2600, 1900, 0]
}

# Filtra os dias com faturamento
faturamento = [v for v in dados["faturamento"] if v > 0]

menor = min(faturamento)
maior = max(faturamento)
media = sum(faturamento) / len(faturamento)
dias_acima_media = sum(1 for v in faturamento if v > media)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
