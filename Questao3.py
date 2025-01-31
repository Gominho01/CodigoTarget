#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# O menor valor de faturamento ocorrido em um dia do mês;
# O maior valor de faturamento ocorrido em um dia do mês;
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Simulação do JSON com faturamento diário(Se tinha algum disponivel no teste, eu não encontrei)
dados = {
    "faturamento": [0, 1500, 2000, 2500, 1800, 0, 2200, 3000, 0, 1700, 2800, 3100, 0, 0, 2600, 1900, 0]
}

# Filtrando os dias com faturamento e ignorando os sem faturamento
faturamento = [v for v in dados["faturamento"] if v > 0]

menor = min(faturamento)
maior = max(faturamento)
media = sum(faturamento) / len(faturamento)
dias_acima_media = sum(1 for v in faturamento if v > media)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
