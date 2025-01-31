def inverter_string(texto):
    invertida = ""
    for char in texto:
        invertida = char + invertida
    return invertida

texto = input("Digite uma string para inverter (ou pressione Enter para usar um valor padrão): ")
if not texto:
    texto = "Exemplo"

print("String invertida:", inverter_string(texto))
