import keyboard
import time
import math
import random
import win32api, win32con

import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.ini')

game_mode = config.get('General', 'GameMode', fallback='Combo')

# Teclas por defecto
c_harass_key = 'C'
v_last_hit_key = 'V'
space_combo_key = 'SPACE'

# Configuración personalizada
if 'Keys' in config.sections():
    if 'Harass' in config.options('Keys'):
        c_harass_key = config.get('Keys', 'Harass')
    if 'LastHit' in config.options('Keys'):
        v_last_hit_key = config.get('Keys', 'LastHit')
    if 'Combo' in config.options('Keys'):
        space_combo_key = config.get('Keys', 'Combo')

keys = {
    'c_harass': c_harass_key,
    'v_last_hit': v_last_hit_key,
    'space_combo': space_combo_key,
}

# Variables de kiteo
last_attack_time = 0
last_attack_target_pos = (0, 0)
last_move_time = 0
projectile_speed = 0

# Funciones para la lógica de kiteo
def calculate_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def attack(target_pos):
    global last_attack_time, last_attack_target_pos
    last_attack_time = time.time()
    last_attack_target_pos = target_pos
    x, y = target_pos
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def move(pos):
    global last_move_time
    last_move_time = time.time()
    x, y = pos
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)

def should_move_after_attack(target_pos):
    distance = calculate_distance(last_attack_target_pos, target_pos)
    if distance > 1000:
        return False
    time_to_impact = distance / projectile_speed
    time_since_last_attack = time.time() - last_attack_time
    if time_to_impact > time_since_last_attack:
        return True
    return False

def should_stutter_step():
    time_since_last_attack = time.time() - last_attack_time
    if time_since_last_attack < 0.5:
        return True
    return False

def should_attack_move(target_pos):
    global last_attack_target_pos
    if last_attack_target_pos == target_pos:
        return False
    return True

def focus_fire(target_pos):
    while True:
        move(target_pos)
        attack(target_pos)
        time.sleep(0.1)
        if not is_target_alive(target_pos):
            break

# Funciones de modos de juego
def combo():
    # Implementación del modo Combo
    target_pos = get_target_pos()
    if target_pos is None:
        return
    if should_move_after_attack(target_pos):
        move(get_random_offset(target_pos))
    elif should_stutter_step():
        move(get_random_offset(target_pos))
    elif should_attack_move(target_pos):
        move(get_future_position(target_pos))
    else:
        attack(target_pos)


def harass():
    # Implementación del modo Harass
    target_pos = get_target_pos()
    if target_pos is None:
        return
    if should_move_after_attack(target_pos):
        move(get_random_offset(target_pos))
    elif should_stutter_step():
        move(get_random_offset(target_pos))
    else:
        attack(target_pos)


def last_hit():
    # Implementación del modo Last Hit
    target_pos = get_lowest_hp_minion_pos()
    if target_pos is None:
        return
    if should_move_after_attack(target_pos):
        move(get_random_offset(target_pos))
    elif should_stutter_step():
        move(get_random_offset(target_pos))
    else:
        attack(target_pos)


def orbwalk():
    # Obtiene el modo de juego actual del usuario
    current_mode = Config().game_mode
    if current_mode == 'Combo':
        combo()
    elif current_mode == 'Harass':
        harass()
    elif current_mode == 'LastHit':
        last_hit()


# Modo afk
def afk():
    # Mueve el cursor de forma aleatoria para simular actividad
    x, y = win32api.GetCursorPos()
    new_x = random.randint(-50, 50)
    new_y = random.randint(-50, 50)
    win32api.SetCursorPos((x+new_x, y+new_y))


# Menu principal
def main_menu():
    # Imprime el menu y recibe la entrada del usuario
    print("\n==== Orbwalker ====\n")
    print("1. Modo Combo")
    print("2. Modo Harass")
    print("3. Modo Last Hit")
    print("4. Modo AFK")
    print("5. Salir")
    option = input("Elige una opcion: ")
    
    # Ejecuta la accion correspondiente
    if option == '1':
        Config().game_mode = 'Combo'
    elif option == '2':
        Config().game_mode = 'Harass'
    elif option == '3':
        Config().game_mode = 'LastHit'
    elif option == '4':
        while True:
            afk()
            time.sleep(random.randint(1, 5))
    elif option == '5':
        exit()
    
    # Vuelve al menu principal
    main_menu()


if __name__ == '__main__':
    main_menu()
