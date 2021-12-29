DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

from functools import reduce
def run():
    # Uso de list comprehesions
    #all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    #all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    #High order function Filter usando funcion anonima lambda
    ##adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #Sobreescribe la linea anterior para recolectar solo los nombres con map
    ##adults = list(map(lambda worker: worker["name"], adults))
    #Se Agrega al diccionario worker los valores de True o False si son mayores a 70
    # |: operador para sumar diccionarios
    ##old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    #Reto 1 usando filter y map de los trabajadores que saben python
    all_python_devs = list(filter(lambda worker: worker["language"] == "python",DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    #Reto 2 usando list comprehesions
    old_people = [worker["name"] for worker in DATA if worker["age"] > 70]
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]


    #Ciclo para imprimir alguna de las variables anteriores
    for worker in adults:
        print(worker)

if __name__ == '__main__':
    run()