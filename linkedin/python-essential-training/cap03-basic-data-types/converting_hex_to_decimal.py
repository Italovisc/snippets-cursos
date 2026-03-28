# Lista contendo números e letras hexadecimais
hex_numbers = {
    '0': 0, 
    '1': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9,
    'A': 10, 
    'B': 11, 
    'C': 12, 
    'D': 13, 
    'E': 14, 
    'F': 15
}

# Converte uma string representando um valor hexadecimal em int do resultado
def hex_to_dec(hex_num):
    # Padronização dos inputs
    hex_num = hex_num.upper()

    # Código que checa se o input é válido
    for s in hex_num:
        if s not in hex_numbers.keys():
            return None
        
    # Realização do cálculo
    total = 0
    hex_num_inverted = hex_num[::-1]

    for i, char in enumerate(hex_num_inverted):
        num = hex_numbers[char]
        total += num * (16 ** i)

    return total
