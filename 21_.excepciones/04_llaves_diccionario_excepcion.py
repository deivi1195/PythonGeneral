# Excepciones a la hora de trabajar con diccionarios

versiones = {
    'Python': '3.8.1',
    'Java': '12',
    'JavaScript': 'ES6',
    'C#': '8'
}

lenguajes = input('Escriba un nombre de lenguaje de programacion: ')

try:
    version = versiones[lenguajes]

    print(f'La version de {lenguajes} es {version}')
except KeyError as e:
    print(f'ERROR: {e}')

print("Fin del Programa.")

# Uso del metodo get()

version = versiones.get('java', '1.0.0')
print(f'La version de {lenguajes} es {version}')



