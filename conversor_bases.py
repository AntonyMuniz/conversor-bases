def binario_para_decimal(bin_str, mostrar_passos=False):
    decimal = 0
    potencia = 0
    if mostrar_passos:
        print("Convertendo binário para decimal passo a passo:")
    for digito in reversed(bin_str):
        valor = int(digito)
        decimal += valor * (2 ** potencia)
        if mostrar_passos:
            print(f"{valor} * 2^{potencia} = {valor * (2 ** potencia)}")
        potencia += 1
    if mostrar_passos:
        print(f"Resultado decimal: {decimal}")
    return decimal

def decimal_para_binario(numero, mostrar_passos=False):
    if numero == 0:
        if mostrar_passos:
            print("Número é 0, binário é 0.")
        return "0"
    resultado = ""
    if mostrar_passos:
        print("Convertendo decimal para binário passo a passo:")
    n = numero
    while n > 0:
        resto = n % 2
        resultado = str(resto) + resultado
        if mostrar_passos:
            print(f"{n} / 2, resto = {resto}")
        n //= 2
    if mostrar_passos:
        print(f"Resultado binário: {resultado}")
    return resultado

def hexadecimal_para_decimal(hex_str, mostrar_passos=False):
    hex_str = hex_str.upper()
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    if mostrar_passos:
        print("Convertendo hexadecimal para decimal passo a passo:")
    potencia = 0
    for digito in reversed(hex_str):
        valor = hex_chars.index(digito)
        decimal += valor * (16 ** potencia)
        if mostrar_passos:
            print(f"{digito} ({valor}) * 16^{potencia} = {valor * (16 ** potencia)}")
        potencia += 1
    if mostrar_passos:
        print(f"Resultado decimal: {decimal}")
    return decimal

def decimal_para_hexadecimal(numero, mostrar_passos=False):
    if numero == 0:
        if mostrar_passos:
            print("Número é 0, hexadecimal é 0.")
        return "0"
    hex_chars = "0123456789ABCDEF"
    resultado = ""
    n = numero
    if mostrar_passos:
        print("Convertendo decimal para hexadecimal passo a passo:")
    while n > 0:
        resto = n % 16
        resultado = hex_chars[resto] + resultado
        if mostrar_passos:
            print(f"{n} / 16, resto = {hex_chars[resto]}")
        n //= 16
    if mostrar_passos:
        print(f"Resultado hexadecimal: {resultado}")
    return resultado

def validar_numero(numero, sistema):
    sistema = sistema.lower()
    if sistema == "binario":
        return all(c in "01" for c in numero)
    elif sistema == "decimal":
        return numero.isdigit()
    elif sistema == "hexadecimal":
        valid_chars = "0123456789abcdefABCDEF"
        return all(c in valid_chars for c in numero)
    else:
        return False

def converter(numero, origem, destino, mostrar_passos=False):
    origem = origem.lower()
    destino = destino.lower()
    
    if origem == "binario":
        decimal = binario_para_decimal(numero, mostrar_passos)
    elif origem == "decimal":
        decimal = int(numero)
    elif origem == "hexadecimal":
        decimal = hexadecimal_para_decimal(numero, mostrar_passos)
    else:
        raise ValueError("Sistema de origem inválido.")
    
    if destino == "binario":
        return decimal_para_binario(decimal, mostrar_passos)
    elif destino == "decimal":
        if mostrar_passos:
            print(f"Decimal final: {decimal}")
        return str(decimal)
    elif destino == "hexadecimal":
        return decimal_para_hexadecimal(decimal, mostrar_passos)
    else:
        raise ValueError("Sistema de destino inválido.")

def escolher_sistema(mensagem):
    sistemas_validos = {
        "1": "binario",
        "2": "decimal",
        "3": "hexadecimal",
        "bin": "binario",
        "dec": "decimal",
        "hex": "hexadecimal"
    }
    while True:
        escolha = input(mensagem).strip().lower()
        if escolha in sistemas_validos:
            return sistemas_validos[escolha]
        else:
            print("Escolha inválida. Use 1, 2, 3 ou bin, dec, hex.")

def main():
    print("=== Conversor de Bases Numéricas ===")
    print("Sistemas disponíveis:\n1 - Binário (bin)\n2 - Decimal (dec)\n3 - Hexadecimal (hex)")
    while True:
        origem = escolher_sistema("Escolha o sistema de origem (1/2/3 ou bin/dec/hex): ")
        destino = escolher_sistema("Escolha o sistema de destino (1/2/3 ou bin/dec/hex): ")
        if origem == destino:
            print("Sistema de origem e destino são iguais. Escolha sistemas diferentes.\n")
            continue
        
        numero = input(f"Digite o número em {origem}: ").strip()
        if not validar_numero(numero, origem):
            print(f"Número inválido para o sistema {origem}. Tente novamente.\n")
            continue
        
        mostrar = input("Quer ver o passo a passo da conversão? (s/n): ").strip().lower()
        mostrar_passos = mostrar == 's'
        
        try:
            resultado = converter(numero, origem, destino, mostrar_passos)
            print(f"\nNúmero {numero} ({origem}) convertido para {destino} é: {resultado}\n")
        except Exception as e:
            print(f"Erro na conversão: {e}")
            continue
        
        repetir = input("Quer fazer outra conversão? (s/n): ").strip().lower()
        if repetir != 's':
            print("Encerrando programa. Até mais!")
            break

if __name__ == "__main__":
    main()
