def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Abisai", "lastname": "Antonio"}

    super_list = [
        {"firstname": "Abisai", "lastname": "Antonio"},
        {"firstname": "Alejandro", "lastname": "Martínez"},
        {"firstname": "Carmen", "lastname": "Torres"},
        {"firstname": "José", "lastname": "García"},
        {"firstname": "María", "lastname": "Castillo"},
    ]
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }
    for key, value in super_dict.items():
        print(key, "-", value)

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')
    print("\n")
    #Otra manera de resolver el mismo problema
    for values in super_list:
        for key, value in values.items():
            print(key + " - " + str(value))

if __name__ == '__main__':
    run()