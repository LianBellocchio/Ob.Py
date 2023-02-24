import time
import random
import math
import pydirectinput
from champion import Champion
from player import Player
from utils import is_in_range, get_closest_enemy, distance_between, normalize_vector, predict_position, get_line_circle_intersection_points

class Orbwalker:
    def __init__(self, champion: Champion, player: Player):
        self.champion = champion
        self.player = player

    def kite(self, target):
        start_time = time.time()
        attack_started = False
        last_pos = self.champion.get_position()

        while self.player.is_alive() and target.is_alive():
            current_time = time.time()
            if current_time - start_time > 5:
                break

            target_distance = distance_between(self.champion.get_position(), target.get_position())

            if is_in_range(target_distance, self.champion.get_autoattack_range()):
                if not attack_started:
                    pydirectinput.mouseDown()
                    attack_started = True
                elif current_time - start_time > 1:
                    pydirectinput.mouseUp()
                    attack_started = False
            else:
                if attack_started:
                    pydirectinput.mouseUp()
                    attack_started = False

                if target_distance < self.champion.get_autoattack_range() * 1.5:
                    move_pos = get_closest_enemy(self.player, [target])
                    if move_pos is not None:
                        pydirectinput.moveTo(*move_pos)
                else:
                    predicted_pos = predict_position(self.champion.get_position(), target.get_position(), target.get_last_move_speed())
                    move_pos = get_line_circle_intersection_points(self.champion.get_position(), predicted_pos, self.champion.get_autoattack_range())[0]
                    if move_pos is None:
                        move_pos = predicted_pos

                    # Calculate a random point around the predicted position to move to
                    # to avoid moving in a predictable way
                    move_dir = normalize_vector((move_pos[0] - self.champion.get_position()[0], move_pos[1] - self.champion.get_position()[1]))
                    move_angle = math.atan2(move_dir[1], move_dir[0])
                    move_radius = random.uniform(50, 150)
                    move_offset = (move_radius * math.cos(move_angle), move_radius * math.sin(move_angle))
                    move_pos = (move_pos[0] + move_offset[0], move_pos[1] + move_offset[1])

                    pydirectinput.moveTo(*move_pos)
                    last_pos = move_pos

        pydirectinput.mouseUp()
