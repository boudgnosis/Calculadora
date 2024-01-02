def options():
    """Menu de opciones para elegir una operaccion aritmetica.
    
    Returns:
        str: ('1', '2', '3','4') 
    """
    select_options = input('What option do you want?\n'
                           '1. Sum\n'
                           '2. Substraction\n'
                           '3. Multiplication\n'
                           '4. Division\n'
                           'Please select the option: ')
    return select_options

option_number = options()

if option_number == '1':
    print('█▀ █░█ █▀▄▀█\n'
          '▄█ █▄█ █░▀░█')
elif option_number == '2':
    print('█▀ █░█ █▄▄ █▀ ▀█▀ █▀█ ▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█\n'
          '▄█ █▄█ █▄█ ▄█ ░█░ █▀▄ █▀█ █▄▄ ░█░ █ █▄█ █░▀█')
elif option_number == '3':
    print('█▀▄▀█ █░█ █░░ ▀█▀ █ █▀█ █░░ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█\n'
          '█░▀░█ █▄█ █▄▄ ░█░ █ █▀▀ █▄▄ █ █▄▄ █▀█ ░█░ █ █▄█ █░▀█')
elif option_number == '4':
    print('█▀▄ █ █░█ █ █▀ █ █▀█ █▄░█\n'
          '█▄▀ █ ▀▄▀ █ ▄█ █ █▄█ █░▀█')
else:
    print('The program is finished because the option not exist.')
    exit()
