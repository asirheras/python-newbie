SUFIJOS = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'], 1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def tamano_aproximado(tamano, un_kilobyte_es_1024_bytes=True):
    '''Convierte un tamaño de fichero en formato legible por personas
    
    Argumentos/parámetros:
    tamano -- tamaño de fichero en bytes
    un_kilobyte_es_1024_bytes -- si True (por defecto),
                                 usa múltiplo de 1024
                                 si False, usa múltiplos de 1000
    Retorna: string 
    '''
    if tamano < 0:
        raise ValueError('El número debe ser no negativo')
    
    multiplo = 1024 if un_kilobyte_es_1024_bytes else 1000
    for sufijo in SUFIJOS[multiplo]:
        tamano /= multiplo
        if tamano < multiplo:
            return '{0:.1f} {1}'.format(tamano, sufijo)
    
    raise ValueError('Número demasiado grande')

if __name__ == '__main__':
    print(tamano_aproximado(1000000000000, False))
    print(tamano_aproximado(1000000000000))
