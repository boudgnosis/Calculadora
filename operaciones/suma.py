from entrada_salida import entrada

def sum_two_numers(n1, n2):
    """Hacemos una suma de dos numeros de coma flotante

    Args:
        n1 (float): Number float
        n2 (float): Number float

    Returns:
        float: retornamos la suma total de ambos numeros
    """
    sum_numbers = n1 + n2
    return sum_numbers


sum_result = sum_two_numers(entrada.n1, entrada.n2)

def has_only_a_zero_after_the_point(sum_result):
    """ Verfica si tiene un solo cero despuesdel '.' decimal.

    Args:
        sum_result (float): Este float se verifica para no retonar un numero 
                            que tenga un .0 y finalice ahi, asi solo retornamos
                            el entero solo.

    Returns:
        bool: Si existe el 0 despues de '.' decimal y no tiene continuación
              devuelve True en caso contrario devuelve False.
    """
    str_number = str(sum_result)
    if '.' in str_number:
        part_decimal = str_number.split('.')
        if len(part_decimal) == 2 and len(part_decimal[1]) == 1 and part_decimal[1] == '0':
            return True
    return False


verifica_el_float = has_only_a_zero_after_the_point(sum_result)

def is_int_or_float(v, s):
    if v == True:
        print(int(s))
    else:
        print(s)


is_int_or_float(verifica_el_float, sum_two_numers())
