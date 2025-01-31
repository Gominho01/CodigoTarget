#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(texto):
    invertida = ""
    for char in texto:
        invertida = char + invertida
    return invertida

texto = input("Digite uma string para inverter (ou pressione Enter para usar um valor padrão): ")
if not texto:
    texto = "Exemplo" #Previamente definida no código

print("String invertida:", inverter_string(texto))
