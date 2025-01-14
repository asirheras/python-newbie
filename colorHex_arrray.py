# La función traductor_color recibe el nombre de un color y la función imprime su valor en hexadecimal. 
# La función solo soporta los 3 colores primarios (rojo, verde y azul) y retorna desconocido ("unknown") 
# para el resto de colores.
# Este es una versión del ejercicio anterior pero usando arrays

def traductor_color(color):
    colores = {
        "rojo": "#FF0000",
        "verde": "#00FF00",
        "azul": "#0000FF"
    }
    return colores.get(color.lower(), "unknown")

# Ejemplos de uso:
#Colores primarios
print(traductor_color("rojo"))   # Output: '#FF0000'
print(traductor_color("verde"))  # Output: '#00FF00'
print(traductor_color("azul"))   # Output: '#0000FF'
#colores desconocidos
print(traductor_color("amarillo"))  # Output: 'unknown'