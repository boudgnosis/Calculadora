from ui import menu
from operaciones import suma

def return_operations():
	match menu.options:
		case '1':
			print(suma.is_int_or_float)
