import random
import os

def read():
    with open("./archivos/datas.txt", "r", encoding="utf-8") as f:
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
    #Que no sean dos o mas letras
    #que no sea numero
    #que no sea simbolo
    while word_to_guess != word:
        print("¡¡Adivina la palabra!!")
        for i in range(len(word)):
            print(word_to_guess[i].upper()+" ", end="")
        letter = normalize(input(str("\nIngresa una letra!!: ")))
        if letter in word:
            word_to_guess = list(word_to_guess)
            for i in range(len(word)):
                if letter == word[i]:
                    word_to_guess[i] = letter
            os.system("cls")
        else:
            os.system("cls")
            print("Letra no encontrada, intenta de nuevo...\n")
        word_to_guess = "".join(word_to_guess)
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