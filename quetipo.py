# Nombre: 
# Fecha:
# Descripción
# # como saber que tipo es una variable usamos el comando TYPE
def determinar_tipo_dato(dato):
    try:
        valor = eval(dato)
    except (NameError, SyntaxError):
        valor = dato

    tipo = type(valor)
    
    if tipo == int:
        return "entero (int)"
    elif tipo == float:
        return "decimal (float)"
    elif tipo == bool:
        return "booleano (bool)"
    elif tipo == str:
        return "cadena de texto (str)"
    else:
        return f"otro tipo ({tipo})"

# Solicitar al usuario que ingrese un dato
dato = input("Por favor, ingresa un dato: ")

# Determinar y mostrar el tipo de dato
tipo_dato = determinar_tipo_dato(dato)
print(f"El dato ingresado es de tipo: {tipo_dato}")
