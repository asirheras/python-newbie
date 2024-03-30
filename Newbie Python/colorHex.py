# La función traductor de color recibe el nombre de un color y la función imprime su valor en hexadecimal. La función solo soporta los 3 colores primarios (rojo, verde y azul) y retorna desconocido ("unknown") para el resto de colores.
def traductor_color(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color

print(traductor_color("red"))  # Output: '#ff0000'
print(traductor_color("green"))  # Output: '#00ff00'
print(traductor_color("blue"))  # Output: '#0000ff'
#colores desconocidos
print(traductor_color("black"))  # Output: 'unknown'
print(traductor_color("white")) # Output: 'unknown'
