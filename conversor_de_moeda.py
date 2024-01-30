def conversor(valor):
    if not type(valor) == float:
        float(valor)
        
    str_valor = f'R$ {valor:_.2f}'
    str_valor = str_valor.replace('.',',').replace('_','.')
    
    return str_valor

