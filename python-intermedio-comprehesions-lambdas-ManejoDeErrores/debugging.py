def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        try:
            if num < 0:
                raise ValueError("Debes ingresar solo números positivos")
            print(divisor(num))
            print("Terminó el programa")
        except ValueError as ve:
            print(ve)
            return False
    except ValueError:
        print("Debes ingresar un número")

if __name__ == '__main__':
    run()