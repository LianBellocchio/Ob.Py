import keyboard
from menu import Menu
from orbwalker import Orbwalker

# Creamos el menú
menu = Menu()

# Creamos el Orbwalker
orbwalker = Orbwalker()

# Definimos las opciones del menú
def toggle_orbwalker():
    orbwalker.toggle()

def set_orbwalker_key():
    key = input("Ingrese la tecla para activar/desactivar el Orbwalker: ")
    orbwalker.set_key(key)

menu.add_option("Activar/Desactivar Orbwalker", toggle_orbwalker)
menu.add_option("Cambiar tecla del Orbwalker", set_orbwalker_key)

# Definimos la tecla para abrir el menú
keyboard.add_hotkey('left shift', menu.open)

# Bucle principal
while True:
    # Actualizamos el Orbwalker
    orbwalker.update()

    # Escuchamos eventos de teclado
    keyboard.wait()
