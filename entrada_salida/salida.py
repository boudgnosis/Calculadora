from ui import menu
from operaciones import suma
from operaciones import resta

def return_operation(options):
    
    if options == '1':
        return suma.sum_two_numers
    elif options == '2':
        return resta.substraction
    else:
        print('error')

return_operation(menu.options)
