def float_para_ieee754(numero_str):
    numero = float(numero_str)

    # representacao do bit de sinal
    sinal = 0 if numero >= 0 else 1
    if sinal == 1:
        numero = -numero
    
    # representacao hexadecimal do float
    representacao_hex = numero.hex()
    
    split_hex = representacao_hex.split('p')
    mantissa_hex = split_hex[0].replace('0x1.', '')
    # expoente + excesso de 127
    expoente = int(split_hex[1]) + 127
    
    # conversao da mantissa para binario
    mantissa_binaria = ''.join(f'{int(c, 16):04b}' for c in mantissa_hex)
    
    # garantir mantissa com 23 bits
    mantissa_binaria = mantissa_binaria[:23].ljust(23, '0')
    
    # representacao binaria
    expoente_binario = f'{expoente:08b}'
    bits = f'{sinal}{expoente_binario}{mantissa_binaria}'
    
    # representacao hexadecimal
    representacao_hex = hex(int(bits, 2))[2:].upper().zfill(8)
    
    return bits, representacao_hex
