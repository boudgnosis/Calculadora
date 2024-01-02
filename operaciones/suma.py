from entrada_salida import entrada

def sum_two_numers(n1, n2):
    """Hacemos una sumaa y comprobamos si el resultado es un entero sin
    una continuacion o si la tiene que esta no sea mayor a .0 para retornar
    un int y en caso contrario el resultado se retornaria como float.

    Args:
        n1 (float): Numero para comprobar si es float o int y sumar con n2
        n2 (float): Numero para comprobar si es float o int y sumar con n1
    """
    sum_numbers = n1 + n2

    str_number = str(sum_numbers)

    if '.' in str_number:
        part_decimal = str_number.split('.')
        if len(part_decimal) == 2 and len(part_decimal[1]) == 1 and part_decimal[1] == '0':
            print(int(sum_numbers))
        else:
            print(sum_numbers)
    else:
        print(sum_numbers)


sum_two_numers(entrada.n1, entrada.n2)
