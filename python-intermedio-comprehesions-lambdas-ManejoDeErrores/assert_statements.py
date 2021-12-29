def divisor(num):
    #divisors = []
    #for i in range(1, num+1):
    #    if num % i == 0:
    #        divisors.append(i)
    divisors = [i for i in range(1, num+1) if num%i == 0]
    return divisors

def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric() and int(num) > 0, "Debes ingresar solo números positivos"
    print(divisor(int(num)))
    print("Terminó el programa")

if __name__ == '__main__':
    run()