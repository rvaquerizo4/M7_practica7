import json

# Creacion de la variable a imprimir
libros = {
    "book": [
        {
            "title": "Pepe",
            "cover": "lsdmfd",
            "year": "32",
            "pages": "213"
        },
        {
            "title": "Pepo",
            "cover": "dsfd",
            "year": "23",
            "pages": "400"
        },
        {
            "title": "Popi",
            "cover": "kddfgdf",
            "year": "45",
            "pages": "330"
        },
        {
            "title": "Pipo",
            "cover": "kdnf",
            "year": "40",
            "pages": "300"
        }
    ]
}


# Funcion para crear un archivo externo
def book():
    # lectura de la variable anterior
    with open('libros', 'w') as file:
        json.dump(libros, file)
    # creacion del archivo
    with open("libros", 'r') as archivo:
        result = json.load(archivo)
        print(result)


def beatybook():
    with open('libros', 'w') as file:
        json.dump(libros, file)


print(book())
print(libros())
