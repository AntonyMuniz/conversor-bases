def decimal_para_hexadecimal(numero):
    if numero == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"
    resultado = ""
    
    while numero > 0:
        resto = numero % 16
        resultado = hex_chars[resto] + resultado
        numero = numero // 16
    
    return resultado

num = int(input("Digite um número decimal: "))
hexadecimal = decimal_para_hexadecimal(num)
print(f"O número {num} em hexadecimal é: {hexadecimal}")
