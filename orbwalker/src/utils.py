import json
import math


def load_json_file(file_path):
    """
    Carga un archivo json y devuelve su contenido en forma de diccionario.

    Args:
        file_path (str): la ruta del archivo json.

    Returns:
        dict: el contenido del archivo json en forma de diccionario.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def distance_between_points(x1, y1, x2, y2):
    """
    Calcula la distancia euclidiana entre dos puntos.

    Args:
        x1 (float): la coordenada x del primer punto.
        y1 (float): la coordenada y del primer punto.
        x2 (float): la coordenada x del segundo punto.
        y2 (float): la coordenada y del segundo punto.

    Returns:
        float: la distancia euclidiana entre los dos puntos.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_nearest_unit(units, x, y):
    """
    Obtiene la unidad más cercana a las coordenadas x e y.

    Args:
        units (list): una lista de unidades.
        x (float): la coordenada x.
        y (float): la coordenada y.

    Returns:
        dict: la unidad más cercana a las coordenadas dadas.
    """
    nearest_unit = None
    nearest_distance = math.inf
    for unit in units:
        distance = distance_between_points(unit["x"], unit["y"], x, y)
        if distance < nearest_distance:
            nearest_unit = unit
            nearest_distance = distance
    return nearest_unit


def get_spell_info(spell_id, spells):
    """
    Obtiene la información de un hechizo.

    Args:
        spell_id (int): el ID del hechizo.
        spells (dict): un diccionario que contiene la información de los hechizos.

    Returns:
        dict: la información del hechizo.
    """
    for spell in spells:
        if spell["id"] == spell_id:
            return spell
    return None


def get_item_info(item_id, items):
    """
    Obtiene la información de un objeto.

    Args:
        item_id (int): el ID del objeto.
        items (dict): un diccionario que contiene la información de los objetos.

    Returns:
        dict: la información del objeto.
    """
    for item in items:
        if item["id"] == item_id:
            return item
    return None
