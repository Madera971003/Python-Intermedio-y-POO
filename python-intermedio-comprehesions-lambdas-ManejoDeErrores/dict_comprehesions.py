import math

def run():
    cubes = {}
    for i in range(1, 101):
        if i%3 != 0:
            cubes[i] = i**3
    #print(cubes)

    my_dict = {i: i**3 for i in range(1, 101) if 1%3 != 0}
    #print(my_dict)

    other_dict = {i: math.sqrt(i) for i in range(1, 1001)}
    print(other_dict)
if __name__ == '__main__':
    run() 