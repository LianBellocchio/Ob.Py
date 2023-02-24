import math
from typing import Optional
from itertools import groupby

from utils import dist, is_in_turret_range, is_in_fountain_range, is_valid_target

class Orbwalker:
def init(self, player):
self.player = player
self.last_attack_tick = 0
self.last_move_tick = 0
self.attack_windup = 0.05
self.attack_animation = 0.35
self.move_delay = 0.05
self.target: Optional['GameObject'] = None
def get_target(self):
    if self.target and not is_valid_target(self.target):
        self.target = None

    if not self.target:
        # Prioritize enemy champions
        enemies = [unit for unit in self.player.game.units if unit.is_enemy_to(self.player) and unit.is_alive and self.player.distance_to(unit) <= self.player.vision_range]
        if enemies:
            self.target = max(enemies, key=lambda u: u.distance_to(self.player))

    return self.target

def attack_if_possible(self):
    target = self.get_target()
    if not target:
        return

    if self.player.game.tick - self.last_attack_tick >= self.player.attack_delay * 1000:
        if self.player.distance_to(target) <= self.player.attack_range and not is_in_turret_range(target) and not is_in_fountain_range(target):
            self.player.issue_attack(target)
            self.last_attack_tick = self.player.game.tick

def move_to_target(self):
    target = self.get_target()
    if not target:
        return

    if self.player.game.tick - self.last_move_tick >= self.move_delay * 1000:
        if self.player.distance_to(target) > self.player.attack_range or is_in_turret_range(target) or is_in_fountain_range(target):
            self.player.issue_move(target.position)
            self.last_move_tick = self.player.game.tick

def kite(self):
    target = self.get_target()
    if not target:
        return

    # Calculate kite vector
    player_pos = self.player.position
    target_pos = target.position
    distance_to_target = dist(player_pos, target_pos)
    if distance_to_target < self.player.attack_range:
        direction = (player_pos - target_pos).normalize()
        angle = math.pi / 3  # 60 degrees
        perpendicular = direction.rotate(angle) if self.player.is_melee else direction.rotate(-angle)
        kiting_pos = target_pos + perpendicular.scale(250)

        # Make sure kiting position is valid
        if not is_in_turret_range(kiting_pos) and not is_in_fountain_range(kiting_pos):
            self.player.issue_move(kiting_pos)

def orbwalk(self):
    self.attack_if_possible()
    self.move_to_target()
    self.kite()

    # Implement prediction of target position
    target = self.get_target()
    if not target:
        return

    if target.is_moving and not is_in_turret_range(target) and not is_in_fountain_range(target):
        prediction = target.position + target.velocity.scale(target.distance_to(self.player) / self.player.attack_range)
        if not is_in_turret_range(prediction) and not is_in_fountain_range(prediction):
            self.player.issue_attack(prediction)

    # Implement collision detection
    target = self.get_target()
    if not target:
        return

    player_pos = self.player.position
    target_pos = target.position
    distance_to_target = dist(player_pos, target_pos)
    if distance_to_target < self.player.attack_range:
        direction = (player_pos - target_pos).normalize()
        angle = math.pi / 3  # 60 degrees
        perpendicular = direction.rotate(angle) if self.player.is_melee else direction.rotate(-angle)
        kiting_pos = target_pos + perpendicular.scale(250)

        # Check for collision
        for game_object in self.player.game.game_objects:
            if game_object == self.player:
                continue
            if game_object.is_wall or game_object.is_turret:
                continue
            if dist(kiting_pos, game_object.position) < game_object.radius + self.player.radius:
                # Collision detected, move in opposite direction
                opposite = direction.rotate(math.pi)
                kiting_pos = target_pos + opposite.scale(250)
                break

        if not is_in_turret_range(kiting_pos) and not is_in_fountain_range(kiting_pos):
            self.player.issue_move(kiting_pos)
