import random
import os

def read():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        datos = [line.strip('\n') for line in f]
    datos = {key:value for key, value in enumerate(datos)}
    return datos

def normalize(word):
    replace_let = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),("\n", ""))
    for a,b in replace_let:
        #Remplaza las vovales con acento a sin acento
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word

def hangman(word):
    word_to_guess = len(word)*"_"
    os.system("cls")
    intentos = 7
    while word_to_guess != word:
        print("Intentos restantes: ", intentos)
        print("¡¡Adivina la palabra!!")
        for i in range(len(word)):
            print(word_to_guess[i].upper()+" ", end="")
        letter = normalize(input("\nIngresa una letra: "))
        #assert len(letter) == 1, "No se permiten más de dos caracteres!"
        try:
            if len(letter) == 0:
                raise ValueError("No se puede ingresar una cadena vacía")
            try:
                if len(letter) > 1:
                    raise ValueError("No se permite más de un caracter")
                if letter in word:
                    word_to_guess = list(word_to_guess)
                    for i in range(len(word)):
                        if letter == word[i]:
                            word_to_guess[i] = letter
                    os.system("cls")
                else:
                    intentos = intentos-1
                    os.system("cls")
                    print("Letra no encontrada, intenta de nuevo...")
                word_to_guess = "".join(word_to_guess)
            except ValueError as more_caracter:
                os.system("cls")
                print(more_caracter)
        except ValueError as ve:
            os.system("cls")
            print(ve)
        if intentos == 0:
            os.system("cls")
            print("Has perdido, ya no tienes vidas\nLa palabra era:")
            for i in range(len(word)):
                print(word[i].upper()+" ", end="")
            break
    if word_to_guess == word:
        os.system("cls")
        print("Felicidades, lo has logrado!!!")
        for i in range(len(word)):
                print(word_to_guess[i].upper()+" ", end="")
def run():
    datos = read()
    word  = normalize(datos.get(random.randint(0, len(datos)-1)))
    hangman(word)
    

if __name__ == '__main__':
    run()