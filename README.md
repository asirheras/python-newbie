# Ejercicios que realizo en los cursos de Python
# 1. Hola mundo!   
   
¿Cómo imprimir en pantalla?   
````python
print("Hello, World!")
````   

**Funciones**: Son bloques de código que realizan una tarea específica. En este caso, la función print() se utiliza para mostrar texto en la pantalla.   
**Palabras clave**: Son palabras reservadas que tienen un significado especial en Python. En este caso, la palabra clave print se utiliza para llamar a la función print().  
**Cadenas**: Son secuencias de caracteres que se utilizan para representar texto. En este caso, la cadena "Hola mundo" se muestra en la pantalla.

# Introducción de información en un progrma de Python

Hay varias formas en las que se puede proporcionar información a un programa en Python. Las más comunes son:

**Entrada por teclado**: Esta es la forma más básica de proporcionar información a un programa. Se utiliza la función `input()` para leer los datos que el usuario ingresa por el teclado. Por ejemplo:
```` python
nombre = input("Ingresa tu nombre: ")
print("Hola,", nombre)
````
**Archivos**: Se pueden leer datos de archivos utilizando la función open(). Esta función abre un archivo y devuelve un objeto de archivo que se puede utilizar para leer los datos del archivo. Por ejemplo:
```python
with open("datos.txt", "r") as archivo:
    datos = archivo.read()
    print(datos)
```

**Argumentos de línea de comandos**: Se pueden pasar argumentos al programa cuando se ejecuta desde la línea de comandos. Estos argumentos se pueden acceder utilizando la variable `sys.argv`. Por ejemplo:

```python
import sys
nombre = sys.argv[1]
edad = sys.argv[2]
```

print("Hola,", nombre, "de", edad, "años")

**Entrada estándar**: La entrada estándar es un flujo de datos que se puede utilizar para proporcionar información a un programa. Se puede acceder a la entrada estándar utilizando la función `sys.stdin`. Por ejemplo:

```python
import sys
datos = sys.stdin.read()
print(datos)
```

**Salida estándar**: La salida estándar es un flujo de datos que se utiliza para mostrar información al usuario. Se puede acceder a la salida estándar utilizando la función print(). Por ejemplo:

`print("Hola, mundo")`

**Interfaces gráficas de usuario (GUIs)**: Se pueden utilizar GUIs para proporcionar información a un programa a través de elementos como botones, menús y cuadros de texto. Las GUIs se crean utilizando bibliotecas como _Tkinter_ o _PyQt_.

**APIs**: Se pueden utilizar APIs para obtener información de fuentes externas, como bases de datos o servicios web. Las APIs se acceden utilizando bibliotecas específicas para cada API.