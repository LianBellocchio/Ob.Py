import math
import json
import os


def get_game_data_path():
    script_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_path, '..', 'data')
    game_data_path = os.path.join(data_path, 'game_data.json')
    return game_data_path


def load_game_data():
    game_data_path = get_game_data_path()
    with open(game_data_path, 'r', encoding='utf-8') as f:
        game_data = json.load(f)
    return game_data


def save_game_data(game_data):
    game_data_path = get_game_data_path()
    with open(game_data_path, 'w', encoding='utf-8') as f:
        json.dump(game_data, f, ensure_ascii=False, indent=4)


def euclidean_distance(point1, point2):
    distance = math.sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]))
    return distance


def closest_point(point, points_list):
    closest = min(points_list, key=lambda x: euclidean_distance(point, x))
    return closest


def mana_percent(player):
    return player.mana / player.max_mana if player.max_mana != 0 else 0


def health_percent(player):
    return player.health / player.max_health if player.max_health != 0 else 0

